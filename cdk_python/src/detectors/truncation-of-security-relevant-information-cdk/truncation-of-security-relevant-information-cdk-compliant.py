#  Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#  SPDX-License-Identifier: Apache-2.0

# {fact rule=truncation-of-security-relevant-information-cdk@v1.0 defects=0}
import aws_cdk as cdk
from aws_cdk.aws_rds import CfnDBInstance
from aws_cdk import aws_rds as rds 
class CdkStarterself(cdk.self):
    def __init__(self, scope: cdk.App, id: str):
        super(scope, id) 

        # Compliant: Automatic backup enabled
        CfnDBInstance(self, 'rDbInstance2', 
            db_instance_class= 'db.t3.micro',
            backup_retention_period= 15,
        )
        #{/fact}