# import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from urllib.parse import urljoin
import re


class Cpp(CrawlSpider):
    name = "cpp"
    allowed_domains = ["cpp.edu"]
    start_urls = ["https://www.cpp.edu/"]
    rules = [
        Rule(
            LinkExtractor(
                allow=(r".*"),
                # deny=(r"mailto:(.*)"),
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
            if (not "https://" in href) and (not "http://" in href):
                url = response.urljoin(href)

            # ignore the other domains in the links list
            if "cpp.edu" in url and not "mailto:" in url:
                links.append(url)

        yield {"url": response.url, "links": links}
