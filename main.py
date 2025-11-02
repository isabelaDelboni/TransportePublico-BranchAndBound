from src.data_processing import carregar_e_limpar_dados

pasta_raw = r".\data\processed/raw"
pasta_processed = r".\data\processed"

dados = carregar_e_limpar_dados(pasta_raw, pasta_processed)

# Verificar dados
print(dados.isna().sum())
print(dados.head())
