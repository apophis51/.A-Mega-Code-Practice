def sample_dictionary(): ####### This method initializes a sample dectionary
    blogs = {
        "vape pens" : "how to clean a vape pen",
        "bongs" : "how do bongs work",
        "bong types" : ["straight-tube","beaker","tall"],
        "keywords" : ["pretty", "big", "nice", "cool"]
    }
    return blogs

def dictionarycommands():
    my_dictionary = sample_dictionary()

    my_dictionary["bong types"].append("nice")  #### add a key to the dictionary
    print("this key has an appended value: ",  my_dictionary["bong types"])

    my_dictionary["bongs"]
    my_dictionary["bongs"] = [my_dictionary["bongs"]] ### converts key to a list so i can append
    my_dictionary["bongs"].append("this is cool")

    print("my list got appended with 'this is cool':", my_dictionary["bongs"],)
    my_dictionary["bong types"].remove("tall") ### removes a value from the key

    print("\n the value tall was removed:", my_dictionary["bong types"])
    my_dictionary.pop("bong types")           ### delete a value from the dictionarand can display at the same timey\
    print("\nA value from the dictionary was removed", my_dictionary)
    print(my_dictionary.pop("keywords"))
    print(my_dictionary)

##dictionarycommands()

def automatedbrowser():
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
    ##from tkinter import *

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    a = "IN"
    url = "https://www.visahq.com/algeria/"
    b = "IN"
    driver.get(url)
    time.sleep(1)
    driver.add_cookie({'name' : 'citizenship_alpha2', 'value' : a}) 
    driver.add_cookie({'name' : 'living_in_alpha2', 'value' : b})
    driver.get(url)
    time.sleep(1)
    ##t = driver.find_element(By.ID , "algeria-visa")
    time.sleep(1)
    try:
        text = driver.find_element(By.CLASS_NAME, "visa-info__redirect_url_text").text
        print(text)
        print(f"https://www.{text}/")
        text = f"https://www.{text}/"
        countrycode = url[22:]
        newparsedurl = f"{text}{countrycode}?residency={b}&citizenship={b}"
        
        time.sleep(1)
        text = str(text)
        #input("")
        driver.get(newparsedurl)

        print(a)
        print(b)
    except:
        pass

    #input("")
    automatedbrowser()

##automatedbrowser()
def picklerr():
    import requests, bs4
    import webbrowser
    import re
    import pickle
    import pandas as pd
    import requests, bs4
    import openpyxl
    from datetime import date 

    class User:
        instances = []
        def __init__(self,firstname, lastname):
            self.firstname = firstname
            self.lastname = lastname
    def printt():
        print("cool")
     

    def save(pickle_object): ### this one overwrites
        class User:
            def __init__(self,firstname, lastname):
                self.firstname = firstname
                self.lastname = lastname
       # my_pickled_object =  pickle.dumps(pickle_object)
        with open('learn_pickle','wb') as file:
       #     pickle_object = pickle.dump(my_pickled_object, file)
             pickle.dump(pickle_object, file)

    def load():  #does not load as an array
        infile = open('learn_pickle','rb')
        pickle_transfer = pickle.load(infile)
        pickle_object = pickle.loads(pickle_transfer)
        return pickle_object

    storeclass = []
    User1 = User("malcolm","vernon")
   # User1 = pickle.dumps(User)
    storeclass.append(User1)
    with open('learn_pickle','wb') as file:
        pickle.dump(User1, file)
    print(User1.firstname)
    User2 = User("steven", "schuler")
    storeclass.append(User2)
    #print(User1)
    #print(User2)
    #print(User1)
    ##save(storeclass)
    #save(User1)
    #people = load()
    x = 0
   # print("my people" , people)
    
##objects defined in a function are local objects

#picklerr()
from collections import UserDict
import pickle

class User:
    instances = []
    def __init__(self,firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
storage = []
User1 = User("malcolm","vernon")
storage.append(User1)
print(User1)
User2 = User("Aron", "davis")
print("printing class", User)
storage.append(User2)
with open ('learn_pickle', 'wb') as file:
    pickle.dump(storage,file)
"""""
with open('learn_pickle','wb') as file:
    pickle.dump(User1, file)
    pickle.dump(User2, file)
"""""
infile = open('learn_pickle','rb')
pickle_transfer = pickle.load(infile)
#me = pickle.load(infile)
#print(pickle_transfer.firstname)
#print(me.firstname)
print(pickle_transfer[0].firstname)
counter = 0
for x in pickle_transfer:             ### reads all first names from the class
    print(pickle_transfer[counter].firstname)
    counter += 1

#this program reverses a list
def reversen(x):
    L = len(x) -1
    reverse = []
    for i in x:
        reverse.append(x[L])
        L -= 1

    return reverse

#print("check this out",reversen([1,8,3,4]))

def list_xor(x,y,z):
    L1 = False
    L2 = False
    if 5 in z:
        print(5)
    for i in y:
        if x == i:
            L1 = True
    for i in z:
        if x == i:
            L2 = True
    if (L1 == True and L2== True) or (L1 == False and L2 == False):
        return "false"
    else:
        return "true"
print(list_xor(1, [0, 0, 0], [1, 5, 6]))


def format_number(number):
    s = str(number)
    newstring = ""
    l = len(s) -1
    lt = l+1
    countt = 0;
    zerocount = 0
    data = "000"
    for h in s:
        zerocount += 1
        countt += 1
        if zerocount == 3 and countt != lt:
            s = s[:l] + "," + s[l:]
            zerocount = 0
        l -= 1


        
    return s

#print(format_number(10005456000))


def add_dots(x):
    count = 0
    new_string = ""
    for i in x:
        if count < len(x)-1:
            new_string = new_string + x[count] + "."
        else:
            new_string = new_string + x[count]
        count += 1
    return new_string

def remove_dots(y):
    newstring = ""
    for i in y:
        if i == ".":
            pass
        else:
            newstring += i
    return newstring

print(remove_dots("f.d.s.e"))
print(add_dots("hello"))

def capital_indexes(x):
    capitals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    return_list =[]
    counter = 0
    for i in x:
        if i in capitals:
            return_list.append(counter)
        counter += 1
    return return_list

#print(capital_indexes("HeLlO"))

def mid(x):
    length = len(x)
    split = (length/2) + .5 - 1
    y = (len(x)/2)
    if length%2 == 0:
        return ""
    else:
        return x[int(split)]





#print(mid("aabdfdbaa"))

def online_count(x):
    keys = x.keys()
    counter = 0;
    for i in keys:
        if x[i] == "online":
            counter +=1
    return counter


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
#babe = 5
#print(isinstance(babe,int))
#print (online_count(statuses))
"""""
https://realpython.com/beautiful-soup-web-scraper-python/
https://www.worthwebscraping.com/how-to-use-cookies-and-session-in-python-web-scraping/
https://realpython.com/python-gui-tkinter/
"""""
def only_ints(x,y):
    if y == True:
        y = "3"
    t = isinstance(x,int)
    p = isinstance(y,int)
    if t == True and p == True:
        return True
    else: 
        return False
#print(only_ints("a",True))


