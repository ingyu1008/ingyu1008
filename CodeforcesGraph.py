from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('ignore-certificate-errors')
options.add_argument('headless')
driver = webdriver.Chrome(executable_path='/chromedriver', options=options)

URL = 'https://codeforces.com/profile/MatWhyTle?graphType=rated'

driver.get(URL)

sleep(1)

driver.find_element_by_id('usersRatingGraphPlaceholder').screenshot('graph.png')

driver.quit()
