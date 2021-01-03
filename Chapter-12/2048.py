from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

elem=browser.find_element_by_tag_name('html')

while True:
    elem.send_keys(Keys.UP)
    elem.send_keys(Keys.RIGHT)
    elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.LEFT)