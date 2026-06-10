from pathlib import Path

import pytest
from datetime import datetime
from lib.generate_log import generate_log

@pytest.fixture
def log_data():
    return ["Entry one", "Entry two", "Entry three"]

@pytest.fixture
def generated_file(log_data, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    filename = generate_log(log_data)
    yield tmp_path / filename

def test_log_file_created(generated_file):
    """Test that the log file is created with today's date in the filename."""
    assert generated_file.exists(), f"{generated_file} not found."

def test_log_file_name_format(generated_file):
    """Test that the filename follows the expected naming convention."""
    today = datetime.now().strftime("%Y%m%d")
    assert generated_file.name == f"log_{today}.txt", "Filename does not match expected format."

def test_log_file_content_matches_input(generated_file, log_data):
    """Test that the content written to the log matches the input list."""
    lines = [line.strip() for line in generated_file.read_text(encoding="utf-8").splitlines()]
    assert lines == log_data, "Log file contents do not match input data."

def test_generate_log_prints_confirmation(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)

    filename = generate_log(["Entry one"])

    captured = capsys.readouterr()
    assert f"Log file created: {filename}" in captured.out

def test_generate_log_raises_error_on_invalid_input():
    """Test that the function raises a ValueError when input is not a list."""
    with pytest.raises(ValueError):
        generate_log("This should be a list")

def test_empty_log_list_creates_empty_file(tmp_path, monkeypatch):
    """Test that passing an empty list still creates an empty log file."""
    monkeypatch.chdir(tmp_path)

    filename = generate_log([])
    assert Path(filename).read_text(encoding="utf-8") == ""
