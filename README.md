# Dashboard de Gestão e Engajamento - Academia

Pipeline de Engenharia de Dados (ETL) e Dashboard Interativo desenvolvido em Python para análise de frequência, retenção e comportamento de alunos de uma academia.

## 🚀 Tecnologias Utilizadas
* **Python**
* **Pandas & NumPy** (Manipulação e transformação de dados)
* **Streamlit** (Interface e construção do Dashboard)
* **Plotly** (Gráficos interativos)

## 📁 Estrutura do Projeto
```text
dashboard-gestao-academia/
│
├── data/
│   ├── raw/                 # Dados brutos gerados pela simulação
│   └── processed/           # Dados tratados e prontos para consumo
│
├── src/
│   └── etl.py               # Script contendo o pipeline de extração e tratamento
│
├── app.py                   # Aplicação principal do Streamlit (Dashboard)
├── requirements.txt         # Dependências do projeto
└── README.md
⚙️ Como Executar o Projeto
1. Clone o repositório:

Bash
git clone https://github.com/SEU-USUARIO/dashboard-gestao-academia.git
cd dashboard-gestao-academia
2. Crie e ative um ambiente virtual:

Bash
python -m venv .venv
.\.venv\Scripts\Activate
3. Instale as dependências:

Bash
pip install -r requirements.txt
4. Execute o pipeline de ETL para gerar e tratar os dados:

Bash
python src/etl.py
5. Inicie o Dashboard interativo:

Bash
streamlit run app.py