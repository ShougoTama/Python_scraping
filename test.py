import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import chromedriver_binary

url = "url:link"　//スクレイピングしたいサイト

options = Options()

options.add_argument('--headless')

driver = webdriver.Chrome() //webを動かすlibrary
driver.get(url) 

name = 'test'
password = '1234'

driver.find_element_by_name('name').send_keys(name)　//htmlのid=nameのエレメント要素にnameの変数を入れていいる
driver.find_element_by_name('password').send_keys(password)//htmlのid=passwordのエレメント要素のpasswordにpasswordの変数を入れている

driver.find_element_by_xpath("//input[@value='LOGIN']").send_keys(Keys.ENTER)

time.sleep(5)

soup = BeautifulSoup(driver.page_source, "lxml")
filename = "test.txt"
f = open(filename, mode="w")

f.write(soup.text)

driver.quit()
