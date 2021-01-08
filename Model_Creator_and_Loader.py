#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from joblib import load #, dump

# mld = pd.read_csv('music.csv')
# gad = mld.drop(columns = ['genre'])
# output = mld['genre']

# model = DecisionTreeClassifier()
# patterns = model.fit(gad, output)
# dump('music recommender model.joblib')

model = load('music recommender model.joblib')
predictions = model.predict([[5, 1]])
predictions


# In[ ]:




