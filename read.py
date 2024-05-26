#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2023/survey_results_public.csv')
df


# In[3]:


df.columns


# In[10]:


filt = df['Country'] == 'India'
x = df[filt]
x


# In[11]:


x.to_excel('/Users/gangasingh/Downloads/demo/modifies.xlsx')


# In[ ]:




