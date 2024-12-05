import pytest
from data import *
from services.requests import *
from Logger import logger as log
from utils.schema_validator import validate_json

# ####################################################################################################
# Test the functionality of the endpoint "/pets/{petId}"
# ####################################################################################################

def test_post_to_update_a_pet(generate_token):
    token, path = generate_token
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': token[0]
}
    pet_id = 1
    payload = {"name":"Garfield", "status":"available"}
    response = post_pet(path, headers, pet_id, payload)
    log.info("Response: %s"%response.json())
    assert response.status_code == 200, log.info("The status code should be 200")
    
    
def test_schema_validator_post_pets_by_id(generate_token):
    token, path = generate_token
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': token[0]
    }

    pet_id = 1
    querystring = {"name":"Garfield", "status":"available"}
    response = post_pet(path, headers, pet_id, querystring).json()
    validate_json(response, "schema_post_pet_by_id.json")
    
