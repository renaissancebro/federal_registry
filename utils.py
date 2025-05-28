import json
import os
from datetime import datetime
import re
from urllib.parse import urlparse
# Save jsons!

def save_to_json(data, base_path):
    date_str = datetime.now().strftime("%Y-%m-%d")
    full_path = f"{date_str}_{base_path}.json"

    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        json.dump(data, f, indent=2 )
        print(f"[+] Saved {len(data)} items to {base_path}")

    print(f"[utils] Saved to {full_path}")


def sanitize_url_for_filename(url):
    parsed = urlparse(url)
    path = parsed.netloc + parsed.path  # combine domain + path
    path = re.sub(r'^www\.', '', path)  # remove www
    path = re.sub(r'[^a-zA-Z0-9]+', '_', path)  # replace non-alphanumerics with 
    print(path)_
    return path.strip('_').lower()
