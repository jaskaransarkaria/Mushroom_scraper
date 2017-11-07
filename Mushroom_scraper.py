''' A program to scrape the web for mushroom information, plans for chat bot (telegram)
to narrow down and provide basic info on what you have found'''

import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from selenium import webdriver
import re


print("Welcome to Mushroom:bot")
print("Our mushroom guide is not a comprehensive guide of UK mushrooms.")
print("There are roughly 15,000 types of wild fungi in the UK;")
print("This is a quickly narrow down the possibilities of what you might have")
print("Use multiple sources to identify your mushrooms, don't blame me if you die.")
print()
print()
print()
print()
print()

def make_soup(url):

    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, 'html.parser')
    return soupdata

def pretty_print(text):

    text = text.split("related species »")[-1]
    text = text.split("660){")[0]
    text = text.split("(adsbygoogle")[0]
    text = re.sub("JanFebMarAprMayJunJulAugSepOctNovDec", '', text)
    text = re.sub("Season", '', text)
    text = re.sub(r'(\w*:)',r'\r\n\1', text)
    print(text.strip())



def click_link(old_link, new_link): #function to click relevant page

    driver = webdriver.Chrome()
    driver.get(old_link)
    elem1 = driver.find_element_by_link_text(new_link)
    elem1.click()
    current_url = driver.current_url
    driver.implicitly_wait(60) #60 seconds
    soup3 = make_soup(current_url)
    soup5 = soup3.get_text()
    elem2 = driver.find_elements_by_class_name("img_thumb") #returns a list


    for e in elem2:

        image_src = e.get_attribute("src")
        print(image_src)
        driver.implicitly_wait(10)
        filename = image_src.split('/')[-1]
        urllib.request.urlretrieve(image_src, filename)   #downloads each e

    pretty_print(soup5)


soup = make_soup("http://www.foragingguide.com/mushrooms/edible_by_common_name")
edible_list = []
for mushroom_edible in soup.find_all(class_="list_div"):
    edible_list.append(mushroom_edible.text)
    print(mushroom_edible.text)

print()
print()
print()
print()
print()

soup2 = make_soup("http://www.foragingguide.com/mushrooms/poisonous_by_common_name")
poisonous_list = []
for mushroom_poisonous in soup2.find_all(class_="list_div"):
    poisonous_list.append(mushroom_poisonous.text)
    print(mushroom_poisonous.text)

print()
print()
print()
print()
print()

mush_choice = input("Choose a mushroom you would like to know a little more about:").title()
print()
print()
print()
print()
print()

if any(mush_choice in s for s in edible_list):
    click_link("http://www.foragingguide.com/mushrooms/edible_by_common_name", mush_choice)

elif any(mush_choice in s for s in poisonous_list):
    click_link("http://www.foragingguide.com/mushrooms/poisonous_by_common_name", mush_choice)