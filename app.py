import requests # tem que instalar
import json

from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    data = request.get_json(silent=True)

    #print(data)
    intentName = data['queryResult']['intent']['displayName']
    nome = data['queryResult']['parameters']['nome']
    chamado = data['queryResult']['parameters']['chamado']


#intentNmae = Abri no dialogflow
    if intentName == 'Abrir':

        data['fulfillmentText'] = f'Ok Sr(a) {nome}, seu chamado \
foi aberto e seu chamado é o de {chamado}.'
        
        return jsonify(data)
    
#run flask app
if __name__ == "__main__":
    app.debug = False
    app.run()



