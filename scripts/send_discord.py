import sys
import os
import json
import urllib.request

def main():
    if len(sys.argv) < 2:
        print("Usage: send_discord.py <file>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"No file at {path}, nothing to send.")
        return

    with open(path, encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        print("File is empty, nothing to send.")
        return

    webhook = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook:
        print("DISCORD_WEBHOOK_URL not set")
        sys.exit(1)

    limit = 1900
    chunks = [text[i:i + limit] for i in range(0, len(text), limit)] or [""]

    for i, chunk in enumerate(chunks):
        payload = json.dumps({
            "username": "Monitor de Passagens",
            "content": chunk,
        }).encode("utf-8")
        req = urllib.request.Request(
            webhook,
            data=payload,
            headers={
                "Content-Type": "application/json",
                "User-Agent": "DiscordBot (https://github.com/CinthiaBecher/monitor-passagens, 1.0)",
            },
            method="POST",
        )
        with urllib.request.urlopen(req) as resp:
            print(f"Chunk {i+1}/{len(chunks)} sent, status {resp.status}")


if __name__ == "__main__":
    main()
