import feedparser

def fetch_rss_feed(url, limit=5):
    # Parses the RSS feed from given url
    feed = feedparser.parse(url)
    #articles = []
    return [{
        "title": entry.title,
	    "link": entry.link,
        "published": entry.get("published", "N/A"),
	    "summary": entry.get("summary", "")
    } for entry in feed.entries[:limit]]
