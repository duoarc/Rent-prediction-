# -*- coding: utf-8 -*-
import scrapy
import requests
# from bs4 import BeautifulSoup as bs



'''proppro_home = requests.get('https://www.propertypro.ng/property-for-rent/').text

soup = bs(proppro_home, 'lxml')

states_soup = soup.select('.states a ')

states = {elem.get_text('title'):'https://www.propertypro.ng' + elem.get('href') for elem in states_soup}'''


# for state, url in states.items():

class PropProSpider(scrapy.Spider):
    name = 'proppro'

    start_urls = ['https://www.propertypro.ng/property-for-rent/']

    def parse(self, response):
        #Select each listing
        listing_selector = '.property-bg'

        price_selector =  '.prop-price span:nth-of-type(2)::text'
        # unit_selector =  '.price+span::text' 
        location_selector =  'h3.pro-location::text'
        bedrooms_selector =  '.prop-aminities span:first-of-type::text' 
        baths_selector =  '.prop-aminities span:nth-of-type(2)::text' 
        # parking_selector  =  '.detailsContainer span:nth-of-type(3)::text' 
        # serviced_selector =  '.title.may-blank::text'
        # furnished_selector = '.score.unvoted::text'
        state_selector = '.search-title::text'

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
                'state' : None
            }
            
        
        next_page_url = response.css("li.page-item:last-of-type a::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

