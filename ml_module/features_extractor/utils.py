from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

def get_nearest_undergroud(descr):
    if len(descr) == 0:
        return None

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
    if len(by_step) != 0:
        return step_res[0]
    if len(by_car) != 0:
        return car_res[0]
    else:
        return None
    
def get_underground_way(underground_name, undergrounds):
    if undergrounds == {} or underground_name is None:
        return None
    return -1 if 'пешком' in undergrounds[underground_name] else 1

def get_underground_time(underground_name, undergrounds):
    if undergrounds == {} or underground_name is None:
        return None
    return undergrounds[underground_name].split(' ')[0]

centered_subways = ['Белорусская', 'Проспект Мира', 'Комсомольская', 'Курская', 'Чкаловская', 'Марксисткая', 'Таганская', 'Павелецкая', 'Добрынинская', 'Серпуховская', 'Октябрьская', 'Парк культуры', 'Киевская', 'Краснопресненская', 'Баррикадная', 'Цветной бульвар', 'Сухаревская', 'Трубная', 'Тургеневская', 'Чистые пруды', 'Красные Ворота', 'Сретенский бульвар', 'Кузнецкий Мост', 'Маяковская', 'Тверская', 'Пушкинская', 'Чеховская', 'Смоленская', 'Арбатская', 'Александровский сад', 'Боровицкая', 'Библиотека имени Ленина', 'Кропоткинская', 'Охотный ряд', 'Лубянка', 'Театральная', 'Площадь Революции', 'Третьяковская', 'Новокузнецкая', 'Кропоткинская', 'Полянка', 'Китай-город']

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