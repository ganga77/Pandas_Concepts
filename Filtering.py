#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2022/survey_results_public.csv', index_col="ResponseId")
df


# In[3]:


schema_df = pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2022/survey_results_schema.csv', index_col='qname')
schema_df


# In[4]:


high_salary = df['ConvertedCompYearly'] > 70000
df[high_salary]


# In[7]:


df.loc[high_salary, ['ProfessionalTech', 'ConvertedCompYearly']]


# In[12]:


#Multiple Filter
onboard_nature = ['Just right', 'Very short']
onboarding = df['Onboarding'].isin(onboard_nature)

combined_condition = high_salary & onboarding

df[combined_condition]


# In[13]:


df.loc[combined_condition, 'LearnCode']


# In[14]:


#using str method
filt = df['EdLevel'].str.contains('M.A.', na=False)
df.loc[filt]


# In[15]:


x=df['EdLevel']


# In[28]:


x=df['EdLevel']
df.loc[[3,8], 'EdLevel']


# In[ ]:




