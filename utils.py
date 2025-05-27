import json
import os


def save_to_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2 ) 
        print(f"[+] Saved {len(data)} items to {path}")

