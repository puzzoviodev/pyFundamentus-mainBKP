metricas = {
    'P/L': {
        'otimo': {'min': 0, 'max': 10},
        'bom': {'min': 10, 'max': 15},
        'regular': {'min': 15, 'max': 20},
        'alto': {'min': 20, 'max': float('inf')},
        'descricao': 'Preço em relação ao lucro. Quanto menor, mais barata a ação.'
    },
    'P/VP': {
        'otimo': {'min': 0, 'max': 1},
        'bom': {'min': 1, 'max': 2},
        'regular': {'min': 2, 'max': 3},
        'alto': {'min': 3, 'max': float('inf')},
        'descricao': 'Preço em relação ao valor patrimonial. Abaixo de 1 indica ação negociada abaixo do patrimônio.'
    },
    'Margem_EBITDA': {
        'ruim': {'min': 0, 'max': 15},
        'regular': {'min': 15, 'max': 25},
        'bom': {'min': 25, 'max': 35},
        'otimo': {'min': 35, 'max': float('inf')},
        'descricao': 'Indica eficiência operacional. Quanto maior, melhor.'
    },
    'Margem_Liquida': {
        'ruim': {'min': 0, 'max': 10},
        'regular': {'min': 10, 'max': 20},
        'bom': {'min': 20, 'max': 30},
        'otimo': {'min': 30, 'max': float('inf')},
        'descricao': 'Lucratividade final. Quanto maior, melhor.'
    },
    'ROE': {
        'ruim': {'min': 0, 'max': 10},
        'regular': {'min': 10, 'max': 15},
        'bom': {'min': 15, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Retorno sobre patrimônio. Maior que 15% é considerado bom.'
    },
    'Dividend_Yield': {
        'baixo': {'min': 0, 'max': 3},
        'regular': {'min': 3, 'max': 6},
        'bom': {'min': 6, 'max': 10},
        'otimo': {'min': 10, 'max': float('inf')},
        'descricao': 'Rendimento de dividendos. Acima de 6% é considerado bom.'
    },
    'Divida_Liquida_EBITDA': {
        'otimo': {'min': float('-inf'), 'max': 1},
        'bom': {'min': 1, 'max': 2.5},
        'regular': {'min': 2.5, 'max': 3.5},
        'alto': {'min': 3.5, 'max': float('inf')},
        'descricao': 'Capacidade de pagar dívidas. Menor que 2.5 é considerado saudável.'
    },
    'FCF_Yield': {
        'baixo': {'min': 0, 'max': 5},
        'regular': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 15, 'max': float('inf')},
        'descricao': 'Rendimento do fluxo de caixa livre. Acima de 10% é considerado bom.'
    }
}


def categorizar_valor(metrica, valor):
    if metrica not in metricas:
        return 'Métrica não reconhecida'

    for categoria, limites in metricas[metrica].items():
        if categoria == 'descricao':
            continue
        if limites['min'] <= valor < limites['max']:
            return categoria
    return 'Valor fora do alcance definido'


# Exemplos de uso
valor_pl = 17
categoria_pl = categorizar_valor('P/L', valor_pl)
print(f'O índice P/L {valor_pl} é categorizado como: {categoria_pl}')


valor_roe = 22
categoria_roe = categorizar_valor('ROE', valor_roe)
print(f'O índice ROE {valor_roe} é categorizado como: {categoria_roe}')
descricao_roe = metricas['ROE']['descricao']
print(descricao_roe)
print(metricas['ROE']['ruim'])
print(metricas['ROE']['regular'])
print(metricas['ROE']['bom'])
print(metricas['ROE']['otimo'])

