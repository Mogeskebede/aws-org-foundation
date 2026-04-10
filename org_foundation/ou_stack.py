from typing import Optional

from aws_cdk import (
    Stack,
)
from aws_cdk import aws_organizations as organizations
from constructs import Construct


class OrganizationalUnitsStack(Stack):
    """
    Creates PROD and NonPROD OUs under a given parent OU or Root ID.
    """

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        parent_ou_id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # PROD OU
        self.prod_ou = organizations.CfnOrganizationalUnit(
            self,
            "ProdOU",
            name="PROD",
            parent_id=parent_ou_id,
        )

        # NonPROD OU
        self.nonprod_ou = organizations.CfnOrganizationalUnit(
            self,
            "NonProdOU",
            name="NonPROD",
            parent_id=parent_ou_id,
        )