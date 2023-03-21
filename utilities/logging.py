import logging

import prefect

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
        result = prefect.get_run_logger()
    except prefect.exceptions.MissingContextError:
        result = logging.getLogger("wfp-prefect")
    return result
