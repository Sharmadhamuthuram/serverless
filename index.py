import json
import boto3

rds_client = boto3.client('rds-data')

database_name = 'serverlessdemo'
db_cluster_arn = 'arn:aws:rds:us-east-1:581209585450:cluster:auroraserverlessdemo'
db_credentials_secrets_store_arn = 'arn:aws:secretsmanager:us-east-1:581209585450:secret:rds-db-credentials/cluster-CSP7J3NNAUUZEEBRPGTUOFR3A4/admin-AQ8Cdz'

def lambda_handler(event, context):
    response = execute_statement('SELECT Temperature from Temperature WHERE LocationId=5');
    return response['records'][0][0]['longValue'];

    

def execute_statement(sql):
    response = rds_client.execute_statement(
        secretArn=db_credentials_secrets_store_arn,
        database=database_name,
        resourceArn=db_cluster_arn,
        sql=sql
        )
    return response;
