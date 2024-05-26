#!/usr/bin/env python
# coding: utf-8

# In[1]:


people = {
    'first': ['Saurabh', 'Tharu'],
    'last': ['Singh', 'Singh'],
    'email': ['saurabh@gmail.com', 'tharu87@gmail.com']
}
import pandas as pd

df = pd.DataFrame(people)
df


# In[2]:


df.sort_values(by=['last', 'first'])
df


# In[4]:


x =df.sort_values(by=['last', 'first'], ascending=False)
x


# In[6]:


df = pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2022/survey_results_public.csv')
df


# In[9]:


df.sort_values(by=['ConvertedCompYearly'], ascending=False, inplace=True)
df


# In[ ]:




