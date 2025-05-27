

def parse_articles(raw):
    return [article["title"].upper() for article in raw]

