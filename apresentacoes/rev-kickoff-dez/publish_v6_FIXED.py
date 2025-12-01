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
MENU_TEMPLATE_PATH = os.path.join(PUBLIC_DIR, "index.html")

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
    """Checks if the git repository is clean (no uncommitted changes)."""
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
    """Creates a URL-friendly slug from text."""
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
    """Generates the main index.html menu."""
    
    items_html = ""
    for item in data:
        lock_icon = "🔒" if item.get('protected') else "🌐"
        badge_class = "badge-protected" if item.get('protected') else "badge-public"
        badge_text = "Privado" if item.get('protected') else "Público"
        display_path = item['path']

        items_html += f"""
        <div class="card">
            <div class="card-header">
                <span class="badge {badge_class}">{lock_icon} {badge_text}</span>
                <span class="date">{item['date'].split(' ')[0]}</span>
            </div>
            <h2>{item['name']}</h2>
            <a href="{display_path}" class="btn">Acessar Apresentação</a>
        </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ELabs Presentations Hub</title>
    <style>
        :root {{
            --bg-color: #1a1a1a;
            --card-bg: #2d2d2d;
            --text-color: #ffffff;
            --accent-color: #0070f3; /* Vercel Blue */
            --private-color: #f5a623;
            --public-color: #50e3c2;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 40px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        h1 {{ margin-bottom: 40px; font-weight: 800; letter-spacing: -1px; }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            width: 100%;
            max-width: 1200px;
        }}
        .card {{
            background: var(--card-bg);
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
            transition: transform 0.2s;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 200px;
        }}
        .card:hover {{ transform: translateY(-5px); }}
        .card-header {{ display: flex; justify-content: space-between; margin-bottom: 15px; font-size: 0.8em; }}
        .badge {{ padding: 4px 8px; border-radius: 4px; font-weight: bold; }}
        .badge-protected {{ background: rgba(245, 166, 35, 0.2); color: var(--private-color); }}
        .badge-public {{ background: rgba(80, 227, 194, 0.2); color: var(--public-color); }}
        .date {{ color: #888; }}
        h2 {{ font-size: 1.4em; margin: 0 0 20px 0; }}
        .btn {{
            display: inline-block;
            background: var(--accent-color);
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 4px;
            text-align: center;
            font-weight: 600;
            transition: background 0.2s;
        }}
        .btn:hover {{ background: #005bb5; }}
    </style>
</head>
<body>
    <h1>ELabs Presentations Hub</h1>
    <div class="grid">
        {items_html}
    </div>
</body>
</html>
"
    
    os.makedirs(PUBLIC_DIR, exist_ok=True)
    with open(MENU_TEMPLATE_PATH, 'w', encoding='utf-8') as f:
        f.write(html_content)

# --- Main Execution ---

def main():
    parser = argparse.ArgumentParser(description="ELabs Publish Tool - Publish presentations to Vercel.")
    parser.add_argument("--name", required=True, help="Name of the presentation (Menu Title)")
    parser.add_argument("--source", required=True, help="Full path to source folder containing index.html")
    parser.add_argument("--slug", help="URL slug (optional, auto-generated from name)")
    parser.add_argument("--protected", action="store_true", help="Protect with password (requires Vercel env var)")
    
    args = parser.parse_args()

    if not os.path.isdir(args.source):
        print(f"❌ Error: Source path is not a valid directory: {args.source}")
        sys.exit(1)

    print("🔍 Checking Git status...")
    if not git_status_clean(os.getcwd()):
        print("❌ Error: Git repository is not clean. Please commit or stash changes in 'Sites' before publishing.")
        # sys.exit(1)

    slug = args.slug if args.slug else slugify(args.name)
    target_dir = os.path.join(PRESENTATIONS_DIR, slug)
    
    print(f"🚀 Publishing '{args.name}' to /{slug}...")

    os.makedirs(PRESENTATIONS_DIR, exist_ok=True)
    
    if os.path.exists(target_dir):
        print(f"⚠️  Target directory exists. Overwriting: {target_dir}")
        shutil.rmtree(target_dir, onerror=remove_readonly)
    
    try:
        shutil.copytree(args.source, target_dir, ignore=shutil.ignore_patterns('.git', '.github', '__pycache__', 'node_modules', '_deploy_tool', '.vercel', 'venv', '.env'))
        print("✅ Files copied successfully.")
    except Exception as e:
        print(f"❌ Error copying files: {e}")
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
        print("⚠️  Warning: No HTML file found. Presentation might not load correctly.")
        final_presentation_path = f"/apresentacoes/{slug}/index.html"
    else:
        relative_html_path = os.path.relpath(os.path.join(target_dir, main_html_file), PUBLIC_DIR)
        final_presentation_path = f"/{relative_html_path.replace(os.path.sep, '/')}"
        print(f"ℹ️  Main HTML identified: {main_html_file}. Path: {final_presentation_path}")

    print("💾 Updating database...")
    data = update_json_db(args.name, slug, args.protected, final_presentation_path)
    
    print("🎨 Regenerating menu...")
    generate_menu_html(data)
    
    print("📦 Committing changes...")
    try:
        run_command("git add .", cwd=os.getcwd())
        status = run_command("git status --porcelain", cwd=os.getcwd())
        if status:
            # FIX: Using string concatenation instead of f-string for safety
            commit_msg = 'git commit -m "Publish: ' + args.name + '"'
            run_command(commit_msg, cwd=os.getcwd())
            print("✅ Committed.")
            print("⬆️  Pushing to Vercel...")
            run_command("git push", cwd=os.getcwd())
            print("🎉 Successfully published! Check your Vercel URL.")
        else:
            print("ℹ️  No changes to commit.")

    except Exception as e:
        print(f"❌ Git Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
