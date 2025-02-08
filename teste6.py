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
    'ROE': {
        'ruim': {'min': 0, 'max': 10},
        'regular': {'min': 10, 'max': 15},
        'bom': {'min': 15, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Retorno sobre patrimônio. Maior que 15% é considerado bom.'
    },
    'ROIA': {
        'ruim': {'min': 0, 'max': 10},
        'regular': {'min': 10, 'max': 15},
        'bom': {'min': 15, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Retorno sobre ativos. Maior que 15% é considerado bom.'
    }
}

for metrica, detalhes in metricas.items():
    print(f'Métrica: {metrica}')
    #print(f'Descrição: {detalhes["descricao"]}')
    #for categoria, limites in detalhes.items():
     #   if categoria == 'descricao':
      #      continue
      #  print(f'  Categoria: {categoria}')
       # print(f'    Min: {limites["min"]}')
       #print(f'    Max: {limites["max"]}')
    #print()
