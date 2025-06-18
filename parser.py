
def parse_articles(raw):
    parsed = []
    for article in raw:
        parsed.append({
            "title": article.get("title", "").upper(),
            "summary": article.get("summary", ""),
            "link": article.get("link", ""),
            "published": article.get("published", ""),
        })
    return parsed

