url?=quotes.toscrape.com
N?=3

install:
	pip install -r requirements.txt

run:
	scrapy runspider websitegraph/spiders/graph_spider.py -a url=$(url) -a N=$(N)

.PHONY: install
