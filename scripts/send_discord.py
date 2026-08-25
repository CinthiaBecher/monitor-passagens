import sys
import os
import json
import urllib.request

LIMIT = 1900


def split_message(text):
    lines = text.split("\n")
    chunks = []
    current = []
    current_len = 0

    def flush():
        nonlocal current, current_len
        if not current:
            return
        chunks.append("\n".join(current))
        current = []
        current_len = 0

    for line in lines:
        line_len = len(line) + 1
        if current and current_len + line_len > LIMIT:
            flush()
        current.append(line)
        current_len += line_len

    flush()
    return [c for c in chunks if c.strip()]


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

    chunks = split_message(text) or [""]

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
