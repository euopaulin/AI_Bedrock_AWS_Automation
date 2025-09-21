import boto3
import json

def automa_ia(): 

    client = boto3.client('bedrock-runtime', region_name='us-east-1')

    # Modelo da IA e prompt
    model_id = "ai21.j2-mid-v1"
    prompt = "Qual é a capital da França?"

    body = json.dumps({
        "prompt": prompt,
        "maxTokens": 200
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