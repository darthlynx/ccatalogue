from flask import Blueprint, request, jsonify, make_response
from ccatalogue.db import get_db

bp = Blueprint('courses', __name__, url_prefix='/courses')


@bp.route('/', methods=['GET'])
def get_courses():
    db = get_db()
    name = request.args.get('name')
    if name:
        courses = db.execute('SELECT * FROM catalogue WHERE course_name = ?', (name,)).fetchone()
        return make_response(jsonify([dict(courses)]), 200)
    date = request.args.get('date')
    if date:
        courses = db.execute('SELECT * FROM catalogue WHERE start_date = ?', (date,)).fetchall()
        return make_response(jsonify([dict(ix) for ix in courses]), 200)
    courses = db.execute('SELECT * FROM catalogue').fetchall()
    return make_response(jsonify([dict(ix) for ix in courses]), 200)


@bp.route('/', methods=['POST'])
def create_course():
    data = request.get_json()
    course_name = data['course_name']
    start_date = data['start_date']
    end_date = data['end_date']
    lectures_number = data['lectures_number']
    db = get_db()
    cur = db.cursor()
    try:
        cur.execute('INSERT INTO catalogue (course_name, start_date, end_date, lectures_number)'
                    ' VALUES (?, ?, ?, ?)',
                    (course_name, start_date, end_date, lectures_number)
                    )
        db.commit()
    except Exception as e:
        print(e)
    return make_response(jsonify({"id": cur.lastrowid}), 200)


@bp.route('/<id>', methods=['PUT'])
def update_course(id):
    data = request.get_json()
    print(data)
    return make_response(jsonify(data), 200)


@bp.route('/<id>', methods=['GET'])
def get_course_by_id(id):
    db = get_db()
    course = db.execute('SELECT * FROM catalogue WHERE id = ?', (id,)).fetchone()
    resp = dict(course) if course else {}
    return make_response(jsonify(resp), 200)


@bp.route('/<id>', methods=['DELETE'])
def delete_course_by_id(id):
    return make_response(jsonify({"id": id}), 200)
