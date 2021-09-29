import json
import boto3

rds_client = boto3.client('rds-data')

database_name = 'rds_db'
db_cluster_arn = 'arn:aws:rds:us-east-1:581209585450:cluster:rds-cluster'
db_credentials_secrets_store_arn = 'arn:aws:secretsmanager:us-east-1:581209585450:secret:dev-AuroraUserSecret-FwSUkt'

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