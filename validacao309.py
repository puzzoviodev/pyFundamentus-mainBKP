def evaluate_div_liquida_ebit(value, ebit):
    if ebit <= 0:  # EBIT negativo ou zero indica problemas operacionais
        return 'critico'
    if value < 0:  # Dívida líquida negativa (excesso de caixa)
        return 'otimo'
    elif value == 0:
        return 'bom'
    elif value <= 1.5:
        return 'bom'
    elif value <= 3:
        return 'moderado'
    elif value <= 4:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_div_liquida_ebitda(value, ebitda):
    if ebitda <= 0:  # EBITDA negativo ou zero indica problemas operacionais
        return 'critico'
    if value < 0:  # Dívida líquida negativa (excesso de caixa)
        return 'otimo'
    elif value == 0:
        return 'bom'
    elif value <= 1:
        return 'bom'
    elif value <= 2.5:
        return 'moderado'
    elif value <= 3.5:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_div_liquida_pl(value, pl):
    if pl <= 0:  # Patrimônio Líquido negativo indica insolvência
        return 'critico'
    if value < 0:  # Dívida líquida negativa é favorável
        return 'otimo'
    elif value <= 0.3:
        return 'bom'
    elif value <= 0.7:
        return 'moderado'
    elif value <= 1:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_dy(value):
    if value == 0:  # Ausência de dividendos
        return 'critico'
    elif value <= 0.02:
        return 'ruim'
    elif value <= 0.04:
        return 'moderado'
    elif value <= 0.06:
        return 'bom'
    else:
        return 'otimo'


def evaluate_ev_ebit(value, ebit):
    if ebit <= 0:  # EBIT negativo ou zero indica problemas operacionais
        return 'critico'
    if value < 0:  # EV/EBIT negativo é favorável
        return 'otimo'
    elif value <= 4:
        return 'otimo'
    elif value <= 8:
        return 'bom'
    elif value <= 12:
        return 'moderado'
    elif value <= 15:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_ev_ebitda(value, ebitda):
    if ebitda <= 0:  # EBITDA negativo ou zero indica problemas operacionais
        return 'critico'
    if value < 0:  # EV/EBITDA negativo é favorável
        return 'otimo'
    elif value <= 3:
        return 'otimo'
    elif value <= 6:
        return 'bom'
    elif value <= 10:
        return 'moderado'
    elif value <= 12:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_giro_ativo(value):
    if value <= 0:  # Receita Líquida ou Ativo Total zero/negativo
        return 'critico'
    elif value <= 0.2:
        return 'pessimo'
    elif value <= 0.4:
        return 'ruim'
    elif value <= 0.8:
        return 'moderado'
    elif value <= 1.2:
        return 'bom'
    else:
        return 'otimo'


def evaluate_liq_corrente(value):
    if value <= 0:  # Ativo Circulante zero/negativo
        return 'critico'
    elif value <= 0.8:
        return 'pessimo'
    elif value <= 1.2:
        return 'ruim'
    elif value <= 1.8:
        return 'moderado'
    elif value <= 2.5:
        return 'bom'
    else:
        return 'otimo'


def evaluate_lpa(value):
    if value <= 0:  # Lucro Líquido ou número de ações zero/negativo
        return 'critico'
    elif value <= 0.1:
        return 'pessimo'
    elif value <= 0.5:
        return 'ruim'
    elif value <= 1:
        return 'moderado'
    elif value <= 2:
        return 'bom'
    else:
        return 'otimo'


def evaluate_m_bruta(value):
    if value <= 0 or value == float('inf'):  # Lucro Bruto ou Receita Líquida zero/negativo
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


def evaluate_m_ebit(value):
    if value <= 0 or value == float('inf'):  # EBIT ou Receita Líquida zero/negativo
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.15:
        return 'ruim'
    elif value <= 0.25:
        return 'moderado'
    elif value <= 0.35:
        return 'bom'
    else:
        return 'otimo'


def evaluate_m_ebitda(value):
    if value <= 0 or value == float('inf'):  # EBITDA ou Receita Líquida zero/negativo
        return 'critico'
    elif value <= 0.1:
        return 'pessimo'
    elif value <= 0.2:
        return 'ruim'
    elif value <= 0.3:
        return 'moderado'
    elif value <= 0.4:
        return 'bom'
    else:
        return 'otimo'


def evaluate_m_liquida(value):
    if value <= 0 or value == float('inf'):  # Lucro Líquido ou Receita Líquida zero/negativo
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.1:
        return 'ruim'
    elif value <= 0.15:
        return 'moderado'
    elif value <= 0.25:
        return 'bom'
    else:
        return 'otimo'


