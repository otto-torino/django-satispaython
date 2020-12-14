import json
from django.test import TestCase
from django_satispaython._core import get_data
from django_satispaython.exceptions import ResponseStatusError


class MockedResponse(object):
    def __init__(self, status_code, data=None):
        self.status_code = status_code
        self.data = data

    def json(self):
        return json.dumps(self.data)


class CoreTestCase(TestCase):

    def test_get_data_error(self):
        """Response error raises the right exception"""
        response = MockedResponse(400)

        error_messages = {
            400: "Bad request dude!"
        }
        try:
            get_data(response, error_messages)
            self.fail()
        except ResponseStatusError as e:
            self.assertEqual(str(e), 'Bad request dude!')

    def test_get_data_success(self):
        """Response success returns response json method output"""
        response = MockedResponse(200, {"foo": "bar", "foo2": None})
        error_messages = {}

        res = get_data(response, error_messages)
        self.assertEqual(res, '{"foo": "bar", "foo2": null}')
