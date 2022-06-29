import inflection
import numpy as np
import pandas as pd

class Rossmann( object ):
    def __init__(self):
    
        return None
    
    def data_preparation(self, df1):
        
        # Limpeza dos labels
        old_labels = df1.columns
        new_labels = [inflection.underscore(i) for i in old_labels]
        df1.columns = new_labels
        
        # Selecionando variáveis que entrarão no modelo
        columns = ['store', 'open', 'promo', 'competition_distance', 'date', 'day_of_week',
       'state_holiday','school_holiday', 'store_type', 'assortment']
        df1 = df1[columns]
        
        # Ajustando a coluna date
        df1["date"] = pd.to_datetime(df1["date"])
        
        
        # Limpeza de NANs
        
        #competition_distance
        df1["competition_distance"].fillna(value = 10*75860, inplace = True )
        
        return df1
    
    def feature_engeneering(self, df1):
        
        df1["date_day"] = df1["date"].dt.day
        df1["date_month"] = df1["date"].dt.month
        df1["date_year"] = df1["date"].dt.year
        df1["date_week"] = df1["date"].dt.isocalendar().week
        
        df1.drop(labels = ["date"], axis = 1, inplace = True)
        
        return df1
    
    def get_prediction(self, model, original_data, test_data):
        
        pred = model.predict(test_data)
        
        original_data["prediction"] = pred
        
        return original_data.to_json(orient = "records", date_format = "iso")
    
    
