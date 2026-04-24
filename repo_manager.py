#!/usr/bin/env python3
"""
Sahiix Repo Manager
Bulk operations across all 167 public repositories.

Commands:
  clone-all           Clone all repos to ./repos/
  status              Show outdated forks behind upstream
  sync-forks          Fast-forward all forks from upstream
  list-originals      List non-fork repos
  list-forks          List forked repos
  languages           Show language distribution
  generate-readme     Create unified portfolio README
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

GITHUB_USER = "sahiixx"
API_BASE = f"https://api.github.com/users/{GITHUB_USER}"


def api_get(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github.v3+json"})
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def fetch_all_repos():
    repos = []
    page = 1
    while True:
        data = api_get(f"{API_BASE}/repos?per_page=100&page={page}")
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos


def run(cmd, cwd=None):
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    return result.returncode == 0, result.stdout, result.stderr


def clone_repo(repo, base_dir="repos"):
    name = repo["name"]
    dest = Path(base_dir) / name
    if dest.exists():
        return name, "exists"
    url = repo["clone_url"]
    ok, out, err = run(f"git clone --depth 1 {url} {dest}")
    return name, "ok" if ok else f"fail: {err.strip()}"


def cmd_clone_all(args):
    repos = fetch_all_repos()
    print(f"Cloning {len(repos)} repos into ./{args.dir}/ ...")
    Path(args.dir).mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = {ex.submit(clone_repo, r, args.dir): r for r in repos}
        for future in as_completed(futures):
            name, status = future.result()
            icon = "✅" if status == "ok" else ("⏩" if status == "exists" else "❌")
            print(f"  {icon} {name}: {status}")
    print("Done.")


def cmd_status(args):
    repos = fetch_all_repos()
    forks = [r for r in repos if r["fork"]]
    print(f"Checking {len(forks)} forks for updates...")
    for repo in forks:
        name = repo["name"]
        dest = Path(args.dir) / name
        if not dest.exists():
            print(f"  ⚠️  {name}: not cloned")
            continue
        ok, out, err = run("git fetch origin --depth 1", cwd=dest)
        if not ok:
            print(f"  ❌ {name}: fetch failed")
            continue
        ok, out, err = run("git rev-list --count HEAD..origin/main", cwd=dest)
        if not ok:
            ok, out, err = run("git rev-list --count HEAD..origin/master", cwd=dest)
        behind = int(out.strip()) if out.strip().isdigit() else 0
        if behind > 0:
            print(f"  📥 {name}: {behind} commits behind")
        else:
            print(f"  ✅ {name}: up to date")


def cmd_sync_forks(args):
    repos = fetch_all_repos()
    forks = [r for r in repos if r["fork"]]
    print(f"Syncing {len(forks)} forks...")
    for repo in forks:
        name = repo["name"]
        dest = Path(args.dir) / name
        if not dest.exists():
            print(f"  ⚠️  {name}: not cloned, skipping")
            continue
        ok, out, err = run("git pull origin main --ff-only", cwd=dest)
        if not ok:
            ok, out, err = run("git pull origin master --ff-only", cwd=dest)
        if ok:
            print(f"  ✅ {name}: synced")
        else:
            print(f"  ❌ {name}: merge conflict or no common ancestor")


def cmd_list_originals(args):
    repos = fetch_all_repos()
    originals = [r for r in repos if not r["fork"]]
    print(f"Original repos ({len(originals)}):\n")
    for r in originals:
        lang = r.get("language") or "N/A"
        stars = r["stargazers_count"]
        print(f"  {'⭐' if stars > 0 else '  '} {r['name']:<35} {lang:<12} ⭐{stars}")


def cmd_list_forks(args):
    repos = fetch_all_repos()
    forks = [r for r in repos if r["fork"]]
    print(f"Forked repos ({len(forks)}):\n")
    for r in forks:
        lang = r.get("language") or "N/A"
        stars = r["stargazers_count"]
        print(f"  {'⭐' if stars > 0 else '  '} {r['name']:<35} {lang:<12} ⭐{stars}")


def cmd_languages(args):
    repos = fetch_all_repos()
    counts = {}
    for r in repos:
        lang = r.get("language")
        if lang:
            counts[lang] = counts.get(lang, 0) + 1
    print("Language distribution:\n")
    for lang, count in sorted(counts.items(), key=lambda x: -x[1]):
        bar = "█" * (count // 2)
        print(f"  {lang:<15} {count:>3} {bar}")


def cmd_generate_readme(args):
    repos = fetch_all_repos()
    # Reuse generate_portfolio.py logic inline
    from datetime import datetime
    originals = [r for r in repos if not r["fork"]]
    forks = [r for r in repos if r["fork"]]
    lines = [
        f"# @{GITHUB_USER} Repository Index",
        "",
        f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
        f"Total repos: {len(repos)} | Originals: {len(originals)} | Forks: {len(forks)}",
        "",
        "## Original Projects",
        "",
        "| Repo | Language | Description | Stars | Updated |",
        "|------|----------|-------------|-------|---------|",
    ]
    for r in sorted(originals, key=lambda x: x["updated_at"], reverse=True):
        lines.append(
            f"| [{r['name']}]({r['html_url']}) | {r.get('language') or '-'} |"
            f" {r['description'] or '-'} | {r['stargazers_count']}⭐ |"
            f" {r['updated_at'][:10]} |"
        )
    lines += ["", "## Forks", "", "| Repo | Language | Stars | Updated |", "|------|----------|-------|---------|"]
    for r in sorted(forks, key=lambda x: x["updated_at"], reverse=True)[:50]:
        lines.append(
            f"| [{r['name']}]({r['html_url']}) | {r.get('language') or '-'} |"
            f" {r['stargazers_count']}⭐ | {r['updated_at'][:10]} |"
        )
    if len(forks) > 50:
        lines.append(f"| *...and {len(forks) - 50} more forks* | | | |")
    out = "\n".join(lines)
    Path("INDEX.md").write_text(out)
    print("Written to INDEX.md")


def main():
    parser = argparse.ArgumentParser(description="Manage all sahiixx repos")
    parser.add_argument("command", choices=[
        "clone-all", "status", "sync-forks",
        "list-originals", "list-forks", "languages", "generate-readme"
    ])
    parser.add_argument("--dir", default="repos", help="Base directory for clones")
    parser.add_argument("--workers", type=int, default=8, help="Clone concurrency")
    args = parser.parse_args()

    commands = {
        "clone-all": cmd_clone_all,
        "status": cmd_status,
        "sync-forks": cmd_sync_forks,
        "list-originals": cmd_list_originals,
        "list-forks": cmd_list_forks,
        "languages": cmd_languages,
        "generate-readme": cmd_generate_readme,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
