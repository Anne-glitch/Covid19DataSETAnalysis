#!/usr/bin/env python
# coding: utf-8

# # COVID-19 Data Set Analysis

# In[1]:


import pandas as pd


# In[25]:


covid19_data = pd.read_csv(r"C:\Users\sabna\Downloads\COVID_19DATA.csv")


# In[26]:


covid19_data


# In[5]:


covid19_data.count()


# In[8]:


covid19_data.isnull().sum()
#null values not found 


# In[9]:


import seaborn as sns


# In[10]:


import matplotlib.pyplot as plt


# In[11]:


#Finding the number of confirmed cases,recovered cases 
#and the number of reported deaths
covid19_data.head(2)



# In[12]:


#covid19_data.groupby('Region').sum()


# In[16]:


#Confirmed cases of the countries in descending numbers of cases 

#covid19_data.groupby('Region')['Confirmed'].sum().sort_values(ascending = False)


# In[18]:


#Recovered and confirmed cases
covid19_data.groupby('Region')['Confirmed', 'Recovered'].sum()


# In[22]:


#Countries removed with cases less than 20 confirmed cases
#country list
covid19_data[covid19_data.Confirmed < 20]


# In[23]:


#Removal
covid19_data = covid19_data[-(covid19_data.Confirmed < 20)]


# In[24]:


#Removed
covid19_data


# In[27]:


#Region with max confirmed cases
covid19_data.groupby('Region')['Confirmed'].sum().sort_values(ascending = False)


# In[29]:


#Minimum Deaths REported 
covid19_data.groupby('Region')['Deaths'].sum().sort_values(ascending = True).head(30)


# In[30]:


#Cases reported in India till today-06/05/2023
covid19_data[covid19_data.Region == 'India']


# In[31]:


#Cases reported in South Korea till today-06/05/2023
covid19_data[covid19_data.Region == 'South Korea']


# In[34]:


#Recovered cases in descending order
covid19_data.sort_values(by = ['Recovered']).head(30)


# In[ ]:




