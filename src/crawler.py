from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from src.config import CFG as cfg
from vectordb import VectorDB
import time

'''
A crawler that runs the spider that is passed over and then checks if there are any outdated links
'''
class Crawler:
    def __init__(self, spider):
        self.spider = spider
        self.config_db = VectorDB(cfg["db_host"], cfg["db_port"], cfg["db_pwd"]).con

    def _run_spider(self):
        self.config_db.set("cfg:{}".format(int(time.time()*1000000)))
        settings = get_project_settings()
        process = CrawlerProcess(settings)
        process.crawl(self.spider)
        process.start()

    def _clean(self):
        # TODO: Remove old sites
        # - For each site check if the site is still reachable
        # - If the status isn't 200, then remove the site, it's vector embedding and all the segments from the search
        #   index
        return True


    def run(self):
        self._run_spider()
        self._clean()

