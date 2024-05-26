#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2022/survey_results_schema.csv')
df


# In[3]:


df.shape


# In[4]:


x = pd.DataFrame(df)
x


# In[5]:


x['qid'] #This is series(columns)


# In[6]:


x[['qid', 'qname']] # Printing multiple (columns)


# In[7]:


x.columns


# In[9]:


x.iloc[1]


# In[10]:


x.iloc[[0,1], 1] # Printing data of first 2 rows and column at index 1


# In[11]:


x.iloc[[0,1], 'qname']


# In[12]:


x.loc[[0,1], 'qname'] #Same like iloc but in second argument, we can pass label


# In[13]:


df = pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2022/survey_results_schema.csv')
df


# In[14]:


df = pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2022/survey_results_public.csv')
df


# In[15]:


df.loc[0:2, "EdLevel"]


# In[16]:


df.loc[0:2, "EdLevel":"LearnCodeOnline"]


# In[ ]:




