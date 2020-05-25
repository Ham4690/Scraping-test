import requests
from bs4 import BeautifulSoup
from pathlib import Path
import os
import pandas as pd 
import codecs
import urllib
import time
import csv

###################################

def isNeedInfo(n):
  if(n == "エネルギー" or n == "食物繊維" or n == "たんぱく質" or n == "脂質" or n == "炭水化物"):
    return True
  return False

def getInfo(soup, num):
  
  product_need_info_list = []
  # picture
  # name
  swp =  soup.find("picture", class_="block")
  im = swp.find("img")
  name = im.get("alt")
  print(name)
  product_need_info_list.append(name)
  # print(im.et("src"))

  # price
  swp =  soup.find(class_="pdp__product-info")
  span = swp.find_all("span", class_="product-section-price-primary-val")

  if len(span) >= 1:
    price = span[num].text  
  else:
    price = span[0].text
  print(price)
  product_need_info_list.append(price)

  # カロリー, タンパク質, 脂質, 炭水化物, 食塩相当量, 食物繊維
  swp = soup.find(id="product-nutrients-block")
  nutrients_list = swp.find_all(class_="pdp-card-item-box")
  for element in nutrients_list :
    product_info = element.find_all("span")
    if isNeedInfo(product_info[0].text):
      product_need_info_list.append(product_info[1].text)
      # data_list.append(product_info[1].text)
  return product_need_info_list


###################################

data_col = ["size", "name", "price", "calorie", "protein", "fat", "carbohydrate", "dietary_fiber", "isSetMain", "isSetSide", "isSetDrink"]
base_url = "https://www.mcdonalds.co.jp"

set_datas_list = []
set_datas_list.append(data_col)

# URL 
base_url = "https://www.mcdonalds.co.jp"
load_url = "https://www.mcdonalds.co.jp/menu/drink/"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "lxml")

detail_oods_atag_list = soup.find_all("a", class_="inline-block")
for atag in detail_oods_atag_list:
    url = atag.get("href")
    html = requests.get(base_url + url)
    soup = BeautifulSoup(html.content, "lxml")

#   # print(soup)
    if soup.find("div", class_="dropdown-menu"):
      # has many size
      html = soup.find("div", class_="dropdown-menu")
      size_list_atag_list = html.find_all("a")
      print(size_list_atag_list)

      count = 0
      for atag in size_list_atag_list:
        print(atag)
        data_list = []
        data_list.append(None)
        url = atag.get("href")
        url = url.split("#")[0]
        html = requests.get(base_url + url)
        soup = BeautifulSoup(html.content, "lxml")
        getInfo_list = getInfo(soup, count)

        for data in getInfo_list :
          data_list.append(data)

        data_list.append(None)
        data_list.append(None)
        data_list.append(None)
        print(data_list)

        set_datas_list.append(data_list)
        print(set_datas_list)

        count += 1
        time.sleep(5)







    else:
  # URL 
      data_list = []
      data_list.append(None)

      # # picture
      # # name
      # swp =  soup.find("picture", class_="block")
      # im = swp.find("im")
      # name = im.et("alt")
      # print(name)
      # data_list.append(name)
      # # print(im.et("src"))

      # # price
      # swp =  soup.find(class_="pdp__product-info")
      # span = swp.find("span", class_="product-section-price-primary-val")
      # price = span.text
      # print(price)
      # data_list.append(price)

      # # カロリー, タンパク質, 脂質, 炭水化物, 食塩相当量, 食物繊維
      # swp = soup.find(id="product-nutrients-block")
      # nutrients_list = swp.find_all(class_="pdp-card-item-box")
      # product_need_info_list = []
      # for element in nutrients_list :
      #   product_info = element.find_all("span")
      #   if isNeedInfo(product_info[0].text):
      #     # product_need_info_list.append(product_info[1].text)
      #     data_list.append(product_info[1].text)

      getInfo_list = getInfo(soup, 0)

      for data in getInfo_list:
        data_list.append(data)

      data_list.append(None)
      data_list.append(None)
      data_list.append(None)
      print(data_list)

      set_datas_list.append(data_list)
      print(set_datas_list)
    time.sleep(5)


with open('data.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerows(set_datas_list)