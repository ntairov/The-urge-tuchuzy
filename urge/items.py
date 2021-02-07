# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import re
from typing import Optional
from urllib.parse import urljoin

import scrapy
from itemloaders.processors import TakeFirst, Join, Compose, Identity, MapCompose
from scrapy.loader import ItemLoader


class UrgeItem(scrapy.Item):
    # define the fields for your item here like:
    product_name = scrapy.Field(serializer=str)
    product_brand = scrapy.Field(serializer=str)
    product_category = scrapy.Field(serializer=str)
    product_img_links = scrapy.Field(serializer=list)
    product_price = scrapy.Field(serializer=int)
    product_sale_price = scrapy.Field(serializer=int)


price_pattern = re.compile(r'\d+', re.I)


def filter_price(value: str) -> Optional[int]:
    """
    Remove '$' and return in decimals i.e $99.95 should be returned as 9995
    :param value:
    :return:
    """
    price = price_pattern.findall(value)
    if price:
        return int(''.join(price))


def normalize_taxonomy(categories: list) -> list:
    """
    Removes redundant characters like: \n\t\n\t /
    :param categories:
    :return:
    """
    taxonomy = [x for x in categories if x.strip() and x.strip() != '/']
    return taxonomy


def generate_img_url(urls: list) -> list:
    """
    Joins raw url to base url "https://www.tuchuzy.com/".
    :param urls:
    :return:
    """
    base_url = 'https://www.tuchuzy.com/'
    image_links = [urljoin(base_url, x) for x in urls]
    return image_links


class ProductLoader(ItemLoader):
    default_output_processor = TakeFirst()

    product_name_in = MapCompose(str.title)
    product_brand_in = MapCompose(str.upper)
    product_category_in = Compose(normalize_taxonomy)
    product_category_out = Join(separator=" >> ")
    product_price_in = MapCompose(filter_price)
    product_sale_price_in = MapCompose(filter_price)
    product_img_links_in = Compose(generate_img_url)
    product_img_links_out = Identity()
