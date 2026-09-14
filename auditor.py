import os
import re


def audit_links(filename):
    if not os.path.isfile(filename):
        return None

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    links = re.findall(r"\[([^\]]*)\]\(([^)]*)\)", content)

    problems = []

    for text, url in links:
        if not text.strip():
            problems.append("Empty link text")

        if not url.strip():
            problems.append(f"Empty URL for: [{text}]")

    return problems
