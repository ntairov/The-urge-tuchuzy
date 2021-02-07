
# tuchuzy_scrapy
Web Scraping Trial task for the urge:

1. Build a Scrapy spider by making use of the 'CrawlSpider'.
2. Use rules to traverse from https://www.tuchuzy.com through to the category pages, and then yield the products found on the product pages.
3. Make good use of the scrapy 'Item Loader' to create items from the page.
4. Use processors to clean some of the data fields.
4. Make use of the Scrapy settings to limit the number of items crawled to 100. 

# Required fields:
- Product Name [Titlecase]
- Brand [Uppercase]
- Category [Separate categories by >> ]
- Image links [ These should be the largest size images you are able to obtain]
- Price [Remove $ and return in decimals i.e $99.95 should be returned as 9995 ]
- Sale Price [If available, remove $ and return in decimals i.e $99.95 should be returned as 9995 ]

Once complete, please return the output along with the code written. 

Your attempt will be judged based on;
- Efficiency of the crawler.
- Code readability and maintainability.
- Well structured and documented.
- Effective and well versed use of the framework.

## How to run locally
 `python3 -m venv env`

 `source env/bin/activate`

 `python pip install -r requirements.txt` 

### Run to start crawling from www.tuchuzy.com/

```
 scrapy crawl tuchuzy -O tuchuzy.json -a tag=shop_store
```
