def classify_financial_metric(metric_name, value):
    """
    Classifica um valor financeiro com base nos intervalos definidos para cada métrica.

    Args:
        metric_name (str): Nome da métrica financeira (ex.: 'Div. liquida/EBIT')
        value (float): Valor da métrica a ser classificado

    Returns:
        dict: Dicionário com a classificação, descrição e descrição detalhada
    """
    # Dicionário com descrições e agrupadores (apenas algumas métricas para brevidade)
    metric_info = {
        'Div. liquida/EBIT': {
            'descricao': 'Dívida líquida dividida pelo EBIT. Mede tempo para quitar dívida com lucro operacional.',
            'agrupador': 'Eficiência'
        },
        'Div. liquida/EBITDA': {
            'descricao': 'Dívida líquida dividida pelo EBITDA. Mede tempo para quitar dívida com fluxo de caixa operacional.',
            'agrupador': 'Eficiência'
        },
        'D.Y': {
            'descricao': 'Dividendos pagos por ação em relação ao preço da ação. Mede retorno via dividendos.',
            'agrupador': 'Outros'
        },
        'P/L': {
            'descricao': 'Preço da ação dividido pelo lucro por ação. Mede valuation em relação ao lucro líquido.',
            'agrupador': 'Valuation'
        }
    }

    if metric_name not in metric_info:
        return {"error": f"Métrica '{metric_name}' não encontrada"}

    # Classificação para 'Div. liquida/EBIT'
    if metric_name == 'Div. liquida/EBIT':
        if value < 0:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Caixa líquido supera dívida, refletindo forte saúde financeira.'
            }
        elif 0 <= value < 1.5:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento controlado, dívida quitável em menos de 1,5 anos de EBIT.'
            }
        elif 1.5 <= value < 3:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento moderado, pagável em 1,5-3 anos de EBIT.'
            }
        elif 3 <= value < 4:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento elevado, leva 3-4 anos de EBIT para pagar a dívida.'
            }
        elif 4 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento crítico, leva mais de 4 anos de EBIT para quitar a dívida líquida.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Dívida líquida negativa pode indicar EBIT negativo ou excesso de caixa líquido.'
            }

    # Classificação para 'Div. liquida/EBITDA'
    if metric_name == 'Div. liquida/EBITDA':
        if value < 0:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Caixa líquido excede dívida, sugerindo forte geração de caixa.'
            }
        elif 0 <= value < 1:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento baixo, dívida quitável rapidamente.'
            }
        elif 1 <= value < 2.5:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento moderado, pagável em 1-2,5 anos de EBITDA.'
            }
        elif 2.5 <= value < 3.5:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento elevado, leva 2,5-3,5 anos de EBITDA para pagar a dívida.'
            }
        elif 3.5 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento crítico, leva mais de 3,5 anos de EBITDA para quitar a dívida.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Prejuízo operacional, com incapacidade de gerar caixa operacional.'
            }

    # Classificação para 'D.Y'
    if metric_name == 'D.Y':
        if 0.06 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Alto retorno, muito atrativo, mas pode indicar risco de insustentabilidade.'
            }
        elif 0.04 <= value < 0.06:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Retorno atrativo, bom para investidores de renda.'
            }
        elif 0.02 <= value < 0.04:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Retorno moderado, oferece equilíbrio entre dividendos e reinvestimento.'
            }
        elif 0.001 <= value < 0.02:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Retorno baixo, pouco atrativo para investidores de dividendos.'
            }
        elif value == 0:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Sem pagamento de dividendos, indicando reinvestimento total ou prejuízo.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Sem pagamento de dividendos, indicando reinvestimento total ou prejuízo.'
            }

    # Classificação para 'P/L'
    if metric_name == 'P/L':
        if 0 <= value < 5:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Extremamente subvalorizada, sugere oportunidade ou lucro inflado.'
            }
        elif 5 <= value < 10:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Subvalorizada, oportunidade em setores cíclicos.'
            }
        elif 10 <= value < 15:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Avaliação razoável, comum em setores maduros.'
            }
        elif 15 <= value < 20:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa cara, comum em setores de crescimento.'
            }
        elif 20 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa extremamente cara, sugerindo sobrevalorização.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Prejuízo por ação, indicando problemas operacionais ou financeiros graves.'
            }


# Função para exibir o resultado de forma formatada
def display_classification(metric_name, value):
    result = classify_financial_metric(metric_name, value)
    if 'error' in result:
        print(result['error'])
    else:
        print(f"Métrica: {result['metrica']}")
        print(f"Valor: {result['valor']}")
        print(f"Classificação: {result['classificacao']}")
        print(f"Descrição: {result['descricao']}")
        print(f"Agrupador: {result['agrupador']}")
        print(f"Descrição Detalhada: {result['descricao_detalhada']}")
        print("-" * 50)


# Testando a função com exemplos
test_cases = [
    ('Div. liquida/EBIT', -1.0),
    ('Div. liquida/EBIT', 2.0),
    ('Div. liquida/EBITDA', 0.5),
    ('D.Y', 0.07),
    ('P/L', 12.0),
    ('P/L', -0.5),
    ('Unknown Metric', 1.0)  # Métrica inválida
]

for metric, value in test_cases:
    display_classification(metric, value)