def evaluate_p_ativo_circulante_liquido(value, ativo_circulante_liquido):
    if ativo_circulante_liquido <= 0:  # Ativo Circulante Líquido negativo indica problemas de liquidez
        return 'critico'
    if value <= 0 or value == float('inf'):
        return 'critico'
    elif value <= 1:
        return 'ruim'
    elif value <= 2:
        return 'moderado'
    elif value <= 3:
        return 'bom'
    else:
        return 'otimo'


def evaluate_p_capital_giro(value, capital_giro):
    if capital_giro <= 0:  # Capital de Giro negativo indica problemas de liquidez
        return 'critico'
    if value <= 0 or value == float('inf'):
        return 'critico'
    elif value <= 2:
        return 'ruim'
    elif value <= 4:
        return 'moderado'
    elif value <= 6:
        return 'bom'
    else:
        return 'otimo'


def evaluate_p_ebit(value, ebit):
    if ebit <= 0:  # EBIT negativo ou zero indica problemas operacionais
        return 'critico'
    if value <= 5:  # Inclui valores negativos e até 5 como ótimo
        return 'otimo'
    elif value <= 10:
        return 'bom'
    elif value <= 15:
        return 'moderado'
    elif value <= 20:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_p_ebitda(value, ebitda):
    if ebitda <= 0:  # EBITDA negativo ou zero indica problemas operacionais
        return 'critico'
    if value <= 3:  # Inclui valores negativos e até 3 como ótimo
        return 'otimo'
    elif value <= 6:
        return 'bom'
    elif value <= 10:
        return 'moderado'
    elif value <= 15:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_p_l(value, lucro_liquido):
    if lucro_liquido <= 0:  # Lucro Líquido negativo indica prejuízo
        return 'critico'
    if value <= 5:  # Inclui valores negativos e até 5 como ótimo
        return 'otimo'
    elif value <= 10:
        return 'bom'
    elif value <= 15:
        return 'moderado'
    elif value <= 20:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_p_vp(value, vp):
    if vp <= 0:  # Valor Patrimonial negativo indica insolvência
        return 'critico'
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


def evaluate_p_ativo(value):
    if value <= 0:  # Ativo Total zero/negativo
        return 'critico'
    elif value <= 0.2:
        return 'pessimo'
    elif value <= 0.3:
        return 'ruim'
    elif value <= 0.5:
        return 'moderado'
    elif value <= 0.8:
        return 'bom'
    else:
        return 'otimo'


def evaluate_pl_ativos(value, pl):
    if pl <= 0:  # Patrimônio Líquido negativo indica insolvência
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.2:
        return 'pessimo'
    elif value <= 0.5:
        return 'ruim'
    elif value <= 0.8:
        return 'moderado'
    elif value <= 1:
        return 'bom'
    else:
        return 'otimo'


def evaluate_psr(value):
    if value <= 0 or value == float('inf'):  # Receita Líquida zero/negativa
        return 'critico'
    elif value <= 0.5:
        return 'otimo'
    elif value <= 1:
        return 'bom'
    elif value <= 2:
        return 'moderado'
    elif value <= 3:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_p_sales_ratio(value):
    if value <= 0 or value == float('inf'):  # Receita Líquida zero/negativa
        return 'critico'
    elif value <= 0.5:
        return 'otimo'
    elif value <= 1:
        return 'bom'
    elif value <= 2:
        return 'moderado'
    elif value <= 3:
        return 'ruim'
    else:
        return 'pessimo'


def evaluate_roa(value):
    if value <= 0:  # Lucro Líquido ou Ativo Total zero/negativo
        return 'critico'
    elif value <= 0.03:
        return 'pessimo'
    elif value <= 0.08:
        return 'ruim'
    elif value <= 0.15:
        return 'moderado'
    elif value <= 0.25:
        return 'bom'
    else:
        return 'otimo'


def evaluate_roe(value, pl):
    if pl <= 0:  # Patrimônio Líquido negativo indica insolvência
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.1:
        return 'ruim'
    elif value <= 0.15:
        return 'moderado'
    elif value <= 0.25:
        return 'bom'
    else:
        return 'otimo'


def evaluate_roic(value):
    if value <= 0:  # Lucro Operacional ou Capital Investido zero/negativo
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


def evaluate_vpa(value, pl):
    if pl <= 0:  # Patrimônio Líquido negativo indica insolvência
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


def evaluate_cagr_lucros_5_anos(value):
    if value <= 0:  # Crescimento nulo ou negativo
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


def evaluate_divida_bruta(value, ebitda):
    if ebitda <= 0:  # EBITDA negativo ou zero indica problemas operacionais
        return 'critico'
    if value <= 0:  # Dívida Bruta zero
        return 'otimo'
    elif value <= 1:
        return 'bom'
    elif value <= 2:
        return 'moderado'
    elif value <= 3:
        return 'ruim'
    else:
        return 'pessimo'


def calculate_indicators(financial_data):
    """Calcula os valores dos indicadores a partir dos dados financeiros brutos."""
    indicators = {}
    try:
        # Dívida Líquida
        divida_liquida = financial_data.get('divida_total', 0) - financial_data.get('caixa', 0)

        # Indicadores
        indicators['div_liquida_ebit'] = divida_liquida / financial_data['ebit'] if financial_data.get(
            'ebit') else float('inf')
        indicators['div_liquida_ebitda'] = divida_liquida / financial_data['ebitda'] if financial_data.get(
            'ebitda') else float('inf')
        indicators['div_liquida_pl'] = divida_liquida / financial_data['pl'] if financial_data.get('pl') else float(
            'inf')
        indicators['m_bruta'] = financial_data.get('lucro_bruto', 0) / financial_data[
            'receita_liquida'] if financial_data.get('receita_liquida') else float('inf')
        indicators['m_ebit'] = financial_data['ebit'] / financial_data['receita_liquida'] if financial_data.get(
            'receita_liquida') else float('inf')
        indicators['m_ebitda'] = financial_data['ebitda'] / financial_data['receita_liquida'] if financial_data.get(
            'receita_liquida') else float('inf')
        indicators['m_liquida'] = financial_data['lucro_liquido'] / financial_data[
            'receita_liquida'] if financial_data.get('receita_liquida') else float('inf')
        indicators['p_ativo_circulante_liquido'] = financial_data.get('valor_mercado', 0) / financial_data[
            'ativo_circulante_liquido'] if financial_data.get('ativo_circulante_liquido') else float('inf')
        indicators['p_capital_giro'] = financial_data.get('valor_mercado', 0) / financial_data[
            'capital_giro'] if financial_data.get('capital_giro') else float('inf')
        indicators['p_ebit'] = financial_data.get('valor_mercado', 0) / financial_data['ebit'] if financial_data.get(
            'ebit') else float('inf')
        indicators['p_ebitda'] = financial_data.get('valor_mercado', 0) / financial_data[
            'ebitda'] if financial_data.get('ebitda') else float('inf')
        indicators['p_l'] = financial_data.get('valor_mercado', 0) / financial_data[
            'lucro_liquido'] if financial_data.get('lucro_liquido') else float('inf')
        indicators['p_vp'] = financial_data.get('preco_acao', 0) / financial_data['vp'] if financial_data.get(
            'vp') else float('inf')
        indicators['pl_ativos'] = financial_data['pl'] / financial_data.get('ativo_total', 0) if financial_data.get(
            'ativo_total') else float('inf')
        indicators['psr'] = financial_data.get('valor_mercado', 0) / financial_data[
            'receita_liquida'] if financial_data.get('receita_liquida') else float('inf')
        indicators['p_sales_ratio'] = indicators['psr']  # Duplicado
        indicators['roe'] = financial_data['lucro_liquido'] / financial_data['pl'] if financial_data.get(
            'pl') else float('inf')
        indicators['vpa'] = financial_data['pl'] / financial_data.get('num_acoes', 1) if financial_data.get(
            'pl') else float('inf')
        indicators['divida_bruta'] = financial_data.get('divida_total', 0) / financial_data[
            'ebitda'] if financial_data.get('ebitda') else float('inf')
    except ZeroDivisionError:
        pass  # Já tratado pelas funções de avaliação
    return indicators


