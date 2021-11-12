from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Centennial(CrawlSpider):
    name = "centennial"
    allowed_domains = ["centennial.cnusd.k12.ca.us"]
    start_urls = ["https://centennial.cnusd.k12.ca.us/"]
    rules = [
        Rule(
            LinkExtractor(
                allow=(r".*"),
            ),
            callback="parse_items",
            follow=True,
        )
    ]

    def parse_items(self, response):
        # Store all of this page's links in an array
        links = []
        for link in response.css("a"):
            href = link.attrib["href"]

            # Resolve relative links
            url = response.urljoin(href)

            # ignore the other domains in the links list
            if "centennial.cnusd.k12.ca.us" in url and not "mailto:" in url:
                links.append(url)

        return {"url": response.url, "links": links}