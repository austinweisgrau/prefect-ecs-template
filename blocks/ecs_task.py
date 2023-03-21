"""
pip install prefect -U
pip install prefect-aws
prefect block register -m prefect_aws.ecs
"""
from prefect_aws.ecs import AwsCredentials, ECSTask


def save_ecs_task() -> None:
    aws_credentials_block = AwsCredentials.load("prod")

    ecs = ECSTask(
        aws_credentials=aws_credentials_block,
        image="your-image-url-here",
        cpu="1024",
        memory="2048",
        stream_output=True,
        configure_cloudwatch_logs=True,
        cluster="your-cluster-name-here",
        execution_role_arn="your-execution-role-arn",
        task_role_arn="your-task-role-arn",
        vpc_id="your-vpc-id",
        task_definition_arn="your-task-definition-arn",
        task_customizations=[
            {
                "op": "add",
                "path": "/networkConfiguration/awsvpcConfiguration/subnets",
                "value": ["your-private-subnet-1", "your-private-subnet-2"],
            }
        ],
    )
    ecs.save("prod", overwrite=True)


if __name__ == "__main__":
    save_ecs_task()
