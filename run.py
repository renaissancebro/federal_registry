from fetchers.reddit_fetcher import get_reddit_articles
from fetchers.rss_fetcher import fetch_rss_feed
from parser import parse_articles
from utils import save_to_json
from datetime import datetime
from utils import sanitize_url_for_filename

tracked_source = []

def run_reddit():
    raw = get_reddit_articles(subreddit="technology", limit = 5)
    parsed = parse_articles(raw)
    save_to_json(parsed, "output/reddit/reddit_articles.json")

def run_rss(url):
    fetched_info = fetch_rss_feed(url)
    site = sanitize_url_for_filename(url)
    parsed = parse_articles(fetched_info)
    save_to_json(parsed, f"output/rss/{site}.json")

def run():
    run_reddit()

    # RSS sites
    run_rss("https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml")
    run_rss("https://www.technologyreview.com/feed/")
    run_rss("https://techcrunch.com/feed/")
    run_rss("http://feeds.reuters.com/reuters/worldNews")


if __name__ == "__main__":
    run()

