from flask import Blueprint, jsonify, request
from models.crag import Crag

crag_controller = Blueprint('crag_controller', __name__)


@crag_controller.route('/crag', methods=['GET'])
def get_crag():
    # Retrieve all crags from the database
    crag = Crag.query.all()
    return jsonify(crag)


@crag_controller.route('/crag/<int:crag_id>', methods=['GET'])
def get_crag(crag_id):
    # Retrieve a specific crag based on the provided crag_id
    crag = Crag.query.get(crag_id)
    if crag is None:
        return jsonify({'error': 'Crag not found'}), 404
    return jsonify(crag)


@crag_controller.route('/crag', methods=['POST'])
def create_crag():
    # Retrieve the data from the request
    data = request.get_json()
    name = data.get('name')
    location = data.get('location')
    description = data.get('description')
    # Create a new Crag instance
    crag = Crag(name=name, location=location, description=description)
    # Save the new crag to the database
    crag.save()
    # Return the created crag details as JSON
    return jsonify(crag), 201

# Add more routes and functionalities as needed
