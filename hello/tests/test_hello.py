from unittest import TestCase

import hello


class TestHello(TestCase):
    def test_is_string(self):
        s = hello.hello()
        self.assertTrue(isinstance(s, basestring))
        self.assertEqual(s, 'Hello World')
        s = hello.hello('David')
        self.assertEqual(s, 'Hello David')

