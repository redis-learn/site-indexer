from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from src.website_dao import WebSiteDAO


class DocComSpider(CrawlSpider):
    name = "docs-redis-com"
    domain = "docs.redis.com"
    allowed_domains = [domain]
    start_urls = ["https://{}".format(domain)]
    categories = ["enterprise"]
    title_selector = "h1"
    text_selector = "div.main-content-left, .home-options"
    rules = (Rule(LinkExtractor(), callback="parse_items", follow=True),)


    def parse_items(self, response):
        site = WebSiteDAO(self.curr_idx_id, response.url, self.categories, response.body, self.text_selector,
                          self.title_selector)
        if site.text:
            site.index()