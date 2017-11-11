
# coding: utf-8

# In[1]:


import json
import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import Imputer

df = pd.read_json("/home/alena/Documents/underpriced/aggregation_module/flats.json", orient='values')


# In[2]:


df['id'] = df['url'].map(lambda url: int(url.split('/')[5]))


# In[3]:


df.set_index(df['id'], inplace=True)
df = df.drop('id', axis=1)


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


# Частотное распределение данных в столбце цена
df['price'].value_counts()[:10]


# ## Work with features

# In[7]:


df = df.drop('apartment_status', axis=1)


# In[8]:


df['has_balcony'] = df['balcony'].map(lambda x: 1 if x.find(u'есть балкон') != -1 else 0)
df['has_loggia'] = df['balcony'].map(lambda x: 1 if x.find(u'есть лоджия') != -1 else 0)
df = df.drop('balcony', axis=1)


# In[9]:


df['ceiling_height'].isnull().sum() # 2582 null out of 3735
df = df.drop('ceiling_height', axis=1)


# In[10]:


# fill with mean
imputer = Imputer(missing_values=np.nan, strategy="median", axis=0)
df['construction_year'] = imputer.fit_transform(df['construction_year'].values.reshape(-1, 1))
df['construction_year'] = df['construction_year'].map(lambda x: int(x))


# In[11]:


imputer = Imputer(missing_values=np.nan, strategy="median", axis=0)
df['combined_bathroom_count'] = imputer.fit_transform(df['combined_bathroom_count'].values.reshape(-1, 1))
df['combined_bathroom_count'] = df['combined_bathroom_count'].map(lambda x: int(x))


# In[12]:


df = df.drop('description', axis=1)


# In[13]:


df['room_type'].isnull().sum() # 2615 out of 3735
df = df.drop('room_type', axis=1)


# In[14]:


df['living_area'] = df['living_area'].map(lambda x: x.replace(',', '.') if ',' in x else x)
df.loc[df.living_area == '–', 'living_area'] = np.nan
df['living_area'] = df['living_area'].map(lambda x: float(x) if x is not None else x)
imputer = Imputer(missing_values=np.nan, strategy="mean", axis=0)
df['living_area'] = imputer.fit_transform(df['living_area'].values.reshape(-1, 1))


# In[15]:


df['kitchen_area'] = df['kitchen_area'].map(lambda x: x.replace(',', '.') if ',' in x else x)
df.loc[df.kitchen_area == '–', 'kitchen_area'] = np.nan
df['kitchen_area'] = df['kitchen_area'].map(lambda x: float(x) if x is not None else x)
imputer = Imputer(missing_values=np.nan, strategy="mean", axis=0)
df['kitchen_area'] = imputer.fit_transform(df['kitchen_area'].values.reshape(-1, 1)) 


# In[16]:


df['parking'].isnull().sum() # 2536 null out of 3735
df = df.drop('parking', axis=1)


# In[17]:


df['ramp'].isnull().sum() # 3403 null out of 3735
df = df.drop('ramp', axis=1)


# In[18]:


df['house_type'].fillna('не указано', inplace=True) # 1031 out of 3735
df['house_type'].value_counts()


# In[19]:


df['floor'].fillna('0 / 0', inplace=True)
df['curr_floor'] = df['floor'].map(lambda x: int(str(x).split(' / ')[0]))
df['total_floor'] = df['floor'].map(lambda x: int(str(x).split(' / ')[1]))
df = df.drop('floor', axis=1)


# In[20]:


df = df.drop('images', axis=1)


# In[21]:


df = df.drop('district', axis=1)


# In[22]:


df = df.drop('room_area', axis=1)


# In[23]:


df['elevator'].isnull().sum() # 781 out of 3735
df = df.drop('elevator', axis=1)


# In[24]:


df['repair'].fillna('не указано', inplace=True)
df['repair'].value_counts()


# In[25]:


df['rooms'] = df['rooms'].map(lambda x: -1 if type(x) == str and x.find(u'студия') != -1 else x)
df['rooms'] = df['rooms'].map(lambda x: 6 if type(x) == str and x.find(u'многокомн') != -1 else x)
df['rooms'] = df['rooms'].map(lambda x: np.nan if type(x) == str                               and x == 'свободная планировка на длительный срок (от года)' else x)
df = df.dropna(axis=0, how='any', subset=['rooms'])
df['rooms'] = df['rooms'].map(lambda x: int(x))


# In[26]:


df['sleeping_place_count'].isnull().sum() # 3733 out of 3735
df = df.drop('sleeping_place_count', axis=1)


# In[27]:


df['split_bathroom_count'].isnull().sum() # 2194 out of 3735
df = df.drop('split_bathroom_count', axis=1)


# In[28]:


df = df.drop('url', axis=1)


# In[29]:


df = df.drop('view', axis=1)


