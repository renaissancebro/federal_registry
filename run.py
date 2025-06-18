from fetchers.rss_fetcher import fetch_rss_feed
from parser import parse_articles
from utils import save_to_json
from datetime import datetime
from utils import sanitize_url_for_filename
from monitor_utils.check import check_last_policy

"""
Flow

Grabs rss entries and creates sqlite, periodically runs checker to see if newest entry on rss is different than on the database, updates
databse if different entry added, email notifier/webhook triggered

Verbs and Nouns

RSS data -> SQlite table -> Newly discovered entry found from RSS -> SQLite updated table -> email message template -> sent email

"""

tracked_source = []


def run_rss(url):
    newest_entry = ...
    fetched_info = fetch_rss_feed(url)
    site = sanitize_url_for_filename(url)
    parsed = parse_articles(fetched_info)
    save_to_json(parsed, f"output/rss/{site}.json")

def run():

    # RSS sites
    run_rss("https://www.federalregister.gov/api/v1/documents.rss?conditions[sections][]=documents&order=newest")


if __name__ == "__main__":
    run()

