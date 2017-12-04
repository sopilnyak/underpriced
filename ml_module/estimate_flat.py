# import sys
# sys.path.append('.')
from features_extractor.utils import centered_subways, encode_with_OneHotEncoder_and_delete_column, encode_with_LabelEncoder, perform_coding_and_delete_column
from sklearn.externals import joblib
import pandas as pd
import os
import numpy as np
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def has_to_int(feature):
    if feature in ['Да', 'да']:
        return 1
    else:
        return 0

def prepare_feature(average_data, label, feature, type):
    if label == 'rooms':
        if feature == 'студия':
            return -1
    try:
        feature = type(feature)
    except (TypeError, ValueError):
        feature = None
    return type(feature) if feature is not None else type(average_data[label])

def estimate_flat(
        area=None, 
        combined_bathroom_count=None,
        construction_year=None,    
        house_type=None,
        kitchen_area=None,
        living_area=None,      
        repair=None,   
        rooms=None,           
        underground_name=None,        
        has_balcony=None,     
        has_loggia=None,      
        curr_floor=None,            
        total_floor=None,
        underground_way=None, 
        underground_time=None):

    json_data = open(os.path.join(BASE_DIR, 'ml_module/features_extractor/average_data.json')).read()
    average_data = json.loads(json_data)

    centered_subways_lower = [item.lower() for item in centered_subways]
    features = {
        'area': prepare_feature(average_data, 'area', area, float),
        'combined_bathroom_count': prepare_feature(average_data, 'combined_bathroom_count', combined_bathroom_count, int),
        'construction_year': prepare_feature(average_data, 'construction_year', construction_year, int), 
        'house_type': house_type,
        'kitchen_area': prepare_feature(average_data, 'kitchen_area', kitchen_area, float),
        'living_area': prepare_feature(average_data, 'living_area', living_area, float),
        'repair': 'отсутствует' if repair is None else repair,
        'rooms': prepare_feature(average_data, 'rooms', rooms, int),
        'underground_name': underground_name.lower(),
        'has_balcony': has_to_int(has_balcony),
        'has_loggia': has_to_int(has_loggia),
        'curr_floor': prepare_feature(average_data, 'curr_floor', curr_floor, int),
        'total_floor': prepare_feature(average_data, 'total_floor', total_floor, int),
        'is_center': underground_name.lower() in centered_subways_lower, 
        'underground_way': -1 if underground_way == 'пешком' else 1,
        'underground_time': prepare_feature(average_data, 'underground_time', underground_time, int)
    }
    #rint(features)
    data = pd.DataFrame(features, index=[0])
    data, metro_le_encoder = encode_with_OneHotEncoder_and_delete_column(data,'underground_name')
    data, house_type_le_encoder = encode_with_OneHotEncoder_and_delete_column(data,'house_type')
    data, repair_le_encoder = encode_with_OneHotEncoder_and_delete_column(data,'repair')
    clf = joblib.load(os.path.join(BASE_DIR, 'ml_module/algorithm/model_random_forest.pkl'))
    
    columns = []
    with open(os.path.join(BASE_DIR, 'ml_module/features_extractor/features.json'), 'r') as f:
        columns = np.array(json.loads(f.readline())['features'])

    columns = np.delete(columns, np.argwhere(columns == 'price'))

    flat = pd.DataFrame(columns=columns)
    flat = flat.append(data)
    flat = flat.fillna(0)
    price = 0
    # TODO: different amount of features sometimes
    try:
        price = round(clf.predict(flat).tolist()[0])
    except:
        raise NameError('SmthWentWrong')
    return price