# Prefect Flows

This repository contains data pipelines and other orchestrated scripts
for Prefect. The Prefect cloud UI is available [here](https://app.prefect.cloud).

This repository was built off the the dataflow-ops [template](https://github.com/anna-geller/dataflow-ops) and
[tutorial](https://towardsdatascience.com/prefect-aws-ecs-fargate-github-actions-make-serverless-dataflows-as-easy-as-py-f6025335effc), which set up a minimal working example of Prefect with an
execution layer in ECS. It was modified mostly to enable the use of a
dedicated (elastic) IP for the ECS tasks, which allowed us to
whitelist the outbound IP with TMC Redshift so we can access our
redshift instance from the production environment.

## Pipelines, Flows, Deployments

Each data pipeline or orchestrated script is called a "flow" in
Prefect. A flow is a python function that has been wrapped with
the `prefect.flow` decorator, which enables concurrent execution of
submethods that are wrapped with the `prefect.task` decorator,
observability of logs and errors in the Prefect UI.

Prefect flows are "bundled" as a "deployment." The list of
deployments, which can be seen in the Prefect UI, is the formal set of
our pipelines in production. Deployments can be set up to run on an
automated schedule.

All flows live in the `flows` folder of the repository.

## Orchestration vs Execution

Prefect handles orchestration and execution as separate
layers. Deployments in Prefect Cloud represent the orchestration
layer, where configured schedules trigger the execution of our
flows. In the execution layer, a Prefect "agent" polls the Prefect
Cloud server to check for triggered flow runs, and executes those flow
runs in configured infrastructure.

Our execution layer is set up in AWS ECS. Our prefect agent runs on a
small ECS Task that runs 24/7. When a flow run is triggered, a new ECS
Task with more compute power is spun up to run the flow, and spun down
after the flow finishes running.

Currently our prefect agent and all prefect flows run in the same
docker container, built with the Dockerfile in the root directory of
this repository.

The execution layer was set up with the AWS CloudFormation script at
`infrastructure/ecs_cluster_prefect_agent.yml` and the ECSTask block at
`blocks/ecs_task.py`.

## CI/CD

Continuous deployment is configured with Github Actions. The script at
`.github/workflows/main.yaml` runs on pushes to the main branch. It
checks for changes to flows or utilities and updates the code in the
production environment.

## Tests

See [the README in the tests folder](tests/README.md)

## Formatting

This repository is formatted using black and isort. For more information see
https://github.com/psf/black and https://github.com/pycqa/isort

Pre-commit hooks are available to enforce black and isort formatting on
commit. You can also set up your IDE to reformat using black and/or isort on
save.

To set up the pre-commit hooks, install pre-commit with `pip install
pre-commit`, and then run `pre-commit install`.

## Installing parsons with friendly dependencies

parsons is a large package with a ton of dependencies. For any given
script, we only need a smalls subset of parsons functionality and
dependencies installed. To install parsons with an appropriate subset
of dependencies, set these two variables in your environment:

- `PIP_NO_BINARY=parsons`
- `PARSONS_LIMITED_DEPENDENCIES=true`

and then install parsons with a command that specifies which
dependencies you require. For example, `pip install
parsons[ngpvan,redshift]`

See [the parsons documentation](https://www.parsonsproject.org/pub/friendly-dependencies/release/1) for more.
