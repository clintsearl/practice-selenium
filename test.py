from selenium import webdriver
from time import sleep as s


driver = webdriver.Chrome()


driver.get("https://saltlakecity.gleague.nba.com/archive-getter/?nba_y=&nba_m=&nba_page=1")
driver.implicitly_wait(1)

element = driver.find_element_by_tag_name("ul")

# print(element.text)
html_page = driver.page_source
print(html_page)

driver.quit