def evaluate_p_l(value, lucro_liquido):
    """
    Avalia o Preço/Lucro (P/L). Faixas baseadas no mercado brasileiro:
    - < 8: Subvalorizado (ótimo)
    - 8-12: Atraente (bom)
    - 12-18: Neutro (moderado)
    - 18-25: Caro (ruim)
    - > 25: Sobrevalorizado (péssimo)
    """
    if lucro_liquido <= 0:  # Lucro Líquido negativo indica prejuízo
        return 'critico'
    if value <= 8:
        return 'otimo'
    elif value <= 12:
        return 'bom'
    elif value <= 18:
        return 'moderado'
    elif value <= 25:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_p_vp(value, vp):
    """
    Avalia o Preço/Valor Patrimonial (P/VP). Faixas baseadas em análise fundamentalista:
    - < 0.8: Subvalorizado (ótimo)
    - 0.8-1.2: Atraente (bom)
    - 1.2-1.8: Neutro (moderado)
    - 1.8-2.5: Caro (ruim)
    - > 2.5: Sobrevalorizado (péssimo)
    """
    if vp <= 0:  # Valor Patrimonial negativo indica insolvência
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.8:
        return 'otimo'
    elif value <= 1.2:
        return 'bom'
    elif value <= 1.8:
        return 'moderado'
    elif value <= 2.5:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_p_ebitda(value, ebitda):
    """
    Avalia o Preço/EBITDA. Faixas ajustadas para mercado brasileiro:
    - < 4: Subvalorizado (ótimo)
    - 4-7: Atraente (bom)
    - 7-10: Neutro (moderado)
    - 10-13: Caro (ruim)
    - > 13: Sobrevalorizado (péssimo)
    """
    if ebitda <= 0:  # EBITDA negativo ou zero indica problemas operacionais
        return 'critico'
    if value <= 0 or value == float('inf'):
        return 'critico'
    elif value <= 4:
        return 'otimo'
    elif value <= 7:
        return 'bom'
    elif value <= 10:
        return 'moderado'
    elif value <= 13:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_p_ebit(value, ebit):
    """
    Avalia o Preço/EBIT. Faixas ajustadas para mercado brasileiro:
    - < 5: Subvalorizado (ótimo)
    - 5-9: Atraente (bom)
    - 9-14: Neutro (moderado)
    - 14-20: Caro (ruim)
    - > 20: Sobrevalorizado (péssimo)
    """
    if ebit <= 0:  # EBIT negativo ou zero indica problemas operacionais
        return 'critico'
    if value <= 5:
        return 'otimo'
    elif value <= 9:
        return 'bom'
    elif value <= 14:
        return 'moderado'
    elif value <= 20:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_ev_ebitda(value, ebitda, ev):
    """
    Avalia o EV/EBITDA. Faixas baseadas em benchmarks fundamentalistas:
    - < 4: Subvalorizado (ótimo)
    - 4-7: Atraente (bom)
    - 7-10: Neutro (moderado)
    - 10-13: Caro (ruim)
    - > 13: Sobrevalorizado (péssimo)
    """
    if ebitda <= 0:  # EBITDA negativo ou zero indica problemas operacionais
        return 'critico'
    if value < 0 and ev < 0:  # EV/EBITDA negativo devido a EV negativo é favorável
        return 'otimo'
    if value < 0:  # EV/EBITDA negativo devido a outros fatores (ex.: erro de cálculo)
        return 'critico'
    elif value <= 4:
        return 'otimo'
    elif value <= 7:
        return 'bom'
    elif value <= 10:
        return 'moderado'
    elif value <= 13:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_ev_ebit(value, ebit):
    """
    Avalia o EV/EBIT. Faixas ajustadas para mercado brasileiro:
    - < 6: Subvalorizado (ótimo)
    - 6-10: Atraente (bom)
    - 10-15: Neutro (moderado)
    - 15-20: Caro (ruim)
    - > 20: Sobrevalorizado (péssimo)
    """
    if ebit <= 0:  # EBIT negativo ou zero indica problemas operacionais
        return 'critico'
    if value < 0:
        return 'otimo'
    elif value <= 6:
        return 'otimo'
    elif value <= 10:
        return 'bom'
    elif value <= 15:
        return 'moderado'
    elif value <= 20:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_p_sr(value):
    """
    Avalia o Preço/Receita (P/SR). Faixas baseadas em médias setoriais:
    - < 0.7: Subvalorizado (ótimo)
    - 0.7-1.2: Atraente (bom)
    - 1.2-2: Neutro (moderado)
    - 2-3: Caro (ruim)
    - > 3: Sobrevalorizado (péssimo)
    """
    if value <= 0 or value == float('inf'):
        return 'critico'
    elif value <= 0.7:
        return 'otimo'
    elif value <= 1.2:
        return 'bom'
    elif value <= 2:
        return 'moderado'
    elif value <= 3:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_p_ativo(value):
    """
    Avalia o Preço/Ativo. Faixas baseadas em análise fundamentalista:
    - < 0.3: Subvalorizado (ótimo)
    - 0.3-0.5: Atraente (bom)
    - 0.5-0.8: Neutro (moderado)
    - 0.8-1.2: Caro (ruim)
    - > 1.2: Sobrevalorizado (péssimo)
    """
    if value <= 0:
        return 'critico'
    elif value <= 0.3:
        return 'otimo'
    elif value <= 0.5:
        return 'bom'
    elif value <= 0.8:
        return 'moderado'
    elif value <= 1.2:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_vpa(value, pl):
    """
    Avalia o Valor Patrimonial por Ação (VPA). Faixas baseadas em crescimento patrimonial:
    - < 0.5: Muito baixo (péssimo)
    - 0.5-1: Baixo (ruim)
    - 1-2: Neutro (moderado)
    - 2-5: Atraente (bom)
    - > 5: Excelente (ótimo)
    """
    if pl <= 0:
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.5:
        return 'pessimo'
    elif value <= 1:
        return 'ruim'
    elif value <= 2:
        return 'moderado'
    elif value <= 5:
        return 'bom'
    else:
        return 'otimo'


def evaluate_lpa(value):
    """
    Avalia o Lucro por Ação (LPA). Faixas baseadas em benchmarks brasileiros:
    - < 0.2: Muito baixo (péssimo)
    - 0.2-0.5: Baixo (ruim)
    - 0.5-1: Neutro (moderado)
    - 1-2: Atraente (bom)
    - > 2: Excelente (ótimo)
    """
    if value <= 0:
        return 'critico'
    elif value <= 0.2:
        return 'pessimo'
    elif value <= 0.5:
        return 'ruim'
    elif value <= 1:
        return 'moderado'
    elif value <= 2:
        return 'bom'
    else:
        return 'otimo'


def evaluate_peg_ratio(value):
    """
    Avalia o PEG Ratio (P/L dividido por crescimento do lucro). Faixas baseadas em Peter Lynch:
    - < 0.5: Subvalorizado (ótimo)
    - 0.5-1: Atraente (bom)
    - 1-1.5: Neutro (moderado)
    - 1.5-2: Caro (ruim)
    - > 2: Sobrevalorizado (péssimo)
    """
    if value <= 0:
        return 'critico'
    elif value <= 0.5:
        return 'otimo'
    elif value <= 1:
        return 'bom'
    elif value <= 1.5:
        return 'moderado'
    elif value <= 2:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_margem_bruta(value):
    """
    Avalia a Margem Bruta. Faixas baseadas em médias setoriais:
    - < 15%: Muito baixa (péssimo)
    - 15-25%: Baixa (ruim)
    - 25-40%: Neutra (moderado)
    - 40-60%: Alta (bom)
    - > 60%: Excelente (ótimo)
    """
    if value <= 0 or value == float('inf'):
        return 'critico'
    elif value <= 0.15:
        return 'pessimo'
    elif value <= 0.25:
        return 'ruim'
    elif value <= 0.4:
        return 'moderado'
    elif value <= 0.6:
        return 'bom'
    else:
        return 'otimo'


def evaluate_margem_ebitda(value):
    """
    Avalia a Margem EBITDA. Faixas baseadas em setores brasileiros:
    - < 10%: Muito baixa (péssimo)
    - 10-20%: Baixa (ruim)
    - 20-30%: Neutra (moderado)
    - 30-45%: Alta (bom)
    - > 45%: Excelente (ótimo)
    """
    if value <= 0 or value == float('inf'):
        return 'critico'
    elif value <= 0.1:
        return 'pessimo'
    elif value <= 0.2:
        return 'ruim'
    elif value <= 0.3:
        return 'moderado'
    elif value <= 0.45:
        return 'bom'
    else:
        return 'otimo'


def evaluate_margem_ebit(value):
    """
    Avalia a Margem EBIT. Faixas baseadas em benchmarks brasileiros:
    - < 8%: Muito baixa (péssimo)
    - 8-15%: Baixa (ruim)
    - 15-25%: Neutra (moderado)
    - 25-40%: Alta (bom)
    - > 40%: Excelente (ótimo)
    """
    if value <= 0 or value == float('inf'):
        return 'critico'
    elif value <= 0.08:
        return 'pessimo'
    elif value <= 0.15:
        return 'ruim'
    elif value <= 0.25:
        return 'moderado'
    elif value <= 0.4:
        return 'bom'
    else:
        return 'otimo'


def evaluate_margem_liquida(value):
    """
    Avalia a Margem Líquida. Faixas baseadas em médias setoriais:
    - < 5%: Muito baixa (péssimo)
    - 5-10%: Baixa (ruim)
    - 10-20%: Neutra (moderado)
    - 20-30%: Alta (bom)
    - > 30%: Excelente (ótimo)
    """
    if value <= 0 or value == float('inf'):
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.1:
        return 'ruim'
    elif value <= 0.2:
        return 'moderado'
    elif value <= 0.3:
        return 'bom'
    else:
        return 'otimo'


def evaluate_roe(value, pl):
    """
    Avalia o ROE (Retorno sobre Patrimônio). Faixas baseadas em mercado brasileiro:
    - < 5%: Muito baixo (péssimo)
    - 5-10%: Baixo (ruim)
    - 10-20%: Neutro (moderado)
    - 20-30%: Alto (bom)
    - > 30%: Excelente (ótimo)
    """
    if pl <= 0:
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.1:
        return 'ruim'
    elif value <= 0.2:
        return 'moderado'
    elif value <= 0.3:
        return 'bom'
    else:
        return 'otimo'


def evaluate_roa(value):
    """
    Avalia o ROA (Retorno sobre Ativos). Faixas baseadas em benchmarks brasileiros:
    - < 3%: Muito baixo (péssimo)
    - 3-6%: Baixo (ruim)
    - 6-10%: Neutro (moderado)
    - 10-15%: Alto (bom)
    - > 15%: Excelente (ótimo)
    """
    if value <= 0:
        return 'critico'
    elif value <= 0.03:
        return 'pessimo'
    elif value <= 0.06:
        return 'ruim'
    elif value <= 0.1:
        return 'moderado'
    elif value <= 0.15:
        return 'bom'
    else:
        return 'otimo'


def evaluate_roic(value):
    """
    Avalia o ROIC (Retorno sobre Capital Investido). Faixas baseadas em benchmarks:
    - < 5%: Muito baixo (péssimo)
    - 5-8%: Baixo (ruim)
    - 8-12%: Neutro (moderado)
    - 12-20%: Alto (bom)
    - > 20%: Excelente (ótimo)
    """
    if value <= 0:
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.08:
        return 'ruim'
    elif value <= 0.12:
        return 'moderado'
    elif value <= 0.2:
        return 'bom'
    else:
        return 'otimo'


def evaluate_divida_liquida_ebitda(value, ebitda):
    """
    Avalia a Dívida Líquida/EBITDA. Faixas baseadas em análise de endividamento:
    - < 0: Excesso de caixa (ótimo)
    - 0-1.5: Baixa (bom)
    - 1.5-3: Neutra (moderado)
    - 3-4: Alta (ruim)
    - > 4: Muito alta (péssimo)
    """
    if ebitda <= 0:
        return 'critico'
    if value < 0:
        return 'otimo'
    elif value <= 1.5:
        return 'bom'
    elif value <= 3:
        return 'moderado'
    elif value <= 4:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_divida_bruta_ebitda(value, ebitda):
    """
    Avalia a Dívida Bruta/EBITDA. Faixas baseadas em benchmarks brasileiros:
    - 0: Sem dívida (ótimo)
    - 0-1.5: Baixa (bom)
    - 1.5-3: Neutra (moderado)
    - 3-4: Alta (ruim)
    - > 4: Muito alta (péssimo)
    """
    if ebitda <= 0:
        return 'critico'
    if value <= 0:
        return 'otimo'
    elif value <= 1.5:
        return 'bom'
    elif value <= 3:
        return 'moderado'
    elif value <= 4:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_divida_liquida_pl(value, pl):
    """
    Avalia a Dívida Líquida/PL. Faixas baseadas em análise de solvência:
    - < 0: Excesso de caixa (ótimo)
    - 0-0.4: Baixa (bom)
    - 0.4-0.8: Neutra (moderado)
    - 0.8-1.2: Alta (ruim)
    - > 1.2: Muito alta (péssimo)
    """
    if pl <= 0:
        return 'critico'
    if value < 0:
        return 'otimo'
    elif value <= 0.4:
        return 'bom'
    elif value <= 0.8:
        return 'moderado'
    elif value <= 1.2:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_giro_ativo(value):
    """
    Avalia o Giro dos Ativos. Faixas baseadas em eficiência operacional:
    - < 0.3: Muito baixo (péssimo)
    - 0.3-0.5: Baixo (ruim)
    - 0.5-1: Neutro (moderado)
    - 1-1.5: Alto (bom)
    - > 1.5: Excelente (ótimo)
    """
    if value <= 0:
        return 'critico'
    elif value <= 0.3:
        return 'pessimo'
    elif value <= 0.5:
        return 'ruim'
    elif value <= 1:
        return 'moderado'
    elif value <= 1.5:
        return 'bom'
    else:
        return 'otimo'


def evaluate_dividend_yield(value):
    """
    Avalia o Dividend Yield. Faixas baseadas em empresas brasileiras:
    - 0%: Sem dividendos (crítico)
    - < 2%: Muito baixo (ruim)
    - 2-4%: Neutro (moderado)
    - 4-6%: Atraente (bom)
    - > 6%: Excelente (ótimo)
    """
    if value == 0:
        return 'critico'
    elif value <= 0.02:
        return 'ruim'
    elif value <= 0.04:
        return 'moderado'
    elif value <= 0.06:
        return 'bom'
    else:
        return 'otimo'


def evaluate_cagr_receita_5_anos(value):
    """
    Avalia o CAGR de Receita (5 anos). Faixas baseadas em crescimento:
    - < 0%: Negativo (crítico)
    - 0-5%: Muito baixo (péssimo)
    - 5-10%: Baixo (ruim)
    - 10-15%: Neutro (moderado)
    - 15-20%: Alto (bom)
    - > 20%: Excelente (ótimo)
    """
    if value <= 0:
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.1:
        return 'ruim'
    elif value <= 0.15:
        return 'moderado'
    elif value <= 0.2:
        return 'bom'
    else:
        return 'otimo'


def evaluate_cagr_lucro_5_anos(value):
    """
    Avalia o CAGR de Lucro (5 anos). Faixas baseadas em crescimento:
    - < 0%: Negativo (crítico)
    - 0-5%: Muito baixo (péssimo)
    - 5-10%: Baixo (ruim)
    - 10-15%: Neutro (moderado)
    - 15-20%: Alto (bom)
    - > 20%: Excelente (ótimo)
    """
    if value <= 0:
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.1:
        return 'ruim'
    elif value <= 0.15:
        return 'moderado'
    elif value <= 0.2:
        return 'bom'
    else:
        return 'otimo'


def calculate_indicators(financial_data):
    """Calcula os valores dos indicadores a partir dos dados financeiros brutos."""
    indicators = {}
    try:
        # Dívida Líquida
        divida_liquida = financial_data.get('divida_total', 0) - financial_data.get('caixa', 0)
        # Enterprise Value
        ev = financial_data.get('valor_mercado', 0) + divida_liquida
        # Número de ações (evita divisão por zero)
        num_acoes = financial_data.get('num_acoes', 1)

        # Indicadores de Valuation
        indicators['p_l'] = financial_data.get('valor_mercado', 0) / financial_data[
            'lucro_liquido'] if financial_data.get('lucro_liquido') else float('inf')
        indicators['p_vp'] = financial_data.get('preco_acao', 0) / financial_data['vp'] if financial_data.get(
            'vp') else float('inf')
        indicators['p_ebitda'] = ev / financial_data['ebitda'] if financial_data.get('ebitda') else float('inf')
        indicators['p_ebit'] = financial_data.get('valor_mercado', 0) / financial_data['ebit'] if financial_data.get(
            'ebit') else float('inf')
        indicators['ev_ebitda'] = ev / financial_data['ebitda'] if financial_data.get('ebitda') else float('inf')
        indicators['ev_ebit'] = ev / financial_data['ebit'] if financial_data.get('ebit') else float('inf')
        indicators['p_sr'] = financial_data.get('valor_mercado', 0) / financial_data[
            'receita_liquida'] if financial_data.get('receita_liquida') else float('inf')
        indicators['p_ativo'] = financial_data.get('valor_mercado', 0) / financial_data.get('ativo_total',
                                                                                            0) if financial_data.get(
            'ativo_total') else float('inf')
        indicators['vpa'] = financial_data['pl'] / num_acoes if financial_data.get('pl') else float('inf')
        indicators['lpa'] = financial_data['lucro_liquido'] / num_acoes if financial_data.get(
            'lucro_liquido') else float('inf')
        # PEG Ratio: (P/L) / (CAGR Lucro 5 anos * 100)
        cagr_lucro = financial_data.get('cagr_lucro_5_anos', 0)
        indicators['peg_ratio'] = indicators['p_l'] / (cagr_lucro * 100) if cagr_lucro > 0 else float('inf')

        # Indicadores de Rentabilidade
        indicators['margem_bruta'] = financial_data.get('lucro_bruto', 0) / financial_data[
            'receita_liquida'] if financial_data.get('receita_liquida') else float('inf')
        indicators['margem_ebitda'] = financial_data['ebitda'] / financial_data[
            'receita_liquida'] if financial_data.get('receita_liquida') else float('inf')
        indicators['margem_ebit'] = financial_data['ebit'] / financial_data['receita_liquida'] if financial_data.get(
            'receita_liquida') else float('inf')
        indicators['margem_liquida'] = financial_data['lucro_liquido'] / financial_data[
            'receita_liquida'] if financial_data.get('receita_liquida') else float('inf')
        indicators['roe'] = financial_data['lucro_liquido'] / financial_data['pl'] if financial_data.get(
            'pl') else float('inf')
        indicators['roa'] = financial_data['lucro_liquido'] / financial_data.get('ativo_total',
                                                                                 0) if financial_data.get(
            'ativo_total') else float('inf')
        # ROIC: (EBIT - Impostos) / (Patrimônio Líquido + Dívida Líquida)
        impostos = financial_data.get('impostos', 0)
        capital_investido = financial_data['pl'] + divida_liquida if financial_data.get('pl') else 0
        indicators['roic'] = (financial_data[
                                  'ebit'] - impostos) / capital_investido if capital_investido != 0 else float('inf')

        # Indicadores de Endividamento
        indicators['divida_liquida_ebitda'] = divida_liquida / financial_data['ebitda'] if financial_data.get(
            'ebitda') else float('inf')
        indicators['divida_bruta_ebitda'] = financial_data.get('divida_total', 0) / financial_data[
            'ebitda'] if financial_data.get('ebitda') else float('inf')
        indicators['divida_liquida_pl'] = divida_liquida / financial_data['pl'] if financial_data.get('pl') else float(
            'inf')

        # Indicadores de Eficiência
        indicators['giro_ativo'] = financial_data['receita_liquida'] / financial_data.get('ativo_total',
                                                                                          0) if financial_data.get(
            'ativo_total') else float('inf')

        # Indicadores de Proventos
        indicators['dividend_yield'] = financial_data.get('dividendos_pagos', 0) / financial_data.get('valor_mercado',
                                                                                                      0) if financial_data.get(
            'valor_mercado') else 0

        # Indicadores de Crescimento
        indicators['cagr_receita_5_anos'] = financial_data.get('cagr_receita_5_anos', 0)
        indicators['cagr_lucro_5_anos'] = financial_data.get('cagr_lucro_5_anos', 0)

        # Armazena EV para uso na avaliação
        indicators['ev'] = ev
    except ZeroDivisionError:
        pass  # Já tratado pelas funções de avaliação
    return indicators


def cross_validate_indicators(indicators):
    """Realiza validação cruzada dos indicadores e retorna um relatório com alertas de inconsistências."""
    results = {}
    alerts = []

    # Avaliar indicadores
    results['p_l'] = evaluate_p_l(indicators.get('p_l', float('inf')), indicators.get('lucro_liquido', 0))
    results['p_vp'] = evaluate_p_vp(indicators.get('p_vp', float('inf')), indicators.get('vp', 0))
    results['p_ebitda'] = evaluate_p_ebitda(indicators.get('p_ebitda', float('inf')), indicators.get('ebitda', 0))
    results['p_ebit'] = evaluate_p_ebit(indicators.get('p_ebit', float('inf')), indicators.get('ebit', 0))
    results['ev_ebitda'] = evaluate_ev_ebitda(indicators.get('ev_ebitda', float('inf')), indicators.get('ebitda', 0),
                                              indicators.get('ev', 0))
    results['ev_ebit'] = evaluate_ev_ebit(indicators.get('ev_ebit', float('inf')), indicators.get('ebit', 0))
    results['p_sr'] = evaluate_p_sr(indicators.get('p_sr', float('inf')))
    results['p_ativo'] = evaluate_p_ativo(indicators.get('p_ativo', float('inf')))
    results['vpa'] = evaluate_vpa(indicators.get('vpa', float('inf')), indicators.get('pl', 0))
    results['lpa'] = evaluate_lpa(indicators.get('lpa', float('inf')))
    results['peg_ratio'] = evaluate_peg_ratio(indicators.get('peg_ratio', float('inf')))
    results['margem_bruta'] = evaluate_margem_bruta(indicators.get('margem_bruta', float('inf')))
    results['margem_ebitda'] = evaluate_margem_ebitda(indicators.get('margem_ebitda', float('inf')))
    results['margem_ebit'] = evaluate_margem_ebit(indicators.get('margem_ebit', float('inf')))
    results['margem_liquida'] = evaluate_margem_liquida(indicators.get('margem_liquida', float('inf')))
    results['roe'] = evaluate_roe(indicators.get('roe', float('inf')), indicators.get('pl', 0))
    results['roa'] = evaluate_roa(indicators.get('roa', float('inf')))
    results['roic'] = evaluate_roic(indicators.get('roic', float('inf')))
    results['divida_liquida_ebitda'] = evaluate_divida_liquida_ebitda(
        indicators.get('divida_liquida_ebitda', float('inf')), indicators.get('ebitda', 0))
    results['divida_bruta_ebitda'] = evaluate_divida_bruta_ebitda(indicators.get('divida_bruta_ebitda', float('inf')),
                                                                  indicators.get('ebitda', 0))
    results['divida_liquida_pl'] = evaluate_divida_liquida_pl(indicators.get('divida_liquida_pl', float('inf')),
                                                              indicators.get('pl', 0))
    results['giro_ativo'] = evaluate_giro_ativo(indicators.get('giro_ativo', float('inf')))
    results['dividend_yield'] = evaluate_dividend_yield(indicators.get('dividend_yield', 0))
    results['cagr_receita_5_anos'] = evaluate_cagr_receita_5_anos(indicators.get('cagr_receita_5_anos', 0))
    results['cagr_lucro_5_anos'] = evaluate_cagr_lucro_5_anos(indicators.get('cagr_lucro_5_anos', 0))

    # Validação cruzada
    valuation_metrics = ['p_l', 'p_ebit', 'p_ebitda', 'ev_ebitda', 'ev_ebit', 'p_sr', 'p_ativo']
    valuation_results = [results[m] for m in valuation_metrics]
    if 'otimo' in valuation_results and 'pessimo' in valuation_results:
        alerts.append(
            "Inconsistência: Avaliações de valuation (P/L, P/EBIT, P/EBITDA, EV/EBITDA, EV/EBIT, P/SR, P/Ativo) muito discrepantes.")

    margin_metrics = ['margem_bruta', 'margem_ebit', 'margem_ebitda', 'margem_liquida']
    margin_results = [results[m] for m in margin_metrics]
    if 'otimo' in margin_results and 'critico' in margin_results:
        alerts.append("Inconsistência: Margens (Bruta, EBIT, EBITDA, Líquida) com avaliações muito discrepantes.")

    debt_metrics = ['divida_liquida_ebitda', 'divida_bruta_ebitda', 'divida_liquida_pl']
    debt_results = [results[m] for m in debt_metrics]
    if 'otimo' in debt_results and 'pessimo' in debt_results:
        alerts.append(
            "Inconsistência: Indicadores de endividamento (Div. Líquida/EBITDA, Div. Bruta/EBITDA, Div. Líquida/PL) muito discrepantes.")

    profitability_metrics = ['roe', 'roa', 'roic']
    profitability_results = [results[m] for m in profitability_metrics]
    if 'otimo' in profitability_results and 'critico' in profitability_results:
        alerts.append(
            "Inconsistência: Indicadores de rentabilidade (ROE, ROA, ROIC) com avaliações muito discrepantes.")

    if results['roe'] == 'critico' and (results['p_l'] in ['otimo', 'bom'] or results['p_vp'] in ['otimo', 'bom']):
        alerts.append("Inconsistência: ROE crítico, mas P/L ou P/VP são favoráveis.")

    return results, alerts


# Exemplo de uso com a Vale S.A.
if __name__ == "__main__":
    # Cenário 1: Dados Reais da Vale
    print("Cenário 1: Vale com Dados Reais")
    financial_data_real = {
        'divida_total': 78000,
        'caixa': 21000,
        'ebit': 90000,
        'ebitda': 110000,
        'pl': 140000,
        'lucro_liquido': 65000,
        'receita_liquida': 210000,
        'lucro_bruto': 95000,
        'ativo_total': 450000,
        'valor_mercado': 301000,
        'preco_acao': 70,
        'vp': 140000 / 4300,
        'num_acoes': 4300,
        'dividendos_pagos': 15000,
        'cagr_receita_5_anos': 0.1,
        'cagr_lucro_5_anos': 0.12,
        'impostos': 20000
    }
    indicators_real = calculate_indicators(financial_data_real)
    results_real, alerts_real = cross_validate_indicators(indicators_real)

    print("Resultados:")
    for indicator, result in results_real.items():
        print(f"{indicator}: {result}")
    print("\nAlertas:")
    for alert in alerts_real:
        print(f"- {alert}")

    # Cenário 2: Hipotético com Denominadores Negativos
    print("\nCenário 2: Vale com Denominadores Negativos (Hipotético)")
    financial_data_hypothetical = {
        'divida_total': 78000,
        'caixa': 21000,
        'ebit': -10000,
        'ebitda': -5000,
        'pl': -10000,
        'lucro_liquido': -15000,
        'receita_liquida': -5000,
        'lucro_bruto': -2000,
        'ativo_total': 450000,
        'valor_mercado': 301000,
        'preco_acao': 70,
        'vp': -10000 / 4300,
        'num_acoes': 4300,
        'dividendos_pagos': 0,
        'cagr_receita_5_anos': -0.05,
        'cagr_lucro_5_anos': -0.03,
        'impostos': 0
    }
    indicators_hypothetical = calculate_indicators(financial_data_hypothetical)
    results_hypothetical, alerts_hypothetical = cross_validate_indicators(indicators_hypothetical)

    print("Resultados:")
    for indicator, result in results_hypothetical.items():
        print(f"{indicator}: {result}")
    print("\nAlertas:")
    for alert in alerts_hypothetical:
        print(f"- {alert}")