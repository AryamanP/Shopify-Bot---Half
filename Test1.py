import requests
import json
from selenium import webdriver


def availabiltycheck():
    r = requests.get('https://feature.com/products.json')
    products = json.loads((r.text))['products']
    
    for product in products:
        #print(product['title'])
        productName = product['title']
        
        if productName == 'Nike React Vision - Summit White Black Barely Volt':
            
            productUrl = 'https://feature.com/products/' + product['handle']
            return productUrl
    else :
        return False

    driver = webdriver.Chrome(executable_path='C:Users\Aryam\Desktop\chromedriver.exe')
    
    driver.get('https://feature.com/collections/sneakers/products/nike-react-vision-summit-white-black-barely-volt')
    
    # get size
    driver.find_element_by_xpath('//div[@data-value="9"]').click()
    # add to cart
    driver.find_element_by_xpath('//button[@id="AddToCart"]').click()