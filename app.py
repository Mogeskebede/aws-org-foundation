#!/usr/bin/env python3
import os

from aws_cdk_lib import App #refactored

from org_foundation.ou_stack import OrganizationalUnitsStack
from org_foundation.identity_center_stack import IdentityCenterStack


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Missing required environment variable: {name}")
    return value


app = cdk.App()

# These are provided via environment variables (set in GitHub Actions or your shell)
aws_account = get_required_env("CDK_DEPLOY_ACCOUNT")
aws_region = get_required_env("CDK_DEPLOY_REGION")

# Parent OU or Root ID where PROD and NonPROD OUs will be created
parent_ou_id = get_required_env("ORG_PARENT_OU_ID")

# IAM Identity Center (AWS SSO) instance ARN
sso_instance_arn = get_required_env("SSO_INSTANCE_ARN")

env = cdk.Environment(account=aws_account, region=aws_region)

ou_stack = OrganizationalUnitsStack(
    app,
    "OrgFoundation-OUs",
    env=env,
    parent_ou_id=parent_ou_id,
)

identity_center_stack = IdentityCenterStack(
    app,
    "OrgFoundation-IdentityCenter",
    env=env,
    sso_instance_arn=sso_instance_arn,
)

# Ensure Identity Center stack can depend on OU stack if you later wire assignments to OUs
identity_center_stack.add_dependency(ou_stack)

app.synth()
