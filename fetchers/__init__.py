#from .rss_fetcher import get_articles as get_rss_articles
# add more as needed

# (Optional) You can define a router for convenience
def get_articles(source=None, limit=5, **kwargs):
    #     url = kwargs.get("url")
    #     if not url:
    #         raise ValueError("RSS source requires 'url' argument.")
    #     return get_rss_articles(url=url, limit=limit)
        # TEMP mock — fallback
        return [
            {"title": "News 1", "link": "https://example.com/news1"},
            {"title": "News 2", "link": "https://example.com/news2"}
        ]
