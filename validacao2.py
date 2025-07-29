def classify_financial_metric(metric_name, value):
    """
    Classifica um valor financeiro com base nos intervalos definidos para cada métrica.

    Args:
        metric_name (str): Nome da métrica financeira (ex.: 'Div. liquida/EBIT')
        value (float): Valor da métrica a ser classificado

    Returns:
        dict: Dicionário com a classificação, descrição e descrição detalhada
    """
    # Dicionário com descrições e agrupadores
    metric_info = {
        'Div. liquida/EBIT': {
            'descricao': 'Dívida líquida dividida pelo EBIT. Mede tempo para quitar dívida com lucro operacional.',
            'agrupador': 'Eficiência'
        },
        'Div. liquida/EBITDA': {
            'descricao': 'Dívida líquida dividida pelo EBITDA. Mede tempo para quitar dívida com fluxo de caixa operacional.',
            'agrupador': 'Eficiência'
        },
        'Div. liquida/PL': {
            'descricao': 'Dívida líquida em relação ao patrimônio líquido. Mede alavancagem financeira.',
            'agrupador': 'Eficiência'
        },
        'D.Y': {
            'descricao': 'Dividendos pagos por ação em relação ao preço da ação. Mede retorno via dividendos.',
            'agrupador': 'Outros'
        },
        'EV/EBIT': {
            'descricao': 'Valor da empresa dividido pelo EBIT. Mede valuation em relação ao lucro operacional.',
            'agrupador': 'Valuation'
        },
        'EV/EBITDA': {
            'descricao': 'Valor da empresa dividido pelo EBITDA. Mede valuation em relação ao fluxo de caixa operacional.',
            'agrupador': 'Valuation'
        },
        'Giro do Ativo': {
            'descricao': 'Receita líquida dividida pelos ativos totais. Mede eficiência na utilização dos ativos.',
            'agrupador': 'Eficiência'
        },
        'Liq. corrente': {
            'descricao': 'Ativo circulante dividido pelo passivo circulante. Mede capacidade de pagar dívidas de curto prazo.',
            'agrupador': 'Liquidez e Solvência'
        },
        'LPA': {
            'descricao': 'Lucro líquido por ação. Mede rentabilidade por ação emitida.',
            'agrupador': 'Outros'
        },
        'M. Bruta': {
            'descricao': 'Lucro bruto dividido pela receita líquida. Mede eficiência na produção ou vendas.',
            'agrupador': 'Eficiência'
        },
        'M. EBIT': {
            'descricao': 'Lucro operacional dividido pela receita líquida. Mede rentabilidade antes de juros e impostos.',
            'agrupador': 'Eficiência'
        },
        'M. EBITDA': {
            'descricao': 'EBITDA dividido pela receita líquida. Mede geração de caixa operacional.',
            'agrupador': 'Eficiência'
        },
        'M. Liquida': {
            'descricao': 'Lucro líquido dividido pela receita líquida. Mede rentabilidade final após todas as despesas.',
            'agrupador': 'Eficiência'
        },
        'P/Ativo Circulante Líquido': {
            'descricao': 'Preço da ação dividido pelo ativo circulante líquido por ação. Mede valuation em relação à liquidez.',
            'agrupador': 'Liquidez e Solvência'
        },
        'P/Capital de Giro': {
            'descricao': 'Preço da ação dividido pelo capital de giro por ação. Mede valuation em relação à capacidade de financiar operações.',
            'agrupador': 'Liquidez e Solvência'
        },
        'P/EBIT': {
            'descricao': 'Preço da ação dividido pelo EBIT por ação. Mede valuation em relação ao lucro operacional.',
            'agrupador': 'Valuation'
        },
        'P/EBITDA': {
            'descricao': 'Preço da ação dividido pelo EBITDA por ação. Mede valuation em relação ao fluxo de caixa operacional.',
            'agrupador': 'Valuation'
        },
        'P/L': {
            'descricao': 'Preço da ação dividido pelo lucro por ação. Mede valuation em relação ao lucro líquido.',
            'agrupador': 'Valuation'
        },
        'P/VP': {
            'descricao': 'Preço da ação dividido pelo valor patrimonial por ação. Mede valuation em relação ao patrimônio.',
            'agrupador': 'Valuation'
        },
        'P/Ativo': {
            'descricao': 'Patrimônio líquido dividido pelos ativos totais. Mede proporção de ativos financiada por capital próprio.',
            'agrupador': 'Alavancagem Financeira'
        },
        'PL/Ativos': {
            'descricao': 'Patrimônio líquido dividido pelos ativos totais. Mede proporção de ativos financiada por capital próprio.',
            'agrupador': 'Eficiência'
        },
        'PSR': {
            'descricao': 'Valor de mercado dividido pela receita líquida. Mede valuation em relação às vendas.',
            'agrupador': 'Valuation'
        },
        'P/Sales Ratio': {
            'descricao': 'Valor de mercado dividido pela receita líquida. Mede valuation em relação às vendas.',
            'agrupador': 'Valuation'
        },
        'ROA': {
            'descricao': 'Lucro líquido dividido pelos ativos totais. Mede retorno sobre os ativos.',
            'agrupador': 'Retorno'
        },
        'ROE': {
            'descricao': 'Lucro líquido dividido pelo patrimônio líquido. Mede retorno sobre o capital dos acionistas.',
            'agrupador': 'Retorno'
        },
        'ROIC': {
            'descricao': 'Lucro operacional após impostos dividido pelo capital investido. Mede retorno sobre o capital total.',
            'agrupador': 'Retorno'
        },
        'VPA': {
            'descricao': 'Patrimônio líquido por ação. Mede valor contábil por ação.',
            'agrupador': 'Outros'
        },
        'CAGR Lucros 5 anos': {
            'descricao': 'Taxa composta de crescimento anual dos lucros nos últimos 5 anos. Mede crescimento de rentabilidade.',
            'agrupador': 'Outros'
        },
        'Divida bruta': {
            'descricao': 'Taxa composta de crescimento anual dos lucros nos últimos 5 anos. Mede crescimento de rentabilidade.',
            'agrupador': 'Outros'
        }
    }

    if metric_name not in metric_info:
        return {"error": "Métrica não encontrada"}

    # Classificação para 'Div. liquida/EBIT'
    if metric_name == 'Div. liquida/EBIT':
        if value < 0:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Caixa líquido supera dívida, refletindo forte saúde financeira. Comum em empresas de tecnologia ou com reservas elevadas (ex.: Nubank). Investidores devem investigar alocação do caixa (ex.: reinvestimento, dividendos) para evitar ineficiências.'
            }
        elif 0 <= value < 1.5:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento controlado, dívida quitável em menos de 1,5 anos de EBIT, indicando baixa alavancagem. Comum em empresas maduras com forte geração de caixa (ex.: Ambev). Sinal de estabilidade, mas deve-se avaliar subinvestimento.'
            }
        elif 1.5 <= value < 3:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento moderado, pagável em 1,5-3 anos de EBIT, aceitável em setores estáveis (ex.: utilities). Investidores devem verificar consistência do EBIT e fluxo de caixa livre para garantir que a alavancagem não comprometa a operação.'
            }
        elif 3 <= value < 4:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento elevado, leva 3-4 anos de EBIT para pagar a dívida, um nível alto para a maioria dos setores. Comum em setores intensivos em capital (ex.: infraestrutura). Investidores devem analisar cobertura de juros e estabilidade do EBIT para avaliar riscos em cenários adversos.'
            }
        elif 4 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento crítico, leva mais de 4 anos de EBIT para quitar a dívida líquida, indicando alavancagem extrema. Comum em empresas em crise ou setores cíclicos (ex.: construção). Aumenta vulnerabilidade a choques econômicos ou aumento de juros. Investidores devem evitar, salvo reestruturação robusta com forte geração de caixa futura.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Dívida líquida negativa pode indicar EBIT negativo (prejuízo operacional grave) ou excesso de caixa líquido. EBIT negativo, comum em empresas em crise (ex.: OI, OIBR3), reflete ineficiência operacional e risco de insolvência. Excesso de caixa, como em empresas de tecnologia (ex.: Nubank), pode indicar ineficiência na alocação de capital, com caixa ocioso não reinvestido. Em 2025, com juros altos, EBIT negativo agrava a pressão financeira. Investidores devem analisar a causa (EBIT negativo vs. caixa elevado) e evitar empresas sem plano claro de recuperação ou alocação eficiente.'
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
                'descricao_detalhada': 'Caixa líquido excede dívida, sugerindo forte geração de caixa ou reservas elevadas. Comum em setores de alto crescimento (ex.: tecnologia). Investidores devem verificar alocação do caixa para evitar ineficiências (ex.: caixa ocioso).'
            }
        elif 0 <= value < 1:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento baixo, dívida quitável rapidamente, indicando forte capacidade de pagamento. Comum em empresas com margens altas (ex.: Weg). Sinal positivo, mas deve-se avaliar se limita crescimento.'
            }
        elif 1 <= value < 2.5:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento moderado, pagável em 1-2,5 anos de EBITDA, aceitável em setores com investimentos moderados (ex.: varejo). Investidores devem monitorar tendência do EBITDA e gestão de dívidas para garantir sustentabilidade.'
            }
        elif 2.5 <= value < 3.5:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento elevado, leva 2,5-3,5 anos de EBITDA para pagar a dívida. Comum em setores cíclicos (ex.: commodities). Investidores devem analisar cobertura de juros, volatilidade do EBITDA e riscos macroeconômicos.'
            }
        elif 3.5 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Endividamento crítico, leva mais de 3,5 anos de EBITDA para quitar a dívida líquida, indicando alavancagem extrema. Aumenta vulnerabilidade a recessões ou aumento de juros. Investidores devem evitar, salvo recuperação clara com forte geração de caixa.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Prejuízo operacional, com incapacidade de gerar caixa operacional, indicando problemas estruturais graves. Comum em empresas em crise (ex.: OIBR3) ou setores com alta concorrência (ex.: varejo, CRFB3). Em 2025, com juros de 10-12%, a margem negativa agrava a pressão financeira, dificultando a cobertura de despesas. Riscos incluem insolvência, perda de market share ou aumento de custos fixos. Analise o fluxo de caixa operacional (FCO < 0 é preocupante) e a composição dos custos operacionais. Verifique balanços trimestrais e planos estratégicos para avaliar viabilidade. Setores cíclicos (ex.: construção, MRVE3) podem ter margens negativas temporariamente, mas exigem recuperação clara. Compare com peers (ex.: varejo ~10%) para avaliar gravidade. Evite empresas com EBITDA negativo recorrente ou sem estratégia definida. Oportunidades surgem em reestruturações robustas com potencial de turnaround.'
            }

    # Classificação para 'Div. liquida/PL'
    if metric_name == 'Div. liquida/PL':
        if value < 0:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Caixa líquido excede dívida, indicando altíssima capitalização. Comum em empresas com reservas elevadas (ex.: Weg). Investidores devem verificar alocação do caixa para evitar ineficiências.'
            }
        elif 0 <= value < 0.3:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Baixa alavancagem, estrutura financeira sólida, indicando empresa bem capitalizada. Comum em setores estáveis (ex.: utilities). Sinal de segurança, mas deve-se avaliar se a baixa dívida limita crescimento.'
            }
        elif 0.3 <= value < 0.7:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Alavancagem moderada, dívida é 30-70% do patrimônio líquido, aceitável em setores como indústria. Investidores devem monitorar cobertura de juros e estabilidade do fluxo de caixa para garantir solvência.'
            }
        elif 0.7 <= value < 1:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Alavancagem elevada, dívida representa 70-100% do patrimônio líquido, um nível alto para a maioria dos setores. Investidores devem analisar capacidade de geração de lucro e prazos da dívida para avaliar sustentabilidade financeira.'
            }
        elif 1 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Alavancagem crítica, dívida líquida excede o patrimônio líquido, indicando dependência extrema de financiamento externo. Comum em empresas em crise (ex.: OI). Investidores devem evitar, salvo reestruturação com forte potencial de recuperação.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Patrimônio líquido negativo, passivos superam ativos, indicando risco crítico de insolvência. Comum em empresas em crise (ex.: OI). Investidores devem exigir plano robusto de recuperação.'
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
                'descricao_detalhada': 'Alto retorno, muito atrativo, mas pode indicar risco de insustentabilidade, especialmente com lucros voláteis. Investidores devem analisar payout ratio e geração de caixa para garantir continuidade dos dividendos.'
            }
        elif 0.04 <= value < 0.06:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Retorno atrativo, bom para investidores de renda. Comum em setores como utilities e bancos (ex.: Engie). Investidores devem confirmar sustentabilidade do fluxo de caixa livre e política de dividendos.'
            }
        elif 0.02 <= value < 0.04:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Retorno moderado, oferece equilíbrio entre dividendos e reinvestimento. Comum em empresas maduras (ex.: Ambev). Investidores devem verificar sustentabilidade do payout e consistência dos lucros.'
            }
        elif 0.001 <= value < 0.02:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Retorno baixo, pouco atrativo para investidores de dividendos. Comum em empresas de crescimento (ex.: Nubank). Investidores devem focar no potencial de valorização das ações em vez de dividendos.'
            }
        elif value == 0:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Sem pagamento de dividendos, indicando reinvestimento total dos lucros (ex.: startups) ou prejuízo financeiro. Investidores focados em renda devem evitar, mas podem considerar se o foco é crescimento de longo prazo.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Sem pagamento de dividendos, indicando reinvestimento total dos lucros (ex.: startups) ou prejuízo financeiro. Investidores focados em renda devem evitar, mas podem considerar se o foco é crescimento de longo prazo.'
            }

    # Classificação para 'EV/EBIT'
    if metric_name == 'EV/EBIT':
        if 0 <= value < 4:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Extremamente subvalorizada, EV muito baixo em relação ao EBIT, sugerindo oportunidade ou EBIT inflado. Investidores devem verificar fluxo de caixa livre e sustentabilidade do EBIT para confirmar oportunidade.'
            }
        elif 4 <= value < 8:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Subvalorizada, EV abaixo de 8x o EBIT indica empresa barata, com potencial de valorização. Comum em setores cíclicos em recuperação (ex.: mineração). Investidores devem confirmar fluxo de caixa livre e tendências setoriais.'
            }
        elif 8 <= value < 12:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Avaliação razoável, equilibrada para empresas maduras com crescimento moderado (ex.: indústria). Investidores devem verificar consistência do EBIT e perspectivas de crescimento para confirmar atratividade.'
            }
        elif 12 <= value < 15:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa cara, múltiplo elevado, comum em setores de crescimento (ex.: saúde). Investidores devem analisar se o crescimento futuro justifica o preço e comparar com média setorial para evitar sobrepreço.'
            }
        elif 15 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa extremamente cara, EV é mais de 15 vezes o EBIT, sugerindo expectativas irreais de crescimento ou sobrevalorização. Comum em setores de tecnologia em bolha. Investidores devem comparar com peers e avaliar crescimento projetado.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Prejuízo operacional, com operação não rentável, indicando ineficiência grave ou investimentos pesados. Comum em empresas em crise (ex.: OIBR3) ou setores com alta concorrência (ex.: varejo, CRFB3). Em 2025, com juros de 10-12%, a margem negativa agrava a pressão financeira, dificultando a cobertura de despesas. Riscos incluem insolvência, perda de market share ou aumento de custos fixos. Analise o fluxo de caixa operacional (FCO < 0 é preocupante) e a composição dos custos operacionais. Verifique balanços trimestrais e planos estratégicos para avaliar viabilidade. Setores cíclicos (ex.: construção, MRVE3) podem ter margens negativas temporariamente, mas exigem recuperação clara. Compare com peers (ex.: varejo ~5%) para avaliar gravidade. Evite empresas com EBIT negativo recorrente ou sem estratégia definida. Oportunidades surgem em reestruturações robustas com potencial de turnaround.'
            }

    # Classificação para 'EV/EBITDA'
    if metric_name == 'EV/EBITDA':
        if 0 <= value < 3:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Extremamente subvalorizada, sugere oportunidade ou EBITDA inflado. Investidores devem verificar fluxo de caixa livre e sustentabilidade do EBITDA.'
            }
        elif 3 <= value < 6:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Subvalorizada, oportunidade em setores cíclicos (ex.: mineração). Investidores devem confirmar fluxo de caixa livre e tendências setoriais.'
            }
        elif 6 <= value < 10:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Avaliação equilibrada, comum em setores maduros (ex.: varejo). Investidores devem verificar consistência do EBITDA e perspectivas de crescimento.'
            }
        elif 10 <= value < 12:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa cara, comum em setores de crescimento (ex.: saúde). Investidores devem analisar se o crescimento futuro justifica o preço e comparar com média setorial.'
            }
        elif 12 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa extremamente cara, EV é mais de 12 vezes o EBITDA, sugerindo sobrevalorização. Comum em setores de tecnologia (ex.: Nubank). Investidores devem comparar com peers e avaliar crescimento projetado.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Prejuízo operacional, com incapacidade de gerar caixa operacional, indicando problemas estruturais graves. Comum em empresas em crise (ex.: OIBR3) ou setores com alta concorrência (ex.: varejo, CRFB3). Em 2025, com juros de 10-12%, a margem negativa agrava a pressão financeira, dificultando a cobertura de despesas. Riscos incluem insolvência, perda de market share ou aumento de custos fixos. Analise o fluxo de caixa operacional (FCO < 0 é preocupante) e a composição dos custos operacionais. Verifique balanços trimestrais e planos estratégicos para avaliar viabilidade. Setores cíclicos (ex.: construção, MRVE3) podem ter margens negativas temporariamente, mas exigem recuperação clara. Compare com peers (ex.: varejo ~10%) para avaliar gravidade. Evite empresas com EBITDA negativo recorrente ou sem estratégia definida. Oportunidades surgem em reestruturações robustas com potencial de turnaround.'
            }

    # Classificação para 'Giro do Ativo'
    if metric_name == 'Giro do Ativo':
        if 1.2 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Alta eficiência, excelente utilização dos ativos, comum em setores dinâmicos (ex.: MGLU3). Investidores devem verificar consistência frente a riscos setoriais.'
            }
        elif 0.8 <= value < 1.2:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Boa eficiência, ativos bem utilizados, comum em varejo (ex.: LREN3). Investidores devem confirmar sustentabilidade da receita.'
            }
        elif 0.4 <= value < 0.8:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Eficiência moderada, aceitável em setores industriais (ex.: CSNA3). Investidores devem analisar tendência da receita e composição dos ativos.'
            }
        elif 0.2 <= value < 0.4:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Eficiência limitada, comum em setores cíclicos (ex.: GGBR4). Investidores devem investigar potencial de melhoria operacional e aumento de vendas.'
            }
        elif 0 <= value < 0.2:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Baixa eficiência, ativos subutilizados, comum em empresas em crise (ex.: OIBR3) ou setores em baixa (ex.: siderurgia). Investidores devem verificar composição dos ativos e fluxo de caixa operacional.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Receita negativa ou ativos mal contabilizados, indicando problemas estruturais graves ou falha contábil. Comum em empresas em crise severa (ex.: OIBR3). Investidores devem evitar, salvo recuperação robusta com plano claro de reestruturação.'
            }

    # Classificação para 'Liq. corrente'
    if metric_name == 'Liq. corrente':
        if 2.5 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Alta liquidez, forte capacidade de pagamento, mas pode indicar caixa ocioso. Comum em tecnologia (ex.: TOTS3). Investidores devem avaliar alocação de capital.'
            }
        elif 1.8 <= value < 2.5:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Boa liquidez, capacidade sólida de cobrir obrigações de curto prazo. Comum em empresas maduras (ex.: WEGE3). Investidores devem confirmar sustentabilidade do fluxo de caixa.'
            }
        elif 1.2 <= value < 1.8:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Liquidez razoável, aceitável em setores estáveis (ex.: ABEV3). Investidores devem verificar qualidade dos ativos circulantes (ex.: estoques, recebíveis).'
            }
        elif 0.8 <= value < 1.2:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Liquidez limitada, risco moderado de dificuldades financeiras. Investidores devem analisar composição do ativo circulante e fluxo de caixa operacional.'
            }
        elif 0 <= value < 0.8:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Incapacidade de cobrir obrigações de curto prazo, indicando risco de insolvência. Comum em empresas em crise (ex.: OIBR3). Investidores devem evitar, salvo reestruturação robusta.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Passivo circulante excede ativo circulante de forma crítica, indicando insolvência iminente. Comum em empresas em crise severa (ex.: OIBR3). Investidores devem evitar, salvo plano robusto de recuperação.'
            }

    # Classificação para 'LPA'
    if metric_name == 'LPA':
        if 2 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Lucro excepcional, refletindo forte rentabilidade. Comum em setores de alta margem (ex.: tecnologia). Investidores devem verificar sustentabilidade frente a riscos setoriais.'
            }
        elif 1 <= value < 2:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Bom lucro por ação, desempenho sólido, comum em setores estáveis (ex.: bancos). Investidores devem confirmar consistência do lucro.'
            }
        elif 0.5 <= value < 1:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Lucro moderado, desempenho razoável, aceitável em setores maduros (ex.: indústria). Investidores devem verificar sustentabilidade do lucro.'
            }
        elif 0.1 <= value < 0.5:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Lucro baixo, desempenho fraco, comum em empresas em crescimento ou setores cíclicos. Investidores devem analisar tendência do lucro e riscos setoriais.'
            }
        elif 0 <= value < 0.1:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Lucro por ação muito baixo, indicando rentabilidade limitada. Comum em setores competitivos (ex.: varejo). Investidores devem investigar potencial de melhoria.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Prejuízo por ação, indicando problemas operacionais ou financeiros graves. Comum em empresas em crise ou com investimentos pesados (ex.: OI). Investidores devem analisar plano de recuperação.'
            }

    # Classificação para 'M. Bruta'
    if metric_name == 'M. Bruta':
        if 0.6 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Alta margem, desempenho excepcional, comum em setores de alto valor agregado (ex.: tecnologia, TOTS3). Investidores devem verificar proteção contra concorrência.'
            }
        elif 0.4 <= value < 0.6:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Boa margem, indicando eficiência sólida. Comum em setores com barreiras de entrada (ex.: ABEV3). Investidores devem confirmar consistência da margem.'
            }
        elif 0.25 <= value < 0.4:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Margem razoável, aceitável em setores industriais (ex.: CSNA3). Investidores devem verificar sustentabilidade da margem e poder de precificação.'
            }
        elif 0.15 <= value < 0.25:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Margem limitada, comum em setores com alta concorrência (ex.: CRFB3). Investidores devem investigar estratégias de diferenciação ou redução de custos.'
            }
        elif 0 <= value < 0.15:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Baixa margem, indicando ineficiência na produção ou vendas. Comum em setores competitivos (ex.: varejo, MGLU3). Investidores devem analisar composição dos custos e potencial de melhoria.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Custo dos produtos vendidos excede a receita, indicando ineficiência grave ou preços insustentáveis. Comum em empresas em crise (ex.: OIBR3) ou setores com alta concorrência (ex.: varejo, CRFB3). Investidores devem evitar, salvo plano robusto de recuperação.'
            }

    # Classificação para 'M. EBIT'
    if metric_name == 'M. EBIT':
        if 0.35 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Alta rentabilidade operacional, desempenho excepcional, comum em setores de alta margem (ex.: tecnologia, TOTS3). Investidores devem verificar proteção contra concorrência e sustentabilidade.'
            }
        elif 0.25 <= value < 0.35:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Boa rentabilidade operacional, desempenho sólido, comum em setores com barreiras de entrada (ex.: utilities, CPFE3). Investidores devem confirmar consistência do EBIT.'
            }
        elif 0.15 <= value < 0.25:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Rentabilidade moderada, desempenho razoável, aceitável em setores com margens moderadas (ex.: varejo, LREN3). Investidores devem analisar sustentabilidade do EBIT e concorrência.'
            }
        elif 0.05 <= value < 0.15:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Rentabilidade operacional limitada, comum em setores com margens moderadas (ex.: indústria, GGBR4). Investidores devem verificar tendência do EBIT e riscos setoriais.'
            }
        elif 0 <= value < 0.05:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Baixa rentabilidade operacional, indicando eficiência limitada. Comum em setores competitivos ou cíclicos (ex.: varejo, MGLU3). Investidores devem analisar potencial de melhoria operacional e redução de custos.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Prejuízo operacional, com operação não rentável, indicando ineficiência grave ou investimentos pesados. Comum em empresas em crise (ex.: OIBR3) ou setores com alta concorrência (ex.: varejo, CRFB3). Em 2025, com juros de 10-12%, a margem negativa agrava a pressão financeira, dificultando a cobertura de despesas. Riscos incluem insolvência, perda de market share ou aumento de custos fixos. Analise o fluxo de caixa operacional (FCO < 0 é preocupante) e a composição dos custos operacionais. Verifique balanços trimestrais e planos estratégicos para avaliar viabilidade. Setores cíclicos (ex.: construção, MRVE3) podem ter margens negativas temporariamente, mas exigem recuperação clara. Compare com peers (ex.: varejo ~5%) para avaliar gravidade. Evite empresas com EBIT negativo recorrente ou sem estratégia definida. Oportunidades surgem em reestruturações robustas com potencial de turnaround.'
            }

    # Classificação para 'M. EBITDA'
    if metric_name == 'M. EBITDA':
        if 0.4 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Geração de caixa excepcional, refletindo liderança de mercado e eficiência superior. Comum em setores de alto valor agregado (ex.: Weg). Investidores devem verificar sustentabilidade frente a riscos setoriais.'
            }
        elif 0.3 <= value < 0.4:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Alta geração de caixa, desempenho excepcional, comum em setores de alta margem (ex.: tecnologia, TOTS3). Investidores devem confirmar sustentabilidade e proteção contra concorrência.'
            }
        elif 0.2 <= value < 0.3:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Boa geração de caixa, desempenho sólido, comum em setores com barreiras de entrada (ex.: utilities, CPFE3). Investidores devem verificar consistência do EBITDA e poder de precificação.'
            }
        elif 0.1 <= value < 0.2:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Geração de caixa moderada, com desempenho razoável, aceitável em setores com margens moderadas (ex.: varejo, LREN3). Em 2025, essa faixa reflete capacidade de cobrir custos operacionais, mas exige análise de pressão competitiva e custos fixos. Investidores devem comparar com peers (ex.: varejo ~15%) e avaliar a sustentabilidade do EBITDA (ex.: variação < 15% em 5 anos). Setores estáveis (ex.: consumo defensivo, ABEV3) são menos arriscados, mas empresas cíclicas (ex.: GGBR4) podem enfrentar volatilidade. Oportunidades surgem em empresas com melhoria operacional, como automação ou expansão de mercado. Riscos incluem aumento de custos ou queda de demanda. Analise o fluxo de caixa livre (FCL > CAPEX) e a composição dos custos operacionais. Verifique balanços trimestrais e tendências setoriais (ex.: consumo estável). Evite empresas com EBITDA instável ou dependência de receitas cíclicas. Analise o ROIC (> 8%) para confirmar eficiência. Setores com barreiras de entrada (ex.: marcas fortes) se destacam.'
            }
        elif 0 <= value < 0.1:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Baixa geração de caixa, com eficiência limitada, comum em setores intensivos em capital (ex.: infraestrutura, CMIG4). Em 2025, com custos elevados, essa faixa indica desafios para melhorar a eficiência sem aumento de preços ou redução de custos fixos. Investidores devem investigar o potencial de melhoria operacional (ex.: automação, corte de despesas) e o poder de precificação. Riscos incluem concorrência agressiva, aumento de insumos ou queda de demanda. Oportunidades surgem em empresas com estratégias de diferenciação (ex.: marcas fortes para LREN3). Analise o fluxo de caixa livre (FCL > 0) e a tendência do EBITDA nos últimos 3 anos. Compare com peers (ex.: varejo ~15%) para avaliar competitividade. Verifique balanços trimestrais e tendências setoriais (ex.: e-commerce). Evite empresas com EBITDA declinante ou dependência de promoções. Analise o ROIC (> 5%) e o CAPEX para confirmar potencial de melhoria. Setores competitivos exigem cautela extra.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Prejuízo operacional, com incapacidade de gerar caixa operacional, indicando problemas estruturais graves. Comum em empresas em crise (ex.: OIBR3) ou setores com alta concorrência (ex.: varejo, CRFB3). Em 2025, com juros de 10-12%, a margem negativa agrava a pressão financeira, dificultando a cobertura de despesas. Riscos incluem insolvência, perda de market share ou aumento de custos fixos. Analise o fluxo de caixa operacional (FCO < 0 é preocupante) e a composição dos custos operacionais. Verifique balanços trimestrais e planos estratégicos para avaliar viabilidade. Setores cíclicos (ex.: construção, MRVE3) podem ter margens negativas temporariamente, mas exigem recuperação clara. Compare com peers (ex.: varejo ~10%) para avaliar gravidade. Evite empresas com EBITDA negativo recorrente ou sem estratégia definida. Oportunidades surgem em reestruturações robustas com potencial de turnaround.'
            }

    # Classificação para 'M. Liquida'
    if metric_name == 'M. Liquida':
        if 0.25 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Alta rentabilidade, desempenho excepcional, comum em setores de alta margem (ex.: tecnologia, TOTS3). Investidores devem verificar sustentabilidade frente a riscos setoriais.'
            }
        elif 0.15 <= value < 0.25:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Boa rentabilidade, desempenho sólido, comum em setores com barreiras de entrada (ex.: ABEV3). Investidores devem confirmar consistência do lucro líquido.'
            }
        elif 0.1 <= value < 0.15:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Rentabilidade moderada, aceitável em setores maduros (ex.: indústria, CSNA3). Investidores devem analisar sustentabilidade do lucro e concorrência.'
            }
        elif 0.05 <= value < 0.1:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Rentabilidade limitada, comum em setores cíclicos (ex.: siderurgia, GGBR4). Investidores devem verificar tendência do lucro líquido e riscos setoriais.'
            }
        elif 0 <= value < 0.05:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Baixa rentabilidade, indicando desafios operacionais ou financeiros. Comum em setores competitivos (ex.: varejo, MGLU3). Investidores devem analisar potencial de melhoria e redução de custos.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Prejuízo líquido, indicando ineficiência operacional ou financeira grave. Comum em empresas em crise (ex.: OIBR3) ou setores com alta concorrência (ex.: varejo, CRFB3). Investidores devem evitar, salvo plano robusto de recuperação.'
            }

    # Classificação para 'P/Ativo Circulante Líquido'
    if metric_name == 'P/Ativo Circulante Líquido':
        if 3 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Alta liquidez em relação ao preço, sugerindo subvalorização ou excesso de caixa. Comum em tecnologia (ex.: TOTS3). Investidores devem avaliar alocação de capital.'
            }
        elif 2 <= value < 3:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Boa liquidez em relação ao preço, indicando equilíbrio financeiro. Comum em empresas maduras (ex.: WEGE3). Investidores devem confirmar sustentabilidade.'
            }
        elif 1 <= value < 2:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Liquidez razoável em relação ao preço, aceitável em setores estáveis (ex.: ABEV3). Investidores devem verificar qualidade dos ativos circulantes.'
            }
        elif 0 <= value < 1:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Liquidez muito baixa em relação ao preço da ação, indicando risco financeiro. Investidores devem analisar qualidade do ativo circulante e fluxo de caixa.'
            }
        elif value == 0:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Preço da ação não reflete liquidez, indicando passivos elevados. Comum em empresas em crise (ex.: OIBR3). Investidores devem evitar, salvo reestruturação robusta.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Ativo circulante líquido negativo (passivo circulante excede ativo circulante), indicando risco crítico de insolvência. Comum em empresas em crise (ex.: OIBR3). Investidores devem evitar, salvo plano robusto de recuperação.'
            }

    # Classificação para 'P/Capital de Giro'
    if metric_name == 'P/Capital de Giro':
        if 6 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Alta capacidade de financiar operações, sugerindo subvalorização ou excesso de caixa. Comum em tecnologia (ex.: TOTS3). Investidores devem avaliar alocação de capital.'
            }
        elif 4 <= value < 6:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Boa capacidade de financiar operações, indicando equilíbrio financeiro. Comum em empresas maduras (ex.: LREN3). Investidores devem confirmar sustentabilidade.'
            }
        elif 2 <= value < 4:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Capacidade moderada de financiar operações, aceitável em setores estáveis (ex.: ABEV3). Investidores devem verificar qualidade do ativo circulante.'
            }
        elif 0 <= value < 2:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Baixa capacidade de financiar operações de curto prazo em relação ao preço. Investidores devem analisar qualidade do capital de giro e fluxo de caixa.'
            }
        elif value == 0:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Preço da ação não reflete capital de giro, indicando passivos elevados. Comum em empresas em crise (ex.: OIBR3). Investidores devem evitar, salvo reestruturação robusta.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Capital de giro negativo (ativo circulante menor que passivo circulante), indicando risco crítico de insolvência. Comum em empresas em crise (ex.: OIBR3). Investidores devem evitar, salvo plano robusto de recuperação.'
            }

    # Classificação para 'P/EBIT'
    if metric_name == 'P/EBIT':
        if 0 <= value < 5:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Extremamente subvalorizada, sugere oportunidade ou EBIT inflado. Comum em setores em recuperação (ex.: PETR4). Investidores devem verificar fluxo de caixa livre e ROIC.'
            }
        elif 5 <= value < 10:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Subvalorizada, oportunidade em setores cíclicos (ex.: mineração, VALE3). Investidores devem confirmar fluxo de caixa livre e sustentabilidade do EBIT.'
            }
        elif 10 <= value < 15:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Avaliação razoável, comum em setores maduros (ex.: varejo, LREN3). Investidores devem verificar consistência do EBIT e tendências setoriais.'
            }
        elif 15 <= value < 20:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa cara, comum em setores de crescimento (ex.: saúde, RDOR3). Investidores devem analisar se o crescimento justifica o preço e comparar com média setorial.'
            }
        elif 20 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa extremamente cara, preço é mais de 20 vezes o EBIT, sugerindo sobrevalorização. Comum em setores de tecnologia (ex.: NUBR33). Investidores devem comparar com peers e avaliar crescimento projetado.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Prejuízo operacional, com EBIT negativo, indicando ineficiência grave ou investimentos pesados. Comum em empresas em crise (ex.: OIBR3). Investidores devem evitar, salvo plano robusto de recuperação.'
            }

    # Classificação para 'P/EBITDA'
    if metric_name == 'P/EBITDA':
        if 0 <= value < 3:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Extremamente subvalorizada, sugere oportunidade ou EBITDA inflado. Comum em setores em recuperação (ex.: PETR4). Investidores devem verificar fluxo de caixa livre e ROIC.'
            }
        elif 3 <= value < 6:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Subvalorizada, oportunidade em setores cíclicos (ex.: mineração, VALE3). Investidores devem confirmar fluxo de caixa livre e sustentabilidade do EBITDA.'
            }
        elif 6 <= value < 10:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Avaliação razoável, comum em setores maduros (ex.: varejo, LREN3). Investidores devem verificar consistência do EBITDA e tendências setoriais.'
            }
        elif 10 <= value < 15:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa cara, comum em setores de crescimento (ex.: saúde, RDOR3). Investidores devem analisar se o crescimento justifica o preço e comparar com média setorial.'
            }
        elif 15 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa extremamente cara, preço é mais de 15 vezes o EBITDA, sugerindo sobrevalorização. Comum em setores de tecnologia (ex.: NUBR33). Investidores devem comparar com peers e avaliar crescimento projetado.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Prejuízo operacional, com EBITDA negativo, indicando ineficiência grave ou problemas estruturais. Comum em empresas em crise (ex.: OIBR3). Investidores devem evitar, salvo plano robusto de recuperação.'
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
                'descricao_detalhada': 'Extremamente subvalorizada, sugere oportunidade ou lucro inflado. Comum em setores em recuperação (ex.: PETR4). Investidores devem verificar fluxo de caixa livre e ROE.'
            }
        elif 5 <= value < 10:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Subvalorizada, oportunidade em setores cíclicos (ex.: mineração, VALE3). Investidores devem confirmar fluxo de caixa livre e sustentabilidade do lucro.'
            }
        elif 10 <= value < 15:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Avaliação razoável, comum em setores maduros (ex.: varejo, LREN3). Investidores devem verificar consistência do lucro e tendências setoriais.'
            }
        elif 15 <= value < 20:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa cara, comum em setores de crescimento (ex.: saúde, RDOR3). Investidores devem analisar se o crescimento justifica o preço e comparar com média setorial.'
            }
        elif 20 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa extremamente cara, preço é mais de 20 vezes o lucro por ação, sugerindo sobrevalorização. Comum em setores de tecnologia (ex.: NUBR33). Investidores devem comparar com peers e avaliar crescimento projetado.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Prejuízo por ação, indicando problemas operacionais ou financeiros graves. Comum em empresas em crise (ex.: OIBR3). Investidores devem evitar, salvo plano robusto de recuperação.'
            }

    # Classificação para 'P/VP'
    if metric_name == 'P/VP':
        if 0 <= value < 0.5:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Extremamente subvalorizada, sugere oportunidade ou patrimônio inflado. Comum em setores em recuperação (ex.: PETR4). Investidores devem verificar fluxo de caixa livre e ROE.'
            }
        elif 0.5 <= value < 1:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'bom',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Subvalorizada, oportunidade em setores cíclicos (ex.: mineração, VALE3). Investidores devem confirmar qualidade do patrimônio e fluxo de caixa livre.'
            }
        elif 1 <= value < 1.5:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'moderado',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Avaliação razoável, comum em setores maduros (ex.: varejo, LREN3). Investidores devem verificar consistência do patrimônio e tendências setoriais.'
            }
        elif 1.5 <= value < 2:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'ruim',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa cara, comum em setores de crescimento (ex.: saúde, RDOR3). Investidores devem analisar se o crescimento justifica o preço e comparar com média setorial.'
            }
        elif 2 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'pessimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Empresa extremamente cara, preço é mais de 2 vezes o valor patrimonial por ação, sugerindo sobrevalorização. Comum em setores de tecnologia (ex.: NUBR33). Investidores devem comparar com peers e avaliar qualidade do patrimônio.'
            }
        else:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'critico',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],
                'descricao_detalhada': 'Patrimônio líquido por ação negativo, indicando risco crítico de insolvência. Comum em empresas em crise (ex.: OIBR3). Investidores devem evitar, salvo plano robusto de recuperação.'
            }

    # Classificação para 'P/Ativo'
    if metric_name == 'P/Ativo':
        if 0.8 <= value:
            return {
                'metrica': metric_name,
                'valor': value,
                'classificacao': 'otimo',
                'descricao': metric_info[metric_name]['descricao'],
                'agrupador': metric_info[metric_name]['agrupador'],