#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv
import requests
url = "https://www.bankofcanada.ca/valet/observations/group/chartered_bank_interest/csv"
with requests.Session() as s:
    download = s.get(url)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
print(decoded_content)
   # for row in my_list:
        #print(row)


# In[ ]:



s=requests.get(url).content

c=pd.read_csv(s)


# In[ ]:


import urllib.request, json 
with urllib.request.urlopen("https://www.bankofcanada.ca/valet/observations/group/chartered_bank_interest/json") as url:
    data = json.load(url)
    print(data)


# In[ ]:




