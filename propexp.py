# -*- coding: utf-8 -*-
import scrapy
import requests
# from bs4 import BeautifulSoup as bs
# from requests.compat import urljoin 


class propexpSpider(scrapy.Spider):
    name = 'propexp'

    start_urls = ['https://propertyexpert.ng/for-rent-property/']

    def parse(self, response):
 
        #Select each listing
        listing_selector = '.archive-property-item'

        price_selector =  '.property-item-details h3.property-item-price::text'
        unit_selector =  '.property-item-details h3.property-item-price span.property-item-per::text' 
        location_selector =  '.property-item-details h4.property-location::text'
        bedrooms_selector =  '.property-item-stats-holder .left li:first-of-type span::text' 
        baths_selector =  '.property-item-stats-holder .left li:nth-of-type(2) span::text' 
        parking_selector  =  '.detailsContainer span:nth-of-type(3)::text' 
        # serviced_selector =  '.title.may-blank::text'
        state_selector = '.property-item-details h4.property-location::text'

        # state = response.css(state_selector).extract_first()

        #Loop over each listing to extract features
        for prop in response.css(listing_selector):
            
        #Extracting the content using css selectors
            yield {
                'price': prop.css(price_selector).extract_first(),
                'unit' : prop.css(unit_selector).extract_first(),
                'location' : prop.css(location_selector).extract_first(),
                'bedrooms' : prop.css(bedrooms_selector).extract_first(),
                'baths' : prop.css(baths_selector).extract_first(),
                'parking_lots'  : None,
                'state' :  prop.css(state_selector).extract_first()
            }
    
        next_page_url = response.css(".next ::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)


