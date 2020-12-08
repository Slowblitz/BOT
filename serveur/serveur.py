from flask import Flask
from flask import jsonify, request
import requests
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# Changer
ip = "10.122.4.166"
api = "http://" + ip + ":5005/webhooks/rest/webhook"


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/GetResponseRasa', methods=['GET', 'POST'])
def getResponseRasa():
    if request.method == 'POST':
        datas = json.loads(request.data)
        message = datas['text']
        print(message)
    core = {"sender": "rasa", "message": message}
    response = requests.post(api, json=core)
    return jsonify(response.json())
