from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Firefox(executable_path=r"./geckodriver")
browser.set_window_size(1080, 1080)
browser.set_window_position(0,0)
sleep(1)
browser.get("https://es.wikipedia.org/wiki/Wikipedia:Portada")
browser.find_element_by_id("searchInput").send_keys("Selenium")
sleep(2)
browser.find_element_by_id("searchInput").send_keys(Keys.ARROW_DOWN)
browser.find_element_by_id("searchInput").send_keys(Keys.RETURN)

sleep(2)

browser.execute_script("window.scrollTo(0,600);")
sleep(2)
browser.execute_script("window.scrollTo(0, -600);")

sleep(5)
browser.close()