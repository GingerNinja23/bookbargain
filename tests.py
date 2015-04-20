import os
import unittest
from bookbargain_api import app as book_api 

'''
Bookbargain API Server Tests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module tests the Bookbargain API server.
This test currently makes a call with a random
ISBN number and checks if the program works 
correctly.

'''


class BookBargainTestCase(unittest.TestCase):
    def setUp(self):
        self.app = book_api.test_client()
        book_api.config['TESTING'] = True


    def tearDown(self):
		pass

    def test_function(self):
        for isbn in ['9789380501932','9780552161275','9780593072493','9780006479895','9780984782802']:
            resp = self.app.get('/api?isbn='+isbn)
            assert 'Success' in resp.data


if __name__ == '__main__':
    unittest.main()
