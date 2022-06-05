# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


import unittest

from shortlink.utils import hash_it, is_valid_url


class TestUtils(unittest.TestCase):
	def test_hashing(self):
		self.assertEqual(hash_it("www.google.com"), hash_it("www.google.com"))
		self.assertNotEqual(hash_it("www.google.com"), hash_it("www.goo.gl"))

	def test_url_validation(self):
		self.assertTrue(is_valid_url("www.google.com"))
		self.assertTrue(is_valid_url("https://www.google.com"))
		self.assertTrue(is_valid_url("http://www.google.com"))
		self.assertTrue(is_valid_url("http://www.google.co.uk"))
		self.assertTrue(is_valid_url("www.google.co.uk"))
		self.assertTrue(is_valid_url("https://goog.le"))
		self.assertFalse(is_valid_url("https://goog.l"))
		self.assertFalse(is_valid_url("goog.l"))
