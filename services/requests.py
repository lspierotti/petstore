import requests
from Logger import logger as log

def get_pet_by_id(path, headers, pet_id):
    '''Get pet by id'''
    endpoint = f"pet/{pet_id}"
    url = ''.join([path,endpoint])
    response = requests.get(url, headers=headers)
    return response

def get_pet_by_tag(path, headers, payload):
    '''Get pet by tag'''
    endpoint = "pet/findByTags"
    url = ''.join([path,endpoint])
    response = requests.get(url, headers=headers, params=payload)
    return response

def get_pet_by_status(path, headers, payload):
    '''Get pet by status'''
    endpoint = "pet/findByStatus"
    url = ''.join([path,endpoint])
    response = requests.get(url, headers=headers, params=payload)
    return response

def delete_pet(path, headers, pet_id):
    '''Delete a pet'''
    endpoint = f"pet/{pet_id}"
    url = ''.join([path,endpoint])
    response = requests.delete(url, headers=headers)
    return response 

def post_pet(path, headers, pet_id, queryparams):
    '''update a pet'''
    endpoint = f"pet/{pet_id}"
    url = ''.join([path,endpoint])
    response = requests.post(url, headers=headers, params = queryparams)
    return response

def post_create_a_pet(path, headers, body):
    '''create a pet'''
    endpoint = "pet"
    url = ''.join([path,endpoint])
    response = requests.post(url, headers=headers, json = body)
    return response