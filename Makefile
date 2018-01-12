url?=quotes.toscrape.com
N?=3

ifneq ($(output),)
	outfile=-o $(output)
else
	outfile=
endif

install:
	pip install -r requirements.txt

run:
	scrapy runspider websitegraph/spiders/graph_spider.py -a url=$(url) -s DEPTH_LIMIT=$(N) $(outfile)


.PHONY: install run
