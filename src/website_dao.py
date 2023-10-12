from src.website import WebSite
from src.config import CFG as cfg
from vectordb import VectorDB
from models.txtmodel import TextModel
import redis

IT_SEG = "segment"
IT_SITE = "site"


class WebSiteDAO(WebSite):
    def __init__(self, idx_id, url, categories, content, text_selector, title_selector="h1"):
        super().__init__(url, categories, content, text_selector, title_selector, title_selector)
        model = TextModel()
        self.site_idx = "{}s:{}".format(IT_SITE, idx_id)
        self.seg_idx = "{}s:{}".format(IT_SEG, idx_id)
        self.site_db = VectorDB(cfg["db_host"], cfg["db_port"], cfg["db_pwd"], model)
        self.segment_db = VectorDB(cfg["db_host"], cfg["db_port"], cfg["db_pwd"], model)

        try:
            self.site_db.create_index(index_name=self.site_idx, schema={"id": "TagField", "url": "TextField",
                                                                        "checksum": "TagField",
                                                                        "categories": "TagField",
                                                                        "text": "TextField", "title": "TextField",
                                                                        "vec": "VectorField", "time": "NumericField"},
                                      item_type=IT_SITE)

            self.segment_db.create_index(index_name=self.seg_idx, schema={"id": "TagField", "site": "TagField",
                                                                          "segment": "NumericField",
                                                                          "text": "TextField",
                                                                          "vec": "VectorField",
                                                                          "time": "NumericField"},

                                         item_type=IT_SEG)

        except redis.exceptions.ResponseError as e:
            if "Index already exists" in str(e):
                pass
            else:
                raise e

    def index(self):
        if self.text:
            self.site_db.add(IT_SITE, self.id, {"id": self.id, "url": self.url, "checksum": self.checksum,
                                                "categories": self.categories, "text": self.text, "title": self.title},
                             self.text)
            i = 0
            for s in self.segments:
                seg_id = "{}:{}".format(self.id, i)
                self.segment_db.add(IT_SEG, seg_id, {"id": seg_id, "site": self.id, "segment": i, "text": s}, s)
                i = i + 1