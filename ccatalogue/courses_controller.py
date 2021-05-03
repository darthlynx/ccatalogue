from flask import Blueprint, request, jsonify, make_response
from ccatalogue.db import get_db

bp = Blueprint('courses', __name__, url_prefix='/courses')


@bp.route('/', methods=['GET'])
def get_courses():
    result = []
    name = request.args.get('name')
    # TODO: filter results by name here
    print(name)
    date = request.args.get('date')
    # TODO: filter results by date here
    print(date)
    return make_response(jsonify(result), 200)


@bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    print(data)
    return make_response(jsonify(data), 200)


@bp.route('/<id>', methods=['PUT'])
def update_course(id):
    data = request.get_json()
    print(data)
    return make_response(jsonify(data), 200)


@bp.route('/<id>', methods=['GET'])
def get_course_by_id(id):
    # print(id)
    data = request.get_json()
    print(data)
    return make_response(jsonify({"id": id}), 200)


@bp.route('/<id>', methods=['DELETE'])
def delete_course_by_id(id):
    return make_response(jsonify({"id": id}), 200)
