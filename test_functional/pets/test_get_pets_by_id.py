import pytest
from data import *
from services.requests import *
from Logger import logger as log
from utils.schema_validator import validate_json

# ####################################################################################################
# Test the functionality of the endpoint "/pets/{petId}"
# ####################################################################################################

@pytest.mark.parametrize("pet_id, status_code_expected", zip([1,2,4],[200]*3) )
def test_get_a_pet_by_id(generate_token, pet_id, status_code_expected):
    token, path = generate_token
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': token[0]
}
    response = get_pet_by_id(path, headers, pet_id)
    log.info("Response: %s"%response.json())
    assert response.status_code == status_code_expected, log.info("The status code should be 200")
    
    
def test_schema_validator_getting_pets_by_id(generate_token):
    token, path = generate_token
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': token[0]
    }

    pet_id = 1
    response = get_pet_by_id(path, headers, pet_id).json()
    validate_json(response, "schema_get_pet_by_id.json")
    
