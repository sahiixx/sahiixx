#!/usr/bin/env python3
"""
Sahiix Portfolio Generator
Fetches public repos from GitHub and generates a categorized portfolio README.
Usage: python generate_portfolio.py > README.md
"""

import json
import urllib.request
from urllib.error import HTTPError
from datetime import datetime

GITHUB_USER = "sahiixx"


def fetch_repos():
    """Fetch all public repos for a user via GitHub API."""
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100&page={page}"
        try:
            with urllib.request.urlopen(url) as resp:
                data = json.load(resp)
                if not data:
                    break
                repos.extend(data)
                page += 1
        except HTTPError as e:
            print(f"Error fetching repos: {e}", file=__import__("sys").stderr)
            break
    return repos


def categorize(repo):
    """Categorize a repo based on name and description."""
    name = repo["name"].lower()
    desc = (repo["description"] or "").lower()
    topics = [t.lower() for t in repo.get("topics", [])]

    if repo["fork"]:
        if any(x in name or x in desc for x in ["agent", "ai ", "llm", "bot", "claude", "gpt", "openai"]):
            return "ai-forks"
        return "forks"

    if any(x in name for x in ["agent", "swarm", "agency", "jarvis", "aios"]):
        return "agents"
    if any(x in name for x in ["os", "system", "platform", "workspace"]):
        return "systems"
    if any(x in name for x in ["demo", "template", "starter", "example"]):
        return "demos"
    if any(x in name for x in ["fix", "cve", "security", "audit", "recon"]):
        return "security"
    if any(x in name for x in ["prompt", "system-prompt"]):
        return "prompts"
    if any(x in name for x in ["n8n", "workflow", "mcp", "integration"]):
        return "integrations"

    return "originals"


def generate_markdown(repos):
    """Generate a portfolio README from repo data."""
    categories = {
        "agents": [],
        "systems": [],
        "security": [],
        "integrations": [],
        "prompts": [],
        "demos": [],
        "originals": [],
        "ai-forks": [],
        "forks": [],
    }

    for repo in repos:
        cat = categorize(repo)
        categories.setdefault(cat, []).append(repo)

    # Sort each category by updated_at desc
    for cat in categories:
        categories[cat].sort(key=lambda r: r["updated_at"], reverse=True)

    lines = [
        f"# @{GITHUB_USER} Portfolio",
        "",
        f"Generated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
        f"Total Public Repos: {len(repos)}",
        "",
        "## Core Projects (Agents & Systems)",
        "",
        "| Repo | Language | Description | Stars | Updated |",
        "|------|----------|-------------|-------|---------|",
    ]

    for repo in categories["agents"] + categories["systems"]:
        lines.append(
            f"| [{repo['name']}]({repo['html_url']}) | {repo.get('language') or '-'} |"
            f" {repo['description'] or '-'} | {repo['stargazers_count']}⭐ |"
            f" {repo['updated_at'][:10]} |"
        )

    lines += ["", "## Security Tools", "", "| Repo | Language | Description | Stars | Updated |", "|------|----------|-------------|-------|---------|"]
    for repo in categories["security"]:
        lines.append(
            f"| [{repo['name']}]({repo['html_url']}) | {repo.get('language') or '-'} |"
            f" {repo['description'] or '-'} | {repo['stargazers_count']}⭐ |"
            f" {repo['updated_at'][:10]} |"
        )

    lines += ["", "## AI/Agent Forks (Active Ecosystem)", "", "| Repo | Language | Origin | Stars | Updated |", "|------|----------|--------|-------|---------|"]
    for repo in categories["ai-forks"]:
        origin = repo.get("full_name", "").replace(f"{GITHUB_USER}/", "")
        lines.append(
            f"| [{repo['name']}]({repo['html_url']}) | {repo.get('language') or '-'} |"
            f" forked | {repo['stargazers_count']}⭐ | {repo['updated_at'][:10]} |"
        )

    lines += ["", "## Other Forks", "", "| Repo | Language | Stars | Updated |", "|------|----------|-------|---------|"]
    for repo in categories["forks"][:20]:  # Limit to top 20
        lines.append(
            f"| [{repo['name']}]({repo['html_url']}) | {repo.get('language') or '-'} |"
            f" {repo['stargazers_count']}⭐ | {repo['updated_at'][:10]} |"
        )
    if len(categories["forks"]) > 20:
        lines.append(f"| *...and {len(categories['forks']) - 20} more forks* | | | |")

    # Language stats
    lang_counts = {}
    for repo in repos:
        lang = repo.get("language")
        if lang:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1

    lines += ["", "## Language Distribution", ""]
    for lang, count in sorted(lang_counts.items(), key=lambda x: -x[1])[:15]:
        lines.append(f"- **{lang}**: {count} repos")

    lines += ["", "---", "", f"*Generated by [generate_portfolio.py](generate_portfolio.py)*"]
    return "\n".join(lines)


def main():
    print("Fetching repos from GitHub API...", file=__import__("sys").stderr)
    repos = fetch_repos()
    print(f"Fetched {len(repos)} repos", file=__import__("sys").stderr)
    md = generate_markdown(repos)
    print(md)


if __name__ == "__main__":
    main()
