import logging
from pathlib import Path

import click

import arto
from arto import settings
from arto.core import cleaner
from arto.core import md5
from arto.core import safe_rm

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
@click.argument("path_to_keep", type=Path)
@click.argument("path_to_clean", type=Path)
@click.option(
    "-f",
    "--force",
    "force_mode",
    is_flag=True,
    default=False,
    help="Delete files without confirm request",
)
@click.option(
    "-d", "--dry-run", is_flag=True, default=False, help="Disable file removal"
)
@verbose_option
def saferm(
    path_to_keep: Path, path_to_clean: Path, force_mode: bool, dry_run: bool, **kwargs
):
    settings.configure(**kwargs)
    safe_rm.start(path_to_keep, path_to_clean, force_mode, dry_run)


@main.command()
@click.argument("path", type=Path)
@verbose_option
def update_md5(path: Path, **kwargs):
    settings.configure(**kwargs)
    md5.update_dir_md5(path)


if __name__ == "__main__":
    main()
