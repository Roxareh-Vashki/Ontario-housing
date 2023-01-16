#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import typing
import logging
from typing import List


# In[25]:


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


# In[26]:


file = r'C:\Users\rokhs\OneDrive\Documents\projects\house\2021\C\98-401-X2021006_English_CSV_data_Ontario.csv'


# In[27]:


data_dict = {
    "Ajax" : 6737617,
    "Aurora" : 10209229,
    "Brampton": 20147608,
    "Markham" : 9034891,
    "Richmond Hill" : 9705094,
    "Vaughan" : 8463538,
    "York" : 8461561,
    "Burlington" : 23257430,
    "Mississauga" : 18229919,
    "Hamilton" : 24289424,
    "Newmarket" : 10333781
    
}


# In[48]:


def get_data(file: str) -> pd.DataFrame:
    # GET THE HEADERS
    headers = pd.read_csv(file, encoding="latin-1", nrows=0)
    headers = headers.columns.tolist()
    
    
        # GET ALL THE ROWS OF ONLY THE CITIES YOU WANT
    data = pd.DataFrame()
    for k, v in data_dict.items():
        logging.info(f"Getting data for: {k}; Starting Row: {v}")
        tmp = pd.read_csv(
            file,
            encoding="latin-1",
            nrows=1977,
            skiprows=v,
            names=headers,
            usecols=["GEO_NAME", "CHARACTERISTIC_NAME", "C1_COUNT_TOTAL"]
        )
        data = pd.concat([data, tmp])
    data["GEO_NAME"] = data["GEO_NAME"].map(
        {
            "Ajax, Town (T)": "Ajax", 
            "Aurora, Town (T)": "Aurora", 
            "Brampton, City (CY)": "Brampton", 
            "Markham, City (CY)": "Markham",
            "Richmond Hill, Town (T)": "Richmond Hill", 
            "Vaughan, City (CY)": "Vaughan",
            "York, Regional municipality (RM)": "York Region",
            "Burlington, City (CY)" : "Burlington",
            "Mississauga, City (CY)" : "Mississauga",
            "Hamilton, municipality (RM)" : "Hamilton",
            "Newmarket, Town (T)" : "Newmarket"
        }
    )
    return data


# In[49]:


def get_sum_characteristics_df(data: pd.DataFrame, match_string: str) -> pd.DataFrame:
    return data[data["CHARACTERISTIC_NAME"].str.contains(match_string)]        [["GEO_NAME", "C1_COUNT_TOTAL"]]


# In[50]:


def get_languages_df(data: pd.DataFrame) -> pd.DataFrame:
    data_idx = data.reset_index()
    return data_idx[data_idx["index"].isin([381, 382, 669, 965, 628])]        [["GEO_NAME", "CHARACTERISTIC_NAME", "C1_COUNT_TOTAL"]]


# In[51]:


if __name__ == "__main__":
    # NOTE: YOU MAY ALSO WANT TO RENAME THE "C1_COUNT_TOTAL" COLUMN
    data = get_data(file)

    median_income_df = get_sum_characteristics_df(data, "Median total income in 2020 among recipient")

    avg_income_df = get_sum_characteristics_df(data, "Average total income in 2020 among recipients")

    familysize_df = get_sum_characteristics_df(data, "Average size of census families")

    languages_df = get_languages_df(data)


# In[52]:


median_income_df


# In[53]:


median_income_df.to_csv(r"C:\Users\rokhs\OneDrive\Documents\projects\house\csv from python\median_income.csv")


# In[54]:


avg_income_df.to_csv(r"C:\Users\rokhs\OneDrive\Documents\projects\house\csv from python\ave_income.csv")


# In[ ]:




