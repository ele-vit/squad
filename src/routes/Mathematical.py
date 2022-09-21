from flask import Blueprint, jsonify, request
from utils.mathematical import Mathematical

app = Blueprint('numbers_blueprint', __name__)


@app.route("/numbers", methods=['GET'])
def numbers():
    try:
        numbers = Mathematical.clean_data(request.args.get('numbers'))
        multiple_number = Mathematical.mcm_for(numbers)
        return jsonify({'least_common_multiple': int(multiple_number)})
    except Exception as e:
        return jsonify({'message': str(e)}), 500


@app.route("/number", methods=['GET'])
def number():
    try:
        if request.args.get('number').isnumeric():
            multiple_number = Mathematical.more_one(request.args.get('number'))
            return jsonify({'more_one': int(multiple_number)})
        else:
            return jsonify({'message':'param not valide'})
    except Exception as e:
        return jsonify({'message': str(e)}), 500
