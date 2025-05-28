import requests

def get_reddit_articles(subreddit="technology", limit=10):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit={limit}"
    headers = {"User-Agent": "Mozilla/5.0"}  # Reddit blocks non-UA requests
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        print(f"[reddit_fetcher] Failed to fetch: {res.status_code}")
        return []

    data = res.json()
    posts = data["data"]["children"]

    articles = []
    for post in posts:
        d = post["data"]
        articles.append({
            "title": d["title"],
            "link": f"https://reddit.com{d['permalink']}",
            "score": d["score"],
            "author": d["author"]
        })

    print(f"[reddit_fetcher] Fetched {len(articles)} posts from r/{subreddit}")
    for article in articles:
        print(article)
    return articles
if __name__ == "__main__":
    get_reddit_articles()

