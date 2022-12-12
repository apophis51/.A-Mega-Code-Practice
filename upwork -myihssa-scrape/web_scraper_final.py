import tkinter as tk

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import requests, bs4
from datetime import date
import json
import tkinter as tk
from tkinter import simpledialog
from pynput.keyboard import Key, Listener
import selenium.webdriver.support.ui as ui
from selenium.webdriver import ActionChains  #

from tkinter import *
from pprint import pprint
import openpyxl
wu = openpyxl.load_workbook('angola.xlsx')
sheet = wu['angola']



counter = 1

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def scrape_bot(counter):
    test = driver.find_elements(By.XPATH, "//td")
    school_name = driver.find_element(By.CLASS_NAME, "p-t-0")
    print(school_name.text)
    count3 = ['b','c','d']
    temp = 0
    time.sleep(2)
    for x in range(len(test)):
        sheet[f'a{counter}'] = school_name.text
        sheet[f"{count3[temp]}{counter}"] = str(test[x].text)
        temp += 1
        if temp == 3:
            temp = 0
            counter +=1
    return counter
 
url = "https://www.myihsaa.net/schools"
driver.get(url)
time.sleep(9)

test = driver.find_elements(By.CLASS_NAME, "btn-block")
looper = 0
time.sleep(2)
#a = 1
tracker = 0
print(tracker)
#while a == 42:
while looper != 42:
    for x in range(len(test)):
    #for x in range(2): 
        for t in range(tracker):
            print(range(tracker))
            mag = driver.find_element(By.LINK_TEXT, '»')
            mag = mag.click()
            time.sleep(4)  
        test = driver.find_elements(By.CLASS_NAME, "btn-block")
        test[looper].click()
        #test[looper].send_keys(Keys.CONTROL + Keys.ENTER) #
        #driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.TAB)     #
        #driver.switch_to(main_window)  #
        time.sleep(6)
        counter = scrape_bot(counter)
        driver.get(url)
        #driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + 'w')  #
        #driver._switch_to(main_window)  #
        time.sleep(7)
        looper +=1
        
    wu.save('angola.xlsx')

    #looper = 0
  
       
    looper = 0
    tracker += 1
    #a = int(input(f"hit 1 to continue and make sure {tracker} is selected"))
    #####


    





