from src.doc_com_spider import DocComSpider
from src.crawler import Crawler


if __name__ == "__main__":
    crawler = Crawler(DocComSpider)
    crawler.run()