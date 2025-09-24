import boto3
import json

def automa_ia(historico_conversa):
    client = boto3.client('bedrock-runtime', region_name='us-east-1')
    model_id = 'amazon.titan-text-express-v1'

    body = {
        #Antes estava sem "Human e Assistant", o que fazia o modelo responder de forma errada.
        #Com human e assistant, o modelo entendeu que se trata de uma conversa entre humano 
        #e IA e não precisa repetir o output a minha frase, somente a frase dele.
        "inputText": historico_conversa,
        "textGenerationConfig": {
            #Após reduzir os tokens, o modelo respondeu corretamente.
            "maxTokenCount": 200,
            "temperature": 0.2,
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
    historico = "Human: Olá, IA!"
    print(f"Inicio do chat. Por favor, digite 'sair' para encerrar a conversa.")

    while True:
        entrada = input("Você: ")
        if entrada.lower() == "sair":
            print("Encerrando o chat.")
            break
        
        novo_prompt = historico + f" Human: {entrada} Assistant:"
        resposta_ia = automa_ia(novo_prompt)
        
        resposta_ia = automa_ia(historico)
        if resposta_ia:
            historico += f" {resposta_ia}"
            print(f"IA: {resposta_ia}")
        else:
            print(f"Não foi possível obter uma resposta da IA.")
            break