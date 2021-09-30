import json
import boto3
import os

rds_client = boto3.client('rds-data')

database_name = os.environ["database_name"]
db_cluster_arn = os.environ["db_cluster_arn"]
db_credentials_secrets_store_arn = os.environ["db_credentials_secrets_store_arn"]

def lambda_handler(event, context):
    response = execute_statement('SELECT Temperature from Temperature WHERE LocationId=5');
    return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "body": json.dumps(response['records'][0][0]['longValue']),
            "headers": {"Access-Control-Allow-Origin": "*"}
        }

    

def execute_statement(sql):
    response = rds_client.execute_statement(
        secretArn=db_credentials_secrets_store_arn,
        database=database_name,
        resourceArn=db_cluster_arn,
        sql=sql
        )
    return response;