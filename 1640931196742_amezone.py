from selenium.webdriver import Chrome

from bs4 import BeautifulSoup
from selenium.webdriver.ie import service

from  selenium.webdriver.ie.service import Service
import pandas as pd 


my_url = "https://www.amazon.in/s?k=samsung&rh=n%3A1389401031&ref=nb_sb_noss"


ser  = Service('Z:/chromedriver.exe')

driver = Chrome(service=ser)
driver.get(my_url)
driver.set_page_load_timeout(5)
content = driver.page_source

soup = BeautifulSoup(content)


price = []
name = []

products_details = []

for pg in soup.find_all('div',attrs={'class':'s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col s-widget-spacing-small sg-col-12-of-16'}):
    nam = (pg.find('span',{'class':"a-size-medium a-color-base a-text-normal"}))
    pris = (pg.find('span',{'class':'a-price-whole'}))

    name.append(nam.text)
    price.append(pris.text)




    # nam = a.find('span',{'class':"a-size-large product-title-word-break"})
    # pris = a.find('span',{'class':"a-offscreen"})
#     name.append(nam.text)
#     price.append(pris.text)

filename ='products2.csv'
df = pd.DataFrame({'products name':name,'price':price})
fil = df.to_csv(filename,index=False,encoding='UTF-8')


  
