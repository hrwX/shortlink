# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


import unittest
from os.path import dirname, realpath


def run_test_suite():
	"""Runs the unit tests without coverage."""

	folder = dirname(realpath(__file__))
	tests = unittest.TestLoader().discover(folder, pattern="test_*")

	return unittest.TextTestRunner(verbosity=2).run(tests).wasSuccessful()
