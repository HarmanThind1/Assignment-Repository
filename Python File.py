#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Python Libraries
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#Read csv file
df = pd.read_csv("Salaries.csv")


# In[3]:


df.head(20)


# In[4]:


#Data type of each column
df.info()


# In[5]:


# If you are looking to return all fundamental statistics for a numerical variable, 
# Then use the describe function. Note that this function work with numerical variables only.
df.describe()


# In[6]:


#Select data for female professors
df_female = df[ df['sex'] == 'Female']
df_female.head()


# In[7]:


# Using filtering, find the mean value of the salary for the discipline A
df[ df['discipline'] =='A'].salary.mean()


# In[8]:


#Show graphs withint Python notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


#Use matplotlib to draw a histogram of a salary data
plt.hist(df['salary'],bins=10, density= True)


# In[11]:


# Use regular matplotlib function to display a barplot
df.groupby(['rank'])['salary'].count().plot(kind='bar')


# In[12]:


# Use seaborn package to display a barplot
sns.set_style("whitegrid")

ax = sns.barplot(x='rank',y ='salary', data=df, estimator=len)


# In[13]:


# Split into 2 groups:
ax = sns.barplot(x='rank',y ='salary', hue='sex', data=df, estimator=len)

