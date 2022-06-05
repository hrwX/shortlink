# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


import json
import unittest

from shortlink import app


class TestRateLimiter(unittest.TestCase):
	def setUp(self) -> None:
		self.client = app.test_client()

	def test_rate_limiter(self):
		for _ in range(12):
			response = self.client.post("/api/v1/encode", query_string={"url": "www.google.com"})

		data = json.loads(response.data)
		self.assertEqual(response.status_code, 429)
		self.assertTrue(data.get("error"))
		self.assertEqual(data.get("error", {}).get("code"), 429)
