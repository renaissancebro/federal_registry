import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    return [{
        "title": entry.title,
	    "link": entry.link,
	    "published": entry.published,
	    "summary": entry.summary
	} for entry in feed.entries]
