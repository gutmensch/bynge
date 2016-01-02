from flask import Blueprint, jsonify

blueprint = Blueprint(__name__, __name__)


class Play:

    value = 0


@blueprint.route('', methods=['GET'])
def counter():
    Play.value += 1
    return jsonify(value=Play.value)


@blueprint.route('', methods=['DELETE'])
def reset_counter():
    Play.value = 0
    return True