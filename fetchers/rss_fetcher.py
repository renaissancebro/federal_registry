import feedparser

def fetch_rss_feed(url, limit=5):
    feed = feedparser.parse(url)
    #articles = []
    return [{
        "title": entry.title,
	    "link": entry.link,
	    "published": entry.published,
	    "summary": entry.summary
	} for entry in feed.entries]
