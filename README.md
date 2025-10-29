## **🧠 Script para Interação com o Foundation Model (FM) do Amazon Bedrock**

Este projeto em Python tem como objetivo demonstrar a interação com um modelo de IA hospedado no Amazon Bedrock, serviço da AWS voltado para modelos fundacionais (Foundation Models).

O código serve como apoio didático e técnico para entender:

O processo de `fine-tuning` de um modelo;

A `lógica de programação` envolvida na criação do script;

E o funcionamento do ambiente do AWS Console.

### **Pré-requisitos**

Conta na AWS Console

>É necessário possuir uma conta ativa na AWS Console
.

Caso ainda não tenha, siga o processo de criação de conta e familiarize-se com o painel da AWS.

**Instalação do AWS CLI**

Após criar sua conta, será necessário instalar o AWS CLI em sua máquina.

O AWS CLI é a ferramenta utilizada para configurar e gerenciar credenciais de acesso aos serviços da AWS.

Guia oficial de instalação: [Documentação AWS CLI](https://docs.aws.amazon.com/pt_br/cli/)

**Configuração das Credenciais AWS**

Após a instalação, execute o comando abaixo para inserir suas credenciais:
```bash
aws configure
```

Informe o `Access Key ID`, `Secret Access Key`, `região padrão (default region)` e `formato de saída (output format)` conforme solicitado.

### **Como Usar**

**Clone este repositório:**
```bash
git clone https://github.com/euopaulin/AI_Bedrock_AWS_Automation.git
```

**Instale as dependências do projeto:**
```code
pip install -r requirements.txt
```

**Execute o script principal:**

```code
python main.py
```

Acompanhe as respostas e interações diretamente pelo terminal.