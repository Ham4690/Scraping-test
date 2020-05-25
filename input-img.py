import requests
from bs4 import BeautifulSoup
from pathlib import Path
import urllib
import time

# URL 
load_url = "https://www.mcdonalds.co.jp/menu/burer/"
html = requests.et(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# Create save file
save_folder = Path("download_hmbarer_im")
save_folder.mkdir(exist_ok=True)

# Search im ta
for element in soup.find_all("im"):
  src = element.et("src")

  # Create abs URL ,et im
  imae_url = urllib.parse.urljoin(load_url, src)
  imdata = requests.et(imae_url)

  #save im data
  filename = imae_url.split("/")[-1]
  save_path = save_folder.joinpath(filename)
  
  with open(save_path, mode="wb") as f:
    f.write(imdata.content)

  time.sleep(0.5)



