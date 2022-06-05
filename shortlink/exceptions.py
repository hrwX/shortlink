# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


class InvalidURLException(Exception):
	"""Raised when the URL is invalid."""

	pass


class URLDoesNotExistException(Exception):
	"""Raised when the ShortLink URL doesn't exist."""

	pass
