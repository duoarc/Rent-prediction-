# -*- coding: utf-8 -*-
import scrapy
import requests
# from bs4 import BeautifulSoup as bs




# for state, url in states.items():

class findnigpropSpider(scrapy.Spider):
    name = 'findnigprop'

    start_urls = ['https://findnigeriaproperty.com/index.php/to-let/residential/result/']

    def parse(self, response):
        #Select each listing
        listing_selector = '.span4'

        price_selector =  '.rpl_plistbox_price::text'
        unit_selector =  '.rpl_plistbox_price::text' 
        location_selector =  '.property_info::text'
        bedrooms_selector =  '.bedroom_icon::text' 
        baths_selector =  '.bathroom_icon::text' 
        # parking_selector  =  '.parking_icon::text' 
        # serviced_selector =  '.title.may-blank::text'
        # furnished_selector = '.score.unvoted::text'
        # state_selector = '.property_info::text'

        #Loop over each listing to extract features
        for prop in response.css(listing_selector):
            
        #Extracting the content using css selectors
            yield {
                'price': prop.css(price_selector).extract_first(),
                'unit' : prop.css(unit_selector).extract_first(),
                'location' : prop.css(location_selector).extract_first(),
                'bedrooms' : prop.css(bedrooms_selector).extract_first(),
                'baths' : prop.css(baths_selector).extract_first(),
                'state' :  None
            }
    
        next_page_url = response.css(".next_link ::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)


'''findnigprop_home = requests.get('https://findnigeriaproperty.com/index.php/to-let/residential/result/').text

soup = bs(findnigprop_home, 'lxml')

states_soup = soup.select('.citiesListContainer a ')

# states_url = {elem.get_text('title'):'https://findnigeriaproperty.com' + elem.get('href') for elem in states_soup}

states = ['https://findnigeriaproperty.com' + elem.get('href') for elem in states_soup]

'''