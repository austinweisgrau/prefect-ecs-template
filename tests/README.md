# Tests on Prefect flows and utilities

To run these tests, from the root directory of the repository:
- install development packages `pip install -r requirements-dev.txt`
- run pytest `python -m pytest`

Note that the `pytest` executable may or may not be based in your
expected python environment, and using `python -m pytest` ensure that
your local python environment is being used to run pytest.

To run pytest with logging pass-through, use
- `python -m pytest -o log_cli=true -o log_level=info`

By default tests that interact with external services like the VAN API
or Redshift are skipped. Excluding these simplifies the test
environment as you do not require credentials or internet access. The
remaining tests run very quickly once the test environment is
loaded. The tests in `tests/tests_strive_ea.py` in particular are very
slow. Include all tests with:
- `INCLUDE_EXTERNAL_TESTS=1 python -m pytest`

Some other useful pytest command line options include:
- `pytest --pdb` will open a debugger if a test fails so you can inspect
  and interact with the stack
- `pytest path/to/file/or/directory` will run the tests just from that
  file or directory

pytest has many useful features and the [pytest documentation](https://docs.pytest.org/en/7.1.x/contents.html) is
excellent.
