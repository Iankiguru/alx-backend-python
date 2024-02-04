#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from your_module import utils  # Replace 'your_module' with the actual module name

class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected_result)


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError, "Key 'a' not found in the nested map"),
        ({"a": 1}, ("a", "b"), KeyError, "Key 'b' not found in the nested map"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception, expected_message):
        with self.assertRaises(expected_exception) as context:
            utils.access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):

    @patch('your_module.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        # Mock the requests.get method
        mocked_get = Mock()
        mocked_get.json.return_value = test_payload
        with patch('your_module.requests.get', return_value=mocked_get) as mock_get:
            result = utils.get_json(test_url)

        # Assert that requests.get was called exactly once with the test_url argument
        mock_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):

    class TestClass:

        def a_method(self):
            return 42

        @utils.memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        with patch.object(TestMemoize.TestClass, 'a_method') as mock_method:
            test_instance = TestMemoize.TestClass()

            # Call a_property twice
            result1 = test_instance.a_property()
            result2 = test_instance.a_property()

            # Assert that a_method is only called once
            mock_method.assert_called_once()

            # Assert that the results of the two calls are the same
            self.assertEqual(result1, result2)

