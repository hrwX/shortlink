# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


from typing import Union


class Config:
	"""
	Base Configuration Class for
	"""

	STATIC_FOLDER = "static"
	TEMPLATES_FOLDER = "templates"
	BASE_URL = "www.short.est"


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
	TESTING = False
	DATABASE = "SQLite"
	SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class TestingConfig(Config):
	"""
	Configuration for Developement Environment
	"""

	FLASK_ENV = "TESTING"
	DEBUG = True
	TESTING = True
	DATABASE = "SQLite"
	SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


def get_config(
	config_type: str,
) -> Union[ProductionConfig, DevelopmentConfig, TestingConfig]:
	config_types = {
		"production": ProductionConfig,
		"development": DevelopmentConfig,
		"testing": TestingConfig,
	}

	return config_types.get(config_type, "development")()
