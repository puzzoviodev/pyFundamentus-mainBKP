import requests

def extrair_indicadores_api(ticker):
    url = f"https://investidor10.com.br/api/acao/indicadores/{ticker}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Erro ao acessar API para {ticker}: {response.status_code}")
        return

    dados = response.json()

    # Indicadores desejados
    indicadores_desejados = ["roe", "roic", "margemBruta", "margemLiquida"]
    nomes_legiveis = {
        "roe": "ROE",
        "roic": "ROIC",
        "margemBruta": "Margem Bruta",
        "margemLiquida": "Margem Líquida"
    }

    print(f"\n📊 Indicadores para {ticker}:")
    for chave in indicadores_desejados:
        valor = dados.get(chave)
        texto = f"{nomes_legiveis[chave]}: {valor if valor is not None else 'Não encontrado'}"
        print(texto)

# 🔍 Teste com PETR4
extrair_indicadores_api("PETR4")
