import streamlink
import subprocess
import requests
import datetime
import time
import os
import getopt
import logging
import re
import sys
import json
import unicodedata
import shutil
from typing import Dict, List
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote.file_detector import LocalFileDetector
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
import config

file_path = "./cong.py"
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
refresh = 15
fuckingbitch = cong.streamfromyt        

def confirm_logged_in(driver: webdriver) -> bool:
          """ Confirm that the user is logged in. The browser needs to be navigated to a YouTube page. """
          try:
              WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "avatar-btn")))
              return True
          except:
              logging.info(f"cant login please renter the config.json with the cookie information")
              exit()

def login_using_cookie_file(driver: webdriver, cookie_file: str):
          """Restore auth cookies from a file. Does not guarantee that the user is logged in afterwards.
          Visits the domains specified in the cookies to set them, the previous page is not restored."""
          domain_cookies: Dict[str, List[object]] = {}
          with open(cookie_file) as file:
              cookies: List = json.load(file)
              # Sort cookies by domain, because we need to visit to domain to add cookies
          for cookie in cookies:
              try:
               domain_cookies[cookie["domain"]].append(cookie)
              except KeyError:
               domain_cookies[cookie["domain"]] = [cookie]

          for domain, cookies in domain_cookies.items():
              driver.get("https://www.youtube.com/")
              for cookie in cookies:
                  cookie.pop("sameSite", None)  # Attribute should be available in Selenium >4
                  cookie.pop("storeId", None)  # Firefox container attribute
                  try:
                      driver.add_cookie(cookie)
                  except:
                      logging.info(f"Couldn't set cookie {cookie['name']} for {domain}")
        
def streamedit(driver: WebDriver,
               twitchname,
               dixk,
               ):
    try:
            logging.info('start edit the stream name')
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ytcp-button#edit-button"))).click()
            time.sleep(2)
            textbox1 = driver.find_element("xpath", "//ytcp-social-suggestion-input/div[@id='textbox']")
            time.sleep(2)
            textbox1.clear()
            time.sleep(0.5)
            textbox1.send_keys(twitchname)
            time.sleep(0.5)
            textbox2 = driver.find_element("xpath", config.youtubedescription)
            time.sleep(2)
            textbox2.clear()
            time.sleep(0.5)
            textbox2.send_keys(dixk)
            time.sleep(2)
            logging.info('edit finish')
            save_button = driver.find_element(By.XPATH, "//ytcp-button[@id='save-button']")
            save_button.click()
            time.sleep(7)
            return
    except NoSuchElementException:
                driver.quit()
                selwebdriver()

def selfromstream(dick, filenameyt):
         logging.info('process of edit name started from stream')
         driver = webdriver.Chrome()
         login_using_cookie_file(driver, cookie_file = 'config.json')
         driver.get("https://www.youtube.com")
         
         assert "YouTube" in driver.title
         
         try:
                      confirm_logged_in(driver)
                      url_to_live = "https://studio.youtube.com/channel/" + config.channelid + "/livestreaming/dashboard"
                      driver.get(url_to_live)
                      time.sleep(20)
                      AbcS = config.youtubestudiotab
                      assert AbcS in driver.title
                      driver.file_detector = LocalFileDetector()
                      streamedit(driver, twitchname=filenameyt, dixk=dick)
                      
         finally:
            logging.info('edit finished contiue the stream')

def selwebdriver():
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        driver = webdriver.Chrome(options=chrome_options)  # Ensure you have Chromedriver installed and in the PATH
        driver.get("https://www.youtube.com/channel/" + config.username + "/live")  # Open a blank page to ensure a valid title is available
        # Get the title of the current tab
        title = driver.title
        current_url = driver.current_url
        titletv = title.replace(" - YouTube", "")
        logging.info("Current Tab Title and link:" + titletv)
        driver.quit()
        try:
            textnoemo = ''.join('[EMOJI]' if unicodedata.category(c) == 'So' else c for c in titletv)
            if "<" in textnoemo or ">" in textnoemo:
                   textnoemo = textnoemo.replace("<", "[ERROR]").replace(">", "[ERROR]")
            if "#" in textnoemo:
                   textnoemo = textnoemo.replace("#", "(#)")
            filenametwitch = config.titleofuser +  " | " + datetime.datetime.now() \
                     .strftime("%Y-%m-%d")
        else:
         deik = "this stream is from " + current_url + " (Stream Name:" + textnoemo + ")"
         logging.info('process of edit name started')
         driver = webdriver.Chrome()
         login_using_cookie_file(driver, cookie_file = 'config.json')
         driver.get("https://www.youtube.com")
         
         assert "YouTube" in driver.title
         
         try:
                      confirm_logged_in(driver)
                      url_to_live = "https://studio.youtube.com/channel/" + config.channelid"/livestreaming/dashboard"
                      driver.get(url_to_live)
                      time.sleep(20)
                      AbcS = config.youtubestudiotab
                      assert AbcS in driver.title
                      driver.file_detector = LocalFileDetector()
                      streamedit(driver, twitchname=filenametwitch, dixk=deik)
                      
         finally:
            logging.info('edit finished contiue the stream')

def edit_the_full():
         with open(file_path, 'r') as file:
          content = file.read()
         edited = "none"
         noned = cong.streamfromyt
         new_content = content.replace(noned, edited)
         with open(file_path, 'w') as file:
          file.write(new_content)
         logging.info("fininsh")
         exit()

if __name__ == "__main__":
    logging.basicConfig(filename="styt_rename.log", level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.getLogger().addHandler(logging.StreamHandler())
    if "AcBcsa9" in fuckingbitch:
        logging.info("already edit by schedule live")
        edit_the_full()
        exit()            
    logging.info('script is started now')
    selwebdriver()
