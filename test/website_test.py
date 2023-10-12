import requests
from src.website import WebSite


TEXT_SELECTOR = "div.main-content-left, .home-options"

def test_content_site():
    url = "https://docs.redis.com/latest/rc/security/vpc-peering/"
    content = requests.get(url).content.decode("utf-8")
    site = WebSite(url, ["operators"], content, TEXT_SELECTOR)
    print(site.text)
    assert site.title == "Enable VPC peering"
    assert site.text.strip().endswith('the private endpoint.')
    assert len(site.segments) == 2

def test_home_site():
    url = "https://docs.redis.com/latest/index.html"
    content = requests.get(url).content.decode("utf-8")
    site = WebSite(url, ["operators"], content, TEXT_SELECTOR)
    assert site.title == "Documentation"
    assert site.text.strip().endswith('FAQs')
    assert len(site.segments) == 0

if __name__ == "__main__":
    test_content_site()
    test_home_site()

