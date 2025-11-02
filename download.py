import pandas as pd
import os

# Caminho onde estão os arquivos CSV
pasta = r"C:\Users\Isabela\Downloads\archive"

# Lista todos os arquivos CSV da pasta
arquivos_csv = [f for f in os.listdir(pasta) if f.endswith('.csv')]

# Lista para guardar cada DataFrame
dataframes = []

for arquivo in arquivos_csv:
    # Caminho completo do arquivo
    caminho = os.path.join(pasta, arquivo)

    # Extrai o ano do nome do arquivo (ex: "2007_Entry_Exit.csv" -> 2007)
    ano = int(arquivo.split('_')[0])

    # Lê o CSV
    df = pd.read_csv(caminho)

    # Adiciona coluna "Ano"
    df['Ano'] = ano

    # Guarda o DataFrame na lista
    dataframes.append(df)

# Junta todos os DataFrames em um único DataFrame
dados = pd.concat(dataframes, ignore_index=True)

# Remove duplicatas
dados = dados.drop_duplicates()

# Verifica valores ausentes
print(dados.isna().sum())

# Mostra as primeiras linhas
print(dados.head())
