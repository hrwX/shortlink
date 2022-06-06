# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


from typing import Dict

from flask import request

from shortlink import app, limiter
from shortlink.api.v1.decoder import Decoder
from shortlink.api.v1.encoder import Encoder


@app.route("/api/v1/encode", methods=["POST"])
@limiter.limit("10/second", override_defaults=False)
def encode() -> Dict[str, str]:
	"""Encodes a long URL to a shortened URL.

	Parameters: fetched from request
	url (str): URL which has to be shortened.
	length (int): Length of the hash to be generated, defaults to 8.
	expiry (datetime str isoformat): Expiration of the link, defaults to 7 days after creation.

	Returns:
	dict: Shortened URL
	"""

	encoder = Encoder(
		url=request.args.get("url"),
		length=request.args.get("length"),
		expiry=request.args.get("expiry"),
	)

	return encoder.get_short_url()


@app.route("/api/v1/decode", methods=["GET"])
@limiter.limit("10/second", override_defaults=False)
def decode() -> Dict[str, str]:
	"""Decodes a shortened URL to its original URL.

	Parameters: fetched from request
	url (str): Short URL to be decoded.

	Returns:
	dict: Original URL
	"""

	decoder = Decoder(url=request.args.get("url"))

	return decoder.get_long_url()


@app.after_request
def after_request(response):
	"""Used for logging and analytics"""
	# TODO logging and analytics
	return response
