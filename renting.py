# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup as bs


'''
renting_home = requests.get('https://www.renting.ng/properties.html').text

soup = bs(renting_home, 'lxml')

states_soup = soup.select('.citiesListContainer a ')

# states_url = {elem.get_text('title'):'https://www.renting.ng.ng' + elem.get('href') for elem in states_soup}

states = ['https://www.renting.ng.ng' + elem.get('href') for elem in states_soup]'''


# for state, url in states.items():

class rentingSpider(scrapy.Spider):
    name = 'renting'

    start_urls = ['https://www.renting.ng/properties.html']

    def parse(self, response):
        #Select each listing
        listing_selector = '.col-md-4'

        price_selector =  '.rent-pro::text'
        unit_selector =  '.rent-pro::text' 
        location_selector =  '.city-label::text'
        bedrooms_selector =  '.inner-data li:nth-of-type(2) .action::text' 
        # baths_selector =  '.inner-data li:nth-of-type(3) .action::text' 
        # parking_selector  =  '.inner-data li:nth-of-type(3) .action::text' 
        # serviced_selector =  '.title.may-blank::text'
        # furnished_selector = '.score.unvoted::text'
        state_selector = '.city-label::text'

        state = response.css(state_selector).extract_first()

        #Loop over each listing to extract features
        for prop in response.css(listing_selector):
            
        #Extracting the content using css selectors
            yield {
                'price': prop.css(price_selector).extract_first(),
                'unit' : prop.css(unit_selector).extract_first(),
                'location' : prop.css(location_selector).extract_first(),
                'bedrooms' : prop.css(bedrooms_selector).extract_first(),
                'baths' : None,
                'state' :  None
            }
        
    
        next_page_url = response.css(".pagination li:last-of-type a::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