# In[30]:


df['area'] = df['area'].map(lambda x: float(x.replace(',', '.')) if ',' in x else float(x))


# In[31]:


centered_subways = ['Белорусская', 'Проспект Мира', 'Комсомольская', 'Курская', 'Чкаловская', 'Марксисткая',                    'Таганская', 'Павелецкая', 'Добрынинская', 'Серпуховская', 'Октябрьская', 'Парк культуры',                    'Киевская', 'Краснопресненская', 'Баррикадная', 'Цветной бульвар', 'Сухаревская', 'Трубная',                    'Тургеневская', 'Чистые пруды', 'Красные Ворота', 'Сретенский бульвар', 'Кузнецкий Мост',                    'Маяковская', 'Тверская', 'Пушкинская', 'Чеховская', 'Смоленская', 'Арбатская', 'Александровский сад',                    'Боровицкая', 'Библиотека имени Ленина', 'Кропоткинская', 'Охотный ряд', 'Лубянка',                    'Театральная', 'Площадь Революции', 'Третьяковская', 'Новокузнецкая', 'Кропоткинская',                    'Полянка', 'Китай-город']


# In[32]:


centered_subways = [item.lower() for item in centered_subways]


# In[33]:


df['underground'] = df['underground'].map(lambda x: np.nan if x == {} else x) 
df = df.dropna(axis=0, how='any', subset=['underground'])


# In[34]:


def get_nearest_undergroud(descr):
    if len(descr) == 1:
        return list(descr.keys())[0]
    
    by_step = {}
    by_car = {}
    for subway in descr.keys():
        if 'пешком' in descr[subway]:
            by_step[subway] = int(descr[subway].split(' ')[0])
        else:
            by_car[subway] = int(descr[subway].split(' ')[0])
    step_res = sorted(by_step, key=by_step.get)
    car_res = sorted(by_car, key=by_car.get)
    if len(by_step) == 0:
        return car_res[0]
    else:
        return step_res[0]


# In[35]:


df['underground'] = df['underground'].map(lambda item: str(get_nearest_undergroud(item)).lower())


# In[36]:


df['is_center'] = df['underground'].map(lambda item: 1 if item in centered_subways else 0)


# In[37]:


df['price'] = df['price'].map(lambda item: item['rub_price'] if 'rub_price' in item else np.nan)
df = df.dropna(axis=0, how='any', subset=['price'])
df['price'] = df['price'].map(lambda item: int(item))


# ## Data Analys

# In[38]:


df.info()


# In[40]:


# Create X and Y for data analys


# In[41]:


df.shape


# In[42]:


df.head()


# ## Coding categorial signs   
# We need to code underground, house_type, repair

# In[43]:


from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

""" 
Add to df new column with name 'column_name_le' consists of 
numbers of categories. Delete old column
"""
def encode_with_LabelEncoder(df, column_name):
    label_encoder = LabelEncoder()
    label_encoder.fit(df[column_name])
    df[column_name+'_le'] = label_encoder.transform(df[column_name])
    df.drop([column_name], axis=1, inplace=True)
    return label_encoder

""" 
Coding with existing LabelEncodet
"""
def encode_with_existing_LabelEncoder(df, column_name, label_encoder):
    df[column_name+'_le'] = label_encoder.transform(df[column_name])
    df.drop([column_name], axis=1, inplace=True)
    
"""
Firstly, coding column with LableEncoder
Then add in df new columns: column_name=category_i
Usage: df, label_encoder = encode_with_OneHotEncoder_and_delete_column(df, column_name)
"""
def encode_with_OneHotEncoder_and_delete_column(df, column_name):
    le_encoder = encode_with_LabelEncoder(df, column_name)
    return perform_coding_and_delete_column(df, column_name, le_encoder), le_encoder

"""
Perform ordinary coding and deleting column
"""
def perform_coding_and_delete_column(df, column_name, le_encoder):
    oh_encoder = OneHotEncoder(sparse=False)
    oh_features = oh_encoder.fit_transform(df[column_name+'_le'].values.reshape(-1,1))
    ohe_columns=[column_name + '=' + le_encoder.classes_[i] for i in range(oh_features.shape[1])]

    df.drop([column_name+'_le'], axis=1, inplace=True)

    df_with_features = pd.DataFrame(oh_features, columns=ohe_columns)
    df_with_features.index = df.index
    return pd.concat([df, df_with_features], axis=1)


# In[44]:


df, metro_le_encoder = encode_with_OneHotEncoder_and_delete_column(df,'underground')
df, house_type_le_encoder = encode_with_OneHotEncoder_and_delete_column(df,'house_type')
df, repair_le_encoder = encode_with_OneHotEncoder_and_delete_column(df,'repair')


# In[45]:


df.to_csv('flats_features.csv')


# In[46]:


df.shape

