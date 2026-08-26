import pandas as pd
import numpy as np
import os

def extrair_dados():
    caminho_raw = 'data/raw/dados_academia.csv'
    
    if not os.path.exists(caminho_raw):
        os.makedirs('data/raw', exist_ok=True)
        np.random.seed(42)
        dados = {
            'id_aluno': np.random.randint(1000, 5000, 1000),
            'idade': np.random.randint(16, 65, 1000),
            'plano': np.random.choice(['Mensal', 'Trimestral', 'Anual'], 1000, p=[0.5, 0.3, 0.2]),
            'visitas_mes': np.random.randint(1, 28, 1000),
            'satisfacao': np.random.randint(1, 6, 1000),
            'gasto_extra_mensal': np.random.uniform(0, 150, 1000).round(2)
        }
        df_temp = pd.DataFrame(dados)
        df_temp.to_csv(caminho_raw, index=False, sep=';')
        
    df = pd.read_csv(caminho_raw, sep=';')
    return df

def transformar_dados(df):
    df = df.drop_duplicates()
    
    condicoes = [
        (df['visitas_mes'] >= 20),
        (df['visitas_mes'] >= 10) & (df['visitas_mes'] < 20),
        (df['visitas_mes'] < 10)
    ]
    resultados = ['Alto', 'Médio', 'Baixo']
    df['engajamento'] = np.select(condicoes, resultados, default='Baixo')
    
    return df

def salvar_dados(df):
    caminho_processed = 'data/processed/dados_academia_tratados.csv'
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv(caminho_processed, index=False, sep=';')
    print("Dados tratados salvos com sucesso na pasta processed!")

if __name__ == "__main__":
    df_bruto = extrair_dados()
    df_limpo = transformar_dados(df_bruto)
    salvar_dados(df_limpo)