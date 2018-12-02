# -*- coding: utf-8 -*-
import scrapy
import requests
# from bs4 import BeautifulSoup as bs
from requests.compat import urljoin 




'''trovit_home = requests.get('https://homes.trovit.ng/rent').text

soup = bs(trovit_home, 'lxml')

states_soup = soup.select('qa-city a ')

# states_url = {elem.get_text('title'):'https://homes.trovit.ng' + elem.get('href') for elem in states_soup}

states = ['https://homes.trovit.ng' + elem.get('href') for elem in states_soup]'''


class trovitSpider(scrapy.Spider):
    name = 'trovit'

    start_urls = ['https://homes.trovit.ng/rent']

    def parse(self, response):
        states = response.css(".qa-city a ::attr(href)").extract()
        for state in states:
            url = urljoin(response.url, state)
            yield scrapy.Request(url, callback=self.parse_state)

    def parse_state(self, response):
        #Select each listing
        listing_selector = '.ng.js-item'

        price_selector =  '.amount::text'
        # unit_selector =  '.price+span::text' 
        location_selector =  '.details h5 span::text'
        bedrooms_selector =  '.price+div.property span::text'
        # bedrooms_selector =  '.features div.property:first-of-type span::text' 
        baths_selector =  '.features div.property:nth-of-type(2) span::text' 
        # parking_selector  =  '.detailsContainer span:nth-of-type(3)::text' 
        # serviced_selector =  '.title.may-blank::text'
        # furnished_selector = '.score.unvoted::text'
        state_selector = 'qa-bc-current::text'

        state = response.css(state_selector).extract_first()

        #Loop over each listing to extract features
        for prop in response.css(listing_selector):
            
        #Extracting the content using css selectors
            yield {
                'price': prop.css(price_selector).extract_first(),
                'unit' : 'per Year',
                'location' : prop.css(location_selector).extract_first(),
                'bedrooms' : prop.css(bedrooms_selector).extract_first(),
                'baths' : prop.css(baths_selector).extract_first(),
                'state' : state
            }
        
    
        next_page_url = response.css(".qa-p-next ::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse_state)

