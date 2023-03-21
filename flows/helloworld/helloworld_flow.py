from prefect import flow, task

from utilities.logging import get_logger


@task
def log_hello(message: str) -> str:
    get_logger().info(message)
    return message


@flow(name="Hello World")
def helloworld() -> None:
    message = "Hello world!"
    log_hello(message)
