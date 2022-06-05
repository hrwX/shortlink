# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


import json
import unittest

from shortlink import app


class TestAPI(unittest.TestCase):
	def setUp(self) -> None:
		self.client = app.test_client()

	def test_encode(self):
		response = self.client.post(
			"/api/v1/encode", query_string={"url": "www.google.com"}
		)
		data = json.loads(response.data or "{}")

		self.assertEqual(response.status_code, 200)
		self.assertEqual(data.get("shortlink"), "www.short.link/be966075")
		self.assertEqual(data.get("url"), "www.google.com")

	def test_decode(self):
		self.client.post("/api/v1/encode", query_string={"url": "www.google.com"})

		response = self.client.get(
			"/api/v1/decode", query_string={"url": "www.short.link/be966075"}
		)
		data = json.loads(response.data or "{}")

		self.assertEqual(response.status_code, 200)
		self.assertEqual(data.get("shortlink"), "www.short.link/be966075")
		self.assertEqual(data.get("url"), "www.google.com")

	def test_throws_invalid_url_error(self):
		response = self.client.post("/api/v1/encode", query_string={"url": "goo.g"})
		data = json.loads(response.data)
		self.assertEqual(response.status_code, 400)
		self.assertTrue(data.get("error"))
		self.assertEqual(data.get("error", {}).get("code"), 400)

	def test_throws_url_does_not_exist_error(self):
		response = self.client.get(
			"/api/v1/decode", query_string={"url": "www.short.link/12345678"}
		)
		data = json.loads(response.data)
		self.assertEqual(response.status_code, 404)
		self.assertTrue(data.get("error"))
		self.assertEqual(data.get("error", {}).get("code"), 404)
