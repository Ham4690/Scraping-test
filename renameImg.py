import lob
import os

imaeNames = lob.lob("./download_hmbarer_im/*")

for name in imaeNames :
  print(name)
  rename = name.split("?")
  print(rename)
  os.rename(name, rename[0])
