from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import mongoengine


def connect_mongodb():
    print('Connecting to MongoDB...')
    mongoengine.connect(host=os.getenv('MONGODB_URI'))
    print('Connected')


load_dotenv(verbose=True)
app = Flask(__name__)
connect_mongodb()


@app.route('/')
def index():
    result = {'status': 'OK'}
    return jsonify(result)


@app.route('/savedSignals')
def saved_signals_list():
    saved_signals = []
    result = {
        '_embedded': {
            'savedSignals': saved_signals
        }
    }
    return result
