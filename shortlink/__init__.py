# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


import os

from flask import Flask, json
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import HTTPException

from shortlink.config import get_config

app = Flask(__name__)
app.config.from_object(get_config(os.environ.get("FLASK_ENV", "development")))

limiter = Limiter(app, key_func=get_remote_address)

db = SQLAlchemy()
db.init_app(app)

# This is an anti-pattern as per python standards as this causes Circular imports.
# Not actually using the models in __init__.py, just ensuring the module is imported
# so that the tables are created in the database.
from shortlink.models import URLs

with app.app_context():
	db.create_all(app=app)
	db.session.commit()

# This is an anti-pattern as per python standards as this causes Circular imports.
# Not actually using the views in __init__.py, just ensuring the module is imported.
# ref: https://flask.palletsprojects.com/en/2.1.x/patterns/packages/
from shortlink.routes import *	# fmt: off


@app.errorhandler(HTTPException)
def handle_exception(exception):
	"""Return JSON instead of HTML for HTTP errors."""
	response = exception.get_response()
	response.data = json.dumps(
		{
			"error": {
				"code": exception.code,
				"name": exception.name,
				"description": exception.description,
			}
		}
	)
	response.content_type = "application/json"

	return response
