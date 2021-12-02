import json
import names
from requests import Session
from pytest import fixture
from pytest import mark
import requests
import pytest
from requests.sessions import session
from datetime import datetime

# TEST --------------- New Profile ---------------------

@mark.createprofile
@pytest.mark.profile
def test_can_create_new_profile_api(logged_in_session):
 # imports auth token in request header  
    auth_header = logged_in_session
    
# Load payload data from external JSON file   
    file = open('/Users/dalefixter/Documents/Projects/pytest_customerio/data/profile/profile_payload_data.json','r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    
# Send post to create new profile
    new_profile_resp = requests.post('https://fly-eu.customer.io/v1/environments/114009/customers', headers=auth_header, json=request_json)
    print(f"These are the profile session headers: {new_profile_resp}")
    
# Validating response code - expected is 202 Accepted    
    assert new_profile_resp.status_code ==202    

    

# TEST --------------- Update Profile ---------------------

# FIXTURE - GET returns list of customers/profiles for org 114009
@fixture
def get_profile_customer_list(logged_in_session):
    auth_header = logged_in_session
    get_profile_list_url = 'https://fly-eu.customer.io/v1/environments/114009/customers?asc=false&email=&filters=&page=1&sort=created_at&source='
    get_list_response = requests.get(url=get_profile_list_url, headers=auth_header)    
    print(get_list_response.text)
    assert get_list_response.status_code == 200
    return get_list_response

# FIXTURE - returns current timestamp and rounds to correct format for JSON payload
@fixture
def get_time_now():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    rounded_timestamp = round(timestamp)
    print("timestamp =", rounded_timestamp)
    return rounded_timestamp

# FIXTURE - generates random first name
@fixture
def random_first_name():
    rand_first_name = names.get_first_name(gender='male')
    return rand_first_name


@mark.updateprofile
@pytest.mark.profile
def test_can_update_profile_api(logged_in_session, get_profile_customer_list, get_time_now, random_first_name):
    fixed_first_name = random_first_name
# imports auth token in request header  
    auth_header = logged_in_session
    
# extract first customer ID in list
    customer_id = json.loads(get_profile_customer_list.text)['customers'][0]['id']
    print(customer_id)
    
# Append customer ID to URL
    edit_profile_url = 'https://fly-eu.customer.io/v1/environments/114009/customers/' + customer_id
    print(edit_profile_url)
    
# Read JSON payload data into dict
    data = {
    "customer": {
        "attributes": {
            "cio_id":customer_id,
            "email":"",
            "id":"MYNEWPROFILE",
            "created_at":get_time_now,
            "firstName":fixed_first_name,
            "lastName":"Smith",
        },
        "identifiers": {
            "cio_id":customer_id,
            "email":None,
            "id":"MYNEWPROFILE"
        },
        "last_visited":0,
        "unsubscribed":False,
        "unsent_drafts":False,
        "devices": []
    }
}

# save parameterized data to JSON file in correct format
    with open('/Users/dalefixter/Documents/Projects/pytest_customerio/data/profile/output.json', 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)
        
# read parameterized JSON data
    file = open('/Users/dalefixter/Documents/Projects/pytest_customerio/data/profile/output.json','r')
    json_input = file.read()
    request_json = json.loads(json_input)
    
# save parameterized data to JSON file in correct format
    response = requests.put(url=edit_profile_url, headers=auth_header, json=request_json)
    print(response.headers)
    
# asserts that status code is 202 ACCEPTED
    assert response.status_code == 202
    
# GET the same customer information again and save to variable
    get_custdata_url = f'https://fly-eu.customer.io/v1/environments/114009/customers/' + customer_id
    get_custdata_resp = requests.get(url=get_custdata_url, headers=auth_header) 
    data = json.loads(get_custdata_resp.text)
    print(get_custdata_resp.text)
    saved_firstName = data['customer']['attributes']['firstName']
    
# asserts that the name sent is indeed the name that has been saved
    assert saved_firstName == fixed_first_name
    print(f"The submitted name was: {fixed_first_name} and the saved name is: {saved_firstName}")


# TEST --------------- Delete Profile ---------------------

# FIXTURE - return customer ID of newly created profile
@fixture
def return_new_customer_id(logged_in_session):
    auth_header = logged_in_session
    get_customer_id = requests.get('https://fly-eu.customer.io/v1/environments/114009/customers/MYNEWPROFILE', headers=auth_header)
    data = json.loads(get_customer_id.text)
    new_customer_id = data['customer']['identifiers']['cio_id']
    print(new_customer_id)
    return new_customer_id

@mark.deleteprofile
@pytest.mark.profile
def test_can_delete_profile_api(logged_in_session, return_new_customer_id):
    auth_header = logged_in_session
    new_customer_id = return_new_customer_id
    url = f'https://fly-eu.customer.io/v1/environments/114009/customers/' + new_customer_id
    print(url)
    delete_cust_resp = requests.delete(url=url, headers=auth_header)
    assert delete_cust_resp.status_code == 204