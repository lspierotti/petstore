import pytest
from data import *
from services.requests import *
from Logger import logger as log
from utils.schema_validator import validate_json
# ####################################################################################################
# Test the functionality of the endpoint "/pets/findsByStatus"
# ####################################################################################################

@pytest.mark.parametrize("status, status_code_expected", zip(["available","pending","sold"],[200]*3) )
def test_get_a_pet_by_status(generate_token, status, status_code_expected):
    token, path = generate_token
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': token[0]
    }
    querystring = {"status":status}
    response = get_pet_by_status(path, headers, querystring)
    log.info("Response: %s"%response.json())
    assert response.status_code == status_code_expected, log.info("The status code should be 200")
    
    
def test_schema_validator_getting_pets_by_status(generate_token):
    token, path = generate_token
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': token[0]
    }
    querystring = {"status":"available"}
    response = get_pet_by_status(path, headers, querystring).json()
    validate_json(response, "schema_get_pet_by_status.json")
    
