#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Importing the required libraries
import requests
import pandas as pd
import math
from bs4 import BeautifulSoup
import typing
import logging
from typing import List

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


# In[7]:


def get_data(url: str) -> pd.DataFrame:
    # GET THE HEADERS
    url = "https://ajax.listing.ca/real-estate-price-history.htm"
    dfs = pd.read_html(url, header = 0 )
    df1 = dfs[7:12]
    
    #list of dataframes to data a dataframe
    df2 = pd.concat(df1)
    df = df2.reset_index(drop = True)
    return df
    

    logging.info(f"Getting data for: {k}; Starting Row: {v}")
    
url = "https://ajax.listing.ca/real-estate-price-history.htm" 
get_data(url)


# In[8]:


def add_year(dataframe):
    dataframe.insert(0,'year', '')
    for i in range(0,60):
        x = 2022 - i*(1/12)
        y = math.ceil(x)
        dataframe.iloc[i, dataframe.columns.get_loc('year')] = y
    return dataframe
    
table = get_data(url)


Ajax_Sales=add_year(table)


Ajax_Sales.head(60)


# In[9]:


Ajax_Sales.to_csv(r"C:\Users\rokhs\OneDrive\Documents\projects\house\csv from python\Ajax_Sales.csv")


# In[10]:


def get_data(url: str) -> pd.DataFrame:
    # GET THE HEADERS
    url = "https://brampton.listing.ca/real-estate-price-history.htm"
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


# In[11]:


def get_data(url: str) -> pd.DataFrame:
    # GET THE HEADERS
    url = "https://richmond-hill.listing.ca/real-estate-price-history.htm"
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


# In[12]:


def get_data(url: str) -> pd.DataFrame:
    # GET THE HEADERS
    url = "https://aurora.listing.ca/real-estate-price-history.htm"
    dfs = pd.read_html(url, header = 0 )
    df1 = dfs[1:12]
    
    #list of dataframes to data a dataframe
    df2 = pd.concat(df1)
    df = df2.reset_index(drop = True)
    return df
    

    logging.info(f"Getting data for: {k}; Starting Row: {v}")
    
url = "https://aurora.listing.ca/real-estate-price-history.htm" 
get_data(url)


def add_year(dataframe):
    dataframe.insert(0,'year', '')
    for i in range(0,120):
        x = 2022 - i*(1/12)
        y = math.ceil(x)
        dataframe.iloc[i, dataframe.columns.get_loc('year')] = y
    return dataframe
    
table = get_data(url)


aurora_Sales=add_year(table)
aurora_Sales.to_csv(r"C:\Users\rokhs\OneDrive\Documents\projects\house\csv from python\aurora_Sales.csv")


# In[13]:


def get_data(url: str) -> pd.DataFrame:
    # GET THE HEADERS
    url = "https://markham.listing.ca/real-estate-price-history.htm"
    dfs = pd.read_html(url, header = 0 )
    df1 = dfs[1:12]
    
    #list of dataframes to data a dataframe
    df2 = pd.concat(df1)
    df = df2.reset_index(drop = True)
    return df
    

    logging.info(f"Getting data for: {k}; Starting Row: {v}")
    
url = "https://markham.listing.ca/real-estate-price-history.htm" 
get_data(url)


def add_year(dataframe):
    dataframe.insert(0,'year', '')
    for i in range(0,120):
        x = 2022 - i*(1/12)
        y = math.ceil(x)
        dataframe.iloc[i, dataframe.columns.get_loc('year')] = y
    return dataframe
    
table = get_data(url)


markham_Sales=add_year(table)
markham_Sales.to_csv(r"C:\Users\rokhs\OneDrive\Documents\projects\house\csv from python\markham_Sales.csv")


# In[14]:


def get_data(url: str) -> pd.DataFrame:
    # GET THE HEADERS
    url = "https://mississauga.listing.ca/real-estate-price-history.htm"
    dfs = pd.read_html(url, header = 0 )
    df1 = dfs[1:12]
    
    #list of dataframes to data a dataframe
    df2 = pd.concat(df1)
    df = df2.reset_index(drop = True)
    return df
    

    logging.info(f"Getting data for: {k}; Starting Row: {v}")
    
url = "https://mississauga.listing.ca/real-estate-price-history.htm" 
get_data(url)


def add_year(dataframe):
    dataframe.insert(0,'year', '')
    for i in range(0,120):
        x = 2022 - i*(1/12)
        y = math.ceil(x)
        dataframe.iloc[i, dataframe.columns.get_loc('year')] = y
    return dataframe
    
table = get_data(url)


mississauga_Sales=add_year(table)
mississauga_Sales.to_csv(r"C:\Users\rokhs\OneDrive\Documents\projects\house\csv from python\mississauga_Sales.csv")


# In[15]:


def get_data(url: str) -> pd.DataFrame:
    # GET THE HEADERS
    url = "https://newmarket.listing.ca/real-estate-price-history.htm"
    dfs = pd.read_html(url, header = 0 )
    df1 = dfs[1:12]
    
    #list of dataframes to data a dataframe
    df2 = pd.concat(df1)
    df = df2.reset_index(drop = True)
    return df
    

    logging.info(f"Getting data for: {k}; Starting Row: {v}")
    
url = "https://newmarket.listing.ca/real-estate-price-history.htm" 
get_data(url)


def add_year(dataframe):
    dataframe.insert(0,'year', '')
    for i in range(0,120):
        x = 2022 - i*(1/12)
        y = math.ceil(x)
        dataframe.iloc[i, dataframe.columns.get_loc('year')] = y
    return dataframe
    
table = get_data(url)


newmarket_Sales=add_year(table)
newmarket_Sales.to_csv(r"C:\Users\rokhs\OneDrive\Documents\projects\house\csv from python\newmarket_Sales.csv")


# In[16]:


def get_data(url: str) -> pd.DataFrame:
    # GET THE HEADERS
    url = "https://vaughan.listing.ca/real-estate-price-history.htm"
    dfs = pd.read_html(url, header = 0 )
    df1 = dfs[1:12]
    
    #list of dataframes to data a dataframe
    df2 = pd.concat(df1)
    df = df2.reset_index(drop = True)
    return df
    

    logging.info(f"Getting data for: {k}; Starting Row: {v}")
    
url = "https://vaughan.listing.ca/real-estate-price-history.htm" 
get_data(url)


def add_year(dataframe):
    dataframe.insert(0,'year', '')
    for i in range(0,120):
        x = 2022 - i*(1/12)
        y = math.ceil(x)
        dataframe.iloc[i, dataframe.columns.get_loc('year')] = y
    return dataframe
    
table = get_data(url)


vaughan_Sales=add_year(table)
vaughan_Sales.to_csv(r"C:\Users\rokhs\OneDrive\Documents\projects\house\csv from python\vaughan_Sales.csv")












