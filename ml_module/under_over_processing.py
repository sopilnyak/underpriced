import sys
sys.path.append('../')
from core.database import get_client
from estimate_flat import estimate_flat
from features_extractor.utils import get_nearest_undergroud, get_underground_way, get_underground_time

if __name__ == "__main__":
    client = get_client()
    db = client.underpriced
    for flat in db.unprocessedFlats.find({'processed': {'$ne': True}}):
        undergrounds = None if 'underground' not in flat else flat['underground']
        underground_name = get_nearest_undergroud(undergrounds)
        if (flat['_id'] == '165528286'):
            continue
        if 'house_type' not in flat:
            continue
        if 'repair' not in flat:
            continue
        if flat['repair'] == 'отсутствует':
            print('wrong')
            continue
            
        try:
            flat['estimated_price'] = estimate_flat(
                area=None if 'area' not in flat else flat['area'].replace(',', '.'), 
                combined_bathroom_count=None if 'combined_bathroom_count' not in flat else flat['combined_bathroom_count'],
                construction_year=None if 'construction_year' not in flat else flat['construction_year'],    
                house_type=None if 'house_type' not in flat else flat['house_type'],
                kitchen_area=None if 'kitchen_area' not in flat else flat['kitchen_area'].replace(',', '.'),
                living_area=None if 'living_area' not in flat else flat['living_area'].replace(',', '.'),      
                repair=None if 'repair' not in flat else flat['repair'],   
                rooms=None if 'rooms' not in flat else flat['rooms'],           
                underground_name=underground_name,        
                has_balcony=None if 'has_balcony' not in flat else flat['has_balcony'],     
                has_loggia=None if 'has_loggia' not in flat else flat['has_loggia'],      
                curr_floor=None if 'curr_floor' not in flat else flat['curr_floor'],            
                total_floor=None if 'total_floor' not in flat else flat['total_floor'], 
                underground_way=get_underground_way(underground_name, undergrounds), 
                underground_time=get_underground_time(underground_name, undergrounds))
        except:
            continue
        print('id ' + str(flat['_id']))
        print(flat['price'])
        print(flat['estimated_price'])
        flat['relative_goodness'] = round((int(flat['price']['rub_price']) - flat['estimated_price']) / flat['estimated_price'] * 100, 1)
        db.flats.replace_one(
            {'_id': flat['_id']}, 
            flat,
            upsert=True)
        db.unprocessedFlats.update_one({'_id': flat['_id']}, {'$set': {'processed': True}})
    client.close()