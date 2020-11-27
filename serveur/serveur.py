from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
#Changer
ip = "192.168.1.28"
api = "http://" + ip + ":5005/webhooks/rest/webhook"

@app.route('/')
def hello_world():
        return 'Hello, World!'

@app.route('/GetResponseRasa')
def getResponseRasa():
        core = {"sender":"rasa", "message":"Donne moi mon emploi du temps"}
        response = requests.post(api, json=core)
        return jsonify(response.json())