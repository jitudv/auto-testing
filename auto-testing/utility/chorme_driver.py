from selenium import webdriver
import time
import logging


def initial_setup():
    logging.info("program start ")
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    # options.binary_location = "/home/jitu/chromedriver/chromedriver"
    logging.info("chromDriver load ")
    driver = webdriver.Chrome("/home/jitu/chromedriver/chromedriver", chrome_options=options)
    driver.get('https://python.org')


if __name__ == '__main__':
    logging.info("we are at main function  ")
    initial_setup();
