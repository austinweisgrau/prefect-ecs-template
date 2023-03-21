"""Create and deploy schedules on Prefect deployments.

This method is idempotent and will restore all deployment
schedules to whatever is written here. This script runs in CI/CD
anytime there is a change to this file pushed to the main branch.

These scripts are intended to update already existing deployments in
the Prefect cloud. Matching the Deployment name and Flow name are case
sensitive.

See documentation on schedule automations in Prefect:
https://docs.prefect.io/concepts/schedules
"""

import datetime
from typing import Optional

from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import IntervalSchedule


def schedule_deployment(
    deployment_name: str,
    flow_name: str,
    interval: datetime.timedelta,
    anchor_date: Optional[datetime.datetime],
) -> None:
    dep = Deployment(name=deployment_name, flow_name=flow_name)
    if not dep.load():
        raise RuntimeError("Deployment was not found in the cloud.")

    dep.schedule = IntervalSchedule(
        interval=interval, anchor_date=anchor_date, timezone="America/New_York"
    )

    dep.apply()


def update_deployment_schedules() -> None:
    schedule_deployment(
        "helloworld",
        "Hello World",
        datetime.timedelta(days=1),  # Daily
        datetime.datetime.today().replace(hour=21, minute=5, second=0),  # At 9:05 pm
    )


if __name__ == "__main__":
    update_deployment_schedules()
