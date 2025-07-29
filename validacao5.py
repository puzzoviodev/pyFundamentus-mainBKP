def avaliar_metricas_pvp(metric_name, value, metric_info):
    if metric_name == 'P/VP':
        if 0 <= value < 0.5:
            classificacao = 'otimo'
            descricao_detalhada = 'Extremamente subvalorizada, sugere oportunidade ou patrimônio inflado...'
        elif 0.5 <= value < 1:
            classificacao = 'bom'
            descricao_detalhada = 'Subvalorizada, oportunidade em setores cíclicos...'
        elif 1 <= value < 1.5:
            classificacao = 'moderado'
            descricao_detalhada = 'Avaliação razoável, comum em setores maduros...'
        elif 1.5 <= value < 2:
            classificacao = 'ruim'
            descricao_detalhada = 'Empresa cara, comum em setores de crescimento...'
        elif value >= 2:
            classificacao = 'pessimo'
            descricao_detalhada = 'Empresa extremamente cara, preço é mais de 2 vezes o valor patrimonial...'
        else:
            classificacao = 'critico'
            descricao_detalhada = 'Patrimônio líquido por ação negativo, indicando risco crítico...'

        return {
            'metrica': metric_name,
            'valor': value,
            'classificacao': classificacao,
            'descricao': metric_info[metric_name]['descricao'],
            'agrupador': metric_info[metric_name]['agrupador'],
            'descricao_detalhada': descricao_detalhada
        }
metric_info = {
    'P/VP': {
        'descricao': 'Preço sobre Valor Patrimonial por ação',
        'agrupador': 'Valuation'
    }
}

# Exemplo com valor 0.8
resultado = avaliar_metricas_pvp('P/VP', 0.8, metric_info)
print(resultado)

resultado = avaliar_metricas_pvp('P/VP', 0.8, metric_info)

print("Métrica:", resultado['metrica'])
print("Valor:", resultado['valor'])
print("Classificação:", resultado['classificacao'])
print("Descrição:", resultado['descricao'])
print("Agrupador:", resultado['agrupador'])
print("Descrição detalhada:", resultado['descricao_detalhada'])

