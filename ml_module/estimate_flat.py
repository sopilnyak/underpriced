from features_extractor import centered_subways, encode_with_OneHotEncoder_and_delete_column, encode_with_LabelEncoder, perform_coding_and_delete_column
from sklearn.externals import joblib
import pandas as pd

def has_to_int(feature):
    if feature in ['Да', ' да']:
        return 1
    else:
        return 0

def estimate_flat(
        area, 
        combined_bathroom_count,
        construction_year,    
        house_type,
        kitchen_area,
        living_area,      
        repair,   
        rooms,           
        underground,        
        has_balcony,     
        has_loggia,      
        curr_floor,            
        total_floor):
    
    centered_subways_lower = [item.lower() for item in centered_subways]
    features = {
    'area': float(area),
    'combined_bathroom_count': int(combined_bathroom_count),
    'construction_year': int(construction_year), 
    'house_type': house_type,
    'kitchen_area': float(kitchen_area),
    'living_area': float(living_area),
    'repair': repair,
    'rooms': int(rooms),
    'underground': underground.lower(),
    'has_balcony': has_to_int(has_balcony),
    'has_loggia': has_to_int(has_loggia),
    'curr_floor': int(curr_floor),
    'total_floor': int(total_floor),
    'is_center': underground.lower() in centered_subways_lower
    }
    
    flat = pd.DataFrame(features, index=[0])
    flat, metro_le_encoder = encode_with_OneHotEncoder_and_delete_column(flat,'underground')
    flat, house_type_le_encoder = encode_with_OneHotEncoder_and_delete_column(flat,'house_type')
    flat, repair_le_encoder = encode_with_OneHotEncoder_and_delete_column(flat,'repair')
    clf = joblib.load('model_random_forest.pkl') 
    
    df = pd.read_csv('flats_features.csv')
    df = df.drop(['price'], axis=1)
    df = df[:1]
    df = df.drop(df.index[0])
    df = df.append(flat)
    df = df.fillna(0)
    return clf.predict(df)