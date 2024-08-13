import logging
import shutil
from pathlib import Path

logger = logging.getLogger("arto")


def rmdir(p: Path, dry_run: bool = False) -> None:
    logger.info(f"Executing: shutil.rmtree({p})")

    if dry_run:
        return
    try:
        shutil.rmtree(p)
    except PermissionError:
        logger.warning(f"Permission denied for {p}")
    except OSError as e:
        logger.error(f"Error: {e}")
        raise e
