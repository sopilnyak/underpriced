from features_extractor import centered_subways, encode_with_OneHotEncoder_and_delete_column, encode_with_LabelEncoder, perform_coding_and_delete_column
from sklearn.externals import joblib
import pandas as pd
import os
import numpy as np
import json


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HARD_PRICE = 30000

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
    except TypeError:
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
        underground=None,        
        has_balcony=None,     
        has_loggia=None,      
        curr_floor=None,            
        total_floor=None):

    json_data = open(os.path.join(BASE_DIR, 'ml_module/average_data.json')).read()
    average_data = json.loads(json_data)

    centered_subways_lower = [item.lower() for item in centered_subways]
    features = {
        'area': prepare_feature(average_data, 'area', area, float),
        'combined_bathroom_count': prepare_feature(average_data, 'combined_bathroom_count', combined_bathroom_count, int),
        'construction_year': prepare_feature(average_data, 'construction_year', construction_year, int), 
        'house_type': house_type,
        'kitchen_area': prepare_feature(average_data, 'kitchen_area', kitchen_area, float),
        'living_area': prepare_feature(average_data, 'living_area', living_area, float),
        'repair': repair,
        'rooms':  prepare_feature(average_data, 'rooms', rooms, int),
        'underground':  underground.lower(),
        'has_balcony': has_to_int(has_balcony),
        'has_loggia': has_to_int(has_loggia),
        'curr_floor': prepare_feature(average_data, 'curr_floor', curr_floor, int),
        'total_floor': prepare_feature(average_data, 'total_floor', total_floor, int),
        'is_center': underground.lower() in centered_subways_lower
    }
    
    data = pd.DataFrame(features, index=[0])
    data, metro_le_encoder = encode_with_OneHotEncoder_and_delete_column(data,'underground')
    data, house_type_le_encoder = encode_with_OneHotEncoder_and_delete_column(data,'house_type')
    data, repair_le_encoder = encode_with_OneHotEncoder_and_delete_column(data,'repair')
    clf = joblib.load(os.path.join(BASE_DIR, 'ml_module/model_random_forest.pkl'))
    
    columns = []
    with open(os.path.join(BASE_DIR, 'ml_module/flats_features.csv'), 'r') as f:
        columns = np.array(f.readline().split(','))

    columns = np.delete(columns, np.argwhere(columns=='price'))
    with open(os.path.join(BASE_DIR, 'ml_module/features.json'), 'w') as outfile:
        all_columns = {}
        all_columns['features'] = columns.tolist()
        json.dump(all_columns, outfile)

    flat = pd.DataFrame(columns=columns)
    flat = flat.append(data)
    flat = flat.fillna(0)
    price = 0
    
    # TODO: different amount of features sometimes
    try:
        price = round(clf.predict(flat).tolist()[0])
    except:
        price = HARD_PRICE
    return price