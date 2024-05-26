#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2022/survey_results_public.csv', index_col="ResponseId")
df


# In[2]:


schema_df = pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2022/survey_results_schema.csv', index_col='qname')
schema_df


# In[5]:


df.apply(len)


# In[10]:


df.rename(columns = {"ConvertedCompYearly": "SalaryUSD"}, inplace=True)


# In[11]:


df


# In[13]:


df['TrueFalse_1'].map({'Yes': True, 'No': False})


# In[14]:


people = {
    'first': ['Ganga', 'Rohit', 'Rajat'],
    'last': ['Singh', 'Kumar', 'Thakur'],
    'email': ['gs9831@gmail.com', 'rohit420@gmail.com', 'rajat100@gmail.com']
}

import pandas as pd
df = pd.DataFrame(people)


# In[15]:


df


# In[16]:


df['full_name']= df['first']+ ' ' + df['last'] #Adding new column


# In[17]:


df


# In[20]:


#Dropping columns
df.drop(columns = ['full_name'])


# In[26]:


#Adding single row
new_row = pd.DataFrame([{'first': 'Tony', 'last': 'Singh', 'email': 'tony@gmail.com'}])


# In[27]:


df = pd.concat([df, new_row], ignore_index=True)


# In[28]:


df


# In[29]:


people = {
    'first': ['Saurabh', 'Tharu'],
    'last': ['Singh', 'Kumar'],
    'email': ['saurabh@gmail.com', 'tharu87@gmail.com']
}

df2 = pd.DataFrame(people)


# In[30]:


df2


# In[31]:


#Adding a data frame

df3 = pd.concat([df, df2], ignore_index=True)


# In[32]:


df3


# In[33]:


#Remving row

df3.drop(index=5)


# In[43]:


#Removing multiple rows

filt = df3['last'] == 'Singh'
df3.drop(index=df3[filt].index)


# In[ ]:




