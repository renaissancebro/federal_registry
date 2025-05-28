

def parse_articles(raw):
    return [[article["title"].upper(), article.get("summary")] for article in raw]

