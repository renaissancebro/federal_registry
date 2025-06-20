from fetchers.rss_fetcher import fetch_rss_feed
from parser import parse_articles
from utils import save_to_json, sanitize_url_for_filename
from monitor_utils.check import save_entry_if_new

def check_rss_feed(url, table="federal_registry"):
    entries = fetch_rss_feed(url, limit=1)
    if not entries:
        print("[!] No entries found.")
        return False

    entry = parse_articles(entries)[0]
    site = sanitize_url_for_filename(url)
    save_to_json([entry], f"output/rss/{site}")

    if save_entry_if_new(entry, table):
        print(f"[+] New entry saved for {table}")
        return True
    else:
        print(f"[-] No new entry for {table}")
        return False

