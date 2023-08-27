from miapp.utils import find_selected_cell
from django.test import TestCase
from unittest.mock import Mock
from miapp.constants import TOKEN_KEY,TOKEN_VALUE

class TestFindSelectedCell(TestCase):

    # Tests that the function returns the valid cell name when Request.POST contains only one element, which is a valid cell name.
    def test_single_valid_cell_name(self):
        request = Mock()
        request.method = 'POST'
        request.POST = {TOKEN_KEY: TOKEN_VALUE, 'cell_1_1': 'value'}
        result = find_selected_cell(request)
        self.assertEqual(result, 'cell_1_1')

    # Tests that the function returns None when Request.POST contains only one element, which is an invalid cell name.
    def test_single_invalid_cell_name(self):
        request = Mock()
        request.method = 'POST'
        request.POST = {TOKEN_KEY: TOKEN_VALUE,'invalid_cell': 'value'}
        result = find_selected_cell(request)
        self.assertIsNone(result)

    # Tests that the function returns None when Request.POST is empty.
    def test_empty_request(self):
        request = Mock()
        request.method = 'POST'
        request.POST = {}
        result = find_selected_cell(request)
        self.assertIsNone(result)

    # Tests that the function returns None when Request.POST contains more than one element.
    def test_multiple_elements(self):
        request = Mock()
        request.method = 'POST'
        request.POST = {TOKEN_KEY: TOKEN_VALUE,'cell_1_1': 'value', 'cell_2_2': 'value'}
        result = find_selected_cell(request)
        self.assertIsNone(result)

    # Tests that the function returns None when Request.POST contains an element with an invalid cell name.
    def test_invalid_cell_name(self):
        request = Mock()
        request.method = 'POST'
        request.POST = {TOKEN_KEY: TOKEN_VALUE,'invalid_cell': 'value'}
        result = find_selected_cell(request)
        self.assertIsNone(result)

    # Tests that the function returns None when the request is not a POST request.
    def test_not_post_request(self):
        request = Mock()
        request.POST = {TOKEN_KEY: TOKEN_VALUE,'cell_1_1': 'value'}
        result = find_selected_cell(request)
        self.assertIsNone(result)