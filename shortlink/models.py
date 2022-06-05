# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


from datetime import datetime, timedelta

from shortlink import db


class URLs(db.Model):
	__tablename__ = "URLs"

	id = db.Column(db.Integer, primary_key=True)
	long_url = db.Column(db.Unicode, nullable=False)
	short_url = db.Column(db.Unicode, nullable=False)
	creation = db.Column(db.DateTime, nullable=False, default=datetime.now())
	expiry = db.Column(db.DateTime, default=datetime.now() + timedelta(days=7))

	def __repr__(self):
		return f"<URLs {self.long_url}:{self.short_url}>"

	def to_dict(self):
		return {
			"long_url": self.long_url,
			"short_url": self.short_url,
			"creation": self.creation,
			"expiry": self.expiry,
		}
