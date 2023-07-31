#!/usr/bin/env python3
"""Familiarize yourself with the utils.access_nested_map function and
understand its purpose. Play with it in the Python console to make
sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that
the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for
ollowing inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock

# Test the 'access_nested_map' function
class TestAccessNestedMap(unittest.TestCase):
    """Test case for 'access_nested_map' function."""

    @parameterized.expand([
        # Test cases with expected outputs
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """Test 'access_nested_map' with different inputs."""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand([
        # Test cases for expected exceptions
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """Test 'access_nested_map' for expected exceptions."""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)

# Test the 'get_json' function
class TestGetJson(unittest.TestCase):
    """Test case for 'get_json' function."""

    @parameterized.expand([
        # Test cases with expected JSON outputs
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, url, expected_output):
        """Test 'get_json' with different URLs."""
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)
            self.assertEqual(response, expected_output)

# Test the 'memoize' decorator
class TestMemoize(unittest.TestCase):
    """Test case for 'memoize' decorator."""

    def test_memoize(self):
        """Test the memoized property for caching."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            # The 'a_method' should be called only once, and the value should be cached
            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
