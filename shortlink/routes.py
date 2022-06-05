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
	encoder = Encoder(
		url=request.args.get("url"),
		length=request.args.get("length"),
		expiry=request.args.get("expiry"),
	)

	return encoder.get_short_url()


@app.route("/api/v1/decode", methods=["GET"])
@limiter.limit("10/second", override_defaults=False)
def decode() -> Dict[str, str]:
	decoder = Decoder(url=request.args.get("url"))

	return decoder.get_long_url()


@app.after_request
def after_request(response):
	return response
