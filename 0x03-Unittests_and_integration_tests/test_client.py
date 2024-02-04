#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from your_module.client import GithubOrgClient  # Replace 'your_module' with the actual module name
import pytest

class TestGithubOrgClient(unittest.TestCase):

    @patch('your_module.client.GithubOrgClient.get_json')
    @pytest.mark.parametrize("org_name, expected_result", [("google", {"org": "google"}), ("abc", {"org": "abc"})])
    def test_org(self, org_name, expected_result):
        # Mock the get_json method
        with patch('your_module.client.GithubOrgClient.get_json', return_value=expected_result) as mock_get_json:
            client = GithubOrgClient(org_name)
            result = client.org()

        # Assert that get_json was called exactly once with the expected argument
        mock_get_json.assert_called_once_with(f'https://api.github.com/orgs/{org_name}')

        # Assert that the result is equal to the expected result
        self.assertEqual(result, expected_result)


class TestGithubOrgClient(unittest.TestCase):

    def test_public_repos_url(self):
        known_payload = {"repos_url": "https://api.github.com/orgs/testorg/repos"}

        # Mock the GithubOrgClient.org property to return the known payload
        with patch('your_module.client.GithubOrgClient.org', return_value=known_payload):
            client = GithubOrgClient("testorg")
            result = client._public_repos_url

        # Assert that the result of _public_repos_url is the expected one based on the mocked payload
        self.assertEqual(result, known_payload["repos_url"])


class TestGithubOrgClient(unittest.TestCase):

    @patch('your_module.client.GithubOrgClient._public_repos_url', return_value="https://api.github.com/orgs/testorg/repos")
    @patch('your_module.client.GithubOrgClient.get_json')
    def test_public_repos(self, mock_get_json, mock_public_repos_url):
        # Mock the get_json method to return a payload of your choice
        chosen_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = chosen_payload

        client = GithubOrgClient("testorg")
        result = client.public_repos()

        # Assert that the list of repos is what you expect from the chosen payload
        self.assertEqual(result, chosen_payload)

        # Assert that the mocked property and the mocked get_json were called once
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/testorg/repos")

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        client = GithubOrgClient("testorg")

        # Call has_license with the provided inputs
        result = client.has_license(repo, license_key)

        # Assert that the result is equal to the expected result
        self.assertEqual(result, expected_result)

@parameterized_class("org_payload", "repos_payload", "expected_repos", "apache2_repos", fixtures=[
    (org_payload, repos_payload, expected_repos, apache2_repos),
])
class TestIntegrationGithubOrgClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls, org_payload, repos_payload, expected_repos, apache2_repos):
        # Mock requests.get using patch and side_effect to return example payloads from fixtures
        cls.get_patcher = patch('your_module.client.requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Set side_effect based on the anticipated URLs
        def get_json_side_effect(url):
            if "orgs" in url:
                return org_payload
            elif "repos" in url:
                return repos_payload
            else:
                return None

        cls.mock_get.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        # Stop the patcher
        cls.get_patcher.stop()

    def test_public_repos(self):
        # Instantiate GithubOrgClient
        client = GithubOrgClient("testorg")

        # Call the public_repos method
        result = client.public_repos()

        # Assert that the result is equal to the expected repos
        self.assertEqual(result, expected_repos)

