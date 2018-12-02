# -*- coding: utf-8 -*-
import scrapy
import requests
# from bs4 import BeautifulSoup as bs
from requests.compat import urljoin 



class Prop24Spider(scrapy.Spider):
    name = 'prop24'

    start_urls = ['https://www.property24.com.ng/to-rent/']

    def parse(self, response):
        states = response.css(".citiesListContainer a ::attr(href)").extract()
        for state in states:
            url = urljoin(response.url, state)
            yield scrapy.Request(url, callback=self.parse_state)

    def parse_state(self, response):
 
        #Select each listing
        listing_selector = '.propertyTileWrapper'

        price_selector =  '.price::text'
        unit_selector =  '.price+span::text' 
        location_selector =  '.address::text'
        bedrooms_selector =  '.detailsContainer span:first-of-type::text' 
        baths_selector =  '.detailsContainer span:nth-of-type(2)::text' 
        parking_selector  =  '.detailsContainer span:nth-of-type(3)::text' 
        # serviced_selector =  '.title.may-blank::text'
        state_selector = '.breadcrumbs li:last-of-type a::text'

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
                'state' :  state
            }
    
        next_page_url = response.css(".activeLink.right .anchorbutton ::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse_state)


''' 
prop24_home = requests.get('https://www.property24.com.ng/to-rent/').text

soup = bs(prop24_home, 'lxml')

states_soup = soup.select('.citiesListContainer a ')

# states_url = {elem.get_text('title'):'https://www.property24.com.ng' + elem.get('href') for elem in states_soup}

states = ['https://www.property24.com.ng' + elem.get('href') for elem in states_soup]
'''