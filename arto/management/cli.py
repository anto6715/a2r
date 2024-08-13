import logging

import click

import arto
from arto import settings
from arto.core import cleaner

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
def clean(config, dry_run, **kwargs):
    settings.configure(**kwargs)
    cleaner.start(config, dry_run)


if __name__ == "__main__":
    main()
