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

    def test_empty_db(self):
        rv = self.app.get('/api?isbn=9789380501932')
        assert 'Success' in rv.data

if __name__ == '__main__':
    unittest.main()
