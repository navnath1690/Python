#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as snx
import plotly.express as px
plt.style.use('dark_background')


# In[2]:


df=pd.read_csv('zomato.csv')
df.shape


# In[3]:


df.info()


# In[4]:


df.drop_duplicates(inplace=True)


# In[5]:


#Rate Data cleaning
def ratealter(value):
    if value=='NEW' or value=='-':
        return np.nan
    else:
        value=str(value).split('/')
        value=value[0]
        return float(value)

df['rate']=df['rate'].apply(ratealter)
df['rate'].head(5)


# In[6]:


df.isnull().sum()


# In[7]:


df['rate'].fillna(df['rate'].mean(), inplace=True)


# In[8]:


df['rate'].isnull().sum()


# In[9]:


df.dropna(inplace=True)


# In[10]:


df.head(5)


# In[11]:


df.rename(columns={'approx_cost(for two people)':'Cost2plates','listed_in(type)':'Type'}, inplace=True)


# In[12]:


df.columns


# In[13]:


df.drop(['url','address','phone'],axis=1,inplace=True)


# In[14]:


df['Cost2plates'].unique()


# In[15]:


#To remove commas from cost2plates column

def commaremove(value):
    value=str(value).replace(",","")
    return value
df['Cost2plates']=df['Cost2plates'].apply(commaremove)


# In[16]:


df['rest_type'].value_counts()


# In[17]:


other_resttypes=(df['rest_type'].value_counts())<1000
def resttypes(value):
    if(value in other_resttypes):
        return value
    else:
        return 'Others'
df['rest_type']=df['rest_type'].apply(resttypes)
df['rest_type']


# In[18]:


location = df['location'].value_counts(ascending=False)
location_lessthan300=location[location<300]
def handle_location(value):
    if(value in location_lessthan300):
        return 'others'
    else:
        return value
df['location']=df['location'].apply(handle_location)
df['location'].value_counts()


# In[19]:


df['cuisines'].nunique()


# In[23]:


import seaborn as sns
plt.figure(figsize=(16,10))
sns.countplot(df['location'])
plt.xticks(rotation=90)


# In[ ]:





# In[24]:


df.columns


# In[39]:


#Cost2plates location wise
sort=df.sort_values(by='Cost2plates',ascending=False)
sns.lineplot(x='location',y='Cost2plates',data=df)
plt.xticks(rotation=90)
plt.show()


# In[48]:


#Countplot of cuisines
sns.countplot(x='cuisines',data=df)
plt.show()
plt.xticks(rotation=90)


# In[46]:


df['cuisines'].value_counts()


# In[47]:


cuisines = df['cuisines'].value_counts(ascending=False)
cuisines_lessthan250=cuisines[cuisines<250]
def handle_cuisines(value):
    if(value in cuisines_lessthan250):
        return 'others'
    else:
        return value
df['cuisines']=df['cuisines'].apply(handle_cuisines)
df['cuisines'].value_counts()


# In[50]:


#Boxplot
sns.boxplot(x='Type',y='rate',data=df)
plt.xticks(rotation=90)
plt.show()


# In[ ]:




