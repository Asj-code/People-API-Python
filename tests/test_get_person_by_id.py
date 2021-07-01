import pytest
import requests
from pprint import pprint as pp
import json
from assertpy.assertpy import assert_that


@pytest.mark.skip(reason="no need to testing this now")
def test_get_person_by_id():
    response = requests.get("http://0.0.0.0:5000/api/people/3")
    people = response.json()
    assert people['fname'] == 'Bunny'
    assert_that(response.content).is_not_empty()


@pytest.mark.skip(reason="no need to testing this now")
def test_get_person_without_id():
    response = requests.get("http://0.0.0.0:5000/api/people/""")
    assert_that(response.status_code).is_equal_to(requests.codes.not_found)
    assert_that(response.content).is_equal_to(
        b'{\n  "detail": "The requested URL was not found on the server. If you ent'
        b'ered the URL manually please check your spelling and try again.",\n  "sta'
        b'tus": 404,\n  "title": "Not Found",\n  "type": "about:blank"\n}\n')

# test_get_people_by_id()
# test_get_person_without_id()