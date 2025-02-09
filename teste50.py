metricas = {
    'M. Liquida': {
        'baixo': {'min': 0, 'max': 3},
        'regular': {'min': 3, 'max': 6},
        'bom': {'min': 6, 'max': 10},
        'otimo': {'min': 10, 'max': float('inf')},
        'descricao': 'Rendimento de dividendos. Acima de 6% é considerado bom.',
        'agrupador': 'Rentabilidade'
    },
    'M. EBIT': {
        'otimo': {'min': float('-inf'), 'max': 1},
        'bom': {'min': 1, 'max': 2.5},
        'regular': {'min': 2.5, 'max': 3.5},
        'alto': {'min': 3.5, 'max': float('inf')},
        'descricao': 'Capacidade de pagar dívidas. Menor que 2.5 é considerado saudável.',
        'agrupador': 'Rentabilidade'
    },
    'M. EBITDA': {
        'baixo': {'min': 0, 'max': 5},
        'regular': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 15, 'max': float('inf')},
        'descricao': 'Rendimento do fluxo de caixa livre. Acima de 10% é considerado bom.',
        'agrupador': 'Rentabilidade'
    },
    'M. Bruta': {
        'otimo': {'min': 0, 'max': 10},
        'bom': {'min': 10, 'max': 15},
        'regular': {'min': 15, 'max': 20},
        'alto': {'min': 20, 'max': float('inf')},
        'descricao': 'Preço em relação ao lucro. Quanto menor, mais barata a ação.',
        'agrupador': 'Rentabilidade'
    }
}

for metrica, detalhes in metricas.items():
    if 'regular' in detalhes:
        print(f"Métrica: {metrica}")
        print(f"  Classificação 'regular': Mínimo = {detalhes['regular']['min']}, Máximo = {detalhes['regular']['max']}")
        teste = f"Mínimo = {detalhes['regular']['min']}, Máximo = {detalhes['regular']['max']}"
        print(teste)
