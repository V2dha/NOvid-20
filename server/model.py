#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# In[2]:


df = pd.read_csv('Cleaned-Data.csv')
df.tail()


# In[3]:





# In[4]:


df.shape


# In[5]:





# In[6]:


df.dtypes


# In[7]:


df['Severity'] = (df.iloc[:, 19:23] == 1).idxmax(1)


# In[8]:


df.head()


# In[9]:


df['Severity'].value_counts()


# In[10]:




# In[54]:


df['Target'] = df['Severity'].replace('Severity_None', 0).replace('Severity_Mild', 1).replace('Severity_Moderate', 1).replace('Severity_Severe', 1)


# In[12]:


df.tail()


# In[13]:


df.iloc[:, 23:26].head()


# In[14]:


df['Contact'] = (df.iloc[:, 23:26] == 1).idxmax(1)


# In[15]:


df.head()


# In[16]:


df['Contact'].value_counts()


# In[17]:


df['Contact'] = df['Contact'].replace('Contact_No', 0).replace('Contact_Yes', 1).replace('Contact_Dont-Know', 2)


# In[18]:


df.head()


# In[19]:


df.dtypes


# In[20]:


df.iloc[:, 11:16].head()


# In[21]:


df['Age_Label'] = (df.iloc[:, 11:16] == 1).idxmax(1)
df['Age_Label'] = df['Age_Label'].replace('Age_0-9', 0).replace('Age_10-19', 1).replace('Age_20-24', 2).replace('Age_25-59', 3).replace('Age_60+', 4)


# In[22]:


df.tail()


# In[23]:


df.iloc[:, 16:19].head()


# In[24]:


df['Gender'] = (df.iloc[:, 16:19] == 1).idxmax(1)
df['Gender'] = df['Gender'].replace('Gender_Female', 1).replace('Gender_Male', 0).replace('Gender_Transgender', 2)


# In[25]:


df.head()


# In[26]:


df.columns


# In[55]:


X = df[['Fever', 'Tiredness', 'Dry-Cough', 'Difficulty-in-Breathing',
       'Sore-Throat', 'Pains', 'Nasal-Congestion',
       'Runny-Nose', 'Diarrhea', 'Contact', 'Age_Label',
       'Gender']]
X.head(30)


# In[56]:


Y = df[['Target']]
Y.head()


# In[57]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 4)
x_train.shape, y_train.shape


# In[58]:


from sklearn.linear_model import LogisticRegression
LR = LogisticRegression()
LR.fit(x_train, y_train)


# In[59]:


y_pred = LR.predict(x_test)


# In[60]:


import sklearn.metrics as skm
skm.multilabel_confusion_matrix(y_test, y_pred)


# In[61]:


print(skm.classification_report(y_test, y_pred))
