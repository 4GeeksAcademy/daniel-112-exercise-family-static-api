"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints

    Start server:
        pipenv run start

    Run test:
        pipenv run test
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)



########################################################################


######################
## EXAMPLE ENDPOINT ##
######################
@app.route('/example', methods=['GET'])
def example():
    # This is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {"hello": "world",
                     "family": members}
    return jsonify(response_body), 200


##############################################################################
######################### Endpoints and their Methods ########################
##############################################################################
"""
TO-DOs:

[x] Create Endpoints:

    [x] Get ALL members
        - GET /members

    [x] Get ONE member
        - GET /members/:id

    [x] Add one member
        - POST /members

    [x] Delete one member
        - DELETE /members/:id
"""

#####################
## GET ALL MEMBERS ##
#####################
@app.route('/members', methods=['GET'])
def handle_get_all_members():
    try:

        members = jackson_family.get_all_members()

        if members:
            return jsonify(members), 200
        else:
             return jsonify({'error': 'there are no members'}), 404
    
    except Exception as error:
        return jsonify({'error': 'server error', 'message': str(error)}), 500


####################
## GET ONE MEMBER ##
####################
@app.route('/members/<int:id>', methods = ['GET'])
def handle_get_member(id):
    try:

        member = jackson_family.get_member(id)

        if member:
            return jsonify(member), 200
        else:
            return jsonify({"error": "ID does not math any member"}), 404
        
    except Exception as error:
        return jsonify({'error': 'server error', 'message': str(error)}), 500


################
## ADD MEMBER ##
################
""" Request body template
{
    "first_name": "String",
    "age": Int (positive),
    "lucky_numbers": [Int, Int, Int...]
}
"""
@app.route('/members', methods=['POST'])
def handle_add_member():
    try:

        request_body = request.get_json()

        if not request_body:
            return jsonify({'error': 'empty request, please fill fields'}), 400

        required_fields = ['first_name', 'age', 'lucky_numbers']

        for field in required_fields:
            if field not in request_body or request_body[field] == "":
                return jsonify({"error": f"missing required field: '{field}'"}), 400

        new_member = jackson_family.add_member(request_body)

        return jsonify(new_member), 200 # con 201 no pasa el test
    
    except Exception as error:
        return jsonify({'error': 'server error', 'message': str(error)}), 500


###################
## DELETE MEMBER ##
###################
@app.route('/members/<int:id>', methods=['DELETE'])
def handle_delete_member(id):
    try:

        is_deleted = jackson_family.delete_member(id)

        if is_deleted:
            return jsonify({"done": True}), 200
        else:
            return jsonify({"error": "ID does not match any member"}), 404
        
    except Exception as error:
        return jsonify({'error': 'server error', 'message': str(error)}), 500

##############################################################################
##############################################################################


# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)



