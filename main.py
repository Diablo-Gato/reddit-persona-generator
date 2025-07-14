# main.py

import sys
import os
from scrapper import get_reddit_data
from llm_utils import generate_persona_from_data

def extract_username_from_url(url):
    return url.strip("/").split("/")[-1]

def save_persona_to_file(username, content):
    output_path = os.path.join("output", f"{username}_persona.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[✅] Saved persona to: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <reddit_profile_url>")
        sys.exit(1)

    url = sys.argv[1]
    username = extract_username_from_url(url)

    print(f"[🔍] Scraping Reddit user: {username}")
    data = get_reddit_data(username)

    if data is None:
        print("[❌] Could not fetch Reddit user data. Exiting.")
        sys.exit(1)

    print("[🧠] Generating persona with LLM...")
    persona = generate_persona_from_data(data)

    if not persona or persona.startswith("Error:"):
        print("[❌] Failed to generate persona.")
        sys.exit(1)

    print("[💾] Saving persona to file...")
    save_persona_to_file(username, persona)
