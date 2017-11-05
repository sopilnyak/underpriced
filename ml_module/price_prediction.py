
# coding: utf-8

# In[164]:


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
from sklearn.model_selection import GridSearchCV


# In[165]:


df = pd.read_csv('flats_features.csv')


# In[166]:


X = df.drop({'price'}, axis=1)
Y = df['price']
X.set_index(X['id'], inplace=True)
X = X.drop('id', axis=1)


# In[167]:


records_count = Y.count()
kf = KFold(n=records_count, n_folds=7, shuffle=True, random_state=42)

for k in range(1, 75, 2):
    clf = RandomForestRegressor(n_estimators=k, random_state=0)
    quality = cross_val_score(clf, X, Y, scoring='r2', cv=kf).mean()
    print (k, quality)


# In[192]:


clf = RandomForestRegressor(n_estimators=73, random_state=42)
clf.fit(X, Y)


# In[193]:


features = X.columns.values
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]

indices = indices[:10]
for i in range(0, len(indices)):
    print(str(features[indices[i]]) + " " + str(importances[indices[i]]))


# In[194]:


predictions = pd.DataFrame(clf.predict(X))[0]
X = X.reset_index()


# In[196]:


res_info = pd.DataFrame(columns=[u'Ошибка,%',u'Ошибка,$',u'Цена м.кв.'])
for i in Y.index:
    error = (Y[i] - predictions[i])
    rel_error = error/predictions[i]*100
    res_info.loc[i] = pd.Series({
            u'Ошибка,%':round(rel_error,1),
            u'Ошибка,$':int(error),
            u'Цена м.кв.':int(Y[i] / X['area'][i])
    })


# In[202]:


predictions = pd.DataFrame(predictions)


# In[204]:


predictions = predictions.set_index(X['id'])


# In[207]:


res_info = res_info.set_index(X['id'])


# In[208]:


res_info


# In[209]:


res_info.sort_values(by=u'Ошибка,%')[:5]


# In[210]:


res_info.sort_values(by=u'Ошибка,%', ascending=False)[:5]


# In[214]:


X.set_index(X['id'], inplace=True)
X = X.drop('id', axis=1)


# In[216]:


X.loc[163828377]


# In[221]:


predictions = predictions[0].map(lambda x: int(x))


# In[222]:


predictions.to_csv('real_prices.csv')


# In[223]:


predictions

