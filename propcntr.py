# -*- coding: utf-8 -*-
import scrapy
import requests
# from bs4 import BeautifulSoup as bs


class propcntrSpider(scrapy.Spider):
    name = 'propcntr'

    start_urls = ['https://www.nigeriapropertycentre.com/for-rent']

    def parse(self, response):
        #Select each listing
        listing_selector = '.property-list' 

        price_selector =  'span.price:nth-of-type(2)::text'
        unit_selector =  '.period::text' 
        location_selector =  'address strong::text'
        bedrooms_selector =  '.wp-block-footer .aux-info li:first-of-type span:first-of-type::text' 
        baths_selector =  '.wp-block-footer .aux-info li:nth-of-type(2) span:first-of-type::text' 
        parking_selector  =  '.wp-block-footer .aux-info li:nth-of-type(4) span:first-of-type::text' 
        # serviced_selector =  '.title.may-blank::text'
        # furnished_selector = '.score.unvoted::text'
        state_selector = '.search-title::text'

        state = response.css(state_selector).extract_first()

        #Loop over each listing to extract features
        for prop in response.css(listing_selector):
            
        #Extracting the content using css selectors
            yield {
                'price': prop.css(price_selector).extract_first(),
                'unit' : prop.css(unit_selector).extract_first(),
                'location' : prop.css(location_selector).extract_first(),
                'bedrooms' : prop.css(bedrooms_selector).extract_first(),
                'baths' : prop.css(baths_selector).extract_first(),
                'parking_lots'  : prop.css(parking_selector).extract_first(),
                'state' : state 
            }
            
        
        next_page_url = response.css(".pPagination li:nth-last-of-type(2) a::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

