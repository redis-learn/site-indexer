import time
from src.crawler import Crawler
from src.doc_com_spider import DocComSpider



if __name__ == "__main__":
    crawler = Crawler(DocComSpider)
    crawler.run()