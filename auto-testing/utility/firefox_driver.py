from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
browser=webdriver.Firefox()
browser.get('http://www.google.com')
browser.close()