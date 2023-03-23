import os.path
import unittest

import responses
from scan_and_send_file import ScanAndSendFile


class TestScaAndSendFile(unittest.TestCase):
    def setUp(self) -> None:
        self.sasf = ScanAndSendFile('wqetry')

        self.path = 'example/directory'
        self.file_name = '2.json'
        self.bad_path = 'not_or_empty_path'
        self.url = 'https://example.com/'
        self.bad_url = 'https://example.com/asdasdsad'

    def tearDown(self) -> None:
        del self.sasf

    @responses.activate
    def test_return_file_good(self):
        responses.add(**{
            'method': responses.POST,
            'url': self.url,
            'status': 200,
        })

        self.assertEqual(self.sasf.go(self.path, self.url), (os.path.join(self.path, self.file_name), 200))

    @responses.activate
    def test_return_file_bad_url(self):
        responses.add(**{
            'method': responses.POST,
            'url': self.bad_url,
            'status': 404,
        })

        self.assertEqual(self.sasf.go(self.path, self.bad_url), (os.path.join(self.path, self.file_name), 404))

    @responses.activate
    def test_return_file_empty_directory(self):
        responses.add(**{
            'method': responses.POST,
            'url': self.url,
            'status': 200,
        })

        self.assertEqual(self.sasf.go(self.bad_path, self.url), None)


if __name__ == '__main__':
    unittest.main()
