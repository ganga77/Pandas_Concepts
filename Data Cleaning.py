#!/usr/bin/env python
# coding: utf-8

# In[90]:


import pandas as pd
df = pd.read_excel(r'/Users/gangasingh/Downloads/Customer Call List.xlsx')
df


# In[91]:


#Removing Duplicates
df = df.drop_duplicates()


# In[92]:


df


# In[93]:


#Droping Columns
df = df.drop(columns={'Not_Useful_Column'})


# In[94]:


df


# In[95]:


df['Last_Name'] = df['Last_Name'].str.lstrip('/')
df['Last_Name'] = df['Last_Name'].str.lstrip('...')
df['Last_Name'] = df['Last_Name'].str.rstrip('_')


# In[96]:


df


# In[97]:


df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','', regex=True)


# In[98]:


df


# In[99]:


df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))
df


# In[100]:


df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3]+ "-" + x[3:6] + "-" + x[6:10])


# In[101]:


df


# In[102]:


df['Phone_Number'] = df['Phone_Number'].str.replace('Na--', '')


# In[103]:


df['Phone_Number'] = df['Phone_Number'].str.replace('nan--', '')


# In[104]:


df


# In[106]:


#Split
df[['Street_Address', 'City', 'Zip_Code']]=df['Address'].str.split(',', n=2, expand= True)


# In[105]:


df


# In[73]:


df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y')


# In[74]:


df


# In[75]:


df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N')
df


# In[115]:


df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y')


# In[116]:


df


# In[111]:


#Handling none, nan etc values

df = df.fillna('')
df


# In[117]:


#We want to drop values in Do_Not_Contact if they are Y

for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)
df        


# In[113]:


#We want to drop values in there is no phone_number 

for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)
df        


# In[86]:


df.set_index("CustomerID", inplace=True)
df


# In[118]:


df


# In[112]:


df


# In[114]:


df


# In[121]:


df = df.drop('Address', axis=1)


# In[122]:


df


# In[123]:


df = df.reset_index(drop=True)


# In[125]:


#Setting Index
df = df.set_index('CustomerID')


# In[126]:


df


# In[ ]:




