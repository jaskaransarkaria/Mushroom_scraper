''' A program to scrape the web for mushroom information, plans for chat bot (telegram)
to narrow down and provide basic info on what you have found'''

import urllib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from selenium import webdriver

print("Welcome to Mushroom:bot")
print("Our mushroom guide is not a comprehensive guide of UK mushrooms.")
print("There are roughly 15,000 types of wild fungi in the UK;")
print("This is a quickly narrow down the possibities of what you might have")
print("Use mutliple sources to identify your mushrooms, don't blame me for anything.")
print()
print()
print()
print()
print()

def make_soup(url):

    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, 'html.parser')
    return soupdata

def click_link(old_link, new_link): #function to click relevant page

    driver = webdriver.Firefox()
    driver.get(old_link)
    elem1 = driver.find_element_by_link_text(new_link)
    elem1 = elem1.click()
    print(get_text(elem1))


soup = make_soup("http://www.foragingguide.com/mushrooms/edible_by_common_name")
edible_list = []
for mushroom_edible in soup.find_all(class_="list_div"):
    edible_list.append(mushroom_edible)
    print(mushroom_edible.text)

print()
print()
print()
print()
print()

soup2 = make_soup("http://www.foragingguide.com/mushrooms/poisonous_by_common_name")
poisonous_list = []
for mushroom_poisonous in soup2.find_all(class_="list_div"):
    poisonous_list.append(mushroom_poisonous)
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

if mush_choice in edible_list:
    click_link("http://www.foragingguide.com/mushrooms/edible_by_common_name", mush_choice)
elif mush_choice in poisonous_list:
    click_link("http://www.foragingguide.com/mushrooms/poisonous_by_common_name", mush_choice)