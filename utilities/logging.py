import logging

from prefect import get_run_logger
from prefect.exceptions import MissingContextError

# Configure wfp-prefect logger
# Note that this logger is only used in development
logger = logging.getLogger("prefect-development")
logger.setLevel(logging.DEBUG)


def get_logger() -> logging.Logger:
    """Returns prefect.get_run_logger() except in a test environment

    prefect.get_run_logger() is incompatible with testing task functions
    outside of a flow context. See
    https://github.com/PrefectHQ/prefect/issues/8568"""
    try:
        result = get_run_logger()
    except MissingContextError:
        result = logging.getLogger("prefect-development")
    return result
