import pandas as pd
import json
import requests
from flask import Flask, request, Response
import os

TOKEN = 

#bot info
#https://api.telegram.org/bot5546751096:AAH-_4Dwul6Lqxvp246yEIWhe7mY-O6l9Q0/getME

#bot updates
#https://api.telegram.org/bot5546751096:AAH-_4Dwul6Lqxvp246yEIWhe7mY-O6l9Q0/getUpdates

#bot message
#https://api.telegram.org/bot5546751096:AAH-_4Dwul6Lqxvp246yEIWhe7mY-O6l9Q0/sendMessage?chat_id=5403219550&text=Hi, i am alive!


#https://api.telegram.org/bot5546751096:AAH-_4Dwul6Lqxvp246yEIWhe7mY-O6l9Q0/setWebhook?url=https://git.heroku.com/app-220701-ross-bot.git


def send_message(chat_id, text):

    #bot message
    url = "https://api.telegram.org/bot{}/".format(TOKEN)
    url = url + "sendMessage?chat_id={}".format(chat_id)    
    r = requests.post(url, json = {"text":text})
    print("Status Code {}".format(r.status_code))
    
    return None

def load_data(store_id):

    # Carregando os dados de teste em produção
    test_df = pd.read_csv(r"test.csv")
    store_df = pd.read_csv(r"store.csv")

    # Juntando os dados das lojas com os dados das vendas
    df = pd.merge(test_df, store_df, how = 'left', on = "Store")

    # Selecionando a loja    
    lojas = store_id
    df = df[df["Store"]==(lojas)]
    
    if not df.empty:
    
        # Retirando do DF de teste os dias que as lojas estavam fechadas e dados faltantes
        df = df[df["Open"] == 1]
        df = df[~df["Open"].isnull()]

        # Convertendo o DF em Json
        data = json.dumps(df.to_dict(orient = "records"))
    
    else:
        data = "error"
    
    return data


def predict(data):

    url = "https://app-220629-sales-pred.herokuapp.com/rossmann/predict"
    header = {'Content-type': "application/json"}
    data = data

    r = requests.post(url, data = data, headers = header)
    print("Status Code {}".format(r.status_code))


    df1 = pd.DataFrame(r.json(), columns = r.json()[0].keys())

    return df1

def parse_message(message):
    
    chat_id = message['message']['chat']["id"]
    store_id = message['message']['text']
    
    store_id = store_id.replace("/","")
    
    try:
        store_id = int(store_id)
    except ValueError:
        store_id = 'error'

    return chat_id, store_id

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    
    if request.method == "POST":
        message = request.get_json()
        chat_id, store_id = parse_message(message)
        
        if store_id != "error":
            #carregando dados
            data = load_data(store_id)
            if data != "error":
                #realizando as previsões
                df1 = predict(data)
                #Calculo
                receita = df1[df1["store"] == store_id]["prediction"].sum()
                msg = "A loja {} irá gerar R$ {:,.2f} de receita nos próximos 6 meses".format(store_id, receita)
                send_message(chat_id, msg)
                return Response("Ok", status = 200)
                    
            else:
                send_message(chat_id, "Loja não disponível")
                return Response("Ok", status = 200)

        else:
            send_message(chat_id, "ID da loja não identificado")
            return Response('Ok', status=200)
    else:
        return "<h1> Rossmann Telegram BOT </h1>"

if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(host = "0.0.0.0", port = port)


