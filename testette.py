import json
import pandas as pd

# Caminho para seu arquivo
caminho_json = r'D:\indicadores_completo.json'
caminho_saida = r'D:\saida.xlsx'

# Carrega o JSON
with open(caminho_json, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Converte para DataFrame
df = pd.DataFrame(data)

# Salva como Excel
df.to_excel(caminho_saida, index=False)
print("Arquivo exportado com sucesso!")