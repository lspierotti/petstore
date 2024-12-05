import pytest
from data import *
from services.requests import *
from Logger import logger as log
from utils.schema_validator import validate_json
# ####################################################################################################
# Test the functionality of the endpoint "/pets/findsByTags"
# ####################################################################################################

@pytest.mark.parametrize("tag, status_code_expected", zip(["tag1","tag2","tag3"],[200]*3) )
def test_get_a_pet_by_tags(generate_token, tag, status_code_expected):
    token, path = generate_token
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': token[0]
    }
    querystring = {"tags":[tag]}
    response = get_pet_by_tag(path, headers, querystring)
    log.info("Response: %s"%response.json())
    assert response.status_code == status_code_expected, log.info("The status code should be 200")
    
    
def test_schema_validator_getting_pets_by_tags(generate_token):
    token, path = generate_token
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': token[0]
    }
    querystring = {"tags":["tag2","tag3"]}
    response = get_pet_by_tag(path, headers, querystring).json()
    validate_json(response, "schema_get_pet_by_status.json")
    
