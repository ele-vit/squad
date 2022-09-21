from flask import Blueprint, jsonify, request
from models.JokeModel import JokeModel
from utils.others_api import ExternalJoke
import random

app = Blueprint('jokes_blueprint', __name__)


@app.route("/", methods=['GET'])
def get_jokes():
    try:
        jokes = JokeModel.get_jokes()
        joke = random.choice(jokes)
        return jsonify(jokes)
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@app.route("/<id>")
def get_joke(id):
    try:
        if id.lower() == 'chuck' or id.lower() == 'dad':
            joke = ExternalJoke.Chuck() if id.lower() == 'chuck' else ExternalJoke.Dad()
            return jsonify(joke)
        else:
            joke = JokeModel.get_joke(id)
            if joke != None:
                return jsonify(joke)
            else:
                return jsonify({'message': 'joke id not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@app.route("/add", methods=['POST'])
def add_joke():
    try:
        joke_value = request.json['joke']
        affected_rows = JokeModel.add_joke(joke_value)
        if affected_rows != {}:
            return jsonify({'status': 'register succesful', 'id': affected_rows['id']})
        else:
            return jsonify({'status': 'error on insert'}), 500
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@app.route("/update/<id>", methods=['PUT'])
def update_joke(id):
    try:
        joke_value = request.json['joke']
        affected_rows = JokeModel.update_joke(id, joke_value)
        if affected_rows != {}:
            return jsonify({'status': 'updated succesful', 'id': affected_rows['id']})
        else:
            return jsonify({'status': 'error on updated'}), 500
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@app.route("/delete/<id>", methods=['DELETE'])
def delete_joke(id):
    try:
        affected_rows = JokeModel.delete_joke(id)
        if affected_rows != {}:
            return jsonify({'status': 'register deleted succesful', 'id': affected_rows['id']})
        else:
            return jsonify({'status': 'error on delete register'}), 500
    except Exception as e:
        return jsonify({'message': str(e)}), 500
