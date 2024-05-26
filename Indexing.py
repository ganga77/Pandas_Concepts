#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df = pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2022/survey_results_public.csv', index_col="ResponseId")
df


# In[10]:


schema_df = pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2022/survey_results_schema.csv', index_col='qname')
schema_df


# In[6]:


df.loc[2, 'CodingActivities']


# In[12]:


schema_df.loc['MainBranch']


# In[13]:


schema_df.sort_index()


# In[ ]:




