import logging
import os
from collections.abc import Generator

import pytest
from prefect.context import get_settings_context
from prefect.testing.utilities import prefect_test_harness

logging.getLogger("alembic").setLevel(logging.WARNING)


@pytest.fixture(autouse=True, scope="session")
def setup_test_environment() -> None:
    """Provide an environmental variable to enable checks if testing is active."""
    os.environ["TESTING"] = "1"


@pytest.fixture(autouse=True, scope="session")
def prefect_test_fixture() -> Generator[None, None, None]:
    """Load a prefect test harness for use during test session.

    Sets up a temporary local database to use in lieu of the
    production Orion server. This means we cannot access blocks stored
    in the production environment, so must recreate those resources to
    be available during a test session."""
    with prefect_test_harness():
        yield


def test_test_harness() -> None:
    """Ensure test harness is active & credentials are available."""
    database_url = get_settings_context().settings.dict()[
        "PREFECT_API_DATABASE_CONNECTION_URL"
    ]
    assert database_url.startswith("sqlite")
