# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import priceloop_api
from priceloop_api.paths.api_v1_0_workspaces_workspace_external_functions_function import delete  # noqa: E501
from priceloop_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV10WorkspacesWorkspaceExternalFunctionsFunction(ApiTestMixin, unittest.TestCase):
    """
    ApiV10WorkspacesWorkspaceExternalFunctionsFunction unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
