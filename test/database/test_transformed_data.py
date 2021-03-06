import unittest
import json
from aws_allowlister.database.database import connect_db
from aws_allowlister.database.transformed_scraping_data import TransformedScrapingData

db_session = connect_db()
transformed_scraping_database = TransformedScrapingData()


class TransformedDataTestCase(unittest.TestCase):
    def test_get_rows(self):
        """database.scrapers.transformed_scraping_data.get_rows"""
        results = transformed_scraping_database.get_rows(db_session=db_session, service_prefix="s3")
        # print(json.dumps(results, indent=4))
        print(len(results))  # 8
        results = transformed_scraping_database.get_rows(db_session=db_session, standard="SOC")
        # print(json.dumps(results, indent=4))
        print(len(results))  # 146
        results = transformed_scraping_database.get_rows(db_session=db_session, service_name="Amazon Simple Storage Service")
        # print(json.dumps(results, indent=4))
        print(len(results))  # 8

    def test_get_service_names_matching_compliance_standard(self):
        """database.scrapers.transformed_scraping_data.get_service_names_matching_compliance_standard"""
        standard_name = "SOC"
        results = transformed_scraping_database.get_sdk_names_matching_compliance_standard(db_session, "SOC")
        # print(results)
        expected_results = {'appstream': 'Amazon AppStream 2.0', 'athena': 'Amazon Athena', 'chime': 'Amazon Chime', 'clouddirectory': 'Amazon Cloud Directory', 'cloudfront': 'Amazon CloudFront', 'cloudwatch': 'Amazon CloudWatch', 'logs': 'Amazon CloudWatch Logs', 'sdkmetrics': 'Amazon CloudWatch SDK Metrics for Enterprise Support', 'comprehend': 'Amazon Comprehend Medical', 'dynamodb': 'Amazon DynamoDB', 'ebs': 'Amazon Elastic Block Store', 'ecr': 'Amazon Elastic Container Registry', 'ecs': 'Amazon Elastic Container Service', 'elasticfilesystem': 'Amazon Elastic File System', 'eks': 'Amazon Elastic Kubernetes Service', 'elasticmapreduce': 'Amazon Elastic MapReduce', 'elasticache': 'Amazon ElastiCache for Redis', 'es': 'Amazon Elasticsearch Service', 'forecast': 'Amazon Forecast', 'freertos': 'Amazon FreeRTOS', 'fsx': 'Amazon FSx', 'guardduty': 'Amazon GuardDuty', 'inspector': 'Amazon Inspector', 'kinesisanalytics': 'Amazon Kinesis Data Analytics', 'firehose': 'Amazon Kinesis Data Firehose', 'kinesisvideo': 'Amazon Kinesis Video Streams', 'lex': 'Amazon Lex', 'mq': 'Amazon MQ', 'neptune-db': 'Amazon Neptune', 'personalize': 'Amazon Personalize', 'polly': 'Amazon Polly', 'quicksight': 'Amazon QuickSight', 'redshift': 'Amazon Redshift', 'rekognition': 'Amazon Rekognition', 'route53': 'Amazon Route 53', 'glacier': 'Amazon S3 Glacier', 'sagemaker': 'Amazon SageMaker', 'sdb': 'Amazon SimpleDB', 'swf': 'Amazon Simple Workflow Service', 'textract': 'Amazon Textract', 'transcribe': 'Amazon Transcribe', 'translate': 'Amazon Translate', 'workdocs': 'Amazon WorkDocs', 'worklink': 'Amazon WorkLink', 'workmail': 'Amazon WorkMail', 'workspaces': 'Amazon WorkSpaces', 'appsync': 'AWS AppSync', 'backup': 'AWS Backup', 'batch': 'AWS Batch', 'acm': 'AWS Certificate Manager', 'cloudformation': 'AWS CloudFormation', 'cloudhsm': 'AWS CloudHSM', 'cloudtrail': 'AWS CloudTrail', 'codebuild': 'AWS CodeBuild', 'codecommit': 'AWS CodeCommit', 'codedeploy': 'AWS CodeDeploy', 'codepipeline': 'AWS CodePipeline', 'config': 'AWS Config', 'controltower': 'AWS Control Tower', 'dataexchange': 'AWS Data Exchange', 'dms': 'AWS Database Migration Service', 'directconnect': 'AWS Direct Connect', 'ds': 'AWS Directory Service', 'elasticbeanstalk': 'AWS Elastic Beanstalk', 'mediaconnect': 'AWS Elemental MediaConnect', 'mediaconvert': 'AWS Elemental MediaConvert', 'medialive': 'AWS Elemental MediaLive', 'fms': 'AWS Firewall Manager', 'globalaccelerator': 'AWS Global Accelerator', 'iam': 'AWS Identity and Access Management', 'iotevents': 'AWS IoT Events', 'greengrass': 'AWS IoT Greengrass', 'kms': 'AWS Key Management Service', 'lambda': 'AWS Lambda', 'license-manager': 'AWS License Manager', 'opsworks-cm': 'AWS OpsWorks Stacksfor Chef Automate', 'organizations': 'AWS Organizations', 'outposts': 'AWS Outposts', 'resource-groups': 'AWS Resource Groups', 'robomaker': 'AWS RoboMaker', 'secretsmanager': 'AWS Secrets Manager', 'securityhub': 'AWS Security Hub', 'sms': 'AWS Server Migration Service', 'serverlessrepo': 'AWS Serverless Application Repository', 'servicecatalog': 'AWS Service Catalog', 'shield': 'AWS Shield', 'snowball': 'AWS Snowball', 'states': 'AWS Step Functions', 'ssm': 'AWS Systems Manager', 'transfer': 'AWS Transfer Family', 'xray': 'AWS X-Ray', 'sms-voice': 'Amazon Pinpoint SMS and Voice Service', 'pinpoint': '', 'connectparticipant': '', 'account': 'AWS Accounts', 'aws-portal': 'AWS Billing', 'rds-data': 'Amazon RDS Data API', 'rds-db': 'Amazon RDS IAM Authentication', 'route53domains': 'Amazon Route53 Domains', 'sts': 'AWS Security Token Service', 'support': 'AWS Support', 'sso': 'AWS SSO', 'sso-directory': 'AWS SSO Directory', 'connect': 'Amazon Connect', 'ec2': 'Amazon EC2', 'macie': 'Amazon Macie', 'apigateway': 'Amazon API Gateway', 'execute-api': 'Amazon API Gateway', 'amplify': 'AWS Amplify', 'amplifybackend': 'AWS Amplify', 'waf': 'AWS Web Application Firewall', 'wafv2': 'AWS Web Application Firewall', 'waf-regional': 'AWS Web Application Firewall', 'autoscaling': 'Amazon EC2 Auto Scaling', 'application-autoscaling': 'Amazon EC2 Auto Scaling', 'health': 'AWS Personal Health Dashboard', 'events': 'Amazon CloudWatch Events', 'cognito': 'Amazon Cognito', 'cognito-idp': 'Amazon Cognito', 'cognito-identity': 'Amazon Cognito', 'cognito-sync': 'Amazon Cognito', 'comprehendmedical': 'Amazon Comprehend Medical', 'datasync': 'AWS DataSync', 'iot': 'AWS IoT Core', 'iotdeviceadvisor': 'AWS IoT Core', 'iotwireless': 'AWS IoT Core', 'iot-device-tester': 'AWS IoT Device Management', 'kinesis': 'Amazon Kinesis Data Streams', 'kafka': 'Amazon Managed Streaming for Apache Kafka', 'opsworks': 'AWS OpsWorks Stacks', 'qldb': 'Amazon Quantum Ledger Database', 'rds': 'Amazon Relational Database Service', 'ses': 'Amazon Simple Email Service', 'sns': 'Amazon Simple Notification Service', 'sqs': 'Amazon Simple Queue Service', 's3': 'Amazon Simple Storage Service', 'storagegateway': 'AWS Storage Gateway', 'elasticloadbalancing': 'Elastic Load Balancing', 'glue': 'AWS Glue', 'lakeformation': 'AWS Glue', 'macie2': 'Amazon Macie'}

    def test_get_sdk_names_matching_compliance_standard(self):
        """database.scrapers.transformed_scraping_data.get_sdk_names_matching_compliance_standard"""
        results = transformed_scraping_database.get_sdk_names_matching_compliance_standard(db_session, "SOC")
        # print(json.dumps(results, indent=4))
        expected_results = {
            "appstream": "Amazon AppStream 2.0",
            "athena": "Amazon Athena",
            "chime": "Amazon Chime",
            "clouddirectory": "Amazon Cloud Directory",
            "cloudfront": "Amazon CloudFront",
            "cloudwatch": "Amazon CloudWatch",
            "logs": "Amazon CloudWatch Logs",
            "sdkmetrics": "Amazon CloudWatch SDK Metrics for Enterprise Support",
            "comprehend": "Amazon Comprehend Medical",
            "dynamodb": "Amazon DynamoDB",
            "ecr": "Amazon Elastic Container Registry",
            "ecs": "Amazon Elastic Container Service",
            "elasticfilesystem": "Amazon Elastic File System",
            "eks": "Amazon Elastic Kubernetes Service",
            "elasticmapreduce": "Amazon Elastic MapReduce",
            "elasticache": "Amazon ElastiCache for Redis",
            "es": "Amazon Elasticsearch Service",
            "freertos": "Amazon FreeRTOS",
            "fsx": "Amazon FSx",
            "guardduty": "Amazon GuardDuty",
            "inspector": "Amazon Inspector",
            "kinesisanalytics": "Amazon Kinesis Data Analytics",
            "firehose": "Amazon Kinesis Data Firehose",
            "kinesisvideo": "Amazon Kinesis Video Streams",
            "macie": "Amazon Macie",
            "mq": "Amazon MQ",
            "neptune-db": "Amazon Neptune",
            "personalize": "Amazon Personalize",
            "polly": "Amazon Polly",
            "quicksight": "Amazon QuickSight",
            "redshift": "Amazon Redshift",
            "rekognition": "Amazon Rekognition",
            "route53": "Amazon Route 53",
            "glacier": "Amazon S3 Glacier",
            "sagemaker": "Amazon SageMaker",
            "sdb": "Amazon SimpleDB",
            "swf": "Amazon Simple Workflow Service",
            "textract": "Amazon Textract",
            "transcribe": "Amazon Transcribe",
            "translate": "Amazon Translate",
            "workdocs": "Amazon WorkDocs",
            "worklink": "Amazon WorkLink",
            "workmail": "Amazon WorkMail",
            "workspaces": "Amazon WorkSpaces",
            "appsync": "AWS AppSync",
            "backup": "AWS Backup",
            "batch": "AWS Batch",
            "acm": "AWS Certificate Manager",
            "cloudformation": "AWS CloudFormation",
            "cloudhsm": "AWS CloudHSM",
            "cloudtrail": "AWS CloudTrail",
            "codebuild": "AWS CodeBuild",
            "codecommit": "AWS CodeCommit",
            "codedeploy": "AWS CodeDeploy",
            "codepipeline": "AWS CodePipeline",
            "config": "AWS Config",
            "controltower": "AWS Control Tower",
            "dataexchange": "AWS Data Exchange",
            "dms": "AWS Database Migration Service",
            "directconnect": "AWS Direct Connect",
            "ds": "AWS Directory Service",
            "elasticbeanstalk": "AWS Elastic Beanstalk",
            "mediaconnect": "AWS Elemental MediaConnect",
            "mediaconvert": "AWS Elemental MediaConvert",
            "medialive": "AWS Elemental MediaLive",
            "fms": "AWS Firewall Manager",
            "globalaccelerator": "AWS Global Accelerator",
            "glue": "AWS Glue",
            "iam": "AWS Identity and Access Management",
            "iotevents": "AWS IoT Events",
            "greengrass": "AWS IoT Greengrass",
            "kms": "AWS Key Management Service",
            "lambda": "AWS Lambda",
            "license-manager": "AWS License Manager",
            "opsworks-cm": "AWS OpsWorks Stacksfor Chef Automate",
            "organizations": "AWS Organizations",
            "outposts": "AWS Outposts",
            "resource-groups": "AWS Resource Groups",
            "robomaker": "AWS RoboMaker",
            "secretsmanager": "AWS Secrets Manager",
            "securityhub": "AWS Security Hub",
            "sms": "AWS Server Migration Service",
            "serverlessrepo": "AWS Serverless Application Repository",
            "servicecatalog": "AWS Service Catalog",
            "shield": "AWS Shield",
            "DDoSProtection": "AWS Shield",
            "snowball": "AWS Snowball",
            "states": "AWS Step Functions",
            "ssm": "AWS Systems Manager",
            "transfer": "AWS Transfer Family",
            "xray": "AWS X-Ray",
            "sms-voice": "Amazon Pinpoint SMS and Voice Service",
            "pinpoint": "",
            "lex": "Amazon Lex",
            "connectparticipant": "",
            "ebs": "Amazon Elastic Block Store",
            "forecast": "Amazon Forecast",
            "account": "AWS Accounts",
            "aws-portal": "AWS Billing",
            "rds-data": "Amazon RDS Data API",
            "rds-db": "Amazon RDS IAM Authentication",
            "route53domains": "Amazon Route53 Domains",
            "sts": "AWS Security Token Service",
            "support": "AWS Support",
            "sso": "AWS SSO",
            "sso-directory": "AWS SSO Directory",
            "connect": "Amazon Connect",
            "ec2": "Amazon EC2",
            "apigateway": "Amazon API Gateway",
            "execute-api": "Amazon API Gateway",
            "amplify": "AWS Amplify",
            "amplifybackend": "AWS Amplify",
            "waf": "AWS Web Application Firewall",
            "wafv2": "AWS Web Application Firewall",
            "waf-regional": "AWS Web Application Firewall",
            "autoscaling": "Amazon EC2 Auto Scaling",
            "application-autoscaling": "Amazon EC2 Auto Scaling",
            "health": "AWS Personal Health Dashboard",
            "events": "Amazon CloudWatch Events",
            "cognito": "Amazon Cognito",
            "cognito-idp": "Amazon Cognito",
            "cognito-identity": "Amazon Cognito",
            "comprehendmedical": "Amazon Comprehend Medical",
            "datasync": "AWS DataSync",
            "iot": "AWS IoT Core",
            "iotdeviceadvisor": "AWS IoT Core",
            "iotwireless": "AWS IoT Core",
            "iot-device-tester": "AWS IoT Device Management",
            "kinesis": "Amazon Kinesis Data Streams",
            "kafka": "Amazon Managed Streaming for Apache Kafka",
            "opsworks, opsworks-cm": "AWS OpsWorks Stacks",
            "qldb": "Amazon Quantum Ledger Database",
            "rds": "Amazon Relational Database Service",
            "ses": "Amazon Simple Email Service",
            "sns": "Amazon Simple Notification Service",
            "sqs": "Amazon Simple Queue Service",
            "s3": "Amazon Simple Storage Service",
            "storagegateway": "AWS Storage Gateway",
            "elasticloadbalancing": "Elastic Load Balancing"
        }
        print(len(results))
