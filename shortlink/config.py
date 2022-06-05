# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


class Config:
	"""
	Base Configuration Class for
	"""

	STATIC_FOLDER = "static"
	TEMPLATES_FOLDER = "templates"
	BASE_URL = "www.short.link"


class ProductionConfig(Config):
	"""
	Configuration for Production Environment
	"""

	FLASK_ENV = "PRODUCTION"
	DEBUG = False
	TESTING = False
	DATABASE = None


class DevelopmentConfig(Config):
	"""
	Configuration for Developement Environment
	"""

	FLASK_ENV = "DEVELOPMENT"
	DEBUG = True
	TESTING = True
	DATABASE = "SQLite"
	SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
