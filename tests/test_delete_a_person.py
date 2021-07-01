import pytest
import requests
from pprint import pprint as pp
import json
from assertpy.assertpy import assert_that


# @pytest.mark.skip(reason="no need to testing this now")
def test_delete_a_person_by_id():
    people = requests.get("http://0.0.0.0:5000/api/people").json()
    people_len = len(people)
    response = requests.delete(url="http://0.0.0.0:5000/api/people/4")

    assert_that(response.status_code).is_equal_to(200)
    assert_that(people).extracting('person_id').does_not_contain('4')

    new_people = requests.get("http://0.0.0.0:5000/api/people").json()
    people_new_len = len(new_people)
    assert_that(people_len).is_not_equal_to(people_new_len)


# @pytest.mark.skip(reason="no need to testing this now")
def test_delete_a_person_with_wrong_id():
    people = requests.get("http://0.0.0.0:5000/api/people").json()
    response = requests.delete(url="http://0.0.0.0:5000/api/people/1000")
    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.content).is_equal_to(b'{\n  "detail": "The requested URL was not found on the server. If you ent'
     b'ered the URL manually please check your spelling and try again.",\n  "sta'
     b'tus": 404,\n  "title": "Not Found",\n  "type": "about:blank"\n}\n')


# @pytest.mark.skip(reason="no need to testing this now")
def test_delete_a_person_with_character_id():
    people = requests.get("http://0.0.0.0:5000/api/people").json()
    response = requests.delete(url="http://0.0.0.0:5000/api/people/hola")
    assert_that(response.status_code).is_equal_to(404)
    assert_that(response.content).is_equal_to(b'{\n  "detail": "The requested URL was not found on the server. If you ent'
     b'ered the URL manually please check your spelling and try again.",\n  "sta'
     b'tus": 404,\n  "title": "Not Found",\n  "type": "about:blank"\n}\n')

# test_delete_a_person_by_id()
# test_delete_a_person_with_wrong_id()
# test_delete_a_person_with_character_id()

