from flask import Blueprint, jsonify

blueprint = Blueprint(__name__, __name__)


class Stream:

    value = 0


@blueprint.route('', methods=['GET'])
def counter():
    Stream.value += 1
    return jsonify(value=Stream.value)

