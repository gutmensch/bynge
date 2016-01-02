from flask import Blueprint, jsonify

blueprint = Blueprint(__name__, __name__)


class Edit:

    value = 0


@blueprint.route('', methods=['GET'])
def counter():
    Edit.value += 1
    return jsonify(value=Edit.value)


@blueprint.route('', methods=['DELETE'])
def reset_counter():
    Edit.value = 0
    return True