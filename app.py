#[GULLES] 3 POINTS

from flask import Flask, jsonify, request
from models import add_note, view_notes, update_note, delete_note

app = Flask(__name__)

@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonfy (view_notes())

@app.route('/notes/<int:notes_id>', methods=['GET', 'DELETE'])
def delete_note(id):
    return jsonfy(delete_note())
    
@app.route('/notes/<int:id>/contents', methods=['PUT'])
def put_note():
    return jsonfy (update_note())

@app.route('/notes/<contents>', methods=['POST'])
def post_note():
    return jsonfy(add_note)

app.run()