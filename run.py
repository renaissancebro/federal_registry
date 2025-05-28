from fetchers.reddit_fetcher import get_reddit_articles
from fetchers.rss_fetcher import fetch_rss_feed
from parser import parse_articles
from utils import save_to_json



def run_reddit():
    raw = get_reddit_articles(subreddit="technology", limit = 5)
    parsed = parse_articles(raw)
    save_to_json(parsed, "output/articles.json")

def run_rss(url):
    fetched_info = fetch_rss_feed(url)
    parsed = parse_articles(fetched_info)
    save_to_json(parsed, "output/articles.json")


def run():
    run_reddit()

    run_rss("https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml")




if __name__ == "__main__":
    run()

