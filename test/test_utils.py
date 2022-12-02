from priceloop_api.utils import DefaultConfiguration, read_nocode, to_nocode

import os
import unittest
import pandas as pd


class UtilsTest(unittest.TestCase):
    configuration = DefaultConfiguration.with_user_credentials(
        os.environ["NOCODE_TEST_USER"],
        os.environ["NOCODE_TEST_PASSWORD"],
        host="alpha-dev.priceloop.ai"
    )

    def test_write_nocode(self):
        data = {'col1': [1, 2], 'col2': [3, 4]}
        df = pd.DataFrame(data=data)
        to_nocode(df, os.environ["NOCODE_TEST_TABLE"], self.configuration, mode="new")
        assert True

    def test_read_nocode(self):
        data = read_nocode(os.environ["NOCODE_TEST_TABLE"],
                           self.configuration, limit=2, offset=0)
        assert True
