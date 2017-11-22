
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.externals import joblib


# In[7]:


df = pd.read_csv('flats_features.csv')


# In[8]:


X = df.drop({'price'}, axis=1)
Y = df['price']
X.set_index(X['id'], inplace=True)
X = X.drop('id', axis=1)


# In[9]:


X.info()


# In[10]:


records_count = Y.count()
kf = KFold(n=records_count, n_folds=7, shuffle=True, random_state=42)

estims = {}

for k in range(1, 75, 2):
    clf = RandomForestRegressor(n_estimators=k, random_state=0)
    quality = cross_val_score(clf, X, Y, scoring='r2', cv=kf).mean()
    print("hey")
    estims[k] = quality


# In[11]:


best_estim = sorted(estims.items(), key=lambda x: -x[1])
print(best_estim)


# In[13]:


clf = RandomForestRegressor(n_estimators=best_estim[0][0], random_state=42)
clf.fit(X, Y)
print("SHAPE")
print(X.shape)
print(X.columns)

# In[14]:


# joblib.dump(clf, 'model_random_forest.pkl') 


# # In[15]:


# features = X.columns.values
# importances = clf.feature_importances_
# indices = np.argsort(importances)[::-1]

# indices = indices[:10]
# for i in range(0, len(indices)):
#     print(str(features[indices[i]]) + " " + str(importances[indices[i]]))


# # In[16]:


# predictions = pd.DataFrame(clf.predict(X))[0]
# X = X.reset_index()


# # In[17]:


# res_info = pd.DataFrame(columns=[u'Ошибка,%',u'Ошибка,$',u'Цена м.кв.'])
# for i in Y.index:
#     error = (Y[i] - predictions[i])
#     rel_error = error/predictions[i]*100
#     res_info.loc[i] = pd.Series({
#             u'Ошибка,%':round(rel_error,1),
#             u'Ошибка,$':int(error),
#             u'Цена м.кв.':int(Y[i] / X['area'][i])
#     })


# # In[18]:


# predictions = pd.DataFrame(predictions)


# # In[19]:


# predictions = predictions.set_index(X['id'])


# # In[20]:


# res_info = res_info.set_index(X['id'])


# # In[21]:


# res_info


# # In[22]:


# res_info.sort_values(by=u'Ошибка,%')[:5]


# # In[23]:


# res_info.sort_values(by=u'Ошибка,%', ascending=False)[:5]


# # In[24]:


# X.set_index(X['id'], inplace=True)
# X = X.drop('id', axis=1)


# # In[26]:


# predictions = predictions[0].map(lambda x: int(x))


# # In[27]:


# predictions.to_csv('real_prices.csv')


# # In[28]:


# predictions

