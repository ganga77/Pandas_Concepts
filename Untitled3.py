#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import date
import smtplib



# In[19]:


URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text().strip()


price = soup2.find('span', class_='a-price').find('span', class_='a-offscreen').get_text().strip()

price = price.strip()[1:]
title = title.strip()


# In[22]:


import datetime
today = datetime.date.today()


# In[23]:


#Writing the data for the first time

import csv

header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open('/Users/gangasingh/Downloads/AmazonWebScrapperDataSet.csv', 'w', newline ='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[24]:


import pandas as pd
df = pd.read_csv(r'/Users/gangasingh/Downloads/AmazonWebScrapperDataSet.csv')

df


# In[29]:


# Now we are appending the data to the csv

with open('/Users/gangasingh/Downloads/AmazonWebScrapperDataSet.csv', 'a+', newline ='', encoding='UTF8') as f:
    writer = csv.writer(f)
    
    writer.writerow(data)


# In[38]:


def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('incredime123@gmail.com','F@stracks777')
    
    subject = "The Shirt you want is below $10! Now is your chance to buy!"
    body = "Ganga, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'incredime123@gmail.com',
        msg
     
    )


# In[32]:


def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id='productTitle').get_text().strip()


    price = soup2.find('span', class_='a-price').find('span', class_='a-offscreen').get_text().strip()

    price = price.strip()[1:]
    title = title.strip()
    
    import datetime
    today = datetime.date.today()
    
    import csv

    header = ['Title', 'Price', 'Date']
    data = [title, price, today]

    with open('/Users/gangasingh/Downloads/AmazonWebScrapperDataSet.csv', 'a+', newline ='', encoding='UTF8') as f:
        writer = csv.writer(f)
        
        writer.writerow(data)
    
    if(price < 10):
        send_mail()
    


# In[36]:


while True:
    check_price()
    time.sleep(50)


# In[37]:


import pandas as pd
df = pd.read_csv(r'/Users/gangasingh/Downloads/AmazonWebScrapperDataSet.csv')

df


# In[ ]:




