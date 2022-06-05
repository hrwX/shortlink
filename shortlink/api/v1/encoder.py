# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


from datetime import datetime, timedelta
from typing import Dict, Optional

from flask import current_app as app
from shortlink import db
from shortlink.exceptions import InvalidURLException
from shortlink.models import URLs
from shortlink.utils import hash_it, is_valid_url


class Encoder:
	def __init__(
		self, url: str, length: Optional[int] = None, expiry: Optional[str] = None
	) -> None:
		self.long_url = url
		self.hash_length = length or 8
		self.creation = datetime.now()
		self.expiry = expiry or self.default_expiry

	def get_short_url(self) -> Dict[str, str]:
		existing_url = self.get_existing_short_url()
		if existing_url:
			return self.get_response(**existing_url.to_dict())

		self.validate_url()
		hash = hash_it(self.long_url, self.hash_length)
		self.short_url = f"{app.config['BASE_URL']}/{hash}"
		self.insert()

		return self.get_response()

	def validate_url(self) -> None:
		if not is_valid_url(self.long_url):
			raise InvalidURLException

	def get_existing_short_url(self) -> URLs:
		return URLs.query.filter(URLs.long_url == self.long_url).first()

	def insert(self) -> None:
		url = URLs(
			long_url=self.long_url,
			short_url=self.short_url,
			expiry=self.expiry,
			creation=self.creation,
		)
		db.session.add(url)
		db.session.commit()

	def get_response(self, **kwargs) -> Dict[str, str]:
		return {
			"url": kwargs.get("url") or self.long_url,
			"shortlink": kwargs.get("short_url") or self.short_url,
			"expiry": kwargs.get("expiry") or self.expiry,
			"creation": kwargs.get("creation") or self.creation,
		}

	@property
	def default_expiry(self) -> datetime:
		return self.creation + timedelta(days=7)
