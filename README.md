Website scraper
=========

Features:

1. Parse selected url with desired depth
2. Build graph of parsed urls and calculates graph's diameter

## Installation

Run

```make install```

## Usage 

### Build graph

First of all you need to run spider. It can be done with the following command
 
```make run```.

You can also set url and the depth level while scraping with command

```make run url=<url> N=<depth>```.

If url is not set, then default one will be used `quotes.toscrape.com`, default depth is `N=5`.

You can also set output file for `spider` by setting `output` param

```make run url=<url> N=<depth> output=<output.json>```.

Script results will be placed in `output` file. Different output formats
are supported, but graph builder uses only `json` now.

If you get hundred megabytes or gigabyte file, then it is wiser to set `jl` (json lines) format,
but graph builder needs to be rewritten in that case.

For simplicity lets use `json` for builder.

### Calculate diameter

Run command

```python3 diameter.py <output.json>```

The result will be something like this

```
Diameter is: 9
Url path is: http://quotes.toscrape.com -> http://quotes.toscrape.com/page/2/ -> http://quotes.toscrape.com/page/3/ -> http://quotes.toscrape.com/page/4/ -> http://quotes.toscrape.com/page/5/ -> http://quotes.toscrape.com/page/6/ -> http://quotes.toscrape.com/page/7/ -> http://quotes.toscrape.com/page/8/ -> http://quotes.toscrape.com/page/9/ -> http://quotes.toscrape.com/page/10/

```
