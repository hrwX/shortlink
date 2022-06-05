# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


import hashlib
import re
from typing import Optional


def hash_it(string: Optional[str] = None, length: Optional[int] = None) -> str:
	"""Generates consistent hash for given string."""
	hexdigest = hashlib.sha224(f"{string or ''}".encode()).hexdigest()

	return hexdigest[:length]


def is_valid_url(url: str) -> bool:
	"""Validates if a URL is valid."""

	return bool(
		re.search(
			r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
			url,
		)
	)
