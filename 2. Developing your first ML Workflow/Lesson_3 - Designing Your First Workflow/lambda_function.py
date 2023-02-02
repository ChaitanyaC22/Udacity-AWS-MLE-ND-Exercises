import json
import HelloBlazePreprocessLambda
from HelloBlazePreprocessLambda import preprocess

def lambda_handler(event, context):
    # NOTE:     
    # Pass S3 URI of dataset (Added to test in lambda -> function -> select respective function -> test (Make 
    # sure to add it there without s3://. This is the URI to the S3 bucket where dataset json zip file is located)
    
    preprocess(event['s3-dataset-uri-key'])   
    return {
        'statusCode': 200,
        'body': "Good to go!"
    }