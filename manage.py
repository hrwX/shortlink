# Copyright (c) 2022, hrwx
# License: MIT. See LICENSE


import sys

import click

from shortlink import app
from shortlink.tests.runner import run_test_suite


@click.group()
@click.pass_context
def main(ctx):
	if len(sys.argv) == 1:
		click.echo(ctx.get_help())


@main.command("start-app", help="Start ShortLink Service.")
def start_app():
	app.run(debug=True)


@main.command("run-tests", help="Start ShortLink Service.")
def run_tests():
	run_test_suite()


if __name__ == "__main__":
	main()
