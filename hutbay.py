# -*- coding: utf-8 -*-
import scrapy
import requests
# from bs4 import BeautifulSoup as bs
from requests.compat import urljoin 



class hutbaySpider(scrapy.Spider):
    name = 'hutbay'

    start_urls = ['https://www.hutbay.com/property/torent']

    def parse(self, response):

        #Select each listing
        listing_selector = '.res-wrap'

        price_selector =  '.price span::text'
        unit_selector =  '.price span span::text' 
        location_selector =  '.addr span a::text'
        bedrooms_selector =  '.lsdown div span::text' 
        # baths_selector =  '.detailsContainer span:nth-of-type(2)::text' 
        # parking_selector  =  '.detailsContainer span:nth-of-type(3)::text' 
        # serviced_selector =  '.title.may-blank::text'
        state_selector = '.addr span a::text'

        # state = response.css(state_selector).extract_first()

        #Loop over each listing to extract features
        for prop in response.css(listing_selector):
            
        #Extracting the content using css selectors
            yield {
                'price': prop.css(price_selector).extract_first(),
                'unit' : prop.css(unit_selector).extract_first(),
                'location' : prop.css(location_selector).extract_first(),
                'bedrooms' : prop.css(bedrooms_selector).extract_first(),
                'baths' : None,
                'state' :  prop.css(state_selector).extract_first()
            }
    
        next_page_url = response.css(".pager a:last-of-type::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)


