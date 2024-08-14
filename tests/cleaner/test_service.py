import logging
from pathlib import Path

import pytest

# Assuming the function `expected_files_are_present` is in a module named `file_checker`
from a2r.core.cleaner.service import expected_files_are_present

# Set up logger
logger = logging.getLogger(__name__)


def test_all_patterns_matched(tmp_path):
    expected_files = {"file1.txt", "*.exe", "simu_grid_?.nc"}
    files = ["file1.txt", "test.exe", "simu_grid_T.nc"]
    for f in files:
        Path(tmp_path / f).touch()

    result = expected_files_are_present(tmp_path, expected_files)
    assert result is True


def test_some_patterns_not_matched(tmp_path):
    expected_files = {"file1.txt", "*.exe", "simu_grid_?.nc"}
    files = ["file1.txt", "test.exe", "simu_grid_T.nc"]
    for f in files:
        Path(tmp_path / f).touch()

    result = expected_files_are_present(tmp_path, expected_files)
    assert result is False


def test_no_files_in_directory(tmp_path):
    expected_files = {"file1.txt", "*.exe"}

    result = expected_files_are_present(tmp_path, expected_files)
    assert result is False


def test_more_file_then_expected(tmp_path):
    expected_files = {"file1.txt", "*.exe", "simu_grid_?.nc"}
    files = ["file1.txt", "test.exe", "simu_grid_T.nc", "unexpected.nc"]

    for f in files:
        Path(tmp_path / f).touch()

    result = expected_files_are_present(tmp_path, expected_files)
    assert result is False


if __name__ == "__main__":
    pytest.main()
