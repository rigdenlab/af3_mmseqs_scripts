import pytest  # noqa: F401

from af3_mmseqs2.af3_script_utils import setup_logger


def test_logging():
    try:
        logger = setup_logger()
        assert logger is not None
    except Exception as e:
        assert False, f"Exception: {e}"
    logger.debug("Debug message")
    logger.info("Info message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
