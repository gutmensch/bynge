from flask import Blueprint, jsonify

blueprint = Blueprint(__name__, __name__)


class Store:

    value = 0


@blueprint.route('', methods=['GET'])
def counter():
    Store.value += 1
    return jsonify(value=Store.value)


@blueprint.route('', methods=['DELETE'])
def reset_counter():
    Store.value = 0
    return True