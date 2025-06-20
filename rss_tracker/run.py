from core import check_rss_feed

def run():
    urls = ["https://www.federalregister.gov/api/v1/documents.rss?conditions[sections][]=documents&order=newest"]
    for url in urls:
        check_rss_feed(url)

if __name__ == "__main__":
    run()
 
