from flask import Flask, request, Response
import pandas as pd
from Rossmann import Rossmann
import pickle

model = pickle.load( open("\\Users\\Eduardo\\repos\\sales_prediction\\model\\final_model.pkl" , "rb") )

app = Flask(__name__)


@app.route('/rossmann/predict', methods=['POST'])

def rossmann_predict():
    
    test_json = request.get_json()
    print()
    
    if test_json:
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index = [0])
            
        else:
            test_raw = pd.DataFrame(test_json, columns = test_json[0].keys())
            
        pipeline = Rossmann()
        
        df1 = pipeline.data_preparation(test_raw)
        
        df1 = pipeline.feature_engeneering(df1)
        
        df_response = pipeline.get_prediction(model, test_raw, df1)
        
        return df_response
        
        
    else:
        return Response('{}', status = 200, mimetype = "application/json")



if __name__ == "__main__":
    app.run('0.0.0.0')