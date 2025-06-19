from fetchers.rss_fetcher import fetch_rss_feed
from parser import parse_articles
from utils import save_to_json, sanitize_url_for_filename
from monitor_utils.check import save_entry_if_new

table = "federal_registry"
site = table

def get_last_rss_entry(url):
    entries = fetch_rss_feed(url, limit=1)
    if not entries:
        print("[!] No entries found.")
        return

    entry = parse_articles(entries)[0]  # Assumes parse_articles returns list of dicts
    site = sanitize_url_for_filename(url)
    save_to_json([entry], f"output/rss/{site}")

    # Save if it's new
    if save_entry_if_new(entry, table):
        print(f"[+] New entry saved for {table}")
        # TODO: trigger email/webhook here
    else:
        print(f"[-] No new entry for {table}")

def run():
    rss_sources = [
        "https://www.federalregister.gov/api/v1/documents.rss?conditions[sections][]=documents&order=newest"
        # Add more RSS URLs as needed
    ]
    for url in rss_sources:
        get_last_rss_entry(url)

if __name__ == "__main__":
    run()

