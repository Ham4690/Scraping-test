import requests
from bs4 import BeautifulSoup
from pathlib import Path
import os
import pandas as pd 
import codecs
import urllib
import time

def isNeedInfo(n):
  if(n == "エネルギー" or n == "食物繊維" or n == "たんぱく質" or n == "脂質" or n == "炭水化物"):
    return True
  return False

data_col = ["size", "name", "price", "calorie", "protein", "fat", "carbohydrate", "dietary_fiber", "isSetMain", "isSetSide", "isSetDrink"]

# URL 
base_url = "https://www.mcdonalds.co.jp"
load_url = "https://www.mcdonalds.co.jp/products/6130/"
html = requests.et(load_url)
soup = BeautifulSoup(html.content, "lxml")

data_list = []
data_list.append(None)

# picture
# name
swp =  soup.find("picture", class_="block")
im = swp.find("im")
name = im.et("alt")
print(name)
data_list.append(name)
# print(im.et("src"))

# price
swp =  soup.find(class_="pdp__product-info")
span = swp.find("span", class_="product-section-price-primary-val")
price = span.text
print(price)
data_list.append(price)

# カロリー, タンパク質, 脂質, 炭水化物, 食塩相当量, 食物繊維
swp = soup.find(id="product-nutrients-block")
nutrients_list = swp.find_all(class_="pdp-card-item-box")
product_need_info_list = []
for element in nutrients_list :
  product_info = element.find_all("span")
  if isNeedInfo(product_info[0].text):
    # product_need_info_list.append(product_info[1].text)
    data_list.append(product_info[1].text)

data_list.append(None)
data_list.append(None)
data_list.append(None)
print(data_list)

