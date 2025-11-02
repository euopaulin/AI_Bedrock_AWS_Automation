import boto3 #Importa o SDK da AWS para Python
import json

#Quando rodar o código será necessário ter as credenciais AWS configuradas na máquina local, pode ser feito atráves do AWS CLI ou variáveis de ambiente

#Aqui crei uma função para interagir com o modelo de linguagem da AWS Bedrock
def automa_ia(historico_conversa):
    client = boto3.client('bedrock-runtime', region_name='us-east-1') #Escolho a região do meu AWS Console
    model_id = 'amazon.titan-text-express-v1' #Escolho o modelo que quero usar. Esse modelo é um FM disponivel na AWS Bedrock

    #Aqui é a configuração do corpo da requisição para o modelo
    body = {
        "inputText": historico_conversa,
        "textGenerationConfig": {
            #Aqui posso ajustar os parâmetros de geração de texto dentro do processo de fine tuning
            "maxTokenCount": 200, #Número máximo de tokens a serem gerados
            "temperature": 0.2, #A temperatura em modelos serve para controlar a aleatoriedade das respostas. Valores mais baixos resultam em respostas mais conservadoras, enquanto valores mais altos geram respostas mais variadas e criativas.
            "topP": 0.8, #O top-p serve para controlar a diversidade das respostas geradas. Ele define um limite cumulativo de probabilidade para os tokens considerados na geração de texto. Valores mais baixos resultam em respostas mais focadas, enquanto valores mais altos permitem maior diversidade.
            "topK": 40 #Já o top-k limita o número de tokens mais prováveis considerados na geração de texto. Valores mais baixos resultam em respostas mais focadas, enquanto valores mais altos permitem maior diversidade.
        }
    }

    #Agora aqui é a lógica para fazer a chamada ao modelo e tratar a resposta
    try: #Aqui o try serve para fazer uma tentativa de chamada ao modelo e capturar possíveis erros
        response = client.invoke_model(
            modelId=model_id,
            contentType='application/json',
            accept='application/json',
            body=json.dumps(body)
        )

        response_body = json.loads(response.get('body').read())
        completion = response_body.get('results')[0].get('outputText')

        print(f"Resposta do modelo: {completion}")

    #Se a tentativa falhar, o except captura o erro e imprime uma mensagem
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

#Aqui criei uma interface simples de chat para interagir com a função automa_ia, esssa interação irá ser printada no terminal
if __name__ == "__main__":
    historico = "Human: Olá, IA!"
    print(f"Inicio do chat. Por favor, digite 'sair' para encerrar a conversa.")

    #Esse loop permite a interação contínua com o modelo até que o usuário decida sair
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