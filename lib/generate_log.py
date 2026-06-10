"""Utilities for generating dated log files."""

from datetime import datetime
from pathlib import Path


def _build_filename() -> str:
    """Return the dated filename used for generated logs."""

    return f"log_{datetime.now().strftime('%Y%m%d')}.txt"


def generate_log(log_data: list[object]) -> str:
    """Write the provided log entries to a dated text file.

    Args:
        log_data: A list of log entries to persist.

    Returns:
        The generated filename.

    Raises:
        ValueError: If log_data is not a list.
    """

    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    filename = _build_filename()
    output_path = Path(filename)
    content = "\n".join(str(item) for item in log_data)
    output_path.write_text(content + ("\n" if content else ""), encoding="utf-8")

    print(f"Log file created: {filename}")
    return filename


if __name__ == "__main__":
    sample_data = ["User logged in", "User updated profile", "Report exported"]
    generate_log(sample_data)