from fetchers import get_articles  # you'll define this
from parser import parse_articles
from utils import save_to_json

def run():
    raw = get_articles(subreddit="technology", limit = 5)
    parsed = parse_articles(raw)
    save_to_json(parsed, "output/articles.json")

if __name__ == "__main__":
    run()

