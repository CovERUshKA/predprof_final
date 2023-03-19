import json
import requests
#from . import miet_api
# import numpy as np
# from time import sleep

# from flask import Flask, render_template
# from flask_cors import CORS

def get_api_data():
    head = {
        'X-Auth-Token': 'c2up4twf'
    }
    req = requests.get('https://dt.miet.ru/ppo_it_final/judge', headers=head)

    api_data = []
    messages = req.json().get('message')
    for message in messages:
        api_data.append(message.get('points'))
    
    return api_data

print(get_api_data())

# def create_app():
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     CORS(app)

#     # http://127.0.0.1:80
#     @app.route('/')
#     def index():
#         return render_template("index.html")
    
#     app.config["CURRENT_PATHS"] = []
    
#     #app.config["CURRENT_PATHS"] = get_api_data()

#     from . import api
#     app.register_blueprint(api.bp)

#     return app