import logging
from pathlib import Path

import click

import arto
from arto import settings
from arto.core import cleaner
from arto.core import md5

logger = logging.getLogger("arto")

verbose_option = click.option(
    "-d", "--debug", "DEBUG", is_flag=True, help="Enable debug mode."
)


@click.group()
@click.version_option(package_name="arto")
def main():
    arto.setup()


@main.command()
@click.argument("config", type=Path)
@click.option("--dry-run", is_flag=True, help="Dry run mode.")
@verbose_option
def clean(config, dry_run, **kwargs):
    settings.configure(**kwargs)
    cleaner.start(config, dry_run)


@main.command()
@click.argument("path", type=Path)
@verbose_option
def update_md5(path: Path, **kwargs):
    settings.configure(**kwargs)
    md5.update_dir_md5(path)


if __name__ == "__main__":
    main()
