# -*- coding: utf-8 -*-
import scrapy
import requests
# from bs4 import BeautifulSoup as bs
from requests.compat import urljoin


class privpropSpider(scrapy.Spider):
    name = 'privprop'

    start_urls = ['https://www.privateproperty.com.ng/property-for-rent']
    
    def parse(self, response):
        '''states = response.css(".search-right-snippet#area-sub-locations a::attr(href)").extract()
        for state in states:
            url = urljoin(response.url, state)
            yield scrapy.Request(url, callback=self.parse_state)

    def parse_state(self, response):'''
 
        #Select each listing
        listing_selector = '.result-card'

        #css selectors
        price_selector =  '.listing-price a::text'
        # unit_selector =  '.price::text' 
        location_selector =  '.full-address::text'
        bedrooms_selector =  '.listing-features .bedroom-attribute::text' 
        baths_selector =  '.listing-features .bathroom-attribute::text' 
        # parking_selector  =  '.detailsContainer span:nth-of-type(3)::text' 
        # serviced_selector =  '.features::text'
        state_selector = '.breadcrumb a:nth-of-type(2) span::text'

        state = response.css(state_selector).extract_first()

        #Loop over each listing to extract features
        for prop in response.css(listing_selector):
            
        #Extracting the content using css selectors
            yield {
                'price': prop.css(price_selector).extract_first(),
                'unit' : None,
                'location' : prop.css(location_selector).extract_first(),
                'bedrooms' : prop.css(bedrooms_selector).extract_first(),
                'baths' : prop.css(baths_selector).extract_first(),
                'parking_lots'  : None,
                'state' :  state
            }
    
        # Next page crawler
        next_page_url = response.css(".btn-next a.link-primary::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)


'''privprop_home = requests.get('https://www.privateproperty.com.ng/property-for-rent').text

soup = bs(privprop_home, 'lxml')

states_soup = soup.select('#area-sub-locations a ')

# states_url = {elem.get_text('title'):'https://www.privateproperty.com.ng' + elem.get('href') for elem in states_soup}

states = ['https://www.privateproperty.com.ng' + elem.get('href') for elem in states_soup]


# for state, url in states.items():

class privpropSpider(scrapy.Spider):
    name = 'privprop'

    start_urls = ['https://www.privateproperty.com.ng/property-for-rent']
    
    def parse(self, response):
        listings = response.css(".result-card .listing-price a::attr(href)").extract()
        for listing in listings:
            url = urljoin(response.url, listing)
            yield scrapy.Request(url, callback=self.parse_listing)

    def parse_listing(self, response):

        #Select each listing
        # listing_selector = '.result-card'

        #css selectors
        price_selector =  '.price::text'
        unit_selector =  '.price::text' 
        location_selector =  '.breadcrumb li:last-of-type span::text'
        bedrooms_selector =  '.features::text' 
        baths_selector =  '.features::text' 
        # parking_selector  =  '.detailsContainer span:nth-of-type(3)::text' 
        # serviced_selector =  '.features::text'
        state_selector = '.breadcrumb a:nth-of-type(2) span::text'

            
        #Extracting the content using css selectors
        yield {
            'price': response.css(price_selector).extract_first(),
            'unit' : response.css(unit_selector).extract_first(),
            'location' : response.css(location_selector).extract_first(),
            'bedrooms' : response.css(bedrooms_selector).extract_first(),
            'baths' : response.css(baths_selector).extract_first(),
            'parking_lots'  : None,
            'state' : response.css(state_selector).extract_first()
        }    

        # Next page crawler
        next_page_url = response.css(".btn-next a.link-primary::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse_listing)'''



        
        

