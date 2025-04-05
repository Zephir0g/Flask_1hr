from flask import render_template, request, jsonify
from models import db, Note


def create_routes(app):

    @app.route('/')
    def index():
        return render_template('index.html')


    # create note endpoint
    @app.route('/notes', methods=["POST"])
    def create_note():
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')

        if not title or not content:
            return {"error": "Title and content are required!"}, 400

        new_note = Note(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()
        return jsonify({
            "id": new_note.id,
            "title": new_note.title,
            "content": new_note.content,
            "created_at": new_note.created_at
        }), 201


    # get note endpoint
    @app.route('/notes', methods=["GET"])
    def get_notes():
        notes = Note.query.order_by(Note.created_at.desc()).all()
        return jsonify({
            "notes": [
                {
                    "id": note.id,
                    "title": note.title,
                    "content": note.content,
                    "created_at": note.created_at.isoformat()
                } for note in notes
            ]
        }), 200


    # get note by id endpoint
    @app.route('/notes/<int:id>', methods=['GET'])
    def get_note(id):
        note = Note.query.get(id)
        if not note:
            return jsonify({'error': 'Note not found'}), 404

        return jsonify({
            'id': note.id,
            'title': note.title,
            'content': note.content,
            'created_at': note.created_at
            }), 200


    # update note endpoint
    @app.route('/notes/<int:id>', methods=["PUT"])
    def update_note(id):
        note = Note.query.get(id)

        if not note:
            return jsonify({'error': 'Note not found'}), 404

        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        if not title:
            return jsonify({'error': 'Title is required!'}), 400

        note.title = title
        note.content = content
        db.session.commit()

        return jsonify({
            'id': note.id,
            'title': note.title,
            'content': note.content,
            'created_at': note.created_at
        }), 200


    # delete note endpoint
    @app.route('/notes/<int:id>', methods=["DELETE"])
    def delete_note(id):
        note = Note.query.get(id)

        if not note:
            return jsonify({'error': 'Note not found'}), 404

        db.session.delete(note)
        db.session.commit()
        return {"message": f"Note {note.title} deleted!"}, 200

