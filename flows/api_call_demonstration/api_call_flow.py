import requests
from prefect import flow, task

from utilities.concurrency import limit_concurrency
from utilities.logging import get_logger


@task
@limit_concurrency(max_workers=3)  # Only 3 API calls will be active at a time
def make_api_call(value: str) -> None:
    """Issue an API call, print result"""
    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)
    if response.status_code == 200:
        get_logger().info(f"Successfully fetched resource. [attempt={value}")
    else:
        raise RuntimeError("API fetch failed.")


@flow
def api_calls() -> None:
    """Make a series of API calls with a rate limit"""

    values = range(50)

    for result in make_api_call.map(values):
        result.wait()  # Wait for all tasks to finish

    get_logger().info("API call flow finished.")


if __name__ == "__main__":
    api_calls()
