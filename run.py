from fetchers.rss_fetcher import fetch_rss_feed
from parser import parse_articles
from utils import save_to_json
from datetime import datetime
from utils import sanitize_url_for_filename

tracked_source = []


def run_rss(url):
    fetched_info = fetch_rss_feed(url)
    site = sanitize_url_for_filename(url)
    parsed = parse_articles(fetched_info)
    save_to_json(parsed, f"output/rss/{site}.json")

def run():

    # RSS sites
    run_rss("https://www.federalregister.gov/api/v1/documents.rss?conditions[sections][]=documents&order=newest")


if __name__ == "__main__":
    run()

