
# This cell will write the function to your local machine. Note the name of the file and the name of the function. 
# Compare this to the 'Handler' parameter. 

import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
