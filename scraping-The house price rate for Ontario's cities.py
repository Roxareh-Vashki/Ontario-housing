#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Importing the required libraries
import requests
import pandas as pd
import math
from bs4 import BeautifulSoup
import typing
import logging
from typing import List

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# url = "https://ajax.listing.ca/real-estate-price-history.htm"
# dfs = pd.read_html(url, header = 0 )
# df1 = dfs[1:12]
# df1


# In[ ]:





# In[4]:


def get_data(url: str) -> pd.DataFrame:
    # GET THE HEADERS
    url = "https://ajax.listing.ca/real-estate-price-history.htm"
    dfs = pd.read_html(url, header = 0 )
    df1 = dfs[1:12]
    
    #list of dataframes to data a dataframe
    df2 = pd.concat(df1)
    df = df2.reset_index(drop = True)
    return df
    

    logging.info(f"Getting data for: {k}; Starting Row: {v}")
    
url = "https://ajax.listing.ca/real-estate-price-history.htm" 
get_data(url)


# In[5]:


#gol.insert(0, 'year', '2022')
#gol['year'] = pd.Series([2022 for x in range(len(gol.index))])
#gol1 = gol[gol.index % 12 != 0]

#def get_year(dataframe):


def add_year(dataframe):
    dataframe.insert(0,'year', '')
    for i in range(0,120):
        x = 2022 - i*(1/12)
        y = math.ceil(x)
        dataframe.iloc[i, dataframe.columns.get_loc('year')] = y
    return dataframe
    
table = get_data(url)


Ajax_Sales=add_year(table)



    
#     #new =gol.iloc[0::11, :]
#     y = i + 2011
#     gol['year'] = pd.Series([y for x in range(1,12)])
Ajax_Sales.head(44)


# In[4]:


xx.tail(15)


# In[9]:


Ajax_Sales.to_csv(r"C:\Users\rokhs\OneDrive\Documents\projects\house\csv from python\Ajax_Sales.csv")


# In[12]:


def get_data(url: str) -> pd.DataFrame:
    # GET THE HEADERS
    url = "https://ajax.listing.ca/real-estate-price-history.htm"
    dfs = pd.read_html(url, header = 0 )
    df1 = dfs[1:12]
    
    #list of dataframes to data a dataframe
    df2 = pd.concat(df1)
    df = df2.reset_index(drop = True)
    return df
    

    logging.info(f"Getting data for: {k}; Starting Row: {v}")
    
url = "https://brampton.listing.ca/real-estate-price-history.htm" 
get_data(url)


def add_year(dataframe):
    dataframe.insert(0,'year', '')
    for i in range(0,120):
        x = 2022 - i*(1/12)
        y = math.ceil(x)
        dataframe.iloc[i, dataframe.columns.get_loc('year')] = y
    return dataframe
    
table = get_data(url)


Brampton_Sales=add_year(table)
Brampton_Sales.to_csv(r"C:\Users\rokhs\OneDrive\Documents\projects\house\csv from python\Brampton_Sales.csv")


# In[14]:


def get_data(url: str) -> pd.DataFrame:
    # GET THE HEADERS
    url = "https://ajax.listing.ca/real-estate-price-history.htm"
    dfs = pd.read_html(url, header = 0 )
    df1 = dfs[1:12]
    
    #list of dataframes to data a dataframe
    df2 = pd.concat(df1)
    df = df2.reset_index(drop = True)
    return df
    

    logging.info(f"Getting data for: {k}; Starting Row: {v}")
    
url = "https://richmond-hill.listing.ca/real-estate-price-history.htm" 
get_data(url)


def add_year(dataframe):
    dataframe.insert(0,'year', '')
    for i in range(0,120):
        x = 2022 - i*(1/12)
        y = math.ceil(x)
        dataframe.iloc[i, dataframe.columns.get_loc('year')] = y
    return dataframe
    
table = get_data(url)


Richmondhill_Sales=add_year(table)
Richmondhill_Sales.to_csv(r"C:\Users\rokhs\OneDrive\Documents\projects\house\csv from python\Richmondhill_Sales.csv")


# In[5]:


# def data_frame(year):
#     df_year=df[2022-year]
#     return(df_year)

# newdf= pd.DataFrame()
# for i in range(2012,2022):
#     ds= data_frame(i)
#     dr = newdf.append(ds)

# print(dr)
# dr.tail()


# In[6]:


# year = 2022
# print(year , dataframe(year))


# In[7]:


#print(f'Total tables: {len(url)}')


# In[ ]:




