# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


from typing import Dict

from flask import request

from shortlink import app
from shortlink.api.v1.decoder import Decoder
from shortlink.api.v1.encoder import Encoder


@app.route("/api/v1/encode", methods=["POST"])
def encode() -> Dict[str, str]:
	encoder = Encoder(
		url=request.args.get("url"),
		length=request.args.get("length"),
		expiry=request.args.get("expiry"),
	)

	return encoder.get_short_url()


@app.route("/api/v1/decode", methods=["GET"])
def decode() -> Dict[str, str]:
	decoder = Decoder(url=request.args.get("url"))

	return decoder.get_long_url()


@app.after_request
def after_request(response):
	return response
