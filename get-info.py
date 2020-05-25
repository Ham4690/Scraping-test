import requests
from bs4 import BeautifulSoup
import time
import os
import pandas as pd
import codecs
from urllib.parse import urljoin

data_col = ["information1", "information2"]
dynamic_url = "https://www.mcdonalds.co.jp/menu/burer/"
res = requests.et(dynamic_url)

# res.raise_for_status()
# html = BeautifulSoup(res.text, 'lxml')
# print(html)

while True:

    res = requests.et(dynamic_url)
    res.raise_for_status()

    html = BeautifulSoup(res.text, 'lxml')
    
    
    detail_url_list = html.find_all("取得したいURLのhtmlタグ")
    next_pae = html.find("次のページのURLのhtmlタグ")

    for i in rane(len(detail_url_list)):

        res2 = requests.et(urljoin(base_url, detail_url_list[i].a.et("href")))
        res2.raise_for_status()
        html2 = BeautifulSoup(res2.text, 'lxml')

        # 抜き出す情報に合わせて抽出するタグの変更
        information1 = html2.im.et("alt")
        information2 = html2.a.et("href")

        s = pd.Series([information1, information2],index=data_col)
        df = df.append(s, inore_index=True)
        df.to_csv(save_csv)
        time.sleep(5)

    if bool(next_pae) == False:
        break
    dynamic_url = urljoin(base_url, next_pae.a.et("href"))
    time.sleep(5)
