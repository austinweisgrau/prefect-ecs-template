from flows.helloworld.helloworld_flow import helloworld, log_hello


def test_message() -> None:
    """Ensure task function returns its input."""
    message = "Test hello!"
    result = log_hello.fn(message)
    assert message == result


def test_flow() -> None:
    """Ensure entire flow can run with no errors."""
    helloworld()
