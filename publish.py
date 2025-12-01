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
# FIXED: Generate directly in the root of the repo, not in a 'public' subfolder
PUBLIC_ROOT_DIR = "." # Represents the root of the Sites repository
PRESENTATIONS_DIR = os.path.join(PUBLIC_ROOT_DIR, "apresentacoes")
MENU_TEMPLATE_SOURCE = "menu_template.html" # External file
MENU_OUTPUT_PATH = os.path.join(PUBLIC_ROOT_DIR, "index.html")

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
        print(f"❌ Error: Template file '{MENU_TEMPLATE_SOURCE}' not found. Please ensure it is in the root of the Sites folder.")
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
    # FIXED: Output directly to PUBLIC_ROOT_DIR (which is '.')
    os.makedirs(PUBLIC_ROOT_DIR, exist_ok=True) # Ensure root exists (it will)
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
    # FIXED: Target directory is directly under PUBLIC_ROOT_DIR
    target_dir = os.path.join(PRESENTATIONS_DIR, slug)
    
    print(f"🚀 Publishing '{args.name}'...")

    # Ensure base directories exist (now just 'apresentacoes' in root)
    os.makedirs(PRESENTATIONS_DIR, exist_ok=True)
    
    if os.path.exists(target_dir):
        print(f"⚠️  Overwriting: {target_dir}")
        shutil.rmtree(target_dir, onerror=remove_readonly)
    
    try:
        shutil.copytree(args.source, target_dir, ignore=shutil.ignore_patterns(
            '.git', '.github', '__pycache__', 'node_modules', '_deploy_tool', '.vercel', 'venv', '.env',
            '.claude', '.docker', 'agents', 'bmb', 'bmm', 'config', 'core', 'data', 'docs', 'Projeto_Esg',
            'scripts', 'src', 'tests', 'workflows',
            '.env.example', '.gitignore', 'git-push.bat', 'menu_template.html', 'middleware.js', 'presentations.json',
            'publish*.py', 'README.md', 'start-*.bat', 'vercel*.json',
            'image-prompts.md', 'objetivo.md', 'Projeto_ExecutiveMeeting_Brainstorm.md', 'ERROR_POSTMORTEM.md', 'CHECKPOINT-*.md'
        ))
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
        # FIXED: Path is now relative to the root of the repo (no 'public/')
        relative_html_path = os.path.relpath(os.path.join(target_dir, main_html_file), PUBLIC_ROOT_DIR) # Use PUBLIC_ROOT_DIR
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
