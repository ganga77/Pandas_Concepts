#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2023/survey_results_public.csv')
df


# In[2]:


survey=pd.read_csv(r'/Users/gangasingh/Downloads/stack-overflow-developer-survey-2023/survey_results_schema.csv')
survey


# In[5]:


df.columns


# In[6]:


df['Country']


# In[7]:


df['Country'].value_counts()


# In[8]:


#GRoupBy. It return an object

country_grp = df.groupby(['Country'])


# In[9]:


country_grp.get_group('India')


# In[12]:


country_grp.get_group('India')['ProfessionalTech']


# In[18]:


country_grp['ProfessionalTech'].value_counts().loc['India']


# In[21]:


country_grp[['Age','ConvertedCompYearly']].value_counts().loc['India']


# In[22]:


#Aggregate function
country_grp['ConvertedCompYearly'].agg(['median', 'mean'])


# In[29]:


country_grp.get_group('India')['LanguageHaveWorkedWith'].str.contains('Python').sum()


# In[48]:


country_uses_python = country_grp['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains('Python').sum())


# In[49]:


country_uses_python


# In[42]:


total_developers = df['Country'].value_counts()


# In[43]:


total_developers


# In[55]:


df3 = pd.concat([total_developers, country_uses_python], axis="columns")


# In[56]:


df3


# In[58]:


df3.rename(columns={'count': 'Total Developers', 'LanguageHaveWorkedWith': 'Devs who knows Python'}, inplace=True)


# In[59]:


df3


# In[60]:


df3['%age Python Devs']= (df3['Devs who knows Python']/df3['Total Developers'] * 100)


# In[61]:


df3


# In[ ]:




