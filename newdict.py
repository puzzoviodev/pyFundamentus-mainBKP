
indicadores = {
    'Dívida Líquida/EBIT': {
        'pessimo': {'min': 4, 'max': float('inf')},
        'ruim': {'min': 3, 'max': 4},
        'moderado': {'min': 1.5, 'max': 3},
        'bom': {'min': 0, 'max': 1.5},
        'otimo': {'min': float('-inf'), 'max': 0},
        'descricao': 'Relação entre dívida líquida e lucro operacional antes de juros e impostos. Valores altos indicam maior alavancagem e risco financeiro.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Endividamento crítico, leva mais de 4 anos de EBIT para quitar a dívida líquida, indicando alavancagem extrema e risco financeiro elevado. Comum em empresas em crise (ex.: OIBR3) ou setores cíclicos em baixa (ex.: construção, CSNA3). Em 2025, com juros de 10-12%, o custo da dívida pressiona ainda mais a geração de caixa, aumentando a vulnerabilidade a choques econômicos, como desaceleração ou aumento de taxas. Empresas nessa faixa frequentemente enfrentam dificuldades para cobrir juros, com risco de default ou necessidade de reestruturação. Investidores devem evitar, salvo sinais claros de recuperação, como redução agressiva de dívida, venda de ativos (ex.: Petrobrás em reestruturações passadas) ou aumento robusto do EBIT via eficiência operacional. Analise a cobertura de juros (EBIT/juros) e a tendência do EBIT nos últimos 3-5 anos para avaliar sustentabilidade. Setores intensivos em capital (ex.: infraestrutura) podem justificar alavancagem, mas exigem fluxo de caixa estável. Empresas com histórico de lucros voláteis ou em setores expostos a commodities (ex.: mineração) são particularmente arriscadas.',
        'descrruim': 'Endividamento elevado, leva de 3 a 4 anos de EBIT para quitar a dívida líquida. Risco significativo, especialmente em setores cíclicos (ex.: mineração, VALE3). Em 2025, com juros altos, a capacidade de pagamento é pressionada. Cautela é necessária; analise estabilidade do EBIT e plano de desalavancagem.',
        'descrmoderado': 'Endividamento moderado, leva de 1,5 a 3 anos de EBIT para quitar a dívida líquida. Aceitável em setores estáveis (ex.: utilities, ENGI11). Em 2025, monitorar fluxo de caixa livre e riscos macroeconômicos para garantir sustentabilidade.',
        'descrbom': 'Endividamento baixo, dívida quitada em até 1,5 anos de EBIT. Sinal de saúde financeira sólida, comum em setores maduros (ex.: bens de consumo, ITUB4). Em 2025, atrativo para investidores conservadores, mas verificar reinvestimento.',
        'descotimo': 'Dívida líquida negativa, caixa excede dívidas. Situação financeira excepcional, comum em tecnologia (ex.: MGLU3 em períodos de alta liquidez). Em 2025, avaliar alocação de caixa para evitar ineficiências.'
    },
    'Dívida Líquida/EBITDA': {
        'pessimo': {'min': 3.5, 'max': float('inf')},
        'ruim': {'min': 2.5, 'max': 3.5},
        'moderado': {'min': 1, 'max': 2.5},
        'bom': {'min': 0, 'max': 1},
        'otimo': {'min': float('-inf'), 'max': 0},
        'descricao': 'Relação entre dívida líquida e EBITDA. Valores altos indicam alavancagem elevada.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Endividamento crítico, acima de 3,5x o EBITDA. Alto risco, comum em crise (ex.: OIBR3). Em 2025, com juros de 10-12%, risco de default é elevado. Evitar, salvo recuperação clara.',
        'descrruim': 'Endividamento elevado, 2,5-3,5x o EBITDA. Risco em setores cíclicos (ex.: CSNA3). Cautela, verificar plano de redução de dívida.',
        'descrmoderado': 'Endividamento moderado, 1-2,5x o EBITDA. Aceitável em setores estáveis (ex.: EGIE3). Monitorar fluxo de caixa.',
        'descrbom': 'Endividamento baixo, até 1x o EBITDA. Sólido, comum em bens de consumo (ex.: ABEV3). Atraente para conservadores.',
        'descotimo': 'Dívida líquida negativa, caixa supera dívidas. Excelente, comum em tecnologia (ex.: WEGR3). Avaliar uso do caixa.'
    },
    'Dívida Líquida/Patrimônio Líquido': {
        'pessimo': {'min': 1, 'max': float('inf')},
        'ruim': {'min': 0.7, 'max': 1},
        'moderado': {'min': 0.3, 'max': 0.7},
        'bom': {'min': 0, 'max': 0.3},
        'otimo': {'min': float('-inf'), 'max': 0},
        'descricao': 'Relação entre dívida líquida e patrimônio líquido. Indica nível de alavancagem em relação ao capital próprio.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Alavancagem crítica, dívida excede PL. Alto risco (ex.: OIBR3). Em 2025, risco de insolvência é elevado. Evitar.',
        'descrruim': 'Alavancagem elevada, 70-100% do PL. Risco moderado (ex.: CSNA3). Cautela, verificar solvência.',
        'descrmoderado': 'Alavancagem moderada, 30-70% do PL. Aceitável (ex.: ENGI11). Monitorar ROE e fluxo de caixa.',
        'descrbom': 'Baixa alavancagem, até 30% do PL. Sólido (ex.: ITUB4). Atraente para conservadores.',
        'descotimo': 'Caixa excede dívida, situação robusta. Comum em tecnologia (ex.: MGLU3). Avaliar alocação de capital.'
    },
    'Patrimônio/Ativos': {
        'pessimo': {'min': 0, 'max': 0.2},
        'ruim': {'min': 0.2, 'max': 0.3},
        'moderado': {'min': 0.3, 'max': 0.5},
        'bom': {'min': 0.5, 'max': 0.7},
        'otimo': {'min': 0.7, 'max': float('inf')},
        'descricao': 'Proporção do patrimônio em relação aos ativos totais. Indica robustez financeira.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Estrutura frágil, patrimônio <20% dos ativos (ex.: OIBR3). Alto risco. Evitar.',
        'descrruim': 'Estrutura limitada, 20-30% dos ativos. Risco moderado (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Estrutura equilibrada, 30-50% dos ativos (ex.: ENGI11). Seguro com boa gestão.',
        'descrbom': 'Estrutura forte, 50-70% dos ativos (ex.: ABEV3). Atraente para conservadores.',
        'descotimo': 'Estrutura robusta, >70% dos ativos (ex.: WEGR3). Excelente, verificar alocação.'
    },
    'PL/Ativos': {
        'pessimo': {'min': 0, 'max': 0.2},
        'ruim': {'min': 0.2, 'max': 0.3},
        'moderado': {'min': 0.3, 'max': 0.5},
        'bom': {'min': 0.5, 'max': 0.7},
        'otimo': {'min': 0.7, 'max': float('inf')},
        'descricao': 'Relação entre patrimônio líquido e ativos totais. Indica solidez financeira.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Patrimônio muito baixo, <20% dos ativos (ex.: OIBR3). Evitar.',
        'descrruim': 'Patrimônio limitado, 20-30% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Patrimônio equilibrado, 30-50% (ex.: ENGI11). Seguro.',
        'descrbom': 'Patrimônio forte, 50-70% (ex.: ABEV3). Atraente.',
        'descotimo': 'Patrimônio robusto, >70% (ex.: WEGR3). Excelente.'
    },
    'Dividend Yield (DY)': {
        'pessimo': {'min': 0, 'max': 0},
        'ruim': {'min': 0.1, 'max': 2},
        'moderado': {'min': 2, 'max': 4},
        'bom': {'min': 4, 'max': 6},
        'otimo': {'min': 6, 'max': float('inf')},
        'descricao': 'Rendimento de dividendos. Acima de 6% é considerado bom.',
        'agrupador': 'Renda',
        'descrpessimo': 'Sem dividendos, foco em reinvestimento ou prejuízo (ex.: startups). Evitar para renda.',
        'descrruim': 'Dividendos baixos, 0,1-2% (ex.: MGLU3). Pouco atrativo para renda.',
        'descrmoderado': 'Dividendos moderados, 2-4% (ex.: ENGI11). Equilíbrio entre renda e reinvestimento.',
        'descrbom': 'Dividendos atrativos, 4-6% (ex.: ITUB4). Ideal para renda.',
        'descotimo': 'Dividendos altos, >6% (ex.: TAEE11). Verificar sustentabilidade.'
    },
    'EV/EBIT': {
        'pessimo': {'min': 20, 'max': float('inf')},
        'ruim': {'min': 15, 'max': 20},
        'moderado': {'min': 10, 'max': 15},
        'bom': {'min': 5, 'max': 10},
        'otimo': {'min': 0, 'max': 5},
        'descricao': 'Relação entre valor da empresa e EBIT. Indica valuation.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >20x (ex.: startups tech). Evitar, salvo crescimento excepcional.',
        'descrruim': 'Valuation alto, 15-20x (ex.: MGLU3). Cautela, verificar crescimento.',
        'descrmoderado': 'Valuation razoável, 10-15x (ex.: ABEV3). Justo com EBIT estável.',
        'descrbom': 'Valuation atrativo, 5-10x (ex.: ITUB4). Ideal para valor.',
        'descotimo': 'Valuation muito atrativo, <5x (ex.: VALE3 em recuperação). Oportunidade.'
    },
    'EV/EBITDA': {
        'pessimo': {'min': 15, 'max': float('inf')},
        'ruim': {'min': 10, 'max': 15},
        'moderado': {'min': 7, 'max': 10},
        'bom': {'min': 4, 'max': 7},
        'otimo': {'min': 0, 'max': 4},
        'descricao': 'Relação entre valor da empresa e EBITDA. Indica valuation.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >15x (ex.: startups tech). Evitar.',
        'descrruim': 'Valuation alto, 10-15x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 7-10x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 4-7x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <4x (ex.: VALE3). Oportunidade.'
    },
    'P/ATIVO': {
        'pessimo': {'min': 2, 'max': float('inf')},
        'ruim': {'min': 1.5, 'max': 2},
        'moderado': {'min': 1, 'max': 1.5},
        'bom': {'min': 0.5, 'max': 1},
        'otimo': {'min': 0, 'max': 0.5},
        'descricao': 'Relação entre preço e ativos totais. Indica valuation.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >2x (ex.: MGLU3). Evitar.',
        'descrruim': 'Valuation alto, 1,5-2x (ex.: startups). Cautela.',
        'descrmoderado': 'Valuation razoável, 1-1,5x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 0,5-1x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <0,5x (ex.: VALE3). Oportunidade.'
    },
    'P/Ativo Circulante Líquido': {
        'pessimo': {'min': 3, 'max': float('inf')},
        'ruim': {'min': 2, 'max': 3},
        'moderado': {'min': 1, 'max': 2},
        'bom': {'min': 0.5, 'max': 1},
        'otimo': {'min': 0, 'max': 0.5},
        'descricao': 'Relação entre preço e ativo circulante líquido. Indica valuation e liquidez.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >3x (ex.: startups). Evitar.',
        'descrruim': 'Valuation alto, 2-3x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 1-2x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 0,5-1x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <0,5x (ex.: VALE3). Oportunidade.'
    },
    'P/Capital de Giro': {
        'pessimo': {'min': 5, 'max': float('inf')},
        'ruim': {'min': 3, 'max': 5},
        'moderado': {'min': 1.5, 'max': 3},
        'bom': {'min': 0.5, 'max': 1.5},
        'otimo': {'min': 0, 'max': 0.5},
        'descricao': 'Relação entre preço e capital de giro. Indica valuation e eficiência.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >5x (ex.: startups). Evitar.',
        'descrruim': 'Valuation alto, 3-5x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 1,5-3x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 0,5-1,5x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <0,5x (ex.: VALE3). Oportunidade.'
    },
    'P/EBIT': {
        'pessimo': {'min': 25, 'max': float('inf')},
        'ruim': {'min': 20, 'max': 25},
        'moderado': {'min': 15, 'max': 20},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 0, 'max': 10},
        'descricao': 'Relação entre preço e EBIT. Indica valuation operacional.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >25x (ex.: startups). Evitar.',
        'descrruim': 'Valuation alto, 20-25x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 15-20x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 10-15x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <10x (ex.: VALE3). Oportunidade.'
    },
    'P/EBITDA': {
        'pessimo': {'min': 15, 'max': float('inf')},
        'ruim': {'min': 10, 'max': 15},
        'moderado': {'min': 7, 'max': 10},
        'bom': {'min': 4, 'max': 7},
        'otimo': {'min': 0, 'max': 4},
        'descricao': 'Relação entre preço e EBITDA. Indica valuation operacional.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >15x (ex.: startups). Evitar.',
        'descrruim': 'Valuation alto, 10-15x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 7-10x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 4-7x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <4x (ex.: VALE3). Oportunidade.'
    },
    'P/L': {
        'pessimo': {'min': 30, 'max': float('inf')},
        'ruim': {'min': 20, 'max': 30},
        'moderado': {'min': 15, 'max': 20},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 0, 'max': 10},
        'descricao': 'Relação entre preço e lucro líquido. Indica valuation.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >30x (ex.: startups). Evitar.',
        'descrruim': 'Valuation alto, 20-30x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 15-20x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 10-15x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <10x (ex.: VALE3). Oportunidade.'
    },
    'P/VPA': {
        'pessimo': {'min': 3, 'max': float('inf')},
        'ruim': {'min': 2, 'max': 3},
        'moderado': {'min': 1.5, 'max': 2},
        'bom': {'min': 1, 'max': 1.5},
        'otimo': {'min': 0, 'max': 1},
        'descricao': 'Relação entre preço e valor patrimonial por ação. Indica valuation.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >3x (ex.: startups). Evitar.',
        'descrruim': 'Valuation alto, 2-3x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 1,5-2x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 1-1,5x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <1x (ex.: VALE3). Oportunidade.'
    },
    'PSR': {
        'pessimo': {'min': 3, 'max': float('inf')},
        'ruim': {'min': 2, 'max': 3},
        'moderado': {'min': 1, 'max': 2},
        'bom': {'min': 0.5, 'max': 1},
        'otimo': {'min': 0, 'max': 0.5},
        'descricao': 'Relação entre preço e receita. Indica valuation em relação às vendas.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >3x (ex.: startups). Evitar.',
        'descrruim': 'Valuation alto, 2-3x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 1-2x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 0,5-1x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <0,5x (ex.: VALE3). Oportunidade.'
    },
    'Giro do Ativo': {
        'pessimo': {'min': 0, 'max': 0.5},
        'ruim': {'min': 0.5, 'max': 1},
        'moderado': {'min': 1, 'max': 1.5},
        'bom': {'min': 1.5, 'max': 2},
        'otimo': {'min': 2, 'max': float('inf')},
        'descricao': 'Eficiência na geração de receita por ativo. Indica produtividade.',
        'agrupador': 'Eficiência',
        'descrpessimo': 'Baixa eficiência, <0,5x (ex.: OIBR3). Evitar.',
        'descrruim': 'Eficiência limitada, 0,5-1x (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Eficiência razoável, 1-1,5x (ex.: ABEV3). Justo.',
        'descrbom': 'Alta eficiência, 1,5-2x (ex.: ITUB4). Ideal.',
        'descotimo': 'Eficiência excepcional, >2x (ex.: WEGR3). Atraente.'
    },
    'Liquidez Corrente': {
        'pessimo': {'min': 0, 'max': 1},
        'ruim': {'min': 1, 'max': 1.2},
        'moderado': {'min': 1.2, 'max': 1.5},
        'bom': {'min': 1.5, 'max': 2},
        'otimo': {'min': 2, 'max': float('inf')},
        'descricao': 'Capacidade de cobrir passivos de curto prazo com ativos circulantes.',
        'agrupador': 'Liquidez',
        'descrpessimo': 'Baixa liquidez, <1 (ex.: OIBR3). Evitar.',
        'descrruim': 'Liquidez limitada, 1-1,2 (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Liquidez razoável, 1,2-1,5 (ex.: ABEV3). Justo.',
        'descrbom': 'Boa liquidez, 1,5-2 (ex.: ITUB4). Ideal.',
        'descotimo': 'Liquidez excepcional, >2 (ex.: WEGR3). Atraente.'
    },
    'LPA': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 0.5},
        'moderado': {'min': 0.5, 'max': 1},
        'bom': {'min': 1, 'max': 2},
        'otimo': {'min': 2, 'max': float('inf')},
        'descricao': 'Lucro por ação. Indica rentabilidade por ação.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Prejuízo por ação (ex.: OIBR3). Evitar.',
        'descrruim': 'Lucro baixo, 0-0,5 (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Lucro razoável, 0,5-1 (ex.: ABEV3). Justo.',
        'descrbom': 'Lucro sólido, 1-2 (ex.: ITUB4). Ideal.',
        'descotimo': 'Lucro excepcional, >2 (ex.: WEGR3). Atraente.'
    },
    'Margem Bruta': {
        'pessimo': {'min': 0, 'max': 10},
        'ruim': {'min': 10, 'max': 20},
        'moderado': {'min': 20, 'max': 30},
        'bom': {'min': 30, 'max': 50},
        'otimo': {'min': 50, 'max': float('inf')},
        'descricao': 'Percentual de lucro bruto sobre receita. Indica eficiência operacional.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Margem muito baixa, <10% (ex.: OIBR3). Evitar.',
        'descrruim': 'Margem limitada, 10-20% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Margem razoável, 20-30% (ex.: ABEV3). Justo.',
        'descrbom': 'Margem sólida, 30-50% (ex.: ITUB4). Ideal.',
        'descotimo': 'Margem excepcional, >50% (ex.: WEGR3). Atraente.'
    },
    'Margem EBIT': {
        'pessimo': {'min': 0, 'max': 5},
        'ruim': {'min': 5, 'max': 10},
        'moderado': {'min': 10, 'max': 15},
        'bom': {'min': 15, 'max': 25},
        'otimo': {'min': 25, 'max': float('inf')},
        'descricao': 'Percentual de lucro operacional sobre receita. Indica eficiência.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Margem muito baixa, <5% (ex.: OIBR3). Evitar.',
        'descrruim': 'Margem limitada, 5-10% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Margem razoável, 10-15% (ex.: ABEV3). Justo.',
        'descrbom': 'Margem sólida, 15-25% (ex.: ITUB4). Ideal.',
        'descotimo': 'Margem excepcional, >25% (ex.: WEGR3). Atraente.'
    },
    'Margem EBITDA': {
        'pessimo': {'min': 0, 'max': 10},
        'ruim': {'min': 10, 'max': 15},
        'moderado': {'min': 15, 'max': 20},
        'bom': {'min': 20, 'max': 30},
        'otimo': {'min': 30, 'max': float('inf')},
        'descricao': 'Percentual de EBITDA sobre receita. Indica geração de caixa operacional.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Margem muito baixa, <10% (ex.: OIBR3). Evitar.',
        'descrruim': 'Margem limitada, 10-15% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Margem razoável, 15-20% (ex.: ABEV3). Justo.',
        'descrbom': 'Margem sólida, 20-30% (ex.: ITUB4). Ideal.',
        'descotimo': 'Margem excepcional, >30% (ex.: WEGR3). Atraente.'
    },
    'Margem Líquida': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 5},
        'moderado': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Percentual de lucro líquido sobre receita. Indica rentabilidade final.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Prejuízo líquido, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Margem baixa, 0-5% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Margem razoável, 5-10% (ex.: ABEV3). Justo.',
        'descrbom': 'Margem sólida, 10-20% (ex.: ITUB4). Ideal.',
        'descotimo': 'Margem excepcional, >20% (ex.: WEGR3). Atraente.'
    },
    'ROA': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 5},
        'moderado': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 15, 'max': float('inf')},
        'descricao': 'Retorno sobre ativos. Indica eficiência na utilização dos ativos.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Retorno negativo, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Retorno baixo, 0-5% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Retorno razoável, 5-10% (ex.: ABEV3). Justo.',
        'descrbom': 'Retorno sólido, 10-15% (ex.: ITUB4). Ideal.',
        'descotimo': 'Retorno excepcional, >15% (ex.: WEGR3). Atraente.'
    },
    'ROE': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 10},
        'moderado': {'min': 10, 'max': 15},
        'bom': {'min': 15, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Retorno sobre patrimônio líquido. Indica rentabilidade para acionistas.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Retorno negativo, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Retorno baixo, 0-10% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Retorno razoável, 10-15% (ex.: ABEV3). Justo.',
        'descrbom': 'Retorno sólido, 15-20% (ex.: ITUB4). Ideal.',
        'descotimo': 'Retorno excepcional, >20% (ex.: WEGR3). Atraente.'
    },
    'CAGR Lucros 5 anos': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 5},
        'moderado': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Crescimento anual composto dos lucros em 5 anos. Indica tendência de crescimento.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Crescimento negativo, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Crescimento baixo, 0-5% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Crescimento razoável, 5-10% (ex.: ABEV3). Justo.',
        'descrbom': 'Crescimento sólido, 10-20% (ex.: ITUB4). Ideal.',
        'descotimo': 'Crescimento excepcional, >20% (ex.: WEGR3). Atraente.'
    },
    'ROIC': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 5},
        'moderado': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 15, 'max': float('inf')},
        'descricao': 'Retorno sobre capital investido. Indica eficiência do capital.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Retorno negativo, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Retorno baixo, 0-5% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Retorno razoável, 5-10% (ex.: ABEV3). Justo.',
        'descrbom': 'Retorno sólido, 10-15% (ex.: ITUB4). Ideal.',
        'descotimo': 'Retorno excepcional, >15% (ex.: WEGR3). Atraente.'
    },
    'VPA': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 1},
        'moderado': {'min': 1, 'max': 5},
        'bom': {'min': 5, 'max': 10},
        'otimo': {'min': 10, 'max': float('inf')},
        'descricao': 'Valor patrimonial por ação. Indica valor contábil por ação.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Valor patrimonial negativo (ex.: OIBR3). Evitar.',
        'descrruim': 'Valor patrimonial baixo, 0-1 (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Valor patrimonial razoável, 1-5 (ex.: ABEV3). Justo.',
        'descrbom': 'Valor patrimonial sólido, 5-10 (ex.: ITUB4). Ideal.',
        'descotimo': 'Valor patrimonial excepcional, >10 (ex.: WEGR3). Atraente.'
    }
}
=====================


```python
indicadores = {
    'Dívida Líquida/EBIT': {
        'pessimo': {'min': 4, 'max': float('inf')},
        'ruim': {'min': 3, 'max': 4},
        'moderado': {'min': 1.5, 'max': 3},
        'bom': {'min': 0, 'max': 1.5},
        'otimo': {'min': float('-inf'), 'max': 0},
        'descricao': 'Relação entre dívida líquida e EBIT. Valores altos indicam maior alavancagem e risco financeiro.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Endividamento crítico, leva mais de 4 anos de EBIT para quitar a dívida líquida, indicando alavancagem extrema e risco financeiro elevado. Comum em empresas em crise (ex.: OIBR3) ou setores cíclicos em baixa (ex.: construção, CSNA3). Em 2025, com juros de 10-12%, o custo da dívida pressiona a geração de caixa, aumentando a vulnerabilidade a choques econômicos, como desaceleração ou aumento de taxas. Evitar, salvo sinais claros de recuperação.',
        'descrruim': 'Endividamento elevado, 3-4 anos de EBIT. Risco significativo, especialmente em setores cíclicos (ex.: mineração, VALE3). Em 2025, verificar estabilidade do EBIT e plano de desalavancagem.',
        'descrmoderado': 'Endividamento moderado, 1,5-3 anos de EBIT. Aceitável em setores estáveis (ex.: utilities, ENGI11). Em 2025, monitorar fluxo de caixa livre e riscos macroeconômicos.',
        'descrbom': 'Endividamento baixo, até 1,5 anos de EBIT. Sólido, comum em setores maduros (ex.: bens de consumo, ITUB4). Atraente para conservadores.',
        'descotimo': 'Dívida líquida negativa, caixa excede dívidas. Situação excepcional, comum em tecnologia (ex.: WEGR3). Avaliar alocação de caixa.'
    },
    'Dívida Líquida/EBITDA': {
        'pessimo': {'min': 3.5, 'max': float('inf')},
        'ruim': {'min': 2.5, 'max': 3.5},
        'moderado': {'min': 1, 'max': 2.5},
        'bom': {'min': 0, 'max': 1},
        'otimo': {'min': float('-inf'), 'max': 0},
        'descricao': 'Relação entre dívida líquida e EBITDA. Valores altos indicam alavancagem elevada.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Endividamento crítico, >3,5x o EBITDA. Alto risco (ex.: OIBR3). Em 2025, com juros de 10-12%, risco de default é elevado. Evitar.',
        'descrruim': 'Endividamento elevado, 2,5-3,5x o EBITDA. Risco em setores cíclicos (ex.: CSNA3). Verificar plano de redução de dívida.',
        'descrmoderado': 'Endividamento moderado, 1-2,5x o EBITDA. Aceitável (ex.: EGIE3). Monitorar fluxo de caixa.',
        'descrbom': 'Endividamento baixo, até 1x o EBITDA. Sólido (ex.: ABEV3). Atraente para conservadores.',
        'descotimo': 'Dívida líquida negativa, caixa supera dívidas. Excelente (ex.: WEGR3). Avaliar uso do caixa.'
    },
    'Dívida Líquida/Patrimônio Líquido': {
        'pessimo': {'min': 1, 'max': float('inf')},
        'ruim': {'min': 0.7, 'max': 1},
        'moderado': {'min': 0.3, 'max': 0.7},
        'bom': {'min': 0, 'max': 0.3},
        'otimo': {'min': float('-inf'), 'max': 0},
        'descricao': 'Relação entre dívida líquida e patrimônio líquido. Indica alavancagem em relação ao capital próprio.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Alavancagem crítica, dívida excede PL (ex.: OIBR3). Alto risco. Evitar.',
        'descrruim': 'Alavancagem elevada, 70-100% do PL (ex.: CSNA3). Cautela, verificar solvência.',
        'descrmoderado': 'Alavancagem moderada, 30-70% do PL (ex.: ENGI11). Monitorar ROE e fluxo de caixa.',
        'descrbom': 'Baixa alavancagem, até 30% do PL (ex.: ITUB4). Atraente para conservadores.',
        'descotimo': 'Caixa excede dívida, situação robusta (ex.: WEGR3). Avaliar alocação de capital.'
    },
    'Patrimônio/Ativos': {
        'pessimo': {'min': float('-inf'), 'max': 0.2},  # Ajustado para incluir negativos
        'ruim': {'min': 0.2, 'max': 0.3},
        'moderado': {'min': 0.3, 'max': 0.5},
        'bom': {'min': 0.5, 'max': 0.7},
        'otimo': {'min': 0.7, 'max': float('inf')},
        'descricao': 'Proporção do patrimônio em relação aos ativos totais. Indica robustez financeira.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Estrutura frágil, patrimônio <20% dos ativos ou negativo (ex.: OIBR3). Alto risco de insolvência. Evitar.',
        'descrruim': 'Estrutura limitada, 20-30% dos ativos (ex.: CSNA3). Cautela, verificar solvência.',
        'descrmoderado': 'Estrutura equilibrada, 30-50% dos ativos (ex.: ENGI11). Seguro com boa gestão.',
        'descrbom': 'Estrutura forte, 50-70% dos ativos (ex.: ABEV3). Atraente para conservadores.',
        'descotimo': 'Estrutura robusta, >70% dos ativos (ex.: WEGR3). Excelente, verificar alocação.'
    },
    'PL/Ativos': {
        'pessimo': {'min': float('-inf'), 'max': 0.2},  # Ajustado para incluir negativos
        'ruim': {'min': 0.2, 'max': 0.3},
        'moderado': {'min': 0.3, 'max': 0.5},
        'bom': {'min': 0.5, 'max': 0.7},
        'otimo': {'min': 0.7, 'max': float('inf')},
        'descricao': 'Relação entre patrimônio líquido e ativos totais. Indica solidez financeira.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Patrimônio muito baixo ou negativo, <20% dos ativos (ex.: OIBR3). Evitar.',
        'descrruim': 'Patrimônio limitado, 20-30% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Patrimônio equilibrado, 30-50% (ex.: ENGI11). Seguro.',
        'descrbom': 'Patrimônio forte, 50-70% (ex.: ABEV3). Atraente.',
        'descotimo': 'Patrimônio robusto, >70% (ex.: WEGR3). Excelente.'
    },
    'Dividend Yield (DY)': {
        'pessimo': {'min': 0, 'max': 0},
        'ruim': {'min': 0.1, 'max': 2},
        'moderado': {'min': 2, 'max': 4},
        'bom': {'min': 4, 'max': 6},
        'otimo': {'min': 6, 'max': float('inf')},
        'descricao': 'Rendimento de dividendos. Acima de 6% é considerado bom.',
        'agrupador': 'Renda',
        'descrpessimo': 'Sem dividendos, foco em reinvestimento ou prejuízo (ex.: startups). Evitar para renda.',
        'descrruim': 'Dividendos baixos, 0,1-2% (ex.: MGLU3). Pouco atrativo para renda.',
        'descrmoderado': 'Dividendos moderados, 2-4% (ex.: ENGI11). Equilíbrio entre renda e reinvestimento.',
        'descrbom': 'Dividendos atrativos, 4-6% (ex.: ITUB4). Ideal para renda.',
        'descotimo': 'Dividendos altos, >6% (ex.: TAEE11). Verificar sustentabilidade.'
    },
    'EV/EBIT': {
        'pessimo': {'min': 20, 'max': float('inf')},
        'ruim': {'min': 15, 'max': 20},
        'moderado': {'min': 10, 'max': 15},
        'bom': {'min': 5, 'max': 10},
        'otimo': {'min': float('-inf'), 'max': 5},  # Ajustado para incluir negativos
        'descricao': 'Relação entre valor da empresa e EBIT. Valores muito baixos ou negativos (EV negativo com EBIT positivo) sugerem subvalorização.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >20x (ex.: startups tech). Alto risco de supervalorização. Em 2025, com juros de 10-12%, evitar salvo crescimento excepcional.',
        'descrruim': 'Valuation alto, 15-20x (ex.: MGLU3). Cautela, verificar crescimento do EBIT.',
        'descrmoderado': 'Valuation razoável, 10-15x (ex.: ABEV3). Justo com EBIT estável.',
        'descrbom': 'Valuation atrativo, 5-10x (ex.: ITUB4). Ideal para investidores de valor.',
        'descotimo': 'Valuation extremamente atrativo, <5x ou negativo devido a EV negativo com EBIT positivo (ex.: VALE3 em recuperação). Oportunidade, verificar alocação de caixa.'
    },
    'EV/EBITDA': {
        'pessimo': {'min': 15, 'max': float('inf')},
        'ruim': {'min': 10, 'max': 15},
        'moderado': {'min': 7, 'max': 10},
        'bom': {'min': 4, 'max': 7},
        'otimo': {'min': float('-inf'), 'max': 4},  # Ajustado para incluir negativos
        'descricao': 'Relação entre valor da empresa e EBITDA. Valores muito baixos ou negativos (EV negativo com EBITDA positivo) sugerem subvalorização.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >15x (ex.: startups tech). Evitar, salvo crescimento excepcional.',
        'descrruim': 'Valuation alto, 10-15x (ex.: MGLU3). Cautela, verificar crescimento.',
        'descrmoderado': 'Valuation razoável, 7-10x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 4-7x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation extremamente atrativo, <4x ou negativo devido a EV negativo com EBITDA positivo (ex.: VALE3). Oportunidade, verificar alocação de caixa.'
    },
    'P/ATIVO': {
        'pessimo': {'min': 2, 'max': float('inf')},
        'ruim': {'min': 1.5, 'max': 2},
        'moderado': {'min': 1, 'max': 1.5},
        'bom': {'min': 0.5, 'max': 1},
        'otimo': {'min': 0, 'max': 0.5},
        'descricao': 'Relação entre preço e ativos totais. Indica valuation.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >2x (ex.: MGLU3). Evitar.',
        'descrruim': 'Valuation alto, 1,5-2x (ex.: startups). Cautela.',
        'descrmoderado': 'Valuation razoável, 1-1,5x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 0,5-1x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <0,5x (ex.: VALE3). Oportunidade.'
    },
    'P/Ativo Circulante Líquido': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 2, 'max': float('inf')},     # Ajustado para refletir alto valuation
        'moderado': {'min': 1, 'max': 2},
        'bom': {'min': 0.5, 'max': 1},
        'otimo': {'min': 0, 'max': 0.5},
        'descricao': 'Relação entre preço e ativo circulante líquido. Indica valuation e liquidez.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Ativo circulante líquido negativo ou valuation muito elevado (ex.: OIBR3). Evitar.',
        'descrruim': 'Valuation alto, >2x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 1-2x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 0,5-1x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <0,5x (ex.: VALE3). Oportunidade.'
    },
    'P/Capital de Giro': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 3, 'max': float('inf')},     # Ajustado para alto valuation
        'moderado': {'min': 1.5, 'max': 3},
        'bom': {'min': 0.5, 'max': 1.5},
        'otimo': {'min': 0, 'max': 0.5},
        'descricao': 'Relação entre preço e capital de giro. Indica valuation e eficiência.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Capital de giro negativo ou valuation muito elevado (ex.: OIBR3). Evitar.',
        'descrruim': 'Valuation alto, >3x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 1,5-3x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 0,5-1,5x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <0,5x (ex.: VALE3). Oportunidade.'
    },
    'P/EBIT': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 20, 'max': float('inf')},     # Ajustado para alto valuation
        'moderado': {'min': 15, 'max': 20},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 0, 'max': 10},
        'descricao': 'Relação entre preço e EBIT. Indica valuation operacional.',
        'agrupador': 'Valuation',
        'descrpessimo': 'EBIT negativo ou valuation elevado, >20x (ex.: OIBR3). Evitar.',
        'descrruim': 'Valuation alto, 20x+ (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 15-20x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 10-15x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <10x (ex.: VALE3). Oportunidade.'
    },
    'P/EBITDA': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 10, 'max': float('inf')},     # Ajustado para alto valuation
        'moderado': {'min': 7, 'max': 10},
        'bom': {'min': 4, 'max': 7},
        'otimo': {'min': 0, 'max': 4},
        'descricao': 'Relação entre preço e EBITDA. Indica valuation operacional.',
        'agrupador': 'Valuation',
        'descrpessimo': 'EBITDA negativo ou valuation elevado, >10x (ex.: OIBR3). Evitar.',
        'descrruim': 'Valuation alto, 10x+ (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 7-10x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 4-7x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <4x (ex.: VALE3). Oportunidade.'
    },
    'P/L': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 20, 'max': float('inf')},     # Ajustado para alto valuation
        'moderado': {'min': 15, 'max': 20},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 0, 'max': 10},
        'descricao': 'Relação entre preço e lucro líquido. Indica valuation.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Lucro negativo ou valuation elevado, >20x (ex.: OIBR3). Evitar.',
        'descrruim': 'Valuation alto, 20x+ (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 15-20x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 10-15x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <10x (ex.: VALE3). Oportunidade.'
    },
    'P/VPA': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 2, 'max': float('inf')},     # Ajustado para alto valuation
        'moderado': {'min': 1.5, 'max': 2},
        'bom': {'min': 1, 'max': 1.5},
        'otimo': {'min': 0, 'max': 1},
        'descricao': 'Relação entre preço e valor patrimonial por ação. Indica valuation.',
        'agrupador': 'Valuation',
        'descrpessimo': 'VPA negativo ou valuation elevado, >2x (ex.: OIBR3). Evitar.',
        'descrruim': 'Valuation alto, 2x+ (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 1,5-2x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 1-1,5x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <1x (ex.: VALE3). Oportunidade.'
    },
    'PSR': {
        'pessimo': {'min': 3, 'max': float('inf')},
        'ruim': {'min': 2, 'max': 3},
        'moderado': {'min': 1, 'max': 2},
        'bom': {'min': 0.5, 'max': 1},
        'otimo': {'min': 0, 'max': 0.5},
        'descricao': 'Relação entre preço e receita. Indica valuation em relação às vendas.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >3x (ex.: startups). Evitar.',
        'descrruim': 'Valuation alto, 2-3x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 1-2x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 0,5-1x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <0,5x (ex.: VALE3). Oportunidade.'
    },
    'Giro do Ativo': {
        'pessimo': {'min': 0, 'max': 0.5},
        'ruim': {'min': 0.5, 'max': 1},
        'moderado': {'min': 1, 'max': 1.5},
        'bom': {'min': 1.5, 'max': 2},
        'otimo': {'min': 2, 'max': float('inf')},
        'descricao': 'Eficiência na geração de receita por ativo. Indica produtividade.',
        'agrupador': 'Eficiência',
        'descrpessimo': 'Baixa eficiência, <0,5x (ex.: OIBR3). Evitar.',
        'descrruim': 'Eficiência limitada, 0,5-1x (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Eficiência razoável, 1-1,5x (ex.: ABEV3). Justo.',
        'descrbom': 'Alta eficiência, 1,5-2x (ex.: ITUB4). Ideal.',
        'descotimo': 'Eficiência excepcional, >2x (ex.: WEGR3). Atraente.'
    },
    'Liquidez Corrente': {
        'pessimo': {'min': 0, 'max': 1},
        'ruim': {'min': 1, 'max': 1.2},
        'moderado': {'min': 1.2, 'max': 1.5},
        'bom': {'min': 1.5, 'max': 2},
        'otimo': {'min': 2, 'max': float('inf')},
        'descricao': 'Capacidade de cobrir passivos de curto prazo com ativos circulantes.',
        'agrupador': 'Liquidez',
        'descrpessimo': 'Baixa liquidez, <1 (ex.: OIBR3). Evitar.',
        'descrruim': 'Liquidez limitada, 1-1,2 (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Liquidez razoável, 1,2-1,5 (ex.: ABEV3). Justo.',
        'descrbom': 'Boa liquidez, 1,5-2 (ex.: ITUB4). Ideal.',
        'descotimo': 'Liquidez excepcional, >2 (ex.: WEGR3). Atraente.'
    },
    'LPA': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 0.5},
        'moderado': {'min': 0.5, 'max': 1},
        'bom': {'min': 1, 'max': 2},
        'otimo': {'min': 2, 'max': float('inf')},
        'descricao': 'Lucro por ação. Indica rentabilidade por ação.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Prejuízo por ação (ex.: OIBR3). Evitar.',
        'descrruim': 'Lucro baixo, 0-0,5 (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Lucro razoável, 0,5-1 (ex.: ABEV3). Justo.',
        'descrbom': 'Lucro sólido, 1-2 (ex.: ITUB4). Ideal.',
        'descotimo': 'Lucro excepcional, >2 (ex.: WEGR3). Atraente.'
    },
    'Margem Bruta': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 0, 'max': 10},
        'moderado': {'min': 10, 'max': 20},
        'bom': {'min': 20, 'max': 30},
        'otimo': {'min': 30, 'max': float('inf')},
        'descricao': 'Percentual de lucro bruto sobre receita. Indica eficiência operacional.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Margem negativa ou muito baixa, <10% (ex.: OIBR3). Evitar.',
        'descrruim': 'Margem limitada, 10-20% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Margem razoável, 20-30% (ex.: ABEV3). Justo.',
        'descrbom': 'Margem sólida, 30-50% (ex.: ITUB4). Ideal.',
        'descotimo': 'Margem excepcional, >50% (ex.: WEGR3). Atraente.'
    },
    'Margem EBIT': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 0, 'max': 5},
        'moderado': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 15, 'max': float('inf')},
        'descricao': 'Percentual de lucro operacional sobre receita. Indica eficiência.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Margem negativa ou muito baixa, <5% (ex.: OIBR3). Evitar.',
        'descrruim': 'Margem limitada, 5-10% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Margem razoável, 10-15% (ex.: ABEV3). Justo.',
        'descrbom': 'Margem sólida, 15-25% (ex.: ITUB4). Ideal.',
        'descotimo': 'Margem excepcional, >25% (ex.: WEGR3). Atraente.'
    },
    'Margem EBITDA': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 0, 'max': 10},
        'moderado': {'min': 10, 'max': 15},
        'bom': {'min': 15, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Percentual de EBITDA sobre receita. Indica geração de caixa operacional.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Margem negativa ou muito baixa, <10% (ex.: OIBR3). Evitar.',
        'descrruim': 'Margem limitada, 10-15% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Margem razoável, 15-20% (ex.: ABEV3). Justo.',
        'descrbom': 'Margem sólida, 20-30% (ex.: ITUB4). Ideal.',
        'descotimo': 'Margem excepcional, >30% (ex.: WEGR3). Atraente.'
    },
    'Margem Líquida': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 5},
        'moderado': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Percentual de lucro líquido sobre receita. Indica rentabilidade final.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Prejuízo líquido, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Margem baixa, 0-5% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Margem razoável, 5-10% (ex.: ABEV3). Justo.',
        'descrbom': 'Margem sólida, 10-20% (ex.: ITUB4). Ideal.',
        'descotimo': 'Margem excepcional, >20% (ex.: WEGR3). Atraente.'
    },
    'ROA': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 5},
        'moderado': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 15, 'max': float('inf')},
        'descricao': 'Retorno sobre ativos. Indica eficiência na utilização dos ativos.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Retorno negativo, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Retorno baixo, 0-5% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Retorno razoável, 5-10% (ex.: ABEV3). Justo.',
        'descrbom': 'Retorno sólido, 10-15% (ex.: ITUB4). Ideal.',
        'descotimo': 'Retorno excepcional, >15% (ex.: WEGR3). Atraente.'
    },
    'ROE': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 10},
        'moderado': {'min': 10, 'max': 15},
        'bom': {'min': 15, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Retorno sobre patrimônio líquido. Indica rentabilidade para acionistas.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Retorno negativo, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Retorno baixo, 0-10% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Retorno razoável, 10-15% (ex.: ABEV3). Justo.',
        'descrbom': 'Ret


        ==============

Revisão das Faixas e Correções

Abaixo, listo os indicadores, analiso as faixas atuais, e indico correções quando necessário. As descrições completas estarão no artefato.

    Dívida Líquida/EBIT
        Atual: Ótimo = min: float('-inf'), max: 0 (negativa)
        Análise: Correto. Dívida líquida negativa (caixa > dívida) é ideal, indicando saúde financeira robusta (ex.: WEGR3). Valores positivos altos são péssimos (ex.: OIBR3).
        Correção: Nenhuma. Faixas e interpretações estão corretas.
    Dívida Líquida/EBITDA
        Atual: Ótimo = min: float('-inf'), max: 0 (negativa)
        Análise: Correto. Mesma lógica do Dívida Líquida/EBIT. Negativo reflete excesso de caixa, o que é "Ótimo" (ex.: MGLU3 em períodos de alta liquidez).
        Correção: Nenhuma.
    Dívida Líquida/Patrimônio Líquido
        Atual: Ótimo = min: float('-inf'), max: 0 (negativa)
        Análise: Correto. Dívida líquida negativa indica baixo risco financeiro, ideal para investidores conservadores (ex.: ITUB4).
        Correção: Nenhuma.
    Patrimônio/Ativos
        Atual: Péssimo = 0 a 0.2, Ótimo = 0.7 a float('inf')
        Análise: Correto. Valores negativos são teoricamente possíveis (patrimônio líquido negativo), mas raros e indicariam insolvência, sendo "Péssimo". Faixas positivas estão adequadas.
        Correção: Adicionar faixa explícita para valores negativos como "Péssimo" (min: float('-inf'), max: 0).
    PL/Ativos
        Atual: Péssimo = 0 a 0.2, Ótimo = 0.7 a float('inf')
        Análise: Mesmo caso do Patrimônio/Ativos. Valores negativos (patrimônio líquido negativo) são "Péssimo".
        Correção: Adicionar faixa negativa explícita para "Péssimo" (min: float('-inf'), max: 0).
    Dividend Yield (DY)
        Atual: Péssimo = 0 a 0, Ótimo = 6 a float('inf')
        Análise: Correto. DY negativo não é possível (dividendos não são negativos). Faixas estão adequadas.
        Correção: Nenhuma.
    EV/EBIT
        Atual: Ótimo = 0 a 5
        Análise: Incorreto. Como discutido anteriormente, EV/EBIT negativo pode ser "Ótimo" se o EV for negativo (alto caixa) e o EBIT for positivo, indicando subvalorização (ex.: WEGR3). Porém, EBIT negativo (prejuízo) resulta em EV/EBIT negativo, mas é "Péssimo". A faixa "Ótimo" deve incluir negativos com descrição clara.
        Correção: Ajustar Ótimo para min: float('-inf'), max: 5 e esclarecer na descrição que negativos são "Ótimos" apenas com EV negativo e EBIT positivo.
    EV/EBITDA
        Atual: Ótimo = 0 a 4
        Análise: Incorreto. Mesma lógica do EV/EBIT. EV/EBITDA negativo pode ser "Ótimo" com EV negativo e EBITDA positivo, mas EBITDA negativo é "Péssimo".
        Correção: Ajustar Ótimo para min: float('-inf'), max: 4 com descrição esclarecendo.
    P/ATIVO
        Atual: Ótimo = 0 a 0.5
        Análise: Correto. P/Ativo negativo não é possível (preço de mercado é positivo). Faixas estão adequadas.
        Correção: Nenhuma.
    P/Ativo Circulante Líquido
        Atual: Ótimo = 0 a 0.5
        Análise: Correto. Ativo circulante líquido (ativos circulantes - passivos circulantes) pode ser negativo, mas isso seria "Péssimo", não "Ótimo". Faixas atuais excluem negativos adequadamente.
        Correção: Adicionar faixa explícita para negativos como "Péssimo" (min: float('-inf'), max: 0).
    P/Capital de Giro
        Atual: Ótimo = 0 a 0.5
        Análise: Correto. Capital de giro negativo (ativo circulante < passivo circulante) seria "Péssimo". Faixas excluem negativos adequadamente.
        Correção: Adicionar faixa explícita para negativos como "Péssimo" (min: float('-inf'), max: 0).
    P/EBIT
        Atual: Ótimo = 0 a 10
        Análise: Incorreto. P/EBIT negativo ocorre com EBIT negativo (prejuízo), que é "Péssimo", não "Ótimo". Faixas devem excluir negativos da categoria "Ótimo".
        Correção: Ajustar Péssimo para incluir min: float('-inf'), max: 0 e Ótimo para min: 0, max: 10.
    P/EBITDA
        Atual: Ótimo = 0 a 4
        Análise: Incorreto. P/EBITDA negativo ocorre com EBITDA negativo, que é "Péssimo". Faixas devem excluir negativos de "Ótimo".
        Correção: Ajustar Péssimo para min: float('-inf'), max: 0 e Ótimo para min: 0, max: 4.
    P/L
        Atual: Ótimo = 0 a 10
        Análise: Incorreto. P/L negativo ocorre com lucro líquido negativo, que é "Péssimo" (ex.: OIBR3 em prejuízo). Faixas devem excluir negativos de "Ótimo".
        Correção: Ajustar Péssimo para min: float('-inf'), max: 0 e Ótimo para min: 0, max: 10.
    P/VPA
        Atual: Ótimo = 0 a 1
        Análise: Correto. P/VPA negativo não é possível (preço e VPA são positivos, exceto em casos raros de VPA negativo, que seriam "Péssimo"). Faixas estão adequadas.
        Correção: Adicionar faixa explícita para VPA negativo como "Péssimo" (min: float('-inf'), max: 0).
    PSR
        Atual: Ótimo = 0 a 0.5
        Análise: Correto. PSR negativo não é possível (preço e receita são positivos). Faixas estão adequadas.
        Correção: Nenhuma.
    Giro do Ativo
        Atual: Péssimo = 0 a 0.5, Ótimo = 2 a float('inf')
        Análise: Correto. Giro do Ativo negativo não é possível (receita é positiva). Faixas estão adequadas.
        Correção: Nenhuma.
    Liquidez Corrente
        Atual: Péssimo = 0 a 1, Ótimo = 2 a float('inf')
        Análise: Correto. Liquidez Corrente negativa não é possível (ativos circulantes são positivos). Faixas estão adequadas.
        Correção: Nenhuma.
    LPA
        Atual: Péssimo = float('-inf') a 0, Ótimo = 2 a float('inf')
        Análise: Correto. LPA negativo indica prejuízo, sendo "Péssimo" (ex.: OIBR3). Faixas estão corretas.
        Correção: Nenhuma.
    Margem Bruta
        Atual: Péssimo = 0 a 10, Ótimo = 50 a float('inf')
        Análise: Correto. Margem Bruta negativa é possível (custos > receita bruta), mas seria "Péssimo". Faixas excluem negativos adequadamente.
        Correção: Adicionar faixa explícita para negativos como "Péssimo" (min: float('-inf'), max: 0).
    Margem EBIT
        Atual: Péssimo = 0 a 5, Ótimo = 25 a float('inf')
        Análise: Incorreto. Margem EBIT negativa (prejuízo operacional) é "Péssimo", não incluída na faixa atual.
        Correção: Ajustar Péssimo para min: float('-inf'), max: 0.
    Margem EBITDA
        Atual: Péssimo = 0 a 10, Ótimo = 30 a float('inf')
        Análise: Incorreto. Margem EBITDA negativa (prejuízo antes de depreciação) é "Péssimo".
        Correção: Ajustar Péssimo para min: float('-inf'), max: 0.
    Margem Líquida
        Atual: Péssimo = float('-inf') a 0, Ótimo = 20 a float('inf')
        Análise: Correto. Margem Líquida negativa indica prejuízo, sendo "Péssimo" (ex.: CSNA3 em crise). Faixas estão corretas.
        Correção: Nenhuma.
    ROA
        Atual: Péssimo = float('-inf') a 0, Ótimo = 15 a float('inf')
        Análise: Correto. ROA negativo indica prejuízo, sendo "Péssimo" (ex.: OIBR3). Faixas estão corretas.
        Correção: Nenhuma.
    ROE
        Atual: Péssimo = float('-inf') a 0, Ótimo = 20 a float('inf')
        Análise: Correto. ROE negativo indica prejuízo, sendo "Péssimo". Faixas estão corretas.
        Correção: Nenhuma.
    CAGR Lucros 5 anos
        Atual: Péssimo = float('-inf') a 0, Ótimo = 20 a float('inf')
        Análise: Correto. Crescimento negativo indica declínio nos lucros, sendo "Péssimo". Faixas estão corretas.
        Correção: Nenhuma.
    ROIC
        Atual: Péssimo = float('-inf') a 0, Ótimo = 15 a float('inf')
        Análise: Correto. ROIC negativo indica ineficiência, sendo "Péssimo". Faixas estão corretas.
        Correção: Nenhuma.
    VPA
        Atual: Péssimo = float('-inf') a 0, Ótimo = 10 a float('inf')
        Análise: Correto. VPA negativo indica patrimônio líquido negativo, sendo "Péssimo" (ex.: OIBR3). Faixas estão corretas.
        Correção: Nenhuma.

Correções Aplicadas

Os principais erros encontrados estão nos indicadores de valuation (EV/EBIT, EV/EBITDA, P/EBIT, P/EBITDA, P/L) e rentabilidade (Margem EBIT, Margem EBITDA, Patrimônio/Ativos, PL/Ativos, P/Ativo Circulante Líquido, P/Capital de Giro, P/VPA), onde valores negativos foram incorretamente excluídos ou não tratados adequadamente. As correções incluem:

    Inclusão de faixas negativas em "Péssimo" para indicadores onde negativos indicam prejuízo ou ineficiência (ex.: P/EBIT, P/EBITDA, P/L, Margem EBIT, Margem EBITDA).
    Ajuste da faixa "Ótimo" em EV/EBIT e EV/EBITDA para incluir negativos (float('-inf')) com descrições esclarecendo que isso se aplica a EV negativo com EBIT/EBITDA positivo.
    Adição de faixas negativas explícitas em indicadores como Patrimônio/Ativos, PL/Ativos, P/Ativo Circulante Líquido, P/Capital de Giro, e P/VPA, classificando-as como "Péssimo".
======

```python
indicadores = {
    'Dívida Líquida/EBIT': {
        'pessimo': {'min': 4, 'max': float('inf')},
        'ruim': {'min': 3, 'max': 4},
        'moderado': {'min': 1.5, 'max': 3},
        'bom': {'min': 0, 'max': 1.5},
        'otimo': {'min': float('-inf'), 'max': 0},
        'descricao': 'Relação entre dívida líquida e EBIT. Valores altos indicam maior alavancagem e risco financeiro.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Endividamento crítico, leva mais de 4 anos de EBIT para quitar a dívida líquida, indicando alavancagem extrema e risco financeiro elevado. Comum em empresas em crise (ex.: OIBR3) ou setores cíclicos em baixa (ex.: construção, CSNA3). Em 2025, com juros de 10-12%, o custo da dívida pressiona a geração de caixa, aumentando a vulnerabilidade a choques econômicos, como desaceleração ou aumento de taxas. Evitar, salvo sinais claros de recuperação.',
        'descrruim': 'Endividamento elevado, 3-4 anos de EBIT. Risco significativo, especialmente em setores cíclicos (ex.: mineração, VALE3). Em 2025, verificar estabilidade do EBIT e plano de desalavancagem.',
        'descrmoderado': 'Endividamento moderado, 1,5-3 anos de EBIT. Aceitável em setores estáveis (ex.: utilities, ENGI11). Em 2025, monitorar fluxo de caixa livre e riscos macroeconômicos.',
        'descrbom': 'Endividamento baixo, até 1,5 anos de EBIT. Sólido, comum em setores maduros (ex.: bens de consumo, ITUB4). Atraente para conservadores.',
        'descotimo': 'Dívida líquida negativa, caixa excede dívidas. Situação excepcional, comum em tecnologia (ex.: WEGR3). Avaliar alocação de caixa.'
    },
    'Dívida Líquida/EBITDA': {
        'pessimo': {'min': 3.5, 'max': float('inf')},
        'ruim': {'min': 2.5, 'max': 3.5},
        'moderado': {'min': 1, 'max': 2.5},
        'bom': {'min': 0, 'max': 1},
        'otimo': {'min': float('-inf'), 'max': 0},
        'descricao': 'Relação entre dívida líquida e EBITDA. Valores altos indicam alavancagem elevada.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Endividamento crítico, >3,5x o EBITDA. Alto risco (ex.: OIBR3). Em 2025, com juros de 10-12%, risco de default é elevado. Evitar.',
        'descrruim': 'Endividamento elevado, 2,5-3,5x o EBITDA. Risco em setores cíclicos (ex.: CSNA3). Verificar plano de redução de dívida.',
        'descrmoderado': 'Endividamento moderado, 1-2,5x o EBITDA. Aceitável (ex.: EGIE3). Monitorar fluxo de caixa.',
        'descrbom': 'Endividamento baixo, até 1x o EBITDA. Sólido (ex.: ABEV3). Atraente para conservadores.',
        'descotimo': 'Dívida líquida negativa, caixa supera dívidas. Excelente (ex.: WEGR3). Avaliar uso do caixa.'
    },
    'Dívida Líquida/Patrimônio Líquido': {
        'pessimo': {'min': 1, 'max': float('inf')},
        'ruim': {'min': 0.7, 'max': 1},
        'moderado': {'min': 0.3, 'max': 0.7},
        'bom': {'min': 0, 'max': 0.3},
        'otimo': {'min': float('-inf'), 'max': 0},
        'descricao': 'Relação entre dívida líquida e patrimônio líquido. Indica alavancagem em relação ao capital próprio.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Alavancagem crítica, dívida excede PL (ex.: OIBR3). Alto risco. Evitar.',
        'descrruim': 'Alavancagem elevada, 70-100% do PL (ex.: CSNA3). Cautela, verificar solvência.',
        'descrmoderado': 'Alavancagem moderada, 30-70% do PL (ex.: ENGI11). Monitorar ROE e fluxo de caixa.',
        'descrbom': 'Baixa alavancagem, até 30% do PL (ex.: ITUB4). Atraente para conservadores.',
        'descotimo': 'Caixa excede dívida, situação robusta (ex.: WEGR3). Avaliar alocação de capital.'
    },
    'Patrimônio/Ativos': {
        'pessimo': {'min': float('-inf'), 'max': 0.2},  # Ajustado para incluir negativos
        'ruim': {'min': 0.2, 'max': 0.3},
        'moderado': {'min': 0.3, 'max': 0.5},
        'bom': {'min': 0.5, 'max': 0.7},
        'otimo': {'min': 0.7, 'max': float('inf')},
        'descricao': 'Proporção do patrimônio em relação aos ativos totais. Indica robustez financeira.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Estrutura frágil, patrimônio <20% dos ativos ou negativo (ex.: OIBR3). Alto risco de insolvência. Evitar.',
        'descrruim': 'Estrutura limitada, 20-30% dos ativos (ex.: CSNA3). Cautela, verificar solvência.',
        'descrmoderado': 'Estrutura equilibrada, 30-50% dos ativos (ex.: ENGI11). Seguro com boa gestão.',
        'descrbom': 'Estrutura forte, 50-70% dos ativos (ex.: ABEV3). Atraente para conservadores.',
        'descotimo': 'Estrutura robusta, >70% dos ativos (ex.: WEGR3). Excelente, verificar alocação.'
    },
    'PL/Ativos': {
        'pessimo': {'min': float('-inf'), 'max': 0.2},  # Ajustado para incluir negativos
        'ruim': {'min': 0.2, 'max': 0.3},
        'moderado': {'min': 0.3, 'max': 0.5},
        'bom': {'min': 0.5, 'max': 0.7},
        'otimo': {'min': 0.7, 'max': float('inf')},
        'descricao': 'Relação entre patrimônio líquido e ativos totais. Indica solidez financeira.',
        'agrupador': 'Endividamento',
        'descrpessimo': 'Patrimônio muito baixo ou negativo, <20% dos ativos (ex.: OIBR3). Evitar.',
        'descrruim': 'Patrimônio limitado, 20-30% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Patrimônio equilibrado, 30-50% (ex.: ENGI11). Seguro.',
        'descrbom': 'Patrimônio forte, 50-70% (ex.: ABEV3). Atraente.',
        'descotimo': 'Patrimônio robusto, >70% (ex.: WEGR3). Excelente.'
    },
    'Dividend Yield (DY)': {
        'pessimo': {'min': 0, 'max': 0},
        'ruim': {'min': 0.1, 'max': 2},
        'moderado': {'min': 2, 'max': 4},
        'bom': {'min': 4, 'max': 6},
        'otimo': {'min': 6, 'max': float('inf')},
        'descricao': 'Rendimento de dividendos. Acima de 6% é considerado bom.',
        'agrupador': 'Renda',
        'descrpessimo': 'Sem dividendos, foco em reinvestimento ou prejuízo (ex.: startups). Evitar para renda.',
        'descrruim': 'Dividendos baixos, 0,1-2% (ex.: MGLU3). Pouco atrativo para renda.',
        'descrmoderado': 'Dividendos moderados, 2-4% (ex.: ENGI11). Equilíbrio entre renda e reinvestimento.',
        'descrbom': 'Dividendos atrativos, 4-6% (ex.: ITUB4). Ideal para renda.',
        'descotimo': 'Dividendos altos, >6% (ex.: TAEE11). Verificar sustentabilidade.'
    },
    'EV/EBIT': {
        'pessimo': {'min': 20, 'max': float('inf')},
        'ruim': {'min': 15, 'max': 20},
        'moderado': {'min': 10, 'max': 15},
        'bom': {'min': 5, 'max': 10},
        'otimo': {'min': float('-inf'), 'max': 5},  # Ajustado para incluir negativos
        'descricao': 'Relação entre valor da empresa e EBIT. Valores muito baixos ou negativos (EV negativo com EBIT positivo) sugerem subvalorização.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >20x (ex.: startups tech). Alto risco de supervalorização. Em 2025, com juros de 10-12%, evitar salvo crescimento excepcional.',
        'descrruim': 'Valuation alto, 15-20x (ex.: MGLU3). Cautela, verificar crescimento do EBIT.',
        'descrmoderado': 'Valuation razoável, 10-15x (ex.: ABEV3). Justo com EBIT estável.',
        'descrbom': 'Valuation atrativo, 5-10x (ex.: ITUB4). Ideal para investidores de valor.',
        'descotimo': 'Valuation extremamente atrativo, <5x ou negativo devido a EV negativo com EBIT positivo (ex.: VALE3 em recuperação). Oportunidade, verificar alocação de caixa.'
    },
    'EV/EBITDA': {
        'pessimo': {'min': 15, 'max': float('inf')},
        'ruim': {'min': 10, 'max': 15},
        'moderado': {'min': 7, 'max': 10},
        'bom': {'min': 4, 'max': 7},
        'otimo': {'min': float('-inf'), 'max': 4},  # Ajustado para incluir negativos
        'descricao': 'Relação entre valor da empresa e EBITDA. Valores muito baixos ou negativos (EV negativo com EBITDA positivo) sugerem subvalorização.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >15x (ex.: startups tech). Evitar, salvo crescimento excepcional.',
        'descrruim': 'Valuation alto, 10-15x (ex.: MGLU3). Cautela, verificar crescimento.',
        'descrmoderado': 'Valuation razoável, 7-10x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 4-7x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation extremamente atrativo, <4x ou negativo devido a EV negativo com EBITDA positivo (ex.: VALE3). Oportunidade, verificar alocação de caixa.'
    },
    'P/ATIVO': {
        'pessimo': {'min': 2, 'max': float('inf')},
        'ruim': {'min': 1.5, 'max': 2},
        'moderado': {'min': 1, 'max': 1.5},
        'bom': {'min': 0.5, 'max': 1},
        'otimo': {'min': 0, 'max': 0.5},
        'descricao': 'Relação entre preço e ativos totais. Indica valuation.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >2x (ex.: MGLU3). Evitar.',
        'descrruim': 'Valuation alto, 1,5-2x (ex.: startups). Cautela.',
        'descrmoderado': 'Valuation razoável, 1-1,5x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 0,5-1x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <0,5x (ex.: VALE3). Oportunidade.'
    },
    'P/Ativo Circulante Líquido': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 2, 'max': float('inf')},     # Ajustado para refletir alto valuation
        'moderado': {'min': 1, 'max': 2},
        'bom': {'min': 0.5, 'max': 1},
        'otimo': {'min': 0, 'max': 0.5},
        'descricao': 'Relação entre preço e ativo circulante líquido. Indica valuation e liquidez.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Ativo circulante líquido negativo ou valuation muito elevado (ex.: OIBR3). Evitar.',
        'descrruim': 'Valuation alto, >2x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 1-2x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 0,5-1x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <0,5x (ex.: VALE3). Oportunidade.'
    },
    'P/Capital de Giro': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 3, 'max': float('inf')},     # Ajustado para alto valuation
        'moderado': {'min': 1.5, 'max': 3},
        'bom': {'min': 0.5, 'max': 1.5},
        'otimo': {'min': 0, 'max': 0.5},
        'descricao': 'Relação entre preço e capital de giro. Indica valuation e eficiência.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Capital de giro negativo ou valuation muito elevado (ex.: OIBR3). Evitar.',
        'descrruim': 'Valuation alto, >3x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 1,5-3x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 0,5-1,5x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <0,5x (ex.: VALE3). Oportunidade.'
    },
    'P/EBIT': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 20, 'max': float('inf')},     # Ajustado para alto valuation
        'moderado': {'min': 15, 'max': 20},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 0, 'max': 10},
        'descricao': 'Relação entre preço e EBIT. Indica valuation operacional.',
        'agrupador': 'Valuation',
        'descrpessimo': 'EBIT negativo ou valuation elevado, >20x (ex.: OIBR3). Evitar.',
        'descrruim': 'Valuation alto, 20x+ (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 15-20x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 10-15x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <10x (ex.: VALE3). Oportunidade.'
    },
    'P/EBITDA': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 10, 'max': float('inf')},     # Ajustado para alto valuation
        'moderado': {'min': 7, 'max': 10},
        'bom': {'min': 4, 'max': 7},
        'otimo': {'min': 0, 'max': 4},
        'descricao': 'Relação entre preço e EBITDA. Indica valuation operacional.',
        'agrupador': 'Valuation',
        'descrpessimo': 'EBITDA negativo ou valuation elevado, >10x (ex.: OIBR3). Evitar.',
        'descrruim': 'Valuation alto, 10x+ (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 7-10x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 4-7x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <4x (ex.: VALE3). Oportunidade.'
    },
    'P/L': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 20, 'max': float('inf')},     # Ajustado para alto valuation
        'moderado': {'min': 15, 'max': 20},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 0, 'max': 10},
        'descricao': 'Relação entre preço e lucro líquido. Indica valuation.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Lucro negativo ou valuation elevado, >20x (ex.: OIBR3). Evitar.',
        'descrruim': 'Valuation alto, 20x+ (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 15-20x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 10-15x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <10x (ex.: VALE3). Oportunidade.'
    },
    'P/VPA': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 2, 'max': float('inf')},     # Ajustado para alto valuation
        'moderado': {'min': 1.5, 'max': 2},
        'bom': {'min': 1, 'max': 1.5},
        'otimo': {'min': 0, 'max': 1},
        'descricao': 'Relação entre preço e valor patrimonial por ação. Indica valuation.',
        'agrupador': 'Valuation',
        'descrpessimo': 'VPA negativo ou valuation elevado, >2x (ex.: OIBR3). Evitar.',
        'descrruim': 'Valuation alto, 2x+ (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 1,5-2x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 1-1,5x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <1x (ex.: VALE3). Oportunidade.'
    },
    'PSR': {
        'pessimo': {'min': 3, 'max': float('inf')},
        'ruim': {'min': 2, 'max': 3},
        'moderado': {'min': 1, 'max': 2},
        'bom': {'min': 0.5, 'max': 1},
        'otimo': {'min': 0, 'max': 0.5},
        'descricao': 'Relação entre preço e receita. Indica valuation em relação às vendas.',
        'agrupador': 'Valuation',
        'descrpessimo': 'Valuation elevado, >3x (ex.: startups). Evitar.',
        'descrruim': 'Valuation alto, 2-3x (ex.: MGLU3). Cautela.',
        'descrmoderado': 'Valuation razoável, 1-2x (ex.: ABEV3). Justo.',
        'descrbom': 'Valuation atrativo, 0,5-1x (ex.: ITUB4). Ideal.',
        'descotimo': 'Valuation muito atrativo, <0,5x (ex.: VALE3). Oportunidade.'
    },
    'Giro do Ativo': {
        'pessimo': {'min': 0, 'max': 0.5},
        'ruim': {'min': 0.5, 'max': 1},
        'moderado': {'min': 1, 'max': 1.5},
        'bom': {'min': 1.5, 'max': 2},
        'otimo': {'min': 2, 'max': float('inf')},
        'descricao': 'Eficiência na geração de receita por ativo. Indica produtividade.',
        'agrupador': 'Eficiência',
        'descrpessimo': 'Baixa eficiência, <0,5x (ex.: OIBR3). Evitar.',
        'descrruim': 'Eficiência limitada, 0,5-1x (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Eficiência razoável, 1-1,5x (ex.: ABEV3). Justo.',
        'descrbom': 'Alta eficiência, 1,5-2x (ex.: ITUB4). Ideal.',
        'descotimo': 'Eficiência excepcional, >2x (ex.: WEGR3). Atraente.'
    },
    'Liquidez Corrente': {
        'pessimo': {'min': 0, 'max': 1},
        'ruim': {'min': 1, 'max': 1.2},
        'moderado': {'min': 1.2, 'max': 1.5},
        'bom': {'min': 1.5, 'max': 2},
        'otimo': {'min': 2, 'max': float('inf')},
        'descricao': 'Capacidade de cobrir passivos de curto prazo com ativos circulantes.',
        'agrupador': 'Liquidez',
        'descrpessimo': 'Baixa liquidez, <1 (ex.: OIBR3). Evitar.',
        'descrruim': 'Liquidez limitada, 1-1,2 (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Liquidez razoável, 1,2-1,5 (ex.: ABEV3). Justo.',
        'descrbom': 'Boa liquidez, 1,5-2 (ex.: ITUB4). Ideal.',
        'descotimo': 'Liquidez excepcional, >2 (ex.: WEGR3). Atraente.'
    },
    'LPA': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 0.5},
        'moderado': {'min': 0.5, 'max': 1},
        'bom': {'min': 1, 'max': 2},
        'otimo': {'min': 2, 'max': float('inf')},
        'descricao': 'Lucro por ação. Indica rentabilidade por ação.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Prejuízo por ação (ex.: OIBR3). Evitar.',
        'descrruim': 'Lucro baixo, 0-0,5 (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Lucro razoável, 0,5-1 (ex.: ABEV3). Justo.',
        'descrbom': 'Lucro sólido, 1-2 (ex.: ITUB4). Ideal.',
        'descotimo': 'Lucro excepcional, >2 (ex.: WEGR3). Atraente.'
    },
    'Margem Bruta': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 0, 'max': 10},
        'moderado': {'min': 10, 'max': 20},
        'bom': {'min': 20, 'max': 30},
        'otimo': {'min': 30, 'max': float('inf')},
        'descricao': 'Percentual de lucro bruto sobre receita. Indica eficiência operacional.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Margem negativa ou muito baixa, <10% (ex.: OIBR3). Evitar.',
        'descrruim': 'Margem limitada, 10-20% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Margem razoável, 20-30% (ex.: ABEV3). Justo.',
        'descrbom': 'Margem sólida, 30-50% (ex.: ITUB4). Ideal.',
        'descotimo': 'Margem excepcional, >50% (ex.: WEGR3). Atraente.'
    },
    'Margem EBIT': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 0, 'max': 5},
        'moderado': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 15, 'max': float('inf')},
        'descricao': 'Percentual de lucro operacional sobre receita. Indica eficiência.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Margem negativa ou muito baixa, <5% (ex.: OIBR3). Evitar.',
        'descrruim': 'Margem limitada, 5-10% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Margem razoável, 10-15% (ex.: ABEV3). Justo.',
        'descrbom': 'Margem sólida, 15-25% (ex.: ITUB4). Ideal.',
        'descotimo': 'Margem excepcional, >25% (ex.: WEGR3). Atraente.'
    },
    'Margem EBITDA': {
        'pessimo': {'min': float('-inf'), 'max': 0},  # Ajustado para negativos
        'ruim': {'min': 0, 'max': 10},
        'moderado': {'min': 10, 'max': 15},
        'bom': {'min': 15, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Percentual de EBITDA sobre receita. Indica geração de caixa operacional.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Margem negativa ou muito baixa, <10% (ex.: OIBR3). Evitar.',
        'descrruim': 'Margem limitada, 10-15% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Margem razoável, 15-20% (ex.: ABEV3). Justo.',
        'descrbom': 'Margem sólida, 20-30% (ex.: ITUB4). Ideal.',
        'descotimo': 'Margem excepcional, >30% (ex.: WEGR3). Atraente.'
    },
    'Margem Líquida': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 5},
        'moderado': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Percentual de lucro líquido sobre receita. Indica rentabilidade final.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Prejuízo líquido, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Margem baixa, 0-5% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Margem razoável, 5-10% (ex.: ABEV3). Justo.',
        'descrbom': 'Margem sólida, 10-20% (ex.: ITUB4). Ideal.',
        'descotimo': 'Margem excepcional, >20% (ex.: WEGR3). Atraente.'
    },
    'ROA': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 5},
        'moderado': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 15, 'max': float('inf')},
        'descricao': 'Retorno sobre ativos. Indica eficiência na utilização dos ativos.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Retorno negativo, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Retorno baixo, 0-5% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Retorno razoável, 5-10% (ex.: ABEV3). Justo.',
        'descrbom': 'Retorno sólido, 10-15% (ex.: ITUB4). Ideal.',
        'descotimo': 'Retorno excepcional, >15% (ex.: WEGR3). Atraente.'
    },
    'ROE': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 10},
        'moderado': {'min': 10, 'max': 15},
        'bom': {'min': 15, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Retorno sobre patrimônio líquido. Indica rentabilidade para acionistas.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Retorno negativo, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Retorno baixo, 0-10% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Retorno razoável, 10-15% (ex.: ABEV3). Justo.',
        'descrbom': 'Retorno sólido, 15-20% (ex.: ITUB4). Ideal.',
        'descotimo': 'Retorno excepcional, >20% (ex.: WEGR3). Atraente.'
    },
    'CAGR Lucros 5 anos': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 5},
        'moderado': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 20},
        'otimo': {'min': 20, 'max': float('inf')},
        'descricao': 'Crescimento anual composto dos lucros em 5 anos. Indica tendência de crescimento.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Crescimento negativo, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Crescimento baixo, 0-5% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Crescimento razoável, 5-10% (ex.: ABEV3). Justo.',
        'descrbom': 'Crescimento sólido, 10-20% (ex.: ITUB4). Ideal.',
        'descotimo': 'Crescimento excepcional, >20% (ex.: WEGR3). Atraente.'
    },
    'ROIC': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 5},
        'moderado': {'min': 5, 'max': 10},
        'bom': {'min': 10, 'max': 15},
        'otimo': {'min': 15, 'max': float('inf')},
        'descricao': 'Retorno sobre capital investido. Indica eficiência do capital.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Retorno negativo, <0% (ex.: OIBR3). Evitar.',
        'descrruim': 'Retorno baixo, 0-5% (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Retorno razoável, 5-10% (ex.: ABEV3). Justo.',
        'descrbom': 'Retorno sólido, 10-15% (ex.: ITUB4). Ideal.',
        'descotimo': 'Retorno excepcional, >15% (ex.: WEGR3). Atraente.'
    },
    'VPA': {
        'pessimo': {'min': float('-inf'), 'max': 0},
        'ruim': {'min': 0, 'max': 1},
        'moderado': {'min': 1, 'max': 5},
        'bom': {'min': 5, 'max': 10},
        'otimo': {'min': 10, 'max': float('inf')},
        'descricao': 'Valor patrimonial por ação. Indica valor contábil por ação.',
        'agrupador': 'Rentabilidade',
        'descrpessimo': 'Valor patrimonial negativo (ex.: OIBR3). Evitar.',
        'descrruim': 'Valor patrimonial baixo, 0-1 (ex.: CSNA3). Cautela.',
        'descrmoderado': 'Valor patrimonial razoável, 1-5 (ex.: ABEV3). Justo.',
        'descrbom': 'Valor patrimonial sólido, 5-10 (ex.: ITUB4). Ideal.',
        'descotimo': 'Valor patrimonial excepcional, >10 (ex.: WEGR3). Atraente.'
    }
}
```
