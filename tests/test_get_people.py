import pytest
import requests
from pprint import pprint as pp
import json
from assertpy.assertpy import assert_that


# @pytest.mark.skip(reason="no need to testing this now")
def test_get_list_of_people():
    response = requests.get("http://0.0.0.0:5000/api/people")
    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.content).is_not_empty()


# test_get_list_of_people()