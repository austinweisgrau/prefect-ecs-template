from functools import wraps
from threading import Semaphore
from typing import Callable


def limit_concurrency(max_workers: int) -> Callable[[Callable], Callable]:
    """Wraps methods to implement concurrency limit

    Prefect task concurrency limits use a 30 second delay between each
    check for an available slot. This is a more performative approach
    using a threading.Semaphore.

    Prefect must be using a "local" task runner for this to work (the
    ConcurrentTaskRunner) and not a distributed task runner like Dask
    or Ray.

    See thread in the Prefect slack for more discussion:
    https://prefect-community.slack.com/archives/C03D12VV4NN/p1677533662427229
    """

    semaphore = Semaphore(max_workers)

    def pseudo_decorator(func: Callable):
        @wraps(func)
        def limited_concurrent_func(*args, **kwargs):
            with semaphore:
                return func(*args, **kwargs)

        return limited_concurrent_func

    return pseudo_decorator
