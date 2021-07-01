import pytest
import requests
from pprint import pprint as pp
import json
from assertpy.assertpy import assert_that


# @pytest.mark.skip(reason="no need to testing this now")
def test_update_a_person():
    file = open('/Users/avalith/Desktop/people-api/data/data_update.json', 'r')
    data_input = file.read()
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.put("http://0.0.0.0:5000/api/people/5", data=data_input, headers=headers)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.content).is_not_empty()

    response_get = requests.get("http://0.0.0.0:5000/api/people/5")
    people = response_get.json()
    assert people['fname'] == 'Nombre'


# @pytest.mark.skip(reason="no need to testing this now")
def test_update_a_person_without_data():
    file = open('/Users/avalith/Desktop/people-api/data/no_data.json', 'r')
    data_input = file.read()
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post("http://0.0.0.0:5000/api/people", data=data_input, headers=headers)
    assert_that(response.status_code).is_equal_to(409)


# @pytest.mark.skip(reason="no need to testing this now")
def test_update_a_person_without_headers():
    file = open('/Users/avalith/Desktop/people-api/data/no_data.json', 'r')
    data_input = file.read()
    response = requests.post("http://0.0.0.0:5000/api/people", data=data_input)
    assert_that(response.status_code).is_equal_to(415)


# test_update_a_person()
# test_update_a_person_without_data()
# test_update_a_person_without_headers()
