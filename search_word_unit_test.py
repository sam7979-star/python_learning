import unittest
from unittest.mock import patch
import io
import sys

from Python_Prac.Search_word_List import search_word_lst


class MyTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['3','apple','banana','grape','app'])
    @patch('sys'.stdout, new_callable=io.StringIO)
    def test_something(self):
        search_word_lst()
        output = mock_stdout.getvalue()

        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
