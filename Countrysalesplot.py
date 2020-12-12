#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


# In[90]:


df=pd.read_csv(r'H:\CLASS\sem 3\Computation Statistics\100SalesRecords.csv')


# In[91]:


df.head()


# In[92]:


#df.describe()


# In[93]:


df.plot()


# In[94]:


plt.figure(figsize=(9,6))
plt.bar(x=df['Region'],
    height=df['Units Sold'],
    color='midnightblue')
plt.xticks(rotation=90)
plt.title('Sales by Region')


# In[95]:


plt.pie(df['Units Sold'],labels=df['Region'],autopct='%1.1f%%')
plt.axis('equal')
plt.tight_layout()
plt.show()


# In[100]:


sns.boxplot(y='Units Sold',data=df)#('Region','Units Sold')


# In[ ]:




