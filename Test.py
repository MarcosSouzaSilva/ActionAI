import os
from google import genai
from google.genai import types
from flask import Flask, request, render_template

GOOGLE_API_KEY = "AIzaSyCiDrREvjMOn_1jbogerWf3xMAMM26f4b0"

MODELO_PADRAO = "gemini-2.0-flash"
# URL para análise do gráfico
URL_GRAFICO = "https://br.investing.com/equities/{acao}-chart"

app = Flask(__name__)

def configurar_api():
    """Configura a chave da API do Google no ambiente."""
    os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY
    print("Chave da API do Google configurada.")

class Agente:
    """Representa um agente com uma função específica."""
    def __init__(self, nome, instrucao_sistema, nome_modelo=MODELO_PADRAO):
        self.nome = nome
        self.chat = genai.Client().chats.create(
            model=nome_modelo,
            config=types.GenerateContentConfig(system_instruction=instrucao_sistema)
        )
        print(f"Agente '{nome}' inicializado.")

    def enviar_mensagem(self, prompt):
        response = self.chat.send_message(prompt)
        return response.text

def criar_agente_pesquisador1(acao):
    instrucao = (f"Você é um analista financeiro. Sua tarefa é analisar o grafico dessa ação : {acao} no site "
                   f"{URL_GRAFICO.format(acao=acao.lower())} e FAZER uma recomendação DE COMPRA. EX : Recomendação de compra: Compra ")
    return Agente(nome="Pesquisador1", instrucao_sistema=instrucao)

def criar_agente_pesquisador2(acao):
    instrucao = f"Você é um pesquisador financeiro. Sua tarefa é complementar a pesquisa do Agente 'Pesquisador1' sobre a ação {acao}, E APENAS FAZER O SEU PUBLICO ALVO, EX: Publico alvo : R$ 45,02."
    return Agente(nome="Pesquisador2", instrucao_sistema=instrucao)

def criar_agente_avaliador():
    instrucao = ("Você é um profissional, expert e analista de investimentos. Com base nas informações fornecidas pelos outros agentes "
                 "e na análise do gráfico, você deve fornecer uma recomendação de compra, preço-alvo e potencial de alta.")
    return Agente(nome="Avaliador", instrucao_sistema=instrucao)

def executar_analise(acao):
    configurar_api()
    pesquisador1 = criar_agente_pesquisador1(acao)
    pesquisador2 = criar_agente_pesquisador2(acao)
    avaliador = criar_agente_avaliador()

    print("\n--- Iniciando a análise da ação ---")

    prompt_pesquisador1 = f"Analise o gráfico da ação {acao} disponível em {URL_GRAFICO.format(acao=acao.lower())} e faça uma recomendação de compra."
    pesquisa1 = pesquisador1.enviar_mensagem(prompt_pesquisador1)

    prompt_pesquisador2 = (f"Complemente a pesquisa sobre a ação {acao}. Aqui está o que o Agente "
                           f"'{pesquisador1.nome}' encontrou:\n\n{pesquisa1}\n\nQual o possível público-alvo para esta ação?")
    pesquisa2 = pesquisador2.enviar_mensagem(prompt_pesquisador2)

    prompt_avaliador = (
        f"Com base nas informações dos Agentes '{pesquisador1.nome}' e '{pesquisador2.nome}', e analisando o gráfico de {acao} em {URL_GRAFICO.format(acao=acao.lower())}, FORNEÇA SUA recomendação de compra, preço-alvo e potencial de alta **APENAS** NO SEGUINTE FORMATO:\n\n"
        "Recomendação de compra : X\n"
        "Preço-alvo : Y\n"
        "Potencial de alta : Z%\n"
        "\n"
        "Retorne a sua resposta estritamente neste formato, sem texto adicional."
    )


    avaliacao = avaliador.enviar_mensagem(prompt_avaliador)

    return avaliacao

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/action.html', methods=['GET', 'POST'])
def action_page():
    resultado = None
    if request.method == 'POST':
        acao = request.form['pergunta']
        resultado = executar_analise(acao)
    return render_template('action.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)