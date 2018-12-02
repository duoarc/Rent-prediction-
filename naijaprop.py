# -*- coding: utf-8 -*-
import scrapy
import requests
# from bs4 import BeautifulSoup as bs





# for state, url in states.items():

class naijapropSpider(scrapy.Spider):
    name = 'naijaprop'

    start_urls = ['http://www.naijaproperty.com/search-results/?action=search&QuickSearchCity%5Bequal%5D=&QuickSearchState%5Bequal%5D=&QuickSearchPrice%5Bnot_less%5D=&QuickSearchPrice%5Bnot_more%5D=&QuickSearchRent%5Bnot_less%5D=&QuickSearchRent%5Bnot_more%5D=&category_sid%5Btree%5D%5B%5D=2']

    def parse(self, response):
        #Select each listing
        listing_selector = '.searchResultItemWrapper'

        price_selector =  '.fieldValueRent.money::text'
        # unit_selector =  '.price+span::text' 
        location_selector =  '.fieldValueAddress::text'
        bedrooms_selector =  '.fieldValueBeds::text' 
        baths_selector =  '.fieldValueBaths::text' 
        # parking_selector  =  '.detailsContainer span:nth-of-type(3)::text' 
        # serviced_selector =  '.title.may-blank::text'
        # furnished_selector = '.score.unvoted::text'
        state_selector = '.fieldValueState::text'


        #Loop over each listing to extract features
        for prop in response.css(listing_selector):
            
        #Extracting the content using css selectors
            yield {
                'price': prop.css(price_selector).extract_first(),
                'unit' : 'per Year',
                'location' : prop.css(location_selector).extract_first(),
                'bedrooms' : prop.css(bedrooms_selector).extract_first(),
                'baths' : prop.css(baths_selector).extract_first(),
                'state' :  prop.css(state_selector).extract_first()
            } 
        
    
        next_page_url = response.css(".nextPageSelector::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)




'''naijaprop_home = requests.get('http://www.naijaproperty.com/search-results/?action=search&QuickSearchCity%5Bequal%5D=&QuickSearchState%5Bequal%5D=&QuickSearchPrice%5Bnot_less%5D=&QuickSearchPrice%5Bnot_more%5D=&QuickSearchRent%5Bnot_less%5D=&QuickSearchRent%5Bnot_more%5D=&category_sid%5Btree%5D%5B%5D=2').text

soup = bs(naijaprop_home, 'lxml')

states_soup = soup.select('.citiesListContainer a ')

# states_url = {elem.get_text('title'):'http://www.naijaproperty.com' + elem.get('href') for elem in states_soup}

states = ['http://www.naijaproperty.com' + elem.get('href') for elem in states_soup]'''