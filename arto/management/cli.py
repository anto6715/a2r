import logging

import click

import arto
from arto import settings

logger = logging.getLogger("arto")

verbose_option = click.option(
    "-d", "--debug", "DEBUG", is_flag=True, help="Enable debug mode."
)


@click.group()
@click.version_option(package_name="arto")
def main():
    arto.setup()


@main.command()
@click.argument("config", type=click.Path(exists=True))
@click.option("--dry-run", is_flag=True, help="Dry run mode.")
@verbose_option
def clean(**kwargs):
    settings.configure(**kwargs)


if __name__ == "__main__":
    main()
