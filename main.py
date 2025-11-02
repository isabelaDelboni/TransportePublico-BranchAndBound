from src.data_processing import carregar_e_limpar_dados

pasta_raw = r"C:\Users\Isabela\Downloads\archive"
pasta_processed = r"C:\Users\Isabela\Downloads\archive\data\processed"

dados = carregar_e_limpar_dados(pasta_raw, pasta_processed)

# Verificar dados
print(dados.isna().sum())
print(dados.head())
