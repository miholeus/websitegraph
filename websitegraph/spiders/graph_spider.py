# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlparse
from websitegraph.items import WebsitegraphItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class GraphSpider(CrawlSpider):
    """
    Looks through page and fetches urls recursively
    """
    name = 'graph_spider'
    start_url = None

    custom_settings = {
        'DEPTH_LIMIT': 5
    }

    rules = (
        Rule(LinkExtractor(allow=("", ), ), callback="parse_items",
             follow=True),
    )

    def __init__(self, **kwargs):
        # logger = logging.getLogger('scrapy.spidermiddlewares.httperror')
        # logger.setLevel(logging.ERROR)

        super().__init__(name=None, **kwargs)

    def get_allowed_domains(self):
        domain = getattr(self, 'url', None)
        if domain is None:
            raise ValueError("Url is not set")
        if not domain.startswith('http'):
            domain = '{scheme}://{domain}'.format(scheme='http', domain=domain)
        # we start from given url
        self.start_url = domain
        if urlparse(domain).hostname is None:
            raise ValueError("Hostname is not valid")
        # set allowed domain to 1 host only
        print("allowed domain " + urlparse(domain).hostname)
        return [urlparse(domain).hostname]

    def start_requests(self):
        self.get_allowed_domains()

        yield scrapy.Request(self.start_url, self.parse)

    def _compile_rules(self):
        extractor = LinkExtractor(allow=("", ), allow_domains=self.get_allowed_domains(), )
        self.rules[0].link_extractor = extractor
        super()._compile_rules()

    def parse_items(self, response):
        items = []
        item = WebsitegraphItem()
        item["depth"] = response.meta["depth"]
        item["current_url"] = response.url
        referring_url = response.request.headers.get('Referer', None)
        if referring_url is not None:
            try:
                referring_url = referring_url.decode("utf-8")
            except AttributeError:
                pass
        item["referring_url"] = referring_url
        items.append(item)
        return items

