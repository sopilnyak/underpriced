# Documentation for ML module

### 1. [features extractor.*](https://github.com/sopilnyak/underpriced/blob/master/ml_module/features_extractor.ipynb)

#### Output:
Features | 
--------|
area | 
combined_bathroom_count|   
construction_year |         
house_type (_encoded_)    |        
kitchen_area |  
living_area |       
price  |    
repair  (_encoded_)  |      
rooms   |             
underground (_encoded_)     |          
has_balcony   |        
has_loggia   |         
curr_floor   |               
total_floor  |              
is_center  |           

##### Totally: 228 features    
    
    
### 2. [price_prediction.*](https://github.com/sopilnyak/underpriced/blob/master/ml_module/price_prediction.ipynb)    
##### Trained model for prediction (using random forest)    
### Output: [real_prices.csv](https://github.com/sopilnyak/underpriced/blob/master/ml_module/real_prices.csv)    

id | predicted_price
-----|-----

### 3. [estimate_flat.py]()
##### Gets model from price_prediciton and returns predicted price.
### Input:
Features | Type
--------| ----
area | float: 123.4
combined_bathroom_count | int: 1  
construction_year | int: 1979  
house_type | string: кирпичный      
kitchen_area | float: 12.45
living_area |  float: 13.45     
repair |  string: евроремонт    
rooms   | int: 2 (или студия)          
underground | string: Смоленская   
has_balcony | string: Да
has_loggia   | string: Нет         
curr_floor   | int: 4       
total_floor  | int: 12 