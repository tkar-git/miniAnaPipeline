"""
These tests validate the processing contract used in CI.

What is checked:
1) Processing succeeds when `data.csv` contains header `x,y,z`.
2) Processing fails with a clear error when the header is missing.

Why this matters:
Students can see both positive and negative CI checks:
valid input must pass, invalid input must fail predictably.
"""

import csv
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROCESS_SCRIPT = PROJECT_ROOT / "process.py"


def run_process_in(folder: Path):
    # Execute process.py in a temporary working directory
    # so each test can control its own input/output files.
    return subprocess.run(
        [sys.executable, str(PROCESS_SCRIPT)],
        cwd=folder,
        capture_output=True,
        text=True,
    )


def test_process_succeeds_when_header_exists(tmp_path: Path):
    # Arrange: create a valid input file with required header.
    data_file = tmp_path / "data.csv"
    with data_file.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y", "z"])
        writer.writerow([3, 4, 0])

    # Act: run the processing script.
    result = run_process_in(tmp_path)

    # Assert: script succeeds and writes output.
    assert result.returncode == 0, result.stderr
    assert (tmp_path / "processed.csv").exists()


def test_process_fails_when_header_is_missing(tmp_path: Path):
    # Arrange: create an invalid input file (missing header row).
    data_file = tmp_path / "data.csv"
    with data_file.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([3, 4, 0])

    # Act: run the processing script.
    result = run_process_in(tmp_path)

    # Assert: script fails with a clear contract error message.
    assert result.returncode != 0
    assert "Input CSV must contain header columns: x,y,z" in result.stderr
