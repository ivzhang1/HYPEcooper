from bs4 import BeautifulSoup
from selenium import webdriver


#https://stockx.com/adidas-yeezy-boost-350-v2-core-black-red-2017, https://stockx.com/adidas-yeezy-boost-350-v2-steeple-grey-beluga-solar-red, https://stockx.com/api/products/ef63b9c9-6102-4d4b-bce5-1b1a8b4cbce1/activity?state=480&currency=USD
pagetargets = ["https://stockx.com/api/products/185ecb6f-2402-467c-8db4-c846bf8cdb7a/activity?state=480&currency=USD", "https://stockx.com/api/products/cc3f95f8-899c-4a97-a9ea-6e375385381b/activity?state=480&currency=USD", "https://stockx.com/api/products/ef63b9c9-6102-4d4b-bce5-1b1a8b4cbce1/activity?state=480&currency=USD"]
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
driver.get(pagetargets[0])
html = driver.page_source
soup = BeautifulSoup (html, "html5lib")
magic = open("dump.txt", "w")
magic.write(str(soup))
magic.close()
driver.quit()




