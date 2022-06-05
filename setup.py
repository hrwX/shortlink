from setuptools import find_packages, setup

setup(
	name="ShortLink",
	version="0.0.1",
	description="",
	author="hrwx",
	author_email="github.com/hrwx",
	packages=find_packages(),
	include_package_data=True,
	install_requires=[
		"flask",
		"flask-sqlalchemy"
	]
)
