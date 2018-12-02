# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup as bs



'''fibre_home = requests.get('https://www.fibre.com/units').text

soup = bs(fibre_home, 'lxml')

states_soup = soup.select('.citiesListContainer a ')

# states_url = {elem.get_text('title'):'https://www.fibre.com' + elem.get('href') for elem in states_soup}

states = ['https://www.fibre.com' + elem.get('href') for elem in states_soup]'''


# for state, url in states.items():

class fibreSpider(scrapy.Spider):
    name = 'fibre' 

    start_urls = ['https://www.fibre.com/units']

    def parse(self, response):
        #Select each listing
        listing_selector = '.sc-jwKygS.dUPdmg'

        price_selector =  '.sc-lhVmIH::text'
        # unit_selector =  '.sc-lhVmIH::text' 
        location_selector =  '.address::text'
        bedrooms_selector =  '.detailsContainer span:first-of-type::text' 
        baths_selector =  '.detailsContainer span:nth-of-type(2)::text' 
        parking_selector  =  '.detailsContainer span:nth-of-type(3)::text' 
        # serviced_selector =  '.title.may-blank::text'
        # furnished_selector = '.score.unvoted::text'
        state_selector = '.token-input-token-facebook::text'

        state = prop.css(state_selector).extract_first()

        #Loop over each listing to extract features
        for prop in response.css(listing_selector):
            
        #Extracting the content using css selectors
            yield {
                'price': prop.css(price_selector).extract_first(),
                'unit' : 'per Month',
                'location' : prop.css(location_selector).extract_first(),
                'bedrooms' : prop.css(bedrooms_selector).extract_first(),
                'baths' : prop.css(baths_selector).extract_first(),
                'parking_lots'  : prop.css(parking_selector).extract_first(),
                'state' :  state
            }
        
    
        next_page_url = response.css(".activeLink.right .anchorbutton ::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)


