#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from numpy import nan


# In[3]:


file = pd.read_csv("playstore_apps.csv",index_col='App')


# In[3]:


file


# # Subtask 1:Remove duplicate data of playstore app file

# In[5]:


file.drop_duplicates(keep=False,inplace=True)


# In[6]:


file.info()


# In[3]:


file_review = pd.read_csv("playstore_reviews.csv",index_col='App')


# In[15]:


file_review


# # Remove duplicate data of app review  file

# In[22]:


file_review.drop_duplicates(keep=False,inplace=True)


# In[23]:


file_review.info()


# # subtask 2:Remove irrelevant values from each column of playstore app

# In[4]:


# Category column of playstore_app
print(file['Category'].unique()) #unique values in Category


# In[5]:


file[file['Category']=='1.9']


# In[6]:


file.drop("Life Made WI-Fi Touchscreen Photo Frame",inplace=True,axis=0)


# In[7]:


print(file['Category'].unique()) #check if relevant values are removed


# In[29]:


print(file['Rating'].unique())


# In[57]:


print(file['Reviews'].unique())


# In[77]:


print(file['Size'].unique())


# In[78]:


print(file['Installs'].unique())


# In[80]:


print(file['Type'].unique())


# In[81]:


print(file['Price'].unique())


# In[82]:


print(file['Content Rating'].unique())


# In[83]:


print(file['Genres'].unique())


# In[84]:


print(file['Last Updated'].unique())


# In[86]:


print(file['Current Ver'].unique())


# In[87]:


print(file['Android Ver'].unique())


# In[89]:


file['Android Ver'].isnull().sum()


# In[90]:


file['Current Ver'].isnull().sum()


# In[96]:


file['Rating'].isnull().sum()


# # Remove irrelevant values from each column of playstore app

# In[12]:


file_review.info()


# In[10]:


file_review.isnull().sum()


# In[11]:


print(file_review['Translated_Review'].unique())


# In[13]:


print(file_review['Sentiment'].unique())


# In[14]:


print(file_review['Sentiment_Polarity'].unique())


# In[16]:


print(file_review['Sentiment_Subjectivity'].unique())


# # Subtask 3: Export the cleaned dataset as a .csv file and prepare the data using excel:

# In[8]:


file.to_csv('file_cleaned.csv')


# In[18]:


file_review.to_csv('file_review_cleaned.csv')


# In[ ]:




