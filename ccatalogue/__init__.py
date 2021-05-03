import os

from flask import Flask, request, jsonify, make_response


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'ccatalogue.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/courses', methods=['GET'])
    def get_courses():
        # print(id)
        name = request.args.get('name')
        # TODO: filter results by name here
        print(name)
        date = request.args.get('date')
        # TODO: filter results by date here
        print(date)
        return make_response(jsonify([]), 200)

    @app.route('/courses', methods=['POST'])
    def create_course():
        data = request.get_json()
        print(data)
        return make_response(jsonify(data), 200)

    @app.route('/courses/<id>', methods=['PUT'])
    def update_course(id):
        data = request.get_json()
        print(data)
        return make_response(jsonify(data), 200)

    @app.route('/courses/<id>', methods=['GET'])
    def get_course_by_id(id):
        # print(id)
        data = request.get_json()
        print(data)
        return make_response(jsonify({"id": id}), 200)

    @app.route('/courses/<id>', methods=['DELETE'])
    def delete_course_by_id(id):
        return make_response(jsonify({"id": id}), 200)

    from . import db
    db.init_app(app)

    return app
