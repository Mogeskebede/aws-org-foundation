from aws_cdk import (
    Stack,
)
from aws_cdk import aws_sso as sso
from constructs import Construct


class IdentityCenterStack(Stack):
    """
    Creates IAM Identity Center (AWS SSO) permission sets for PROD and NonPROD.
    Assumes built-in directory is already configured as the identity source.
    """

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        sso_instance_arn: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # PROD Admin permission set
        self.prod_admin_permission_set = sso.CfnPermissionSet(
            self,
            "ProdAdminPermissionSet",
            instance_arn=sso_instance_arn,
            name="Prod-Admin",
            description="Admin access for PROD accounts",
            session_duration="PT4H",
            managed_policies=[
                "arn:aws:iam::aws:policy/AdministratorAccess"
            ],
        )

        # Nonprod PowerUser permission set
        self.nonprod_poweruser_permission_set = sso.CfnPermissionSet(
            self,
            "NonProdPowerUserPermissionSet",
            instance_arn=sso_instance_arn,
            name="NonProd-PowerUser",
            description="PowerUser access for NonPROD accounts",
            session_duration="PT8H",
            managed_policies=[
                "arn:aws:iam::aws:policy/PowerUserAccess"
            ],
        )

        # NOTE:
        # You can add CfnAssignment resources here to bind permission sets
        # to specific accounts and groups once you have:
        # - target_id (account ID)
        # - principal_id (group ID in Identity Center)
        #
        # Example (to be customized):
        #
        # sso.CfnAssignment(
        #     self,
        #     "ProdAdminAssignment",
        #     instance_arn=sso_instance_arn,
        #     permission_set_arn=self.prod_admin_permission_set.attr_permission_set_arn,
        #     principal_id="<GROUP_ID>",
        #     principal_type="GROUP",
        #     target_id="<ACCOUNT_ID>",
        #     target_type="AWS_ACCOUNT",
        # )