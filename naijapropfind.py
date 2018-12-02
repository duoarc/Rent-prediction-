# -*- coding: utf-8 -*-
import scrapy
import requests
# from bs4 import BeautifulSoup as bs


class naijapropfindSpider(scrapy.Spider):
    name = 'naijapropfind'

    start_urls = ['http://www.naijapropertyfinders.com/index.php/en/show/purpose/rent']

    def parse(self, response):
        #Select each listing
        listing_selector = '.facility'

        price_selector =  '.property-thumb-meta .property-price::text'
        # unit_selector =  '.sc-lhVmIH::text' 
        location_selector =  '.estate-description::text'
        bedrooms_selector =  '.bedrooms .content::text' 
        baths_selector =  '.bathrooms .content::text' 
        # parking_selector  =  '.detailsContainer span:nth-of-type(3)::text' 
        # serviced_selector =  '.title.may-blank::text'
        # furnished_selector = '.score.unvoted::text'
        # state_selector = '.token-input-token-facebook::text'

        #Loop over each listing to extract features
        for prop in response.css(listing_selector):
            
        #Extracting the content using css selectors
            yield {
                'price': prop.css(price_selector).extract_first(),
                'unit' : 'per Year',
                'location' : prop.css(location_selector).extract_first(),
                'bedrooms' : prop.css(bedrooms_selector).extract_first(),
                'baths' : prop.css(baths_selector).extract_first(),
                'state' :  None
            }
        
    
        '''next_page_url = response.css(".activeLink.right .anchorbutton ::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)


http://www.naijapropertyfinders.com_home = requests.get('http://www.naijapropertyfinders.com/index.php/en/show/purpose/rent').text

soup = bs(http://www.naijapropertyfinders.com_home, 'lxml')

states_soup = soup.select('.citiesListContainer a ')

# states_url = {elem.get_text('title'):'http://www.naijapropertyfinders.com' + elem.get('href') for elem in states_soup}

states = ['http://www.naijapropertyfinders.com' + elem.get('href') for elem in states_soup]'''





