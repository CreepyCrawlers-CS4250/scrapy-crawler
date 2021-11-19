from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Cpp(CrawlSpider):
    name = "cpp"
    allowed_domains = ["asi.cpp.edu"]
    start_urls = ["https://asi.cpp.edu/"]
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
            if "asi.cpp.edu" in url:
                links.append(url)

        return {"url": response.url, "links": links}