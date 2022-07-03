from flask import Flask, request, Response
import pandas as pd
from Rossmann import Rossmann
import pickle
import os

#Carregar o modelo
model = pickle.load( open("model/final_model.pkl" , "rb") )

app = Flask(__name__)
@app.route('/rossmann/predict', methods=['POST'])

#função para obtenção das previsões
def rossmann_predict(): 
    
    test_json = request.get_json()
    
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
    port = os.environ.get("PORT",5000)
    app.run(host = '0.0.0.0', port=port)