import boto3
import json

def automa_ia():
    client = boto3.client('bedrock-runtime', region_name='us-east-1')
    model_id = 'amazon.titan-text-express-v1'

    body = {
        "inputText": "Olá, meu nome é Paulo. Como você está?",
        "textGenerationConfig": {
            "maxTokenCount": 200,
            "temperature": 0.5,
        }
    }

    try:
        response = client.invoke_model(
            modelId=model_id,
            contentType='application/json',
            accept='application/json',
            body=json.dumps(body)
        )

        response_body = json.loads(response.get('body').read())
        completion = response_body.get('results')[0].get('outputText')

        print(f"Resposta do modelo: {completion}")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    automa_ia()