def cross_validate_indicators(indicators):
    """Realiza validação cruzada dos indicadores e retorna um relatório com alertas de inconsistências."""
    results = {}
    alerts = []

    # Avaliar indicadores
    results['div_liquida_ebit'] = evaluate_div_liquida_ebit(indicators.get('div_liquida_ebit', float('inf')),
                                                            indicators.get('ebit', 0))
    results['div_liquida_ebitda'] = evaluate_div_liquida_ebitda(indicators.get('div_liquida_ebitda', float('inf')),
                                                                indicators.get('ebitda', 0))
    results['div_liquida_pl'] = evaluate_div_liquida_pl(indicators.get('div_liquida_pl', float('inf')),
                                                        indicators.get('pl', 0))
    results['m_bruta'] = evaluate_m_bruta(indicators.get('m_bruta', float('inf')))
    results['m_ebit'] = evaluate_m_ebit(indicators.get('m_ebit', float('inf')))
    results['m_ebitda'] = evaluate_m_ebitda(indicators.get('m_ebitda', float('inf')))
    results['m_liquida'] = evaluate_m_liquida(indicators.get('m_liquida', float('inf')))
    results['p_ativo_circulante_liquido'] = evaluate_p_ativo_circulante_liquido(
        indicators.get('p_ativo_circulante_liquido', float('inf')), indicators.get('ativo_circulante_liquido', 0))
    results['p_capital_giro'] = evaluate_p_capital_giro(indicators.get('p_capital_giro', float('inf')),
                                                        indicators.get('capital_giro', 0))
    results['p_ebit'] = evaluate_p_ebit(indicators.get('p_ebit', float('inf')), indicators.get('ebit', 0))
    results['p_ebitda'] = evaluate_p_ebitda(indicators.get('p_ebitda', float('inf')), indicators.get('ebitda', 0))
    results['p_l'] = evaluate_p_l(indicators.get('p_l', float('inf')), indicators.get('lucro_liquido', 0))
    results['p_vp'] = evaluate_p_vp(indicators.get('p_vp', float('inf')), indicators.get('vp', 0))
    results['pl_ativos'] = evaluate_pl_ativos(indicators.get('pl_ativos', float('inf')), indicators.get('pl', 0))
    results['psr'] = evaluate_psr(indicators.get('psr', float('inf')))
    results['p_sales_ratio'] = evaluate_p_sales_ratio(indicators.get('p_sales_ratio', float('inf')))
    results['roe'] = evaluate_roe(indicators.get('roe', float('inf')), indicators.get('pl', 0))
    results['vpa'] = evaluate_vpa(indicators.get('vpa', float('inf')), indicators.get('pl', 0))
    results['divida_bruta'] = evaluate_divida_bruta(indicators.get('divida_bruta', float('inf')),
                                                    indicators.get('ebitda', 0))

    # Validação cruzada
    # 1. Consistência entre P/L, P/EBIT, P/EBITDA
    valuation_metrics = ['p_l', 'p_ebit', 'p_ebitda']
    valuation_results = [results[m] for m in valuation_metrics]
    if 'otimo' in valuation_results and 'pessimo' in valuation_results:
        alerts.append("Inconsistência: Avaliações de valuation (P/L, P/EBIT, P/EBITDA) muito discrepantes.")

    # 2. Consistência entre Margens
    margin_metrics = ['m_bruta', 'm_ebit', 'm_ebitda', 'm_liquida']
    margin_results = [results[m] for m in margin_metrics]
    if 'otimo' in margin_results and 'critico' in margin_results:
        alerts.append("Inconsistência: Margens (Bruta, EBIT, EBITDA, Líquida) com avaliações muito discrepantes.")

    # 3. Consistência entre indicadores de endividamento
    debt_metrics = ['div_liquida_ebit', 'div_liquida_ebitda', 'div_liquida_pl', 'divida_bruta']
    debt_results = [results[m] for m in debt_metrics]
    if 'otimo' in debt_results and 'pessimo' in debt_results:
        alerts.append(
            "Inconsistência: Indicadores de endividamento (Div. Líquida/EBIT, Div. Líquida/EBITDA, Div. Líquida/PL, Dívida Bruta) muito discrepantes.")

    # 4. Consistência entre ROE, P/L e P/VP
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
        'ativo_circulante_liquido': 25000,
        'capital_giro': 25000,
        'valor_mercado': 301000,
        'preco_acao': 70,
        'vp': 140000 / 4300,
        'ativo_total': 450000,
        'num_acoes': 4300
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
        'ativo_circulante_liquido': -5000,
        'capital_giro': -5000,
        'valor_mercado': 301000,
        'preco_acao': 70,
        'vp': -10000 / 4300,
        'ativo_total': 450000,
        'num_acoes': 4300
    }
    indicators_hypothetical = calculate_indicators(financial_data_hypothetical)
    results_hypothetical, alerts_hypothetical = cross_validate_indicators(indicators_hypothetical)

    print("Resultados:")
    for indicator, result in results_hypothetical.items():
        print(f"{indicator}: {result}")
    print("\nAlertas:")
    for alert in alerts_hypothetical:
        print(f"- {alert}")