#!/usr/bin/env python3.8
import threading
import logging
from flask import Flask, jsonify, request


import settings

app = Flask(__name__)
SURNAME_DATA = {}

logger = logging.getLogger('werkzeug')
handler = logging.FileHandler('test.log')
logger.addHandler(handler)


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify({'surname': surname}), 200
    else:
        return jsonify(f'Surname for user "{name}" not found'), 400


@app.route('/add_surname', methods=['POST'])
def post_user_surname():
    data = request.get_json()
    name = data.get('name')
    surname = data.get('surname')
    if name in SURNAME_DATA:
        return jsonify(f'User with name "{name}" already got surname "{SURNAME_DATA[name]}"'), 400
    else:
        SURNAME_DATA[name] = surname
        return jsonify({'name': name, 'surname': SURNAME_DATA[name]}), 200


@app.route('/change_surname', methods=['PUT'])
def put_user_surname():
    data = request.get_json()
    name = data.get('name')
    surname = data.get('surname')
    if name not in SURNAME_DATA:
        return jsonify(f"User '{name}' doesn't exist"), 400
    else:
        SURNAME_DATA[name] = surname
        return jsonify({'name': name, 'surname': SURNAME_DATA[name]}), 200


@app.route('/delete_surname/<name>', methods=['DELETE'])
def delete_user_surname(name):
    if name in SURNAME_DATA:
        del SURNAME_DATA[name]
        return jsonify(f'Surname for user "{name} deleted successfully"'), 200
    else:
        return jsonify(f'Surname for user "{name}" not found'), 400


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'Ok, exiting'), 200


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server
