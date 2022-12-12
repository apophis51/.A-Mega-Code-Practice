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

from tkinter import *
 
country = {
"zimbabwe"	:	"zw	"	,
"united states"	:	"us"	,
"united kingdom" :	"GB" ,
"uae"	:	"ae"	,
"ukraine"	:	"ua"	,
"turkey"	:	"tr"	,
"thailand"	:	"th"	,
"switzerland"	:	"ch"	,
"sri lanka"	:	"lk"	,
"spain"	:	"es"	,
"south africa"	:	"za"	,
"singapore"	:	"sg"	,
"saudi arabia"	:	"sa"	,
"russia"	:	"ru"	,
"romania"	:	"ro"	,
"qatar"	:	"qa"	,
"portugal"	:	"pt"	,
"philippines"	:	"ph"	,
"papua new guinea"	:	"pg"	,
"pakistan"	:	"pk"	,
"nigeria"	:	"ng"	,
"new zealand"	:	"nz"	,
"netherlands"	:	"nl"	,
"nepal"	:	"ne"	,
"mexico"	:	"mx"	,
"malaysia"	:	"my"	,
"lebanon"	:	"lb"	,
"kuwait"	:	"kw"	,
"kenya"	:	"ke"	,
"jordan"	:	"jo"	,
"jamaica"	:	"jm"	,
"ivory coast"	:	"ci"	,
"italy"	:	"it",
"iraq"	:	"iq"	,
"iran"	:	"ir"	,
"indonesia"	:	"id"	,
"india"	:	"in"	,
"haiti"	:	"hi"	,
"ghana"	:	"gh"	,
"germany"	:	"de"	,
"filip"	:	"ph"	,
"ethiopia"	:	"et"	,
"equatorial guinea"	:	"gq"	,
"egypt"	:	"eg"	,
"denmark"	:	"dk"	,
"colombia"	:	"co"	,
"china"	:	"cn"	,
"canada"	:	"ca"	,
"brazil"	:	"br"	,
"belize"	:	"bz"	,
"bangladesh"	:	"bd"	,
"australia"	:	"au"	,
"afghan" :	"af"	,
"ireland": "ie",
"greece": "gr,",
"cyprus": "cy",
"kazakhstan": "kz",
"zimbabwe": "zw",
"tanzania": "tz",
"poland": "pl",
"mali": "ml",
"france": "fr",
"cuba": "cu", 
"austria": "at",
"vietnam": "vn"
}






driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Create an empty Tkinter window
"""""" 
def from_kg():
    # Get user value from input box and multiply by 1000 to get kilograms
    
    url = e2_value.get()
    value = e3_value.get()
    returnvalue = country[value]
    print(returnvalue)
    """""
    a= 'https://www.visahq.com'
    b=  e2_value.get()
    c= '/'
    d = url
    e = '/'

    

    url = ''.join([a,c,d,e])
    """""
    a = returnvalue.upper()
    b = returnvalue.upper()
    driver.get(url)
    time.sleep(1)
    driver.add_cookie({'name' : 'citizenship_alpha2', 'value' : a}) 
    driver.add_cookie({'name' : 'living_in_alpha2', 'value' : b})
    driver.get(url)
    time.sleep(2)
    driver.find_element(By.CLASS_NAME("header_landing select2_icons_fix"))
    print(a)
    print(b)
 

    time.sleep(3)



    



"""""

def on_press(key):
    print('{0} pressed'.format(
        key))

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.backspace:
        # Stop listener
        return False

with Listener(
        on_press= on_press,
        on_release=on_release) as listener:
    listener.join()
"""
 

 
window=Tk()


# Create a Label widget with "Kg" as label
e1=Label(window,text="VISAHQ INFO")
e1.grid(row=0,column=0) # The Label is placed in position 0, 0 in the window

e2_value=StringVar()  # Create a special StringVar object
e2=Entry(window,textvariable=e2_value)  # Create an Entry box for users to enter the value
e2.grid(row=0,column=1)


e3_value=StringVar()  # Create a special StringVar object
e3=Entry(window,textvariable=e3_value)  # Create an Entry box for users to enter the value
e3.grid(row=0,column=2)
 

 
# Create a button widget
# The from_kg() function is called when the button is pushed
b1=Button(window,text="get page",command=from_kg)
b1.grid(row=0,column=4)
 

 
# This makes sure to keep the main window open
window.mainloop()