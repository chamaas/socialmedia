import scrapy
import time
from scrapy.http.request import Request
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from socialmedia.spiders import DRIVER_DIR
from socialmedia.spiders import SEARCH_ENGINE_DATA
from socialmedia.items import LivreItem
from socialmedia.spiders import utils



class GoogleSpider(scrapy.Spider):
    """
    Scrapy for Babelio 
    """
    name = 'GoogleSpider'
    allowed_domains = ['www.google.com']

    def __init__(self):
        """
        initialize driver
        """
        WINDOW_SIZE="1500,1500"
        chrome_options = Options()
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(f"{DRIVER_DIR}",chrome_options=chrome_options)
        self.engine = SEARCH_ENGINE_DATA

    def start_requests(self):
        """
        gets links Babelio
        """
        for key in list(self.engine.keys()):
            print("ENGINE KEY", key)

            
            urls = utils.get_link(key)
            print("urls",urls)
            for url in urls:
                self.driver.get(url)
                time.sleep(2)
                links=self.driver.find_elements_by_css_selector(self.engine[key]["search_pattern"])
            
                if not isinstance(links, list):
                    links = [links]
                search_results=[]
                while len(links):
                    link= links.pop()
                    link= link.get_attribute("href")
                    search_results.append(link)
                linkb=[]
                for search_result in search_results:
                    if utils.is_book(search_result):
                        linkb.append(search_result)
                
                try:
                     yield scrapy.Request(url=linkb[0],callback=self.parse_babelio)
                except:
                    pass

               
                
       
        
    def parse_babelio(self,response):
        
        item = LivreItem()
 
        item['author'] = response.css('div.col.col-8 > span > a > span[itemprop=name]::text').getall()
        item['rate'] = response.css('div.col.col-8 > span > span.texte_t2.rating::text').get()
        item['reviews_number'] =response.css('div.col.col-8 > span >  span[itemprop=ratingCount]::text').get().replace("\n","").replace("\t","")
        item["summary"]=response.css('#d_bio::text')
 
        yield item