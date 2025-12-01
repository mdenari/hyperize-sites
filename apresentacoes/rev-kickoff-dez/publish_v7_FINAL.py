import os
import sys
import shutil
import json
import argparse
import subprocess
import re
import stat
from datetime import datetime

# --- Configuration ---
PRESENTATIONS_DB = "presentations.json"
PUBLIC_DIR = "public"
PRESENTATIONS_DIR = os.path.join(PUBLIC_DIR, "apresentacoes")
MENU_TEMPLATE_SOURCE = "menu_template.html" # External file
MENU_OUTPUT_PATH = os.path.join(PUBLIC_DIR, "index.html")

# --- Helper Functions ---

def remove_readonly(func, path, _):
    """Clear the readonly bit and reattempt the removal."""
    os.chmod(path, stat.S_IWRITE)
    func(path)

def run_command(command, cwd=None):
    """Executes a shell command."""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            check=True,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(e.stderr)
        sys.exit(1)

def git_status_clean(cwd):
    """Checks if the git repository is clean."""
    try:
        status = run_command("git status --porcelain", cwd=cwd)
        if re.search(r"^[MD ]", status, re.MULTILINE):
            print("\n--- Git Status Details ---")
            print(status)
            print("------------------------\n")
            return False
        return True
    except:
        return False

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

def update_json_db(name, slug, protected, final_path):
    """Updates the presentations.json database."""
    db_path = PRESENTATIONS_DB
    
    if os.path.exists(db_path):
        with open(db_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    entry = {
        "name": name,
        "slug": slug,
        "path": final_path,
        "protected": protected,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    updated = False
    for i, item in enumerate(data):
        if item['slug'] == slug:
            data[i] = entry
            updated = True
            break
    
    if not updated:
        data.append(entry)

    data.sort(key=lambda x: x['date'], reverse=True)

    with open(db_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    return data

def generate_menu_html(data):
    """Generates the main index.html using the external template."""
    
    # 1. Read the external template
    if not os.path.exists(MENU_TEMPLATE_SOURCE):
        print(f"❌ Error: Template file '{MENU_TEMPLATE_SOURCE}' not found. Please create it.")
        sys.exit(1)

    with open(MENU_TEMPLATE_SOURCE, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # 2. Generate the items HTML
    items_html = ""
    for item in data:
        lock_icon = "🔒" if item.get('protected') else "🌐"
        badge_class = "badge-protected" if item.get('protected') else "badge-public"
        badge_text = "Privado" if item.get('protected') else "Público"
        display_path = item['path']

        # Simple HTML concatenation - No complex f-strings
        items_html += '<div class="card">\n'
        items_html += '    <div class="card-header">\n'
        items_html += f'        <span class="badge {badge_class}">{lock_icon} {badge_text}</span>\n'
        items_html += f'        <span class="date">{item["date"].split(" ")[0]}</span>\n'
        items_html += '    </div>\n'
        items_html += f'    <h2>{item["name"]}</h2>\n'
        items_html += f'    <a href="{display_path}" class="btn">Acessar Apresentação</a>\n'
        items_html += '</div>\n'

    # 3. Inject items into template
    final_html = template_content.replace('<!-- ITEMS_PLACEHOLDER -->', items_html)

    # 4. Write output
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    with open(MENU_OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(final_html)

# --- Main Execution ---

def main():
    parser = argparse.ArgumentParser(description="ELabs Publish Tool")
    parser.add_argument("--name", required=True, help="Presentation Name")
    parser.add_argument("--source", required=True, help="Source Path")
    parser.add_argument("--slug", help="Slug")
    parser.add_argument("--protected", action="store_true", help="Protected?")
    
    args = parser.parse_args()

    if not os.path.isdir(args.source):
        print(f"❌ Error: Invalid source: {args.source}")
        sys.exit(1)

    print("🔍 Checking Git status...")
    if not git_status_clean(os.getcwd()):
        print("❌ Error: Git dirty. Please commit first.")
        # sys.exit(1) # Warning only

    slug = args.slug if args.slug else slugify(args.name)
    target_dir = os.path.join(PRESENTATIONS_DIR, slug)
    
    print(f"🚀 Publishing '{args.name}'...")

    os.makedirs(PRESENTATIONS_DIR, exist_ok=True)
    
    if os.path.exists(target_dir):
        print(f"⚠️  Overwriting: {target_dir}")
        shutil.rmtree(target_dir, onerror=remove_readonly)
    
    try:
        shutil.copytree(args.source, target_dir, ignore=shutil.ignore_patterns('.git', '.github', '__pycache__', 'node_modules', '_deploy_tool', '.vercel', 'venv', '.env'))
        print("✅ Files copied.")
    except Exception as e:
        print(f"❌ Copy Error: {e}")
        sys.exit(1)
        
    main_html_file = "index.html"
    found_html = False
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.lower().endswith('.html'):
                if file.lower() == "index.html":
                    main_html_file = file
                    found_html = True
                    break
                if not found_html:
                    main_html_file = file
                    found_html = True
        if found_html:
            break

    if not found_html:
        final_presentation_path = f"/apresentacoes/{slug}/index.html"
    else:
        relative_html_path = os.path.relpath(os.path.join(target_dir, main_html_file), PUBLIC_DIR)
        final_presentation_path = f"/{relative_html_path.replace(os.path.sep, '/')}"

    print("💾 Database...")
    data = update_json_db(args.name, slug, args.protected, final_presentation_path)
    
    print("🎨 Menu...")
    generate_menu_html(data)
    
    print("📦 Git...")
    try:
        run_command("git add .", cwd=os.getcwd())
        status = run_command("git status --porcelain", cwd=os.getcwd())
        if status:
            # Safe string concatenation for commit message
            commit_msg = 'git commit -m "Publish: ' + args.name + '"'
            run_command(commit_msg, cwd=os.getcwd())
            print("✅ Committed.")
            print("⬆️  Pushing...")
            run_command("git push", cwd=os.getcwd())
            print("🎉 Done!")
        else:
            print("ℹ️  No changes.")

    except Exception as e:
        print(f"❌ Git Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
