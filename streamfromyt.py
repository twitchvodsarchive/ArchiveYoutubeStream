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
import styt_rename

file_path = './cong.py'

def apiloop(driver):
     driver.get("https://www.youtube.com/channel/" + config.username + "/live")  # Open a blank page to ensure a valid title is available
 time.sleep(5)
 try:
     # Find the element with class 'ytp-offline-slate-bar'
    element = driver.find_element("xpath", "//span[@dir='auto' and contains(@class, 'bold') and contains(@class, 'style-scope') and contains(@class, 'yt-formatted-string') and text()=' 位觀眾等待中']")
    eleget = element.text
    print(eleget)
    if "位觀眾等待中" not in eleget:
      logging.info("is streaming")
      exit()
 except NoSuchElementException:
     logging.info("is streaming lol")
     exit()
 current_url = driver.current_url
 title = driver.title
 titletv = title.replace(" - YouTube", "")
 if "https://www.youtube.com/watch?v=" not in current_url:
    print("no live no life")
    time.sleep(600)
    apiloop(driver)
 link_url = current_url
 logging.info(link_url)
 if "True" in config.schedulelive:
  if config.titleofliveschedule in titletv:
     logging.info("gfys freeeeeeeeeeee chat")
     time.sleep(600)
     apiloop(driver)
 textnoemo = ''.join('[EMOJI]' if unicodedata.category(c) == 'So' else c for c in titletv)
 if "<" in textnoemo or ">" in textnoemo:
        textnoemo = textnoemo.replace("<", "[ERROR]").replace(">", "[ERROR]")
 if "#" in textnoemo:
        textnoemo = textnoemo.replace("#", "(#)")
 filenameyt = config.titleofuser +  " | " + datetime.datetime.now() \
         .strftime("%Y-%m-%d")
 dick = "this stream is from " + current_url + " (Stream Name:" + textnoemo + ")"
 with open(file_path, 'r') as file:
  content = file.read()
 edited = "AcBcsa9"
 noned = config.streamfromyt
 new_content = content.replace(noned, edited)
 with open(file_path, 'w') as file:
  file.write(new_content)
 styt_rename.selfromstream(dick, filenameyt)
 logging.info("fininsh")
 exit()

def loop_api():
 chrome_options = Options() # Run Chrome in headless mode
 chrome_options.add_argument("--headless")
 driver = webdriver.Chrome(options=chrome_options)  # Ensure you have Chromedriver installed and in the PATH
 time.sleep(3)
 driver.get("https://www.youtube.com/channel/" + config.username + "/live")  # Open a blank page to ensure a valid title is available
 time.sleep(5)
 try:
     # Find the element with class 'ytp-offline-slate-bar'
    element = driver.find_element("xpath", "//span[@dir='auto' and contains(@class, 'bold') and contains(@class, 'style-scope') and contains(@class, 'yt-formatted-string') and text()=' 位觀眾等待中']")
    eleget = element.text
    print(eleget)
    if config.someonewaiting not in eleget:
      logging.info("is streaming")
      exit()
 except NoSuchElementException:
     logging.info("is streaming lol")
     exit()
 current_url = driver.current_url
 title = driver.title
 titletv = title.replace(" - YouTube", "")
 if "https://www.youtube.com/watch?v=" not in current_url:
    print("no live no life")
    time.sleep(600)
    apiloop(driver)
 link_url = current_url
 logging.info(link_url)
 if "True" in config.schedulelive:
  if config.titleofliveschedule in titletv:
     logging.info("gfys freeeeeeeeeeee chat")
     time.sleep(600)
     apiloop(driver)
 textnoemo = ''.join('[EMOJI]' if unicodedata.category(c) == 'So' else c for c in titletv)
 if "<" in textnoemo or ">" in textnoemo:
        textnoemo = textnoemo.replace("<", "[ERROR]").replace(">", "[ERROR]")
 if "#" in textnoemo:
        textnoemo = textnoemo.replace("#", "(#)")
 filenameyt = config.titleofuser +  " | " + datetime.datetime.now() \
         .strftime("%Y-%m-%d")
 dick = "this stream is from " + current_url + " (Stream Name:" + textnoemo + ")"
 with open(file_path, 'r') as file:
  content = file.read()
 edited = "AcBcsa9"
 noned = cong.streamfromyt
 new_content = content.replace(noned, edited)
 with open(file_path, 'w') as file:
  file.write(new_content)
 styt_rename.selfromstream(dick, filenameyt)
 logging.info("fininsh")
 exit()

if __name__ == "__main__":
    logging.basicConfig(filename="streamfromyt.log", level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info("start checking hahahah")
    loop_api()

