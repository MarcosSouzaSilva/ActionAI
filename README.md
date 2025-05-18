# ActionIA - Plataforma Inteligente de Análise de Ações

## 1. Visão Geral

ActionIA é uma aplicação web que emprega a inteligência artificial da API Gemini do Google para a análise do mercado de ações. A plataforma permite que usuários consultem o potencial de investimento em ações através da análise de seus gráficos e da avaliação de múltiplos fatores por agentes de IA especializados. A interface de usuário é construída com Flask (Python) para o backend e HTML para o frontend.

## 2. Funcionalidades Principais

-   **Análise Inteligente de Ações:** Utilização de modelos de linguagem avançados para interpretar dados de gráficos de ações e gerar insights.
-   **Recomendações de Investimento:** Fornecimento de recomendações de compra baseadas na análise realizada.
-   **Estimativa de Preço-Alvo:** Apresentação de uma estimativa para o possível público-alvo da ação.
-   **Avaliação de Potencial de Alta:** Cálculo e exibição do potencial de valorização da ação.
-   **Interface Web Intuitiva:** Frontend amigável para a entrada de códigos de ações e visualização dos resultados da análise.

## 3. Arquitetura do Sistema

O sistema ActionIA é composto pelos seguintes componentes principais:

-   **Backend (Flask):** Responsável por receber as requisições do usuário, orquestrar a interação com a API Gemini e renderizar as páginas web.
-   **Inteligência Artificial (Google Gemini API):** Empregada através de agentes especializados para a análise de dados e geração de recomendações.
-   **Frontend (HTML e CSS):** Camada de apresentação para a interação do usuário e exibição dos resultados.

### 3.1. Agentes de IA

O processo de análise é conduzido por uma colaboração de agentes de IA distintos:

-   **Pesquisador Financeiro (Nível 1):** Analisa o gráfico da ação consultada no Investing.com e formula uma recomendação de compra inicial.
-   **Pesquisador Financeiro (Nível 2):** Complementa a análise do primeiro pesquisador, focando na determinação do possível preço-alvo da ação.
-   **Analista de Investimentos (Avaliador):** Consolida as informações fornecidas pelos pesquisadores e, com base na análise do gráfico, emite uma recomendação final de compra, o preço-alvo e o potencial de alta.

## 4. Tecnologias Empregadas

-   **Python (versão 3.13):** Linguagem de programação do backend.
-   **Flask (versão 3.1.1):** Microframework web para Python.
-   **google-generativeai (versão 1.15.0):** Biblioteca para interagir com os modelos Gemini.
-   **HTML5:** Linguagem de marcação para a estrutura da web.
-   **CSS3:** Para o estilo da interface web.

*(Substitua 'X.x' pelas versões reais das bibliotecas/frameworks)*

## 5. Configuração e Instalação

### 5.1. Pré-requisitos

-   Instalação do Python 3.13
-   Gerenciador de pacotes Pip.
-   Uma chave de API válida para o Google Gemini.

### 5.2. Passos de Instalação

1.  Clone o repositório do projeto:
    ```bash
    git clone [https://github.com/MarcosSouzaSilva/ActionsAI.git](https://github.com/MarcosSouzaSilva/ActionsAI.git)
    cd ActionsAI
    ```

2.  Instale as dependências do Python:
    ```bash
    pip install -r requirements.txt
    ```
    *(Certifique-se de ter um arquivo `requirements.txt` contendo `google-generativeai` e `flask`)*

3.  Configuração da Chave da API Gemini:
    -   Abra o arquivo `app.py`.
    -   Localize a linha: `GOOGLE_API_KEY = "CHAVE DA API DO GEMINI"`
    -   Substitua o valor placeholder pela sua chave de API real.

## 6. Execução da Aplicação

1.  No terminal, navegue até o diretório raiz do projeto.
2.  Execute o servidor Flask:
    ```bash
    python app.py
    ```

3.  Abra um navegador web e acesse `http://127.0.0.1:5000/`.

## 7. Contribuições

Contribuições para o projeto são bem-vindas. Por favor, siga as diretrizes padrão para pull requests e submissão de issues.

