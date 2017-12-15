# -*- coding: utf-8 -*-
import scrapy


class RlmoviespiderSpider(scrapy.Spider):
    name = "rlMovieSpider"
    allowed_domains = ["http://subhd.com/db0/movie"]
    start_urls = ['http://http://subhd.com/db0/movie/']

    def parse(self, response):
        pass
