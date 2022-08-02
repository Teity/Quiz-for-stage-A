#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_excel(r'C://Users/Ivy/Downloads/FoodBalanceSheets_E_Africa_NOFLAG.xlsx')


# In[3]:


df


# In[4]:


df[['Element Code','Item','Y2014','Y2017']].groupby('Item').sum()


# In[5]:


df.describe()


# In[6]:


df.info()


# In[7]:


60943-59408


# In[8]:


df.corr()


# In[9]:


df.groupby('Element').sum().sort_values(by='Y2018')


# In[10]:


df.columns.str.replace(' ','')


# In[11]:


df[['Area','Y2018','Element']].groupby(by=['Element','Area']).sum()


# In[ ]:




