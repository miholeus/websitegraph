# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlparse


class GraphSpider(scrapy.Spider):
    """
    Looks through page and fetches urls recursively
    """
    name = 'graph_spider'
    depth = 3
    start_url = None

    def __init__(self, name=None, **kwargs):
        super().__init__(name=None, **kwargs)
        domain = getattr(self, 'url', None)
        if domain is None:
            raise ValueError("Url is not set")
        if not domain.startswith('http://') or not domain.startswith('https://'):
            domain = '{scheme}://{domain}'.format(scheme='http', domain=domain)
        # we start from given url
        self.start_url = domain
        if urlparse(domain).hostname is None:
            raise ValueError("Hostname is not valid")
        # set allowed domain to 1 host only
        self.allowed_domains = [urlparse(domain).hostname]

    def start_requests(self):
        depth = getattr(self, 'N', None)
        if depth is not None:
            self.depth = depth

        yield scrapy.Request(self.start_url, self.parse)

    # def __init__(self, *args, **kwargs):
    #     logger = logging.getLogger('scrapy.spidermiddlewares.httperror')
    #     logger.setLevel(logging.ERROR)
    #     super().__init__(*args, **kwargs)

    def parse(self, response):
        base_url = response.url.rstrip('/')
        urls = response.css('a::attr(href)').extract()
        print("base url is " + base_url)
        for url in urls:
            if response.urljoin(url).rstrip('/') == base_url:
                continue
            yield {
                'base_url': base_url,
                'url': url
            }
        # another loop is done because we want to save the order of fetched urls
        for url in urls:
            yield response.follow(url, callback=self.parse)

