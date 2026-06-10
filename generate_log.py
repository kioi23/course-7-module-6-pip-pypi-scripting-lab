"""Compatibility wrapper for the log generator.

This keeps both `from generate_log import generate_log` and
`from lib.generate_log import generate_log` working.
"""

from lib.generate_log import generate_log

__all__ = ["generate_log"]
