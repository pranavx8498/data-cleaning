#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[3]:


df=pd.read_csv('titanic.csv')


# In[4]:


sns.displot(df.Age.dropna(),kind='hist')


# In[5]:


df.boxplot(['Age'])# their are ouliers


# In[9]:


# using standerd daviation but only with gaussion distributed data
ub_loundry=df.Age.mean()+3**df.Age.std()
lb_loundry=df.Age.mean()-3**df.Age.std()
df_no_out=df[(df.Age<ub_loundry) & (df.Age>lb_loundry)]


# In[19]:


#usinng z score z=x-mean/S.D.
df['zscore']=df.Age-df.Age.mean()/df.Age.std()
df_with_zscore=df[(df.zscore<-3) | (df.zscore>3)]


# In[22]:


#IQR
IQR=df.Age.quantile(0.75)-df.Age.quantile(0.25)
lower_l=(df.Age.quantile(0.25))-(IQR**1.5)
upper_l=((df.Age.quantile(0.75))+(IQR**1.5))
df_iqr=df[(df.Age>lower_l)&df.Age<upper_l]


# In[ ]:




