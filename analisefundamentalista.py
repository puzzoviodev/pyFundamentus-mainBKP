def evaluate_pl(PL):
    '''Avalia o Preço/Lucro (P/L) com base em faixas definidas para o mercado brasileiro:
    - P/L < 0: Crítico (prejuízo, risco elevado)
    - 0 ≤ P/L ≤ 10: Ótimo (subvalorizado, oportunidade de compra)
    - 10 < P/L ≤ 15: Moderado (valuation justo, crescimento moderado)
    - 15 < P/L ≤ 20: Ruim (sobrevalorizado, cautela necessária)
    - 20 < P/L ≤ 30: Péssimo (muito caro, alto risco)
    - P/L > 30: Fora da faixa (extremamente sobrevalorizado, risco elevado)'''
    definicao = '''Indicador que relaciona o preço da ação ao lucro por ação, medindo quantos anos seriam necessários para recuperar o investimento com base nos lucros atuais. É amplamente usado para avaliar se uma ação está cara ou barata em relação aos lucros gerados.'''
    agrupador = 'Valuation'
    formula = 'P/L = Preço da Ação / Lucro por Ação'
    try:
        if PL < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'PL < 0',
                'descricao': 'P/L negativo indica que a empresa está com prejuízo, sugerindo riscos como problemas operacionais, má gestão ou dificuldades de mercado. Pode ser temporário em setores cíclicos (ex.: celulose, mineração), mas exige análise de fundamentos como EBITDA e fluxo de caixa para avaliar recuperação.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= PL <= 10:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= PL <= 10',
                'descricao': 'P/L baixo sugere que a ação está subvalorizada ou que o mercado tem perspectiva negativa sobre o futuro da empresa. Comum em setores maduros (ex.: bancos, utilities) ou em empresas com desafios financeiros temporários. Pode representar uma oportunidade de valor se o mercado estiver subestimando o potencial de recuperação.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < PL <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '10 < PL <= 15',
                'descricao': 'P/L indica valuation justo, típico de empresas com crescimento estável e fundamentos sólidos. Comum em setores consolidados com margens previsíveis (ex.: varejo, energia). Menos potencial de upside que ações subvalorizadas, mas oferece equilíbrio entre risco e retorno.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < PL <= 20:
            return {
                'classificacao': 'Ruim',
                'faixa': '15 < PL <= 20',
                'descricao': 'P/L elevado sugere sobrevalorização moderada, indicando que o mercado espera crescimento, mas com riscos crescentes. Pode ser justificado em setores dinâmicos (ex.: varejo tech), mas exige análise de perspectivas de lucro e comparação com pares do setor.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < PL <= 30:
            return {
                'classificacao': 'Pessimo',
                'faixa': '20 < PL <= 30',
                'descricao': 'P/L muito alto indica que a ação está cara, com expectativas de crescimento elevadas que podem não se concretizar. Comum em setores de alto crescimento (ex.: tecnologia), mas há risco significativo de correção se os resultados desapontarem.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # PL > 30
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'PL > 30',
                'descricao': 'P/L extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas de mercado. Pode ser aceitável em setores de crescimento excepcional (ex.: tecnologia, biotech), mas o risco de correção é alto. Análise detalhada do crescimento futuro é essencial.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar P/L: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_pebitda(pebitda):
    '''Avalia o Preço/EBITDA com base em faixas definidas para o mercado brasileiro:
    - P/EBITDA < 0: Crítico (EBITDA negativo, risco elevado)
    - 0 ≤ P/EBITDA ≤ 4: Ótimo (subvalorizado, oportunidade de compra)
    - 4 < P/EBITDA ≤ 7: Moderado (valuation justo, crescimento moderado)
    - 7 < P/EBITDA ≤ 10: Ruim (sobrevalorizado, cautela necessária)
    - 10 < P/EBITDA ≤ 15: Péssimo (muito caro, alto risco)
    - P/EBITDA > 15: Fora da faixa (extremamente sobrevalorizado, risco elevado)'''
    definicao = '''Indicador que relaciona o preço da ação ao EBITDA, medindo a capacidade da empresa de gerar caixa operacional em relação ao seu valor de mercado. É útil para comparar empresas independentemente de sua estrutura de capital.'''
    agrupador = 'Valuation'
    formula = 'P/EBITDA = Preço da Ação / EBITDA por Ação'
    try:
        if pebitda < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'P/EBITDA < 0',
                'descricao': 'P/EBITDA negativo indica EBITDA negativo, sugerindo ineficiência operacional ou prejuízo. Comum em setores cíclicos em baixa (ex.: siderurgia, mineração) ou empresas em crise. Exige análise de fluxo de caixa e recuperação.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= pebitda <= 4:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= P/EBITDA <= 4',
                'descricao': 'P/EBITDA baixo sugere subvalorização, indicando oportunidade de compra. Comum em setores maduros (ex.: siderurgia como GGBR4) ou empresas com margens temporariamente comprimidas. Confirme com análise de endividamento.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 4 < pebitda <= 7:
            return {
                'classificacao': 'Moderado',
                'faixa': '4 < P/EBITDA <= 7',
                'descricao': 'P/EBITDA indica valuation justo, típico de empresas com geração de caixa estável (ex.: utilities como CPLE6). Oferece equilíbrio entre risco e retorno, mas com limitado potencial de upside.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 7 < pebitda <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '7 < P/EBITDA <= 10',
                'descricao': 'P/EBITDA elevado sugere sobrevalorização moderada, comum em setores de crescimento (ex.: varejo como MGLU3). Exige análise de crescimento futuro e comparação com pares do setor.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < pebitda <= 15:
            return {
                'classificacao': 'Pessimo',
                'faixa': '10 < P/EBITDA <= 15',
                'descricao': 'P/EBITDA muito alto indica ação cara, com expectativas de crescimento elevadas. Risco de correção se os resultados desapontarem, comum em tecnologia ou consumo cíclico.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # pebitda > 15
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/EBITDA > 15',
                'descricao': 'P/EBITDA extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas (ex.: startups de tecnologia). Análise detalhada do crescimento e margens é essencial.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar P/EBITDA: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_pvp(pvp):
    '''Avalia o Preço/Valor Patrimonial (P/VP) com base em faixas definidas para o mercado brasileiro:
    - P/VP < 0: Crítico (patrimônio negativo, risco elevado)
    - 0 ≤ P/VP ≤ 0.8: Ótimo (subvalorizado, oportunidade de compra)
    - 0.8 < P/VP ≤ 1.5: Moderado (valuation justo, crescimento moderado)
    - 1.5 < P/VP ≤ 2.5: Ruim (sobrevalorizado, cautela necessária)
    - 2.5 < P/VP ≤ 4: Péssimo (muito caro, alto risco)
    - P/VP > 4: Fora da faixa (extremamente sobrevalorizado, risco elevado)'''
    definicao = '''Indicador que compara o preço da ação com o valor patrimonial por ação, avaliando se a empresa está sendo negociada acima ou abaixo de seu valor contábil. É útil para identificar subvalorização ou sobrevalorização em relação aos ativos líquidos.'''
    agrupador = 'Valuation'
    formula = 'P/VP = Preço da Ação / Valor Patrimonial por Ação'
    try:
        if pvp < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'P/VP < 0',
                'descricao': 'P/VP negativo indica patrimônio líquido negativo, sugerindo insolvência ou sérios problemas financeiros. Comum em empresas em recuperação judicial (ex.: OI). Exige análise detalhada de ativos e passivos.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= pvp <= 0.8:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= P/VP <= 0.8',
                'descricao': 'P/VP baixo sugere subvalorização, indicando oportunidade de compra. Comum em setores maduros (ex.: bancos como BBDC4) ou empresas com ativos subavaliados pelo mercado.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.8 < pvp <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.8 < P/VP <= 1.5',
                'descricao': 'P/VP indica valuation justo, típico de empresas com estrutura de capital equilibrada (ex.: indústrias como SUZB3). Oferece equilíbrio entre risco e retorno.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < pvp <= 2.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '1.5 < P/VP <= 2.5',
                'descricao': 'P/VP elevado sugere sobrevalorização moderada, comum em setores de crescimento (ex.: varejo como LREN3). Exige análise de intangíveis e perspectivas de lucro.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2.5 < pvp <= 4:
            return {
                'classificacao': 'Pessimo',
                'faixa': '2.5 < P/VP <= 4',
                'descricao': 'P/VP muito alto indica ação cara, com expectativas elevadas de crescimento. Comum em tecnologia (ex.: TOTS3), mas com risco de correção.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # pvp > 4
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/VP > 4',
                'descricao': 'P/VP extremamente elevado sugere sobrevalorização severa, típica de empresas com altos intangíveis ou especulação (ex.: startups). Análise detalhada do crescimento é essencial.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar P/VP: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_pebit(pebit):
    '''Avalia o Preço/EBIT com base em faixas definidas para o mercado brasileiro:
    - P/EBIT < 0: Crítico (EBIT negativo, risco elevado)
    - 0 ≤ P/EBIT ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
    - 5 < P/EBIT ≤ 10: Moderado (valuation justo, crescimento moderado)
    - 10 < P/EBIT ≤ 15: Ruim (sobrevalorizado, cautela necessária)
    - 15 < P/EBIT ≤ 20: Péssimo (muito caro, alto risco)
    - P/EBIT > 20: Fora da faixa (extremamente sobrevalorizado, risco elevado)'''
    definicao = '''Indicador que relaciona o preço da ação ao EBIT, medindo a capacidade da empresa de gerar lucro operacional em relação ao seu valor de mercado. É útil para avaliar a lucratividade antes de impostos e juros.'''
    agrupador = 'Valuation'
    formula = 'P/EBIT = Preço da Ação / EBIT por Ação'
    try:
        if pebit < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'P/EBIT < 0',
                'descricao': 'P/EBIT negativo indica EBIT negativo, sugerindo ineficiência operacional ou prejuízo. Comum em setores com alta depreciação (ex.: siderurgia). Exige análise de fluxo de caixa.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= pebit <= 5:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= P/EBIT <= 5',
                'descricao': 'P/EBIT baixo sugere subvalorização, indicando oportunidade de compra. Comum em setores cíclicos (ex.: mineração como VALE3) ou empresas com desafios temporários.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < pebit <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '5 < P/EBIT <= 10',
                'descricao': 'P/EBIT indica valuation justo, típico de empresas com geração de lucro operacional estável (ex.: energia como ELET3). Equilíbrio entre risco e retorno.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < pebit <= 15:
            return {
                'classificacao': 'Ruim',
                'faixa': '10 < P/EBIT <= 15',
                'descricao': 'P/EBIT elevado sugere sobrevalorização moderada, comum em setores de crescimento (ex.: varejo). Exige análise de margens e crescimento futuro.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < pebit <= 20:
            return {
                'classificacao': 'Pessimo',
                'faixa': '15 < P/EBIT <= 20',
                'descricao': 'P/EBIT muito alto indica ação cara, com expectativas de crescimento elevadas. Risco de correção em setores como tecnologia.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # pebit > 20
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/EBIT > 20',
                'descricao': 'P/EBIT extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas. Análise detalhada do crescimento é essencial.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar P/EBIT: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_evebitda(evebitda):
    '''Avalia o EV/EBITDA com base em faixas definidas para o mercado brasileiro:
    - EV/EBITDA < 0: Crítico (EBITDA negativo, risco elevado)
    - 0 ≤ EV/EBITDA ≤ 4: Ótimo (subvalorizado, oportunidade de compra)
    - 4 < EV/EBITDA ≤ 7: Moderado (valuation justo, crescimento moderado)
    - 7 < EV/EBITDA ≤ 10: Ruim (sobrevalorizado, cautela necessária)
    - 10 < EV/EBITDA ≤ 15: Péssimo (muito caro, alto risco)
    - EV/EBITDA > 15: Fora da faixa (extremamente sobrevalorizado, risco elevado)'''
    definicao = '''Indicador que relaciona o valor da empresa (valor de mercado + dívida líquida) ao EBITDA, avaliando a capacidade de geração de caixa em relação ao valor total da companhia. É útil para comparar empresas com diferentes estruturas de capital.'''
    agrupador = 'Valuation'
    formula = 'EV/EBITDA = (Valor de Mercado + Dívida Líquida) / EBITDA'
    try:
        if evebitda < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'EV/EBITDA < 0',
                'descricao': 'EV/EBITDA negativo indica EBITDA negativo, sugerindo problemas operacionais graves. Comum em empresas em crise ou setores cíclicos (ex.: mineração). Exige análise de recuperação.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= evebitda <= 4:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= EV/EBITDA <= 4',
                'descricao': 'EV/EBITDA baixo sugere subvalorização, indicando oportunidade de compra. Comum em setores com ativos pesados (ex.: mineração como VALE3). Confirme com análise de endividamento.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 4 < evebitda <= 7:
            return {
                'classificacao': 'Moderado',
                'faixa': '4 < EV/EBITDA <= 7',
                'descricao': 'EV/EBITDA indica valuation justo, típico de empresas com geração de caixa estável (ex.: utilities como ELET3). Equilíbrio entre risco e retorno.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 7 < evebitda <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '7 < EV/EBITDA <= 10',
                'descricao': 'EV/EBITDA elevado sugere sobrevalorização moderada, comum em setores de crescimento (ex.: consumo como ABEV3). Exige análise de crescimento futuro.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < evebitda <= 15:
            return {
                'classificacao': 'Pessimo',
                'faixa': '10 < EV/EBITDA <= 15',
                'descricao': 'EV/EBITDA muito alto indica empresa cara, com expectativas de crescimento elevadas. Risco de correção em setores como tecnologia.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # evebitda > 15
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'EV/EBITDA > 15',
                'descricao': 'EV/EBITDA extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas (ex.: startups). Análise detalhada é essencial.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar EV/EBITDA: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_evebit(evebit):
    '''Avalia o EV/EBIT com base em faixas definidas para o mercado brasileiro:
    - EV/EBIT < 0: Crítico (EBIT negativo, risco elevado)
    - 0 ≤ EV/EBIT ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
    - 5 < EV/EBIT ≤ 10: Moderado (valuation justo, crescimento moderado)
    - 10 < EV/EBIT ≤ 15: Ruim (sobrevalorizado, cautela necessária)
    - 15 < EV/EBIT ≤ 20: Péssimo (muito caro, alto risco)
    - EV/EBIT > 20: Fora da faixa (extremamente sobrevalorizado, risco elevado)'''
    definicao = '''Indicador que relaciona o valor da empresa (valor de mercado + dívida líquida) ao EBIT, avaliando a lucratividade operacional em relação ao valor total da companhia. É útil para comparar empresas antes de impostos e juros.'''
    agrupador = 'Valuation'
    formula = 'EV/EBIT = (Valor de Mercado + Dívida Líquida) / EBIT'
    try:
        if evebit < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'EV/EBIT < 0',
                'descricao': 'EV/EBIT negativo indica EBIT negativo, sugerindo ineficiência operacional. Comum em setores com alta depreciação (ex.: siderurgia). Exige análise de fluxo de caixa.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= evebit <= 5:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= EV/EBIT <= 5',
                'descricao': 'EV/EBIT baixo sugere subvalorização, indicando oportunidade de compra. Comum em setores cíclicos (ex.: mineração como VALE3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < evebit <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '5 < EV/EBIT <= 10',
                'descricao': 'EV/EBIT indica valuation justo, típico de empresas com lucro operacional estável (ex.: energia como ELET3). Equilíbrio entre risco e retorno.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < evebit <= 15:
            return {
                'classificacao': 'Ruim',
                'faixa': '10 < EV/EBIT <= 15',
                'descricao': 'EV/EBIT elevado sugere sobrevalorização moderada, comum em setores de crescimento (ex.: consumo). Exige análise de margens.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < evebit <= 20:
            return {
                'classificacao': 'Pessimo',
                'faixa': '15 < EV/EBIT <= 20',
                'descricao': 'EV/EBIT muito alto indica empresa cara, com expectativas de crescimento elevadas. Risco de correção em setores como tecnologia.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # evebit > 20
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'EV/EBIT > 20',
                'descricao': 'EV/EBIT extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas. Análise detalhada é essencial.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar EV/EBIT: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_giro_ativos(giro):
    '''Avalia o Giro de Ativos (Receita Líquida/Ativos Totais) com base em faixas definidas:
    - Giro < 0: Crítico (receita negativa, risco elevado)
    - 0 ≤ Giro ≤ 0.2: Péssimo (eficiência muito baixa)
    - 0.2 < Giro ≤ 0.5: Ruim (eficiência limitada)
    - 0.5 < Giro ≤ 1.0: Moderado (eficiência adequada)
    - 1.0 < Giro ≤ 2.0: Ótimo (alta eficiência)
    - Giro > 2.0: Fora da faixa (eficiência excepcional)'''
    definicao = '''Indicador que mede a eficiência com que a empresa utiliza seus ativos totais para gerar receita. Um giro alto sugere maior eficiência operacional, enquanto um giro baixo pode indicar subutilização de ativos.'''
    agrupador = 'Eficiência'
    formula = 'Giro de Ativos = Receita Líquida / Ativos Totais'
    try:
        if giro < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'Giro < 0',
                'descricao': 'Giro de ativos negativo indica receita negativa, sugerindo graves problemas operacionais. Exige análise detalhada da estrutura de custos.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= giro <= 0.2:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0 <= Giro <= 0.2',
                'descricao': 'Giro muito baixo sugere baixa eficiência no uso de ativos, comum em infraestrutura (ex.: CCRD3) ou setores com ativos pesados.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < giro <= 0.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.2 < Giro <= 0.5',
                'descricao': 'Giro limitado indica eficiência moderada, comum em utilities (ex.: CPLE6). Exige análise de margens e ciclo operacional.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < giro <= 1.0:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < Giro <= 1.0',
                'descricao': 'Giro adequado sugere eficiência equilibrada, comum em indústrias (ex.: WEGE3). Bom equilíbrio entre ativos e receita.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.0 < giro <= 2.0:
            return {
                'classificacao': 'Otimo',
                'faixa': '1.0 < Giro <= 2.0',
                'descricao': 'Giro alto indica alta eficiência no uso de ativos, comum em varejo (ex.: MGLU3). Sinal de boa gestão operacional.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # giro > 2.0
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Giro > 2.0',
                'descricao': 'Giro extremamente alto sugere eficiência excepcional, comum em tecnologia (ex.: TOTS3). Pode indicar alavancagem ou modelo de negócios leve.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Giro de Ativos: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_divida_liquida_pl(dl_pl):
    '''Avalia a Dívida Líquida/Patrimônio Líquido com base em faixas definidas:
    - DL/PL < -1: Crítico (caixa excessivo, possível ineficiência)
    - -1 ≤ DL/PL < 0: Ótimo (caixa supera dívida)
    - 0 ≤ DL/PL ≤ 0.5: Moderado (endividamento baixo)
    - 0.5 < DL/PL ≤ 1: Ruim (endividamento moderado)
    - 1 < DL/PL ≤ 2: Péssimo (endividamento alto)
    - DL/PL > 2: Fora da faixa (endividamento excessivo)'''
    definicao = """É um indicador financeiro que mede o nível de endividamento de uma empresa em relação ao seu patrimônio líquido. 
    Ele mostra quanto da dívida líquida representa em comparação ao valor que pertence aos acionistas (patrimônio líquido). 
    Trata-se de uma métrica importante para avaliar a saúde financeira da empresa e sua capacidade de gerenciar obrigações e riscos associados ao endividamento."""
    agrupador = 'Eficiência'
    formula = "Dívida Líquida/PL = Dívida Líquida / Patrimônio Líquido"

    try:
        if dl_pl < -1:
            return {
                'classificacao': 'Critico',
                'faixa': 'DL/PL < -1',
                'descricao': 'DL/PL extremamente negativa indica caixa excessivo, comum em tecnologia (ex.: WIZS3). Pode sugerir ineficiência na alocação de capital.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif -1 <= dl_pl < 0:
            return {
                'classificacao': 'Otimo',
                'faixa': '-1 <= DL/PL < 0',
                'descricao': 'DL/PL negativa indica solidez financeira, com caixa superando dívidas. Comum em empresas com alta geração de caixa (ex.: VALE3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= dl_pl <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0 <= DL/PL <= 0.5',
                'descricao': 'DL/PL baixa indica endividamento controlado, comum em consumo (ex.: ABEV3). Equilíbrio financeiro sólido.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < dl_pl <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < DL/PL <= 1',
                'descricao': 'DL/PL moderada sugere endividamento aceitável, comum em indústrias (ex.: SUZB3). Exige monitoramento de fluxo de caixa.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < dl_pl <= 2:
            return {
                'classificacao': 'Pessimo',
                'faixa': '1 < DL/PL <= 2',
                'descricao': 'DL/PL alta indica endividamento elevado, comum em utilities (ex.: ENGI11). Risco de alavancagem requer atenção.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # dl_pl > 2
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'DL/PL > 2',
                'descricao': 'DL/PL extremamente alta sugere endividamento excessivo, comum em construção (ex.: CYRE3). Alto risco financeiro.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar DL/PL: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_divida_liquida_ebitda(dl_ebitda):
    '''Avalia a Dívida Líquida/EBITDA com base em faixas definidas:
    - DL/EBITDA < -2: Crítico (caixa excessivo, possível ineficiência)
    - -2 ≤ DL/EBITDA < 0: Ótimo (caixa supera dívida)
    - 0 ≤ DL/EBITDA ≤ 1.5: Moderado (endividamento baixo)
    - 1.5 < DL/EBITDA ≤ 3: Ruim (endividamento moderado)
    - 3 < DL/EBITDA ≤ 4.5: Péssimo (endividamento alto)
    - DL/EBITDA > 4.5: Fora da faixa (endividamento excessivo)'''
    definicao = '''Indicador que mede a capacidade da empresa de pagar sua dívida líquida com base no EBITDA gerado. Representa quantos anos de EBITDA seriam necessários para quitar a dívida líquida, avaliando a sustentabilidade do endividamento.'''
    agrupador = 'Endividamento'
    formula = 'Dívida Líquida/EBITDA = Dívida Líquida / EBITDA'
    try:
        if dl_ebitda < -2:
            return {
                'classificacao': 'Critico',
                'faixa': 'DL/EBITDA < -2',
                'descricao': 'DL/EBITDA extremamente negativa indica caixa excessivo, comum em empresas com alta liquidez (ex.: VALE3). Pode sugerir ineficiência na alocação de capital.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif -2 <= dl_ebitda < 0:
            return {
                'classificacao': 'Otimo',
                'faixa': '-2 <= DL/EBITDA < 0',
                'descricao': 'DL/EBITDA negativa indica solidez financeira, com caixa superando dívidas. Comum em empresas com forte geração de caixa (ex.: WEGE3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= dl_ebitda <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0 <= DL/EBITDA <= 1.5',
                'descricao': 'DL/EBITDA baixa indica endividamento controlado, comum em consumo (ex.: ABEV3). Sinal de saúde financeira.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < dl_ebitda <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '1.5 < DL/EBITDA <= 3',
                'descricao': 'DL/EBITDA moderada sugere endividamento aceitável, comum em indústrias (ex.: SUZB3). Exige monitoramento.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < dl_ebitda <= 4.5:
            return {
                'classificacao': 'Pessimo',
                'faixa': '3 < DL/EBITDA <= 4.5',
                'descricao': 'DL/EBITDA alta indica endividamento elevado, comum em utilities (ex.: ENGI11). Risco de alavancagem.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # dl_ebitda > 4.5
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'DL/EBITDA > 4.5',
                'descricao': 'DL/EBITDA extremamente alta sugere endividamento excessivo, comum em empresas alavancadas (ex.: OI). Alto risco financeiro.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar DL/EBITDA: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_divida_liquida_ebit(dl_ebit):
    '''Avalia a Dívida Líquida/EBIT com base em faixas definidas:
    - DL/EBIT < -3: Crítico (caixa excessivo, possível ineficiência)
    - -3 ≤ DL/EBIT < 0: Ótimo (caixa supera dívida)
    - 0 ≤ DL/EBIT ≤ 2: Moderado (endividamento baixo)
    - 2 < DL/EBIT ≤ 4: Ruim (endividamento moderado)
    - 4 < DL/EBIT ≤ 6: Péssimo (endividamento alto)
    - DL/EBIT > 6: Fora da faixa (endividamento excessivo)'''
    definicao = '''Indicador que mede a capacidade da empresa de pagar sua dívida líquida com base no EBIT gerado. Representa quantos anos de EBIT seriam necessários para quitar a dívida líquida, avaliando a sustentabilidade do endividamento antes de impostos e juros.'''
    agrupador = 'Endividamento'
    formula = 'Dívida Líquida/EBIT = Dívida Líquida / EBIT'
    try:
        if dl_ebit < -3:
            return {
                'classificacao': 'Critico',
                'faixa': 'DL/EBIT < -3',
                'descricao': 'DL/EBIT extremamente negativa indica caixa excessivo, sugerindo ineficiência na alocação de capital. Comum em empresas com alta liquidez.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif -3 <= dl_ebit < 0:
            return {
                'classificacao': 'Otimo',
                'faixa': '-3 <= DL/EBIT < 0',
                'descricao': 'DL/EBIT negativa indica solidez financeira, com caixa superando dívidas. Comum em empresas com forte geração de caixa.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= dl_ebit <= 2:
            return {
                'classificacao': 'Moderado',
                'faixa': '0 <= DL/EBIT <= 2',
                'descricao': 'DL/EBIT baixa indica endividamento controlado, comum em consumo (ex.: ABEV3). Sinal de saúde financeira.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < dl_ebit <= 4:
            return {
                'classificacao': 'Ruim',
                'faixa': '2 < DL/EBIT <= 4',
                'descricao': 'DL/EBIT moderada sugere endividamento aceitável, comum em indústrias (ex.: SUZB3). Exige monitoramento.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 4 < dl_ebit <= 6:
            return {
                'classificacao': 'Pessimo',
                'faixa': '4 < DL/EBIT <= 6',
                'descricao': 'DL/EBIT alta indica endividamento elevado, comum in utilities. Risco de alavancagem.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # dl_ebit > 6
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'DL/EBIT > 6',
                'descricao': 'DL/EBIT extremamente alta sugere endividamento excessivo, indicando alto risco financeiro.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar DL/EBIT: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_pl_ativos(pl_ativos):
    '''Avalia o Patrimônio Líquido/Ativos com base em faixas definidas:
    - PL/Ativos < 0: Crítico (patrimônio negativo, risco elevado)
    - 0 ≤ PL/Ativos ≤ 0.1: Péssimo (alta alavancagem)
    - 0.1 < PL/Ativos ≤ 0.3: Ruim (alavancagem moderada)
    - 0.3 < PL/Ativos ≤ 0.5: Moderado (estrutura equilibrada)
    - 0.5 < PL/Ativos ≤ 0.7: Ótimo (patrimônio sólido)
    - PL/Ativos > 0.7: Fora da faixa (pouco endividamento)'''
    definicao = '''Indicador que mede a proporção do patrimônio líquido em relação aos ativos totais, avaliando o grau de alavancagem financeira da empresa. Um valor alto indica baixa dependência de dívidas, enquanto um valor baixo sugere maior alavancagem.'''
    agrupador = 'Estrutura de Capital'
    formula = 'PL/Ativos = Patrimônio Líquido / Ativos Totais'
    try:
        if pl_ativos < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'PL/Ativos < 0',
                'descricao': 'PL/Ativos negativo indica patrimônio líquido negativo, sugerindo insolvência. Comum em empresas em crise (ex.: OI).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= pl_ativos <= 0.1:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0 <= PL/Ativos <= 0.1',
                'descricao': 'PL/Ativos muito baixo sugere alta alavancagem, comum em bancos (ex.: ITUB4). Risco financeiro elevado.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.1 < pl_ativos <= 0.3:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.1 < PL/Ativos <= 0.3',
                'descricao': 'PL/Ativos baixo indica alavancagem moderada, comum em utilities (ex.: ENGI11). Exige monitoramento.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 < pl_ativos <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.3 < PL/Ativos <= 0.5',
                'descricao': 'PL/Ativos equilibrado sugere estrutura financeira saudável, comum em indústrias (ex.: SUZB3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < pl_ativos <= 0.7:
            return {
                'classificacao': 'Otimo',
                'faixa': '0.5 < PL/Ativos <= 0.7',
                'descricao': 'PL/Ativos alto indica patrimônio sólido, comum em consumo (ex.: ABEV3). Sinal de baixa alavancagem.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # pl_ativos > 0.7
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'PL/Ativos > 0.7',
                'descricao': 'PL/Ativos extremamente alto sugere pouco endividamento, comum em tecnologia (ex.: TOTS3). Pode indicar subvalorização.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar PL/Ativos: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_passivos_ativos(passivos_ativos):
    '''Avalia o Passivos/Ativos com base em faixas definidas:
    - Passivos/Ativos < 0: Crítico (impossível)
    - 0 ≤ Passivos/Ativos ≤ 0.3: Ótimo (baixo endividamento)
    - 0.3 < Passivos/Ativos ≤ 0.5: Moderado (endividamento controlado)
    - 0.5 < Passivos/Ativos ≤ 0.7: Ruim (endividamento moderado)
    - 0.7 < Passivos/Ativos ≤ 0.9: Péssimo (endividamento alto)
    - Passivos/Ativos > 0.9: Fora da faixa (endividamento excessivo)'''
    definicao = '''Indicador que mede a proporção dos passivos totais em relação aos ativos totais, avaliando o nível de endividamento da empresa. Um valor alto indica maior dependência de dívidas, enquanto um valor baixo sugere maior solidez financeira.'''
    agrupador = 'Endividamento'
    formula = 'Passivos/Ativos = Passivos Totais / Ativos Totais'
    try:
        if passivos_ativos < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'Passivos/Ativos < 0',
                'descricao': 'Passivos/Ativos negativo é impossível, indicando erro nos dados financeiros.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= passivos_ativos <= 0.3:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= Passivos/Ativos <= 0.3',
                'descricao': 'Passivos/Ativos baixo indica baixo endividamento, comum em tecnologia (ex.: TOTS3). Sinal de saúde financeira.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 < passivos_ativos <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.3 < Passivos/Ativos <= 0.5',
                'descricao': 'Passivos/Ativos moderado sugere endividamento controlado, comum em consumo (ex.: ABEV3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < passivos_ativos <= 0.7:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < Passivos/Ativos <= 0.7',
                'descricao': 'Passivos/Ativos elevado indica endividamento moderado, comum em indústrias (ex.: SUZB3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.7 < passivos_ativos <= 0.9:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0.7 < Passivos/Ativos <= 0.9',
                'descricao': 'Passivos/Ativos alto sugere endividamento elevado, comum em utilities (ex.: ENGI11). Risco financeiro.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # passivos_ativos > 0.9
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Passivos/Ativos > 0.9',
                'descricao': 'Passivos/Ativos extremamente alto indica endividamento excessivo, comum em bancos (ex.: ITUB4). Alto risco.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Passivos/Ativos: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_liquidez_corrente(lc):
    '''Avalia a Liquidez Corrente com base em faixas definidas:
    - Liquidez < 0.8: Crítico (alta insolvência)
    - 0.8 ≤ Liquidez ≤ 1: Péssimo (liquidez muito baixa)
    - 1 < Liquidez ≤ 1.2: Ruim (liquidez limitada)
    - 1.2 < Liquidez ≤ 1.5: Moderado (liquidez adequada)
    - 1.5 < Liquidez ≤ 2: Ótimo (alta liquidez)
    - Liquidez > 2: Fora da faixa (liquidez excessiva)'''
    definicao = '''Indicador que mede a capacidade da empresa de pagar suas obrigações de curto prazo com os ativos circulantes. Um valor maior que 1 indica que a empresa pode cobrir suas dívidas de curto prazo, enquanto valores muito altos podem sugerir ineficiência no uso do capital.'''
    agrupador = 'Liquidez'
    formula = 'Liquidez Corrente = Ativo Circulante / Passivo Circulante'
    try:
        if lc < 0.8:
            return {
                'classificacao': 'Critico',
                'faixa': 'Liquidez < 0.8',
                'descricao': 'Liquidez muito baixa indica alto risco de insolvência, comum em empresas alavancadas (ex.: OI). Exige análise de fluxo de caixa.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.8 <= lc <= 1:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0.8 <= Liquidez <= 1',
                'descricao': 'Liquidez baixa sugere dificuldades em cobrir obrigações de curto prazo, comum em setores alavancados.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < lc <= 1.2:
            return {
                'classificacao': 'Ruim',
                'faixa': '1 < Liquidez <= 1.2',
                'descricao': 'Liquidez limitada indica capacidade moderada de cumprir obrigações, comum em indústrias (ex.: SUZB3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.2 < lc <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1.2 < Liquidez <= 1.5',
                'descricao': 'Liquidez adequada sugere equilíbrio financeiro, comum em consumo (ex.: ABEV3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < lc <= 2:
            return {
                'classificacao': 'Otimo',
                'faixa': '1.5 < Liquidez <= 2',
                'descricao': 'Liquidez alta indica forte capacidade de cumprir obrigações, comum em tecnologia (ex.: TOTS3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # lc > 2
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Liquidez > 2',
                'descricao': 'Liquidez extremamente alta pode indicar ineficiência na alocação de capital, comum em empresas com caixa elevado.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Liquidez Corrente: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_peg_ratio(peg):
    '''Avalia o PEG Ratio com base em faixas definidas:
    - PEG < 0: Crítico (crescimento negativo, risco elevado)
    - 0 ≤ PEG ≤ 0.5: Ótimo (subvalorizado com alto crescimento)
    - 0.5 < PEG ≤ 1: Moderado (valuation justo)
    - 1 < PEG ≤ 1.5: Ruim (sobrevalorizado, cautela necessária)
    - 1.5 < PEG ≤ 2: Péssimo (muito caro, alto risco)
    - PEG > 2: Fora da faixa (extremamente sobrevalorizado)'''
    definicao = '''Indicador que relaciona o P/L com a taxa de crescimento esperada dos lucros, avaliando se o preço da ação é justificado pelo seu potencial de crescimento. Um PEG baixo sugere subvalorização em relação ao crescimento esperado.'''
    agrupador = 'Valuation'
    formula = 'PEG = (Preço/Lucro) / Crescimento Anual Esperado do Lucro (%)'
    try:
        if peg < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'PEG < 0',
                'descricao': 'PEG negativo indica crescimento esperado negativo ou P/L negativo, sugerindo problemas financeiros ou de mercado.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= peg <= 0.5:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= PEG <= 0.5',
                'descricao': 'PEG baixo sugere subvalorização com alto potencial de crescimento, comum em tecnologia (ex.: TOTS3). Oportunidade de compra.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < peg <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < PEG <= 1',
                'descricao': 'PEG indica valuation justo, equilibrando preço e crescimento, comum em varejo (ex.: MGLU3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < peg <= 1.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '1 < PEG <= 1.5',
                'descricao': 'PEG elevado sugere sobrevalorização moderada, indicando expectativas de crescimento moderadas.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < peg <= 2:
            return {
                'classificacao': 'Pessimo',
                'faixa': '1.5 < PEG <= 2',
                'descricao': 'PEG muito alto indica ação cara em relação ao crescimento, comum em setores especulativos.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # peg > 2
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'PEG > 2',
                'descricao': 'PEG extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas. Análise detalhada é essencial.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar PEG Ratio: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_p_ativo(p_ativo):
    '''Avalia o Preço/Ativo Total com base em faixas definidas:
    - P/Ativo < 0: Crítico (impossível)
    - 0 ≤ P/Ativo ≤ 0.2: Ótimo (subvalorizado)
    - 0.2 < P/Ativo ≤ 0.5: Moderado (valuation justo)
    - 0.5 < P/Ativo ≤ 1: Ruim (sobrevalorizado)
    - 1 < P/Ativo ≤ 1.5: Péssimo (muito caro)
    - P/Ativo > 1.5: Fora da faixa (extremamente sobrevalorizado)'''
    definicao = '''Indicador que compara o preço da ação com os ativos totais por ação, avaliando se a empresa está sendo negociada acima ou abaixo do valor de seus ativos. É útil para identificar subvalorização em empresas com muitos ativos.'''
    agrupador = 'Valuation'
    formula = 'P/Ativo = Preço da Ação / Ativos Totais por Ação'
    try:
        if p_ativo < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'P/Ativo < 0',
                'descricao': 'P/Ativo negativo é impossível, indicando erro nos dados financeiros.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= p_ativo <= 0.2:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= P/Ativo <= 0.2',
                'descricao': 'P/Ativo baixo sugere subvalorização, comum em mineração (ex.: VALE3). Oportunidade de compra.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < p_ativo <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.2 < P/Ativo <= 0.5',
                'descricao': 'P/Ativo indica valuation justo, típico de energia (ex.: ELET3). Equilíbrio entre risco e retorno.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < p_ativo <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < P/Ativo <= 1',
                'descricao': 'P/Ativo elevado sugere sobrevalorização, comum em consumo (ex.: ABEV3). Exige análise de ativos.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < p_ativo <= 1.5:
            return {
                'classificacao': 'Pessimo',
                'faixa': '1 < P/Ativo <= 1.5',
                'descricao': 'P/Ativo muito alto indica ação cara, comum em tecnologia.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # p_ativo > 1.5
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/Ativo > 1.5',
                'descricao': 'P/Ativo extremamente elevado sugere sobrevalorização severa, indicando alto risco.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar P/Ativo: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_vpa(vpa_preco):
    '''Avalia o VPA/Preço com base em faixas definidas:
    - VPA/Preço < 0: Crítico (patrimônio negativo)
    - 0 ≤ VPA/Preço ≤ 0.5: Fora da faixa (sobrevalorizado)
    - 0.5 < VPA/Preço ≤ 0.8: Péssimo (muito caro)
    - 0.8 < VPA/Preço ≤ 1: Ruim (sobrevalorizado)
    - 1 < VPA/Preço ≤ 1.5: Moderado (valuation justo)
    - VPA/Preço > 1.5: Ótimo (subvalorizado)'''
    definicao = '''Indicador que compara o valor patrimonial por ação com o preço da ação, avaliando se a empresa está subvalorizada ou sobrevalorizada em relação ao seu patrimônio líquido. Um valor alto sugere subvalorização.'''
    agrupador = 'Valuation'
    formula = 'VPA/Preço = Valor Patrimonial por Ação / Preço da Ação'
    try:
        if vpa_preco < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'VPA/Preço < 0',
                'descricao': 'VPA/Preço negativo indica patrimônio líquido negativo, sugerindo insolvência (ex.: OI).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= vpa_preco <= 0.5:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': '0 <= VPA/Preço <= 0.5',
                'descricao': 'VPA/Preço muito baixo indica sobrevalorização severa, comum em tecnologia (ex.: TOTS3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < vpa_preco <= 0.8:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0.5 < VPA/Preço <= 0.8',
                'descricao': 'VPA/Preço baixo sugere ação cara, comum em varejo (ex.: MGLU3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.8 < vpa_preco <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.8 < VPA/Preço <= 1',
                'descricao': 'VPA/Preço indica sobrevalorização moderada, comum em consumo (ex.: ABEV3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < vpa_preco <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < VPA/Preço <= 1.5',
                'descricao': 'VPA/Preço indica valuation justo, típico de indústrias (ex.: SUZB3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        else:  # vpa_preco > 1.5
            return {
                'classificacao': 'Otimo',
                'faixa': 'VPA/Preço > 1.5',
                'descricao': 'VPA/Preço alto sugere subvalorização, comum em setores maduros (ex.: bancos como BBDC4).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar VPA/Preço: {str(e)}. Verifique se o valor fornecido é um número válido.',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_p_acl(p_acl):
    '''Avalia o Preço/Ativo Circulante Líquido com base em faixas definidas:
    - P/ACL < 0: Crítico (impossível)
    - 0 ≤ P/ACL ≤ 0.2: Ótimo (subvalorizado)
    - 0.2 < P/ACL ≤ 0.5: Moderado (valuation justo)
    - 0.5 < P/ACL ≤ 1: Ruim (sobrevalorizado)
    - 1 < P/ACL ≤ 1.5: Péssimo (muito caro)
    - P/ACL > 1.5: Fora da faixa (extremamente sobrevalorizado)'''
    definicao = '''Indicador que compara o preço da ação com o ativo circulante líquido por ação (ativo circulante menos passivo circulante), avaliando a liquidez imediata da empresa em relação ao seu valor de mercado.'''
    agrupador = 'Valuation'
    formula = 'P/ACL = Preço da Ação / (Ativo Circulante - Passivo Circulante) por Ação'
    try:
        if p_acl < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'P/ACL < 0',
                'descricao': 'P/ACL negativo é impossível, indicando erro nos dados financeiros.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= p_acl <= 0.2:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= P/ACL <= 0.2',
                'descricao': 'P/ACL baixo sugere subvalorização, comum em empresas com alta liquidez (ex.: VALE3). Oportunidade de compra.',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < p_acl <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.2 < P/ACL <= 0.5',
                'descricao': 'P/ACL indica valuation justo, comum em energia (ex.: ELET3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < p_acl <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < P/ACL <= 1',
                'descricao': 'P/ACL elevado sugere sobrevalorização, comum em consumo (ex.: ABEV3).',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < p_acl