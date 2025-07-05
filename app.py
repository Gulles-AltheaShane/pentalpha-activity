#[GULLES] 3 POINTS

from flask import Flask, jsonify, request
from models import add_note, view_notes, update_note, delete_note

app = Flask(__name__)

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify (view_notes())

@app.route('/notes/<int:notes_id>', methods=['GET', 'DELETE'])
def note_detail(notes_id):
        return jsonify(delete_note(notes_id))

@app.route('/notes/<int:id>/contents', methods=['PUT'])
def put_note(id):
    return jsonify(update_note(id, data))

@app.route('/notes', methods=['POST'])
def post_note():
    return jsonify(add_note(data))

if __name__ == '__main__':
    app.run()