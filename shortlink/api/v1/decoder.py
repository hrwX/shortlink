# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


from datetime import datetime
from typing import Dict, Optional

from shortlink.exceptions import InvalidURLException, URLDoesNotExistException
from shortlink.models import URLs
from shortlink.utils import is_valid_url


class Decoder:
	def __init__(self, url: str) -> None:
		self.short_url = url

	def get_long_url(self) -> Dict[str, str]:
		self.validate_url()
		long_url = self.get_long_url_from_db()

		if long_url:
			return self.get_response(**long_url.to_dict())

		raise URLDoesNotExistException

	def get_long_url_from_db(self) -> Optional[URLs]:
		return URLs.query.filter(
			URLs.short_url == self.short_url, URLs.expiry >= datetime.now()
		).first()

	def validate_url(self) -> None:
		if not is_valid_url(self.short_url):
			raise InvalidURLException

	def get_response(self, **kwargs) -> Dict[str, str]:
		return {
			"url": kwargs.get("long_url"),
			"shortlink": kwargs.get("short_url"),
			"expiry": kwargs.get("expiry"),
			"creation": kwargs.get("creation"),
		}
