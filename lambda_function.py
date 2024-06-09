import json
import boto3

def lambda_handler(event, context):
    
    glue_client = boto3.client('glue')
    
    
    for record in event['Records']:
        s3_event = record['eventName']
        if s3_event == "ObjectCreated:Put":

            try:
                # Start the AWS Glue job
                response = glue_client.start_job_run(
                    JobName='ECommerce_ETL_pipeline'
                    )
                
                print(f"Started Glue job with ID: {response['JobRunId']}")
            
            except Exception as e:
                print(f"Error starting Glue Job: {e}")
                raise e
        
            

    return 
