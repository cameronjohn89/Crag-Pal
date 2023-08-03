from flask import Blueprint, jsonify, request
from models.crag import Crag
from schemas import CragSchema
from database import db

# Create the blueprint for auth controller

crag_controller = Blueprint('crag_controller', __name__)

# Route for creating a crag

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
    db.session.add(crag)
    db.session.commit()

    # Serialize the crag object to a dictionary
    crag_data = {
        'crag_id': crag.crag_id,  # Use crag_id instead of id
        'name': crag.name,
        'location': crag.location,
        'description': crag.description
    }

    # Return the created crag details as JSON
    return jsonify(crag_data), 201

# Retrieve crag route

@crag_controller.route('/crag', methods=['GET'])
def get_crags():
    # Retrieve all crags from the database
    crags = Crag.query.all()
# Serialize the list of crags to JSON using the CragSchema
    crag_schema = CragSchema(many=True)
    crags_json = crag_schema.dump(crags)

    # Return the serialized crags as JSON
    return jsonify(crags_json)


@crag_controller.route('/crag/<int:crag_id>', methods=['GET'])
def get_crag_by_id(crag_id):
    # Retrieve a specific crag based on the provided crag_id
    crag = Crag.query.get(crag_id)
    if crag is None:
        return jsonify({'error': 'Crag not found'}), 404
    return jsonify(crag)


# Add more routes and functionalities as needed
