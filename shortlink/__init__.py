# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig())

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
