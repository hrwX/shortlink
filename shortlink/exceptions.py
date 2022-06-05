# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


from werkzeug.exceptions import HTTPException


class InvalidURLException(HTTPException):
	"""Raised when the URL is invalid."""

	code = 400
	description = "The URL posted for shortening, is invalid."


class URLDoesNotExistException(HTTPException):
	"""Raised when the ShortLink URL doesn't exist."""

	code = 404
	description = "The requested ShortLink URL does not exist."
