import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from services.requests import *
import os

# Get the abs path file
base_dir = os.path.dirname(os.path.abspath(__file__))
# Goes up one level
parent_dir = os.path.dirname(base_dir)
# Add features folder to the path
features_dir = os.path.join(parent_dir, "features")
scenarios(features_dir)


# Step 1: Authenticate and create a pet
@when('the user is authenticated with a valid token and create an new pet')
def post_create_a_new_pet(generate_token):
    token, path = generate_token
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': token[0]
    }

    body = {
        "id": 300,
        "name": "spider",
        "category": {
            "id": 1,
            "name": "Peter Parker"
        },
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
            "id": 1,
            "name": "tag1"
            }
        ],
        "status": "available"
    }
    response = post_create_a_pet(path, headers, body)
    log.info("Response: %s"%response.json())
    pytest.response = response

@then('the response status should be 200')
def check_ok_status():
    assert pytest.response.status_code == 200, f"Expected status code 200, but got {pytest.response.status_code}"

@then('the response should include the pet ID in the response')
def validate_the_id_in_the_response():
    assert pytest.response.json()["id"] == 300, f"Expected the id = 300. The pet was created with this id"

# Step 2: Retrieve the pet created
@when('the user sends a GET request to retrieve the pet by its ID')
def get_the_pet_created_by_id(generate_token):
    token, path = generate_token
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': token[0]
    }
    pet_id = 300
    response = get_pet_by_id(path, headers, pet_id)
    pytest.response = response

@then(parsers.parse('the response should include the category name "{name_pet}"'))
def get_the_name_of_pet(name_pet):
    assert pytest.response.json()["category"]["name"] == name_pet

# Step 3: Update the pet
@when(parsers.parse('the user sends a request to update the category name to "{new_name_pet}"'))
def update_the_values_of_pet(generate_token, new_name_pet):
    token, path = generate_token
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': token[0]
    }
    
    pet_id = 300
    querystring = {"name":new_name_pet, "status":"available"}
    response = post_pet(path, headers, pet_id, querystring)
    pytest.response = response

# Step 4: Delete the favourite image
@when('the user sends a DELETE request to remove the pet by its ID')
def delete_the_favourite_image(generate_token):
    token, path = generate_token
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': token[0]
    }
    
    pet_id = 300
    response = delete_pet(path, headers, pet_id)
    pytest.response = response
