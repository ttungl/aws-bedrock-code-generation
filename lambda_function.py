import boto3
import botocore.config
import json
from datetime import datetime

def generate_code(message: str, language: str)-> str:
    prompt_text = f"""Human: Write {language} code for the following instructions: {message}.
    Assistant: 
    """

    body = json.dumps({
        "prompt": prompt_text,
        "max_tokens_to_sample": 2048,
        "temperature": 0.1,
        "top_k": 250,
        "top_p": 0.2,
        "stop_sequences": ["\n\nHuman:"]
    })

    try:
        bedrock = boto3.client('bedrock-runtime', 
                                # region='us-west-2', 
                                config=botocore.config.Config(read_timeout=300, 
                                                                retries={'max_attempts': 3}))
        
        response = bedrock.invoke_model(
            body=body,
            modelId="anthropic.claude-v2"
        )

        response_body = json.loads(response.get('body').read().decode('utf-8'))
        return response_body.get('completion')
    except Exception as e:
        print(f"Error generating code: {e}")
        return e


def save_code_to_s3_bucket(code: str, s3_bucket, s3_key):
    try:
        s3 = boto3.client('s3')
        s3.put_object(Body=code, Bucket=s3_bucket, Key=s3_key)
        print(f"Code saved to S3: {s3_bucket}")
    except Exception as e:
        print(f"Error saving code to S3: {e}")
        return e


def lambda_handler(event, context):
    print(f"Event: {event}")
    print(f"Context: {context}")

    try:
        even_body = json.loads(event['body'])
        message = even_body['message']
        language = even_body['language']

        generated_code = generate_code(message, language)
        if generated_code:
            current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            if language=="python":
                s3_key = f"code-output/{current_time}.py"
            elif language=="rust":
                s3_key = f"code-output/{current_time}.rs"

            s3_bucket = "bedrock-bucket-tungyt"

            save_code_to_s3_bucket(generated_code, s3_bucket, s3_key)
            
        else:
            print("Failed to generate code.")

        return {
            'statusCode': 200,
            'body': json.dumps(f'Code generated and saved to S3: {generated_code}')
        }
    except Exception as e:
        print(f"Error in lambda_handler: {e}")
        return {
            'statusCode': 404,
            'body': json.dumps('Error generating code.')
        }


