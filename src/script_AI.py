import boto3
import json

def automa_ia(): 

    client = boto3.client('bedrock-runtime', region_name='us-east-1')

def auto_ai():
 
    model_id = "amazon.nova-pro-v1:0"

    body = json.dumps({
        "prompt": "Olás, meu nome é Paulo. Como você está?",
        "maxTokens": 200,
        "temperature": 0.5
    })

    try:
        response = client.invoke_model(
            modelId=model_id,
            contentType='application/json',
            accept='application/json',
            body=body
        )

        # Decodifica a resposta
        response_body = json.loads(response.get('body').read())
        completion = response_body.get('completions')[0].get('data').get('text')

        print(f"Resposta do modelo: {completion}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
if __name__ == "__main__":
    automa_ia()