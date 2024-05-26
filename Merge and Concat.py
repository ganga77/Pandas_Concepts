#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df1 = pd.read_csv(r'/Users/gangasingh/Downloads/LOTR.csv')
df1


# In[2]:


df2 = pd.read_csv(r'/Users/gangasingh/Downloads/LOTR 2.csv')
df2


# In[3]:


df1.merge(df2) #innerJoin


# In[6]:


df1.merge(df2, how = 'outer')


# In[5]:


df1.merge(df2, how = 'left')


# In[7]:


df1.merge(df2, how = 'right')


# In[8]:


pd.concat([df1, df2])


# In[ ]:




