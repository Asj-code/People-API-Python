import pytest
import requests
from pprint import pprint as pp
from assertpy.assertpy import assert_that


@pytest.mark.skip(reason="no need to testing this now")
def test_create_a_person():
    file = open('/Users/avalith/Desktop/people-api/data/data.json', 'r')
    data_input = file.read()
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post("http://0.0.0.0:5000/api/people", data=data_input, headers=headers)
    assert_that(response.status_code).is_equal_to(requests.codes.no_content)
    assert_that(response.content).is_equal_to(b'')


@pytest.mark.skip(reason="no need to testing this now")
def test_create_a_person_without_data():
    file = open('/Users/avalith/Desktop/people-api/data/no_data.json', 'r')
    data_input = file.read()
    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post("http://0.0.0.0:5000/api/people", data=data_input, headers=headers)
    assert_that(response.status_code).is_equal_to(requests.codes.conflict)


@pytest.mark.skip(reason="no need to testing this now")
def test_create_a_person_without_headers():
    file = open('/Users/avalith/Desktop/people-api/data/no_data.json', 'r')
    data_input = file.read()
    response = requests.post("http://0.0.0.0:5000/api/people", data=data_input)
    assert_that(response.status_code).is_equal_to(requests.codes.unsupported_media_type)

# test_create_a_person()
# test_create_a_person_without_data()
# test_create_a_person_without_headers()