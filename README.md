Documentação do Projeto de Análise de Ações com IA
Este documento fornece uma visão geral e explicações do código para um projeto que utiliza HTML, Python, Flask e a API do Gemini para analisar ações.

Visão Geral do Projeto
O projeto é uma aplicação web que permite aos usuários inserir o código de uma ação e receber uma análise gerada por IA. A análise inclui uma recomendação de compra, preço-alvo e potencial de alta. A aplicação utiliza o modelo Gemini do Google para realizar a análise, buscando informações sobre a ação e seu gráfico.

Arquivos do Projeto
O projeto consiste nos seguintes arquivos:

app.py: O arquivo principal do Python que contém o código do Flask e a lógica para interagir com a API do Gemini.

index.html: A página inicial da web que contém a interface do usuário para inserir o código da ação.

action.html: A página que exibe os resultados da análise da ação.

templates/: Diretório que contém os arquivos HTML.

Explicação do Código
app.py
Importações:

import os # Importa o módulo os para interagir com o sistema operacional (ex: variáveis de ambiente).
from google import genai # Importa a biblioteca genai do Google para usar o Gemini.
from google.genai import types # Importa tipos específicos do genai.
from flask import Flask, request, render_template # Importa o Flask e funções relacionadas.

Configuração da API:

GOOGLE_API_KEY = "SUA_CHAVE_DA_API_DO_GEMINI" # Substitua por sua chave da API.
MODELO_PADRAO = "gemini-2.0-flash"
URL_GRAFICO = "https://br.investing.com/equities/{acao}-chart" # URL para obter gráficos de ações.

def configurar_api():
    """Configura a chave da API do Google no ambiente."""
    os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY # Define a chave da API como variável de ambiente.
    print("Chave da API do Google configurada.")

A chave da API do Gemini é configurada como uma variável de ambiente para que a biblioteca genai possa encontrá-la.

Classe Agente:

class Agente:
    """Representa um agente com uma função específica."""
    def __init__(self, nome, instrucao_sistema, nome_modelo=MODELO_PADRAO):
        self.nome = nome # Nome do agente.
        self.chat = genai.Client().chats.create( # Inicializa um chat com o Gemini.
            model=nome_modelo, # Define o modelo a ser usado.
            config=types.GenerateContentConfig(system_instruction=instrucao_sistema) # Define a instrução do sistema.
        )
        print(f"Agente '{nome}' inicializado.")

    def enviar_mensagem(self, prompt):
        """Envia uma mensagem para o agente e retorna a resposta."""
        response = self.chat.send_message(prompt) # Envia o prompt para o Gemini.
        return response.text # Retorna o texto da resposta.

A classe Agente representa um agente de IA com uma função específica. Cada agente tem um nome e uma instrução do sistema que define seu comportamento.

Funções para Criar Agentes:

def criar_agente_pesquisador1(acao):
    """Cria um agente para analisar o gráfico da ação e fazer uma recomendação de compra."""
    instrucao = (f"Você é um analista financeiro... {URL_GRAFICO.format(acao=acao.lower())}...")
    return Agente(nome="Pesquisador1", instrucao_sistema=instrucao)

def criar_agente_pesquisador2(acao):
    """Cria um agente para complementar a pesquisa do Agente 'Pesquisador1'."""
    instrucao = f"Você é um pesquisador financeiro... sobre a ação {acao}..."
    return Agente(nome="Pesquisador2", instrucao_sistema=instrucao)

def criar_agente_avaliador():
    """Cria um agente para fornecer uma recomendação de compra, preço-alvo e potencial de alta."""
    instrucao = ("Você é um profissional, expert e analista de investimentos... recomendação de compra, preço-alvo e potencial de alta.")
    return Agente(nome="Avaliador", instrucao_sistema=instrucao)

Essas funções criam instâncias da classe Agente com diferentes instruções de sistema para realizar tarefas específicas na análise da ação.

Função executar_analise(acao):

def executar_analise(acao):
    """Executa a análise da ação usando os agentes."""
    configurar_api() # Configura a chave da API.
    pesquisador1 = criar_agente_pesquisador1(acao) # Cria o agente pesquisador1.
    pesquisador2 = criar_agente_pesquisador2(acao) # Cria o agente pesquisador2.
    avaliador = criar_agente_avaliador() # Cria o agente avaliador.

    print("\n--- Iniciando a análise da ação ---")

    prompt_pesquisador1 = f"Analise o gráfico da ação {acao}... {URL_GRAFICO.format(acao=acao.lower())}..."
    pesquisa1 = pesquisador1.enviar_mensagem(prompt_pesquisador1) # Envia o prompt para o pesquisador1.

    prompt_pesquisador2 = (f"Complemente a pesquisa sobre a ação {acao}... '{pesquisador1.nome}' encontrou:\n\n{pesquisa1}...")
    pesquisa2 = pesquisador2.enviar_mensagem(prompt_pesquisador2) # Envia o prompt para o pesquisador2.

    prompt_avaliador = ("Com base nas informações dos Agentes... preço-alvo e potencial de alta **APENAS** no seguinte formato:\n\n"
                        "Recomendação de compra : X\n"
                        "Preço-alvo : Y\n"
                        "Potencial de alta : Z%\n")
    avaliacao = avaliador.enviar_mensagem(prompt_avaliador) # Envia o prompt para o avaliador.
    return avaliacao # Retorna a avaliação.

Essa função coordena a análise da ação, criando os agentes, enviando prompts e coletando as respostas.

Rotas do Flask:

app = Flask(__name__) # Cria a instância do Flask.

@app.route('/')
def home():
    return render_template('index.html') # Renderiza a página inicial.

@app.route('/action.html', methods=['GET', 'POST'])
def action_page():
    resultado = None
    if request.method == 'POST':
        acao = request.form['pergunta'] # Obtém a ação do formulário.
        resultado = executar_analise(acao) # Executa a análise.
    return render_template('action.html', resultado=resultado) # Renderiza a página de resultados.

if __name__ == '__main__':
    app.run(debug=True) # Inicia o servidor Flask.

O código define duas rotas:

/: Renderiza o template index.html.

/action.html: Renderiza o template action.html e processa o formulário para analisar uma ação.

index.html
Este arquivo HTML define a página inicial da aplicação web. Ele contém um formulário onde o usuário pode inserir o código de uma ação para análise.

action.html
Este arquivo HTML exibe os resultados da análise da ação. Se o formulário em index.html for enviado, a função action_page em app.py processará a solicitação e renderizará este template com os resultados.

Como Executar o Projeto
Instale o Python: Verifique se o Python está instalado no seu sistema.

Instale o Flask:

pip install Flask

Instale a biblioteca do Gemini:

pip install google-generativeai

Obtenha uma chave da API do Gemini: Obtenha uma chave da API do Google Gemini e substitua "SUA_CHAVE_DA_API_DO_GEMINI" no arquivo app.py pela sua chave.

Execute o aplicativo:

python app.py

Abra o navegador: Acesse http://localhost:5000 no seu navegador para ver a página inicial.
