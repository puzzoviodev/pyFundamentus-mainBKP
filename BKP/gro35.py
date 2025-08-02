import unittest

def evaluate_pl(pl):
    """
    Avalia o Preço/Lucro (P/L) com base em faixas refinadas para o mercado brasileiro.
    - P/L < 0: Crítico (prejuízo)
    - 0 ≤ P/L ≤ 7: Ótimo (subvalorizado)
    - 7 < P/L ≤ 15: Moderado (justo)
    - 15 < P/L ≤ 25: Ruim (sobrevalorizado)
    - 25 < P/L ≤ 35: Péssimo (muito caro)
    - P/L > 35: Fora da faixa (extremamente sobrevalorizado)
    """
    if not isinstance(pl, (int, float)):
        raise TypeError("P/L deve ser um número (int ou float)")
    if pl < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/L < 0', 'descricao': 'P/L negativo indica prejuízo, comum em setores cíclicos (ex.: celulose) ou empresas em crise. Exige análise de recuperação.'}
    elif 0 <= pl <= 7:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/L <= 7', 'descricao': 'P/L baixo sugere subvalorização, atrativo para investidores de valor. Comum em bancos (ex.: ITUB4) e utilities.'}
    elif 7 < pl <= 15:
        return {'classificacao': 'Moderado', 'faixa': '7 < P/L <= 15', 'descricao': 'P/L indica valuation justo, típico de empresas com crescimento estável (ex.: ENGI11).'}
    elif 15 < pl <= 25:
        return {'classificacao': 'Ruim', 'faixa': '15 < P/L <= 25', 'descricao': 'P/L elevado sugere sobrevalorização, comum em setores de crescimento (ex.: MGLU3). Exige cautela.'}
    elif 25 < pl <= 35:
        return {'classificacao': 'Péssimo', 'faixa': '25 < P/L <= 35', 'descricao': 'P/L muito alto indica ação cara, com risco de correção. Comum em empresas com altas expectativas.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/L > 35', 'descricao': 'P/L extremamente elevado, típico de startups ou empresas em bolhas. Alto risco.'}

def evaluate_pebitda(pebitda):
    """
    Avalia o Preço/EBITDA com base em faixas refinadas para o mercado brasileiro.
    - P/EBITDA < 0: Crítico (EBITDA negativo)
    - 0 ≤ P/EBITDA ≤ 4: Ótimo (subvalorizado)
    - 4 < P/EBITDA ≤ 7: Moderado (justo)
    - 7 < P/EBITDA ≤ 10: Ruim (sobrevalorizado)
    - 10 < P/EBITDA ≤ 15: Péssimo (muito caro)
    - P/EBITDA > 15: Fora da faixa (extremamente sobrevalorizado)
    """
    if not isinstance(pebitda, (int, float)):
        raise TypeError("P/EBITDA deve ser um número (int ou float)")
    if pebitda < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/EBITDA < 0', 'descricao': 'P/EBITDA negativo indica EBITDA negativo, sugerindo ineficiência operacional.'}
    elif 0 <= pebitda <= 4:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/EBITDA <= 4', 'descricao': 'P/EBITDA baixo sugere subvalorização, comum em setores cíclicos (ex.: GGBR4). Oportunidade de compra.'}
    elif 4 < pebitda <= 7:
        return {'classificacao': 'Moderado', 'faixa': '4 < P/EBITDA <= 7', 'descricao': 'P/EBITDA indica valuation justo, típico de empresas estáveis (ex.: CPLE6).'}
    elif 7 < pebitda <= 10:
        return {'classificacao': 'Ruim', 'faixa': '7 < P/EBITDA <= 10', 'descricao': 'P/EBITDA elevado sugere sobrevalorização, comum em varejo (ex.: MGLU3).'}
    elif 10 < pebitda <= 15:
        return {'classificacao': 'Péssimo', 'faixa': '10 < P/EBITDA <= 15', 'descricao': 'P/EBITDA muito alto indica ação cara, com risco de correção.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/EBITDA > 15', 'descricao': 'P/EBITDA extremamente elevado, típico de empresas de tecnologia em crescimento.'}

def evaluate_pvp(pvp):
    """
    Avalia o Preço/Valor Patrimonial (P/VP) com base em faixas refinadas.
    - P/VP < 0: Crítico (patrimônio negativo)
    - 0 ≤ P/VP ≤ 0.8: Ótimo (subvalorizado)
    - 0.8 < P/VP ≤ 1.5: Moderado (justo)
    - 1.5 < P/VP ≤ 2.5: Ruim (sobrevalorizado)
    - 2.5 < P/VP ≤ 4: Péssimo (muito caro)
    - P/VP > 4: Fora da faixa (extremamente sobrevalorizado)
    """
    if not isinstance(pvp, (int, float)):
        raise TypeError("P/VP deve ser um número (int ou float)")
    if pvp < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/VP < 0', 'descricao': 'P/VP negativo indica patrimônio líquido negativo, sugerindo insolvência.'}
    elif 0 <= pvp <= 0.8:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/VP <= 0.8', 'descricao': 'P/VP baixo sugere subvalorização, comum em bancos (ex.: BBDC4) e setores maduros.'}
    elif 0.8 < pvp <= 1.5:
        return {'classificacao': 'Moderado', 'faixa': '0.8 < P/VP <= 1.5', 'descricao': 'P/VP indica valuation justo, típico de indústrias (ex.: SUZB3).'}
    elif 1.5 < pvp <= 2.5:
        return {'classificacao': 'Ruim', 'faixa': '1.5 < P/VP <= 2.5', 'descricao': 'P/VP elevado sugere sobrevalorização, comum em varejo (ex.: LREN3).'}
    elif 2.5 < pvp <= 4:
        return {'classificacao': 'Péssimo', 'faixa': '2.5 < P/VP <= 4', 'descricao': 'P/VP muito alto indica ação cara, comum em tecnologia (ex.: TOTS3).'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/VP > 4', 'descricao': 'P/VP extremamente elevado, típico de startups ou empresas com intangíveis.'}

def evaluate_pebit(pebit):
    """
    Avalia o Preço/EBIT com base em faixas refinadas.
    - P/EBIT < 0: Crítico (EBIT negativo)
    - 0 ≤ P/EBIT ≤ 5: Ótimo (subvalorizado)
    - 5 < P/EBIT ≤ 10: Moderado (justo)
    - 10 < P/EBIT ≤ 15: Ruim (sobrevalorizado)
    - 15 < P/EBIT ≤ 20: Péssimo (muito caro)
    - P/EBIT > 20: Fora da faixa (extremamente sobrevalorizado)
    """
    if not isinstance(pebit, (int, float)):
        raise TypeError("P/EBIT deve ser um número (int ou float)")
    if pebit < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/EBIT < 0', 'descricao': 'P/EBIT negativo indica EBIT negativo, sugerindo ineficiência operacional.'}
    elif 0 <= pebit <= 5:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/EBIT <= 5', 'descricao': 'P/EBIT baixo sugere subvalorização, comum em setores com alta depreciação (ex.: siderurgia).'}
    elif 5 < pebit <= 10:
        return {'classificacao': 'Moderado', 'faixa': '5 < P/EBIT <= 10', 'descricao': 'P/EBIT indica valuation justo, típico de empresas estáveis (ex.: energia).'}
    elif 10 < pebit <= 15:
        return {'classificacao': 'Ruim', 'faixa': '10 < P/EBIT <= 15', 'descricao': 'P/EBIT elevado sugere sobrevalorização, comum em varejo.'}
    elif 15 < pebit <= 20:
        return {'classificacao': 'Péssimo', 'faixa': '15 < P/EBIT <= 20', 'descricao': 'P/EBIT muito alto indica ação cara.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/EBIT > 20', 'descricao': 'P/EBIT extremamente elevado, típico de empresas de crescimento.'}

def evaluate_evebitda(evebitda):
    """
    Avalia o EV/EBITDA com base em faixas refinadas.
    - EV/EBITDA < 0: Crítico (EBITDA negativo)
    - 0 ≤ EV/EBITDA ≤ 4: Ótimo (subvalorizado)
    - 4 < EV/EBITDA ≤ 7: Moderado (justo)
    - 7 < EV/EBITDA ≤ 10: Ruim (sobrevalorizado)
    - 10 < EV/EBITDA ≤ 15: Péssimo (muito caro)
    - EV/EBITDA > 15: Fora da faixa (extremamente sobrevalorizado)
    """
    if not isinstance(evebitda, (int, float)):
        raise TypeError("EV/EBITDA deve ser um número (int ou float)")
    if evebitda < 0:
        return {'classificacao': 'Crítico', 'faixa': 'EV/EBITDA < 0', 'descricao': 'EV/EBITDA negativo indica EBITDA negativo, sugerindo problemas operacionais.'}
    elif 0 <= evebitda <= 4:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= EV/EBITDA <= 4', 'descricao': 'EV/EBITDA baixo sugere subvalorização, comum em mineração (ex.: VALE3).'}
    elif 4 < evebitda <= 7:
        return {'classificacao': 'Moderado', 'faixa': '4 < EV/EBITDA <= 7', 'descricao': 'EV/EBITDA indica valuation justo, típico de energia (ex.: ELET3).'}
    elif 7 < evebitda <= 10:
        return {'classificacao': 'Ruim', 'faixa': '7 < EV/EBITDA <= 10', 'descricao': 'EV/EBITDA elevado sugere sobrevalorização, comum em consumo (ex.: ABEV3).'}
    elif 10 < evebitda <= 15:
        return {'classificacao': 'Péssimo', 'faixa': '10 < EV/EBITDA <= 15', 'descricao': 'EV/EBITDA muito alto indica empresa cara.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'EV/EBITDA > 15', 'descricao': 'EV/EBITDA extremamente elevado, típico de tecnologia.'}

def evaluate_evebit(evebit):
    """
    Avalia o EV/EBIT com base em faixas refinadas.
    - EV/EBIT < 0: Crítico (EBIT negativo)
    - 0 ≤ EV/EBIT ≤ 5: Ótimo (subvalorizado)
    - 5 < EV/EBIT ≤ 10: Moderado (justo)
    - 10 < EV/EBIT ≤ 15: Ruim (sobrevalorizado)
    - 15 < EV/EBIT ≤ 20: Péssimo (muito caro)
    - EV/EBIT > 20: Fora da faixa (extremamente sobrevalorizado)
    """
    if not isinstance(evebit, (int, float)):
        raise TypeError("EV/EBIT deve ser um número (int ou float)")
    if evebit < 0:
        return {'classificacao': 'Crítico', 'faixa': 'EV/EBIT < 0', 'descricao': 'EV/EBIT negativo indica EBIT negativo, sugerindo ineficiência.'}
    elif 0 <= evebit <= 5:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= EV/EBIT <= 5', 'descricao': 'EV/EBIT baixo sugere subvalorização, comum em mineração.'}
    elif 5 < evebit <= 10:
        return {'classificacao': 'Moderado', 'faixa': '5 < EV/EBIT <= 10', 'descricao': 'EV/EBIT indica valuation justo, típico de energia.'}
    elif 10 < evebit <= 15:
        return {'classificacao': 'Ruim', 'faixa': '10 < EV/EBIT <= 15', 'descricao': 'EV/EBIT elevado sugere sobrevalorização, comum em consumo.'}
    elif 15 < evebit <= 20:
        return {'classificacao': 'Péssimo', 'faixa': '15 < EV/EBIT <= 20', 'descricao': 'EV/EBIT muito alto indica empresa cara.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'EV/EBIT > 20', 'descricao': 'EV/EBIT extremamente elevado, típico de empresas de crescimento.'}

def evaluate_giro_ativos(giro):
    """
    Avalia o Giro de Ativos (Receita Líquida/Ativos Totais).
    - Giro < 0: Crítico (receita negativa)
    - 0 ≤ Giro ≤ 0.2: Péssimo (eficiência muito baixa)
    - 0.2 < Giro ≤ 0.5: Ruim (eficiência baixa)
    - 0.5 < Giro ≤ 1.0: Moderado (eficiência aceitável)
    - 1.0 < Giro ≤ 2.0: Ótimo (alta eficiência)
    - Giro > 2.0: Fora da faixa (eficiência excepcional)
    """
    if not isinstance(giro, (int, float)):
        raise TypeError("Giro de Ativos deve ser um número (int ou float)")
    if giro < 0:
        return {'classificacao': 'Crítico', 'faixa': 'Giro < 0', 'descricao': 'Giro negativo indica receita negativa, sugerindo graves problemas.'}
    elif 0 <= giro <= 0.2:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= Giro <= 0.2', 'descricao': 'Giro muito baixo, comum em infraestrutura (ex.: CCRD3), indicando baixa eficiência.'}
    elif 0.2 < giro <= 0.5:
        return {'classificacao': 'Ruim', 'faixa': '0.2 < Giro <= 0.5', 'descricao': 'Giro baixo, típico de energia (ex.: CPLE6), com eficiência limitada.'}
    elif 0.5 < giro <= 1.0:
        return {'classificacao': 'Moderado', 'faixa': '0.5 < Giro <= 1.0', 'descricao': 'Giro aceitável, comum em indústria (ex.: WEGE3).'}
    elif 1.0 < giro <= 2.0:
        return {'classificacao': 'Ótimo', 'faixa': '1.0 < Giro <= 2.0', 'descricao': 'Giro alto, indicando alta eficiência, comum em varejo (ex.: MGLU3).'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Giro > 2.0', 'descricao': 'Giro extremamente alto, típico de tecnologia (ex.: TOTS3), mas pode indicar alavancagem.'}

def evaluate_divida_liquida_pl(dl_pl):
    """
    Avalia a Dívida Líquida/Patrimônio Líquido.
    - DL/PL < -1: Crítico (caixa excessivo)
    - -1 ≤ DL/PL < 0: Ótimo (caixa supera dívida)
    - 0 ≤ DL/PL ≤ 0.5: Moderado (endividamento baixo)
    - 0.5 < DL/PL ≤ 1: Ruim (endividamento moderado)
    - 1 < DL/PL ≤ 2: Péssimo (endividamento alto)
    - DL/PL > 2: Fora da faixa (endividamento excessivo)
    """
    if not isinstance(dl_pl, (int, float)):
        raise TypeError("DL/PL deve ser um número (int ou float)")
    if dl_pl < -1:
        return {'classificacao': 'Crítico', 'faixa': 'DL/PL < -1', 'descricao': 'DL/PL extremamente negativa indica caixa excessivo, comum em tecnologia (ex.: WIZS3), mas pode ser ineficiente.'}
    elif -1 <= dl_pl < 0:
        return {'classificacao': 'Ótimo', 'faixa': '-1 <= DL/PL < 0', 'descricao': 'DL/PL negativa indica solidez financeira, comum em tecnologia.'}
    elif 0 <= dl_pl <= 0.5:
        return {'classificacao': 'Moderado', 'faixa': '0 <= DL/PL <= 0.5', 'descricao': 'DL/PL baixa, comum em consumo (ex.: ABEV3).'}
    elif 0.5 < dl_pl <= 1:
        return {'classificacao': 'Ruim', 'faixa': '0.5 < DL/PL <= 1', 'descricao': 'DL/PL moderada, comum em indústria (ex.: SUZB3).'}
    elif 1 < dl_pl <= 2:
        return {'classificacao': 'Péssimo', 'faixa': '1 < DL/PL <= 2', 'descricao': 'DL/PL alta, comum em utilities (ex.: ENGI11), com risco de alavancagem.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'DL/PL > 2', 'descricao': 'DL/PL extremamente alta, comum em construção (ex.: CYRE3), indicando alto risco.'}

def evaluate_divida_liquida_ebitda(dl_ebitda):
    """
    Avalia a Dívida Líquida/EBITDA.
    - DL/EBITDA < -2: Crítico (caixa excessivo)
    - -2 ≤ DL/EBITDA < 0: Ótimo (caixa supera dívida)
    - 0 ≤ DL/EBITDA ≤ 1.5: Moderado (endividamento baixo)
    - 1.5 < DL/EBITDA ≤ 3: Ruim (endividamento moderado)
    - 3 < DL/EBITDA ≤ 4.5: Péssimo (endividamento alto)
    - DL/EBITDA > 4.5: Fora da faixa (endividamento excessivo)
    """
    if not isinstance(dl_ebitda, (int, float)):
        raise TypeError("DL/EBITDA deve ser um número (int ou float)")
    if dl_ebitda < -2:
        return {'classificacao': 'Crítico', 'faixa': 'DL/EBITDA < -2', 'descricao': 'DL/EBITDA extremamente negativa indica caixa excessivo, comum em empresas de caixa alto (ex.: VALE3).'}
    elif -2 <= dl_ebitda < 0:
        return {'classificacao': 'Ótimo', 'faixa': '-2 <= DL/EBITDA < 0', 'descricao': 'DL/EBITDA negativa indica solidez, comum em empresas com alta geração de caixa.'}
    elif 0 <= dl_ebitda <= 1.5:
        return {'classificacao': 'Moderado', 'faixa': '0 <= DL/EBITDA <= 1.5', 'descricao': 'DL/EBITDA baixa, comum em empresas com baixo endividamento (ex.: WEG).'}
    elif 1.5 < dl_ebitda <= 3:
        return {'classificacao': 'Ruim', 'faixa': '1.5 < DL/EBITDA <= 3', 'descricao': 'DL/EBITDA moderada, comum em indústrias (ex.: SUZB3).'}
    elif 3 < dl_ebitda <= 4.5:
        return {'classificacao': 'Péssimo', 'faixa': '3 < DL/EBITDA <= 4.5', 'descricao': 'DL/EBITDA alta, indicando risco de alavancagem.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'DL/EBITDA > 4.5', 'descricao': 'DL/EBITDA extremamente alta, comum em empresas alavancadas (ex.: OI).'}

def evaluate_divida_liquida_ebit(dl_ebit):
    """
    Avalia a Dívida Líquida/EBIT.
    - DL/EBIT < -3: Crítico (caixa excessivo)
    - -3 ≤ DL/EBIT < 0: Ótimo (caixa supera dívida)
    - 0 ≤ DL/EBIT ≤ 2: Moderado (endividamento baixo)
    - 2 < DL/EBIT ≤ 4: Ruim (endividamento moderado)
    - 4 < DL/EBIT ≤ 6: Péssimo (endividamento alto)
    - DL/EBIT > 6: Fora da faixa (endividamento excessivo)
    """
    if not isinstance(dl_ebit, (int, float)):
        raise TypeError("DL/EBIT deve ser um número (int ou float)")
    if dl_ebit < -3:
        return {'classificacao': 'Crítico', 'faixa': 'DL/EBIT < -3', 'descricao': 'DL/EBIT extremamente negativa indica caixa excessivo.'}
    elif -3 <= dl_ebit < 0:
        return {'classificacao': 'Ótimo', 'faixa': '-3 <= DL/EBIT < 0', 'descricao': 'DL/EBIT negativa indica solidez financeira.'}
    elif 0 <= dl_ebit <= 2:
        return {'classificacao': 'Moderado', 'faixa': '0 <= DL/EBIT <= 2', 'descricao': 'DL/EBIT baixa, indicando endividamento controlado.'}
    elif 2 < dl_ebit <= 4:
        return {'classificacao': 'Ruim', 'faixa': '2 < DL/EBIT <= 4', 'descricao': 'DL/EBIT moderada, sugerindo endividamento aceitável.'}
    elif 4 < dl_ebit <= 6:
        return {'classificacao': 'Péssimo', 'faixa': '4 < DL/EBIT <= 6', 'descricao': 'DL/EBIT alta, indicando endividamento elevado.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'DL/EBIT > 6', 'descricao': 'DL/EBIT extremamente alta, sugerindo endividamento excessivo.'}

def evaluate_pl_ativos(pl_ativos):
    """
    Avalia o Patrimônio Líquido/Ativos.
    - PL/Ativos < 0: Crítico (patrimônio negativo)
    - 0 ≤ PL/Ativos ≤ 0.1: Péssimo (alta alavancagem)
    - 0.1 < PL/Ativos ≤ 0.3: Ruim (alavancagem moderada)
    - 0.3 < PL/Ativos ≤ 0.5: Moderado (estrutura equilibrada)
    - 0.5 < PL/Ativos ≤ 0.7: Ótimo (patrimônio sólido)
    - PL/Ativos > 0.7: Fora da faixa (pouco endividamento)
    """
    if not isinstance(pl_ativos, (int, float)):
        raise TypeError("PL/Ativos deve ser um número (int ou float)")
    if pl_ativos < 0:
        return {'classificacao': 'Crítico', 'faixa': 'PL/Ativos < 0', 'descricao': 'PL/Ativos negativo indica patrimônio líquido negativo.'}
    elif 0 <= pl_ativos <= 0.1:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= PL/Ativos <= 0.1', 'descricao': 'PL/Ativos muito baixo, comum em bancos (ex.: ITUB4), com alta alavancagem.'}
    elif 0.1 < pl_ativos <= 0.3:
        return {'classificacao': 'Ruim', 'faixa': '0.1 < PL/Ativos <= 0.3', 'descricao': 'PL/Ativos baixo, comum em utilities (ex.: ENGI11).'}
    elif 0.3 < pl_ativos <= 0.5:
        return {'classificacao': 'Moderado', 'faixa': '0.3 < PL/Ativos <= 0.5', 'descricao': 'PL/Ativos equilibrado, comum em indústria (ex.: SUZB3).'}
    elif 0.5 < pl_ativos <= 0.7:
        return {'classificacao': 'Ótimo', 'faixa': '0.5 < PL/Ativos <= 0.7', 'descricao': 'PL/Ativos alto, comum em consumo (ex.: ABEV3).'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'PL/Ativos > 0.7', 'descricao': 'PL/Ativos extremamente alto, comum em tecnologia (ex.: TOTS3), indicando pouco endividamento.'}

def evaluate_passivos_ativos(passivos_ativos):
    """
    Avalia o Passivos/Ativos.
    - Passivos/Ativos < 0: Crítico (impossível)
    - 0 ≤ Passivos/Ativos ≤ 0.3: Ótimo (baixo endividamento)
    - 0.3 < Passivos/Ativos ≤ 0.5: Moderado (endividamento controlado)
    - 0.5 < Passivos/Ativos ≤ 0.7: Ruim (endividamento moderado)
    - 0.7 < Passivos/Ativos ≤ 0.9: Péssimo (endividamento alto)
    - Passivos/Ativos > 0.9: Fora da faixa (endividamento excessivo)
    """
    if not isinstance(passivos_ativos, (int, float)):
        raise TypeError("Passivos/Ativos deve ser um número (int ou float)")
    if passivos_ativos < 0:
        return {'classificacao': 'Crítico', 'faixa': 'Passivos/Ativos < 0', 'descricao': 'Passivos/Ativos negativo é impossível.'}
    elif 0 <= passivos_ativos <= 0.3:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= Passivos/Ativos <= 0.3', 'descricao': 'Passivos/Ativos baixo, comum em tecnologia (ex.: TOTS3).'}
    elif 0.3 < passivos_ativos <= 0.5:
        return {'classificacao': 'Moderado', 'faixa': '0.3 < Passivos/Ativos <= 0.5', 'descricao': 'Passivos/Ativos moderado, comum em consumo (ex.: ABEV3).'}
    elif 0.5 < passivos_ativos <= 0.7:
        return {'classificacao': 'Ruim', 'faixa': '0.5 < Passivos/Ativos <= 0.7', 'descricao': 'Passivos/Ativos elevado, comum em indústria (ex.: SUZB3).'}
    elif 0.7 < passivos_ativos <= 0.9:
        return {'classificacao': 'Péssimo', 'faixa': '0.7 < Passivos/Ativos <= 0.9', 'descricao': 'Passivos/Ativos alto, comum em utilities (ex.: ENGI11).'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Passivos/Ativos > 0.9', 'descricao': 'Passivos/Ativos extremamente alto, comum em bancos (ex.: ITUB4).'}

def evaluate_liquidez_corrente(lc):
    """
    Avalia a Liquidez Corrente.
    - Liquidez < 0.8: Crítico (alta insolvência)
    - 0.8 ≤ Liquidez ≤ 1: Péssimo (liquidez muito baixa)
    - 1 < Liquidez ≤ 1.2: Ruim (liquidez limitada)
    - 1.2 < Liquidez ≤ 1.5: Moderado (liquidez adequada)
    - 1.5 < Liquidez ≤ 2: Ótimo (alta liquidez)
    - Liquidez > 2: Fora da faixa (liquidez excessiva)
    """
    if not isinstance(lc, (int, float)):
        raise TypeError("Liquidez Corrente deve ser um número (int ou float)")
    if lc < 0.8:
        return {'classificacao': 'Crítico', 'faixa': 'Liquidez < 0.8', 'descricao': 'Liquidez muito baixa indica alto risco de insolvência.'}
    elif 0.8 <= lc <= 1:
        return {'classificacao': 'Péssimo', 'faixa': '0.8 <= Liquidez <= 1', 'descricao': 'Liquidez baixa, comum em setores alavancados.'}
    elif 1 < lc <= 1.2:
        return {'classificacao': 'Ruim', 'faixa': '1 < Liquidez <= 1.2', 'descricao': 'Liquidez limitada, indicando capacidade moderada.'}
    elif 1.2 < lc <= 1.5:
        return {'classificacao': 'Moderado', 'faixa': '1.2 < Liquidez <= 1.5', 'descricao': 'Liquidez adequada, sugerindo equilíbrio.'}
    elif 1.5 < lc <= 2:
        return {'classificacao': 'Ótimo', 'faixa': '1.5 < Liquidez <= 2', 'descricao': 'Liquidez alta, indicando forte capacidade.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Liquidez > 2', 'descricao': 'Liquidez extremamente alta, pode indicar ineficiência.'}

def evaluate_peg_ratio(peg):
    """
    Avalia o PEG Ratio.
    - PEG < 0: Crítico (crescimento negativo)
    - 0 ≤ PEG ≤ 0.5: Ótimo (subvalorizado com alto crescimento)
    - 0.5 < PEG ≤ 1: Moderado (valuation justo)
    - 1 < PEG ≤ 1.5: Ruim (sobrevalorizado)
    - 1.5 < PEG ≤ 2: Péssimo (muito caro)
    - PEG > 2: Fora da faixa (extremamente sobrevalorizado)
    """
    if not isinstance(peg, (int, float)):
        raise TypeError("PEG Ratio deve ser um número (int ou float)")
    if peg < 0:
        return {'classificacao': 'Crítico', 'faixa': 'PEG < 0', 'descricao': 'PEG negativo indica crescimento esperado negativo ou P/L negativo.'}
    elif 0 <= peg <= 0.5:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= PEG <= 0.5', 'descricao': 'PEG baixo sugere subvalorização com alto potencial de crescimento.'}
    elif 0.5 < peg <= 1:
        return {'classificacao': 'Moderado', 'faixa': '0.5 < PEG <= 1', 'descricao': 'PEG indica valuation justo, equilibrando preço e crescimento.'}
    elif 1 < peg <= 1.5:
        return {'classificacao': 'Ruim', 'faixa': '1 < PEG <= 1.5', 'descricao': 'PEG elevado sugere sobrevalorização moderada.'}
    elif 1.5 < peg <= 2:
        return {'classificacao': 'Péssimo', 'faixa': '1.5 < PEG <= 2', 'descricao': 'PEG muito alto indica ação cara em relação ao crescimento.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'PEG > 2', 'descricao': 'PEG extremamente elevado, típico de empresas especulativas.'}

def evaluate_p_ativo(p_ativo):
    """
    Avalia o Preço/Ativo Total.
    - P/Ativo < 0: Crítico (impossível)
    - 0 ≤ P/Ativo ≤ 0.2: Ótimo (subvalorizado)
    - 0.2 < P/Ativo ≤ 0.5: Moderado (justo)
    - 0.5 < P/Ativo ≤ 1: Ruim (sobrevalorizado)
    - 1 < P/Ativo ≤ 1.5: Péssimo (muito caro)
    - P/Ativo > 1.5: Fora da faixa (extremamente sobrevalorizado)
    """
    if not isinstance(p_ativo, (int, float)):
        raise TypeError("P/Ativo deve ser um número (int ou float)")
    if p_ativo < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/Ativo < 0', 'descricao': 'P/Ativo negativo é impossível.'}
    elif 0 <= p_ativo <= 0.2:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/Ativo <= 0.2', 'descricao': 'P/Ativo baixo, comum em mineração (ex.: VALE3).'}
    elif 0.2 < p_ativo <= 0.5:
        return {'classificacao': 'Moderado', 'faixa': '0.2 < P/Ativo <= 0.5', 'descricao': 'P/Ativo justo, típico de energia (ex.: ELET3).'}
    elif 0.5 < p_ativo <= 1:
        return {'classificacao': 'Ruim', 'faixa': '0.5 < P/Ativo <= 1', 'descricao': 'P/Ativo elevado, comum em consumo (ex.: ABEV3).'}
    elif 1 < p_ativo <= 1.5:
        return {'classificacao': 'Péssimo', 'faixa': '1 < P/Ativo <= 1.5', 'descricao': 'P/Ativo muito alto, comum em tecnologia.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/Ativo > 1.5', 'descricao': 'P/Ativo extremamente elevado, indicando sobrevalorização severa.'}

def evaluate_vpa(vpa_preco):
    """
    Avalia o VPA/Preço.
    - VPA/Preço < 0: Crítico (patrimônio negativo)
    - 0 ≤ VPA/Preço ≤ 0.5: Fora da faixa (sobrevalorizado)
    - 0.5 < VPA/Preço ≤ 0.8: Péssimo (muito caro)
    - 0.8 < VPA/Preço ≤ 1: Ruim (sobrevalorizado)
    - 1 < VPA/Preço ≤ 1.5: Moderado (valuation justo)
    - VPA/Preço > 1.5: Ótimo (subvalorizado)
    """
    if not isinstance(vpa_preco, (int, float)):
        raise TypeError("VPA/Preço deve ser um número (int ou float)")
    if vpa_preco < 0:
        return {'classificacao': 'Crítico', 'faixa': 'VPA/Preço < 0', 'descricao': 'VPA/Preço negativo indica patrimônio líquido negativo.'}
    elif 0 <= vpa_preco <= 0.5:
        return {'classificacao': 'Fora da faixa', 'faixa': '0 <= VPA/Preço <= 0.5', 'descricao': 'VPA/Preço muito baixo indica sobrevalorização severa.'}
    elif 0.5 < vpa_preco <= 0.8:
        return {'classificacao': 'Péssimo', 'faixa': '0.5 < VPA/Preço <= 0.8', 'descricao': 'VPA/Preço baixo, sugerindo ação cara.'}
    elif 0.8 < vpa_preco <= 1:
        return {'classificacao': 'Ruim', 'faixa': '0.8 < VPA/Preço <= 1', 'descricao': 'VPA/Preço moderado, indicando sobrevalorização.'}
    elif 1 < vpa_preco <= 1.5:
        return {'classificacao': 'Moderado', 'faixa': '1 < VPA/Preço <= 1.5', 'descricao': 'VPA/Preço indica valuation justo.'}
    else:
        return {'classificacao': 'Ótimo', 'faixa': 'VPA/Preço > 1.5', 'descricao': 'VPA/Preço alto sugere subvalorização em relação ao patrimônio.'}

def evaluate_lpa(lpa):
    """
    Avalia o Lucro por Ação (LPA).
    - LPA < 0: Crítico (prejuízo)
    - 0 ≤ LPA ≤ 0.2: Péssimo (lucro muito baixo)
    - 0.2 < LPA ≤ 0.5: Ruim (lucro limitado)
    - 0.5 < LPA ≤ 1: Moderado (lucro adequado)
    - 1 < LPA ≤ 2: Ótimo (lucro alto)
    - LPA > 2: Fora da faixa (lucro excepcional)
    """
    if not isinstance(lpa, (int, float)):
        raise TypeError("LPA deve ser um número (int ou float)")
    if lpa < 0:
        return {'classificacao': 'Crítico', 'faixa': 'LPA < 0', 'descricao': 'LPA negativo indica prejuízo por ação.'}
    elif 0 <= lpa <= 0.2:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= LPA <= 0.2', 'descricao': 'LPA muito baixo, comum em empresas em crise.'}
    elif 0.2 < lpa <= 0.5:
        return {'classificacao': 'Ruim', 'faixa': '0.2 < LPA <= 0.5', 'descricao': 'LPA limitado, indicando lucratividade moderada.'}
    elif 0.5 < lpa <= 1:
        return {'classificacao': 'Moderado', 'faixa': '0.5 < LPA <= 1', 'descricao': 'LPA adequado, sugerindo lucratividade equilibrada.'}
    elif 1 < lpa <= 2:
        return {'classificacao': 'Ótimo', 'faixa': '1 < LPA <= 2', 'descricao': 'LPA alto, indicando forte lucratividade.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'LPA > 2', 'descricao': 'LPA extremamente alto, sugerindo lucratividade excepcional.'}

def evaluate_psr(psr):
    """
    Avalia o Preço/Receita (P/SR).
    - P/SR < 0: Crítico (receita negativa)
    - 0 ≤ P/SR ≤ 0.3: Ótimo (subvalorizado)
    - 0.3 < P/SR ≤ 0.8: Moderado (justo)
    - 0.8 < P/SR ≤ 1.5: Ruim (sobrevalorizado)
    - 1.5 < P/SR ≤ 2.5: Péssimo (muito caro)
    - P/SR > 2.5: Fora da faixa (extremamente sobrevalorizado)
    """
    if not isinstance(psr, (int, float)):
        raise TypeError("P/SR deve ser um número (int ou float)")
    if psr < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/SR < 0', 'descricao': 'P/SR negativo indica receita negativa.'}
    elif 0 <= psr <= 0.3:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/SR <= 0.3', 'descricao': 'P/SR baixo, comum em mineração (ex.: VALE3).'}
    elif 0.3 < psr <= 0.8:
        return {'classificacao': 'Moderado', 'faixa': '0.3 < P/SR <= 0.8', 'descricao': 'P/SR justo, típico de energia (ex.: ELET3).'}
    elif 0.8 < psr <= 1.5:
        return {'classificacao': 'Ruim', 'faixa': '0.8 < P/SR <= 1.5', 'descricao': 'P/SR elevado, comum em consumo (ex.: ABEV3).'}
    elif 1.5 < psr <= 2.5:
        return {'classificacao': 'Péssimo', 'faixa': '1.5 < P/SR <= 2.5', 'descricao': 'P/SR muito alto, comum em tecnologia.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/SR > 2.5', 'descricao': 'P/SR extremamente elevado, indicando sobrevalorização severa.'}

def evaluate_p_ativo_circ_liq(p_acl):
    """
    Avalia o Preço/Ativo Circulante Líquido.
    - P/ACL < 0: Crítico (ativo circulante líquido negativo)
    - 0 ≤ P/ACL ≤ 0.2: Ótimo (subvalorizado)
    - 0.2 < P/ACL ≤ 0.5: Moderado (justo)
    - 0.5 < P/ACL ≤ 1: Ruim (sobrevalorizado)
    - 1 < P/ACL ≤ 1.5: Péssimo (muito caro)
    - P/ACL > 1.5: Fora da faixa (extremamente sobrevalorizado)
    """
    if not isinstance(p_acl, (int, float)):
        raise TypeError("P/ACL deve ser um número (int ou float)")
    if p_acl < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/ACL < 0', 'descricao': 'P/ACL negativo indica ativo circulante líquido negativo.'}
    elif 0 <= p_acl <= 0.2:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/ACL <= 0.2', 'descricao': 'P/ACL baixo sugere subvalorização em relação à liquidez.'}
    elif 0.2 < p_acl <= 0.5:
        return {'classificacao': 'Moderado', 'faixa': '0.2 < P/ACL <= 0.5', 'descricao': 'P/ACL indica valuation justo.'}
    elif 0.5 < p_acl <= 1:
        return {'classificacao': 'Ruim', 'faixa': '0.5 < P/ACL <= 1', 'descricao': 'P/ACL elevado sugere sobrevalorização.'}
    elif 1 < p_acl <= 1.5:
        return {'classificacao': 'Péssimo', 'faixa': '1 < P/ACL <= 1.5', 'descricao': 'P/ACL muito alto indica ação cara.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/ACL > 1.5', 'descricao': 'P/ACL extremamente elevado, indicando sobrevalorização severa.'}

def evaluate_liquidez_media_diaria(lmd):
    """
    Avalia a Liquidez Média Diária (em R$ milhões).
    - LMD < 0.1: Crítico (baixa negociabilidade)
    - 0.1 ≤ LMD ≤ 1: Péssimo (liquidez muito baixa)
    - 1 < LMD ≤ 5: Ruim (liquidez limitada)
    - 5 < LMD ≤ 10: Moderado (liquidez adequada)
    - 10 < LMD ≤ 50: Ótimo (alta liquidez)
    - LMD > 50: Fora da faixa (liquidez excepcional)
    """
    if not isinstance(lmd, (int, float)):
        raise TypeError("Liquidez Média Diária deve ser um número (int ou float)")
    if lmd < 0.1:
        return {'classificacao': 'Crítico', 'faixa': 'LMD < 0.1', 'descricao': 'Liquidez muito baixa, indicando alta iliquidez.'}
    elif 0.1 <= lmd <= 1:
        return {'classificacao': 'Péssimo', 'faixa': '0.1 <= LMD <= 1', 'descricao': 'Liquidez baixa, comum em small caps.'}
    elif 1 < lmd <= 5:
        return {'classificacao': 'Ruim', 'faixa': '1 < LMD <= 5', 'descricao': 'Liquidez limitada, indicando negociabilidade moderada.'}
    elif 5 < lmd <= 10:
        return {'classificacao': 'Moderado', 'faixa': '5 < LMD <= 10', 'descricao': 'Liquidez adequada, sugerindo boa negociabilidade.'}
    elif 10 < lmd <= 50:
        return {'classificacao': 'Ótimo', 'faixa': '10 < LMD <= 50', 'descricao': 'Liquidez alta, comum em blue chips (ex.: PETR4).'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'LMD > 50', 'descricao': 'Liquidez extremamente alta, indicando excelente negociabilidade.'}

def evaluate_patrimonio_liquido_pl_vm(pl_vm):
    """
    Avalia o Patrimônio Líquido/Valor de Mercado.
    - PL/VM < 0: Crítico (patrimônio negativo)
    - 0 ≤ PL/VM ≤ 0.3: Péssimo (patrimônio muito baixo)
    - 0.3 < PL/VM ≤ 0.6: Ruim (patrimônio limitado)
    - 0.6 < PL/VM ≤ 1: Moderado (patrimônio adequado)
    - 1 < PL/VM ≤ 1.5: Ótimo (patrimônio sólido)
    - PL/VM > 1.5: Fora da faixa (patrimônio elevado)
    """
    if not isinstance(pl_vm, (int, float)):
        raise TypeError("PL/VM deve ser um número (int ou float)")
    if pl_vm < 0:
        return {'classificacao': 'Crítico', 'faixa': 'PL/VM < 0', 'descricao': 'Patrimônio Líquido/VM negativo indica patrimônio líquido negativo.'}
    elif 0 <= pl_vm <= 0.3:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= PL/VM <= 0.3', 'descricao': 'PL/VM muito baixo, sugerindo patrimônio insuficiente.'}
    elif 0.3 < pl_vm <= 0.6:
        return {'classificacao': 'Ruim', 'faixa': '0.3 < PL/VM <= 0.6', 'descricao': 'PL/VM limitado, indicando patrimônio moderado.'}
    elif 0.6 < pl_vm <= 1:
        return {'classificacao': 'Moderado', 'faixa': '0.6 < PL/VM <= 1', 'descricao': 'PL/VM adequado, sugerindo equilíbrio.'}
    elif 1 < pl_vm <= 1.5:
        return {'classificacao': 'Ótimo', 'faixa': '1 < PL/VM <= 1.5', 'descricao': 'PL/VM alto, indicando patrimônio sólido.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'PL/VM > 1.5', 'descricao': 'PL/VM extremamente alto, sugerindo possível subvalorização.'}

def evaluate_ativos_vm(ativos_vm):
    """
    Avalia o Ativos/Valor de Mercado.
    - Ativos/VM < 0: Crítico (impossível)
    - 0 ≤ Ativos/VM ≤ 0.3: Péssimo (ativos muito baixos)
    - 0.3 < Ativos/VM ≤ 0.6: Ruim (ativos limitados)
    - 0.6 < Ativos/VM ≤ 1: Moderado (ativos adequados)
    - 1 < Ativos/VM ≤ 1.5: Ótimo (ativos sólidos)
    - Ativos/VM > 1.5: Fora da faixa (ativos elevados)
    """
    if not isinstance(ativos_vm, (int, float)):
        raise TypeError("Ativos/VM deve ser um número (int ou float)")
    if ativos_vm < 0:
        return {'classificacao': 'Crítico', 'faixa': 'Ativos/VM < 0', 'descricao': 'Ativos/VM negativo é impossível.'}
    elif 0 <= ativos_vm <= 0.3:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= Ativos/VM <= 0.3', 'descricao': 'Ativos/VM muito baixo, sugerindo ativos insuficientes.'}
    elif 0.3 < ativos_vm <= 0.6:
        return {'classificacao': 'Ruim', 'faixa': '0.3 < Ativos/VM <= 0.6', 'descricao': 'Ativos/VM limitado, indicando ativos moderados.'}
    elif 0.6 < ativos_vm <= 1:
        return {'classificacao': 'Moderado', 'faixa': '0.6 < Ativos/VM <= 1', 'descricao': 'Ativos/VM adequado, sugerindo equilíbrio.'}
    elif 1 < ativos_vm <= 1.5:
        return {'classificacao': 'Ótimo', 'faixa': '1 < Ativos/VM <= 1.5', 'descricao': 'Ativos/VM alto, indicando ativos sólidos.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Ativos/VM > 1.5', 'descricao': 'Ativos/VM extremamente alto, sugerindo possível subvalorização.'}

def evaluate_ativo_circulante_vm(ac_vm):
    """
    Avalia o Ativo Circulante/Valor de Mercado.
    - AC/VM < 0: Crítico (impossível)
    - 0 ≤ AC/VM ≤ 0.1: Péssimo (liquidez muito baixa)
    - 0.1 < AC/VM ≤ 0.3: Ruim (liquidez limitada)
    - 0.3 < AC/VM ≤ 0.5: Moderado (liquidez adequada)
    - 0.5 < AC/VM ≤ 1: Ótimo (alta liquidez)
    - AC/VM > 1: Fora da faixa (liquidez excepcional)
    """
    if not isinstance(ac_vm, (int, float)):
        raise TypeError("AC/VM deve ser um número (int ou float)")
    if ac_vm < 0:
        return {'classificacao': 'Crítico', 'faixa': 'AC/VM < 0', 'descricao': 'AC/VM negativo é impossível.'}
    elif 0 <= ac_vm <= 0.1:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= AC/VM <= 0.1', 'descricao': 'AC/VM muito baixo, sugerindo liquidez insuficiente.'}
    elif 0.1 < ac_vm <= 0.3:
        return {'classificacao': 'Ruim', 'faixa': '0.1 < AC/VM <= 0.3', 'descricao': 'AC/VM limitado, indicando liquidez moderada.'}
    elif 0.3 < ac_vm <= 0.5:
        return {'classificacao': 'Moderado', 'faixa': '0.3 < AC/VM <= 0.5', 'descricao': 'AC/VM adequado, sugerindo equilíbrio.'}
    elif 0.5 < ac_vm <= 1:
        return {'classificacao': 'Ótimo', 'faixa': '0.5 < AC/VM <= 1', 'descricao': 'AC/VM alto, indicando alta liquidez.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'AC/VM > 1', 'descricao': 'AC/VM extremamente alto, sugerindo liquidez excepcional.'}

def evaluate_divida_bruta_vm(db_vm):
    """
    Avalia a Dívida Bruta/Valor de Mercado.
    - DB/VM < 0: Crítico (impossível)
    - 0 ≤ DB/VM ≤ 0.2: Ótimo (baixo endividamento)
    - 0.2 < DB/VM ≤ 0.5: Moderado (endividamento controlado)
    - 0.5 < DB/VM ≤ 1: Ruim (endividamento moderado)
    - 1 < DB/VM ≤ 1.5: Péssimo (endividamento alto)
    - DB/VM > 1.5: Fora da faixa (endividamento excessivo)
    """
    if not isinstance(db_vm, (int, float)):
        raise TypeError("DB/VM deve ser um número (int ou float)")
    if db_vm < 0:
        return {'classificacao': 'Crítico', 'faixa': 'DB/VM < 0', 'descricao': 'DB/VM negativo é impossível.'}
    elif 0 <= db_vm <= 0.2:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= DB/VM <= 0.2', 'descricao': 'DB/VM baixo, indicando endividamento mínimo.'}
    elif 0.2 < db_vm <= 0.5:
        return {'classificacao': 'Moderado', 'faixa': '0.2 < DB/VM <= 0.5', 'descricao': 'DB/VM moderado, sugerindo endividamento controlado.'}
    elif 0.5 < db_vm <= 1:
        return {'classificacao': 'Ruim', 'faixa': '0.5 < DB/VM <= 1', 'descricao': 'DB/VM elevado, indicando endividamento moderado.'}
    elif 1 < db_vm <= 1.5:
        return {'classificacao': 'Péssimo', 'faixa': '1 < DB/VM <= 1.5', 'descricao': 'DB/VM alto, sugerindo endividamento elevado.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'DB/VM > 1.5', 'descricao': 'DB/VM extremamente alto, indicando endividamento excessivo.'}

def evaluate_disponibilidade_vm(disp_vm):
    """
    Avalia a Disponibilidade/Valor de Mercado.
    - Disp/VM < 0: Crítico (impossível)
    - 0 ≤ Disp/VM ≤ 0.05: Péssimo (disponibilidade muito baixa)
    - 0.05 < Disp/VM ≤ 0.1: Ruim (disponibilidade limitada)
    - 0.1 < Disp/VM ≤ 0.2: Moderado (disponibilidade adequada)
    - 0.2 < Disp/VM ≤ 0.5: Ótimo (alta disponibilidade)
    - Disp/VM > 0.5: Fora da faixa (disponibilidade excepcional)
    """
    if not isinstance(disp_vm, (int, float)):
        raise TypeError("Disp/VM deve ser um número (int ou float)")
    if disp_vm < 0:
        return {'classificacao': 'Crítico', 'faixa': 'Disp/VM < 0', 'descricao': 'Disp/VM negativo é impossível.'}
    elif 0 <= disp_vm <= 0.05:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= Disp/VM <= 0.05', 'descricao': 'Disp/VM muito baixo, sugerindo liquidez imediata insuficiente.'}
    elif 0.05 < disp_vm <= 0.1:
        return {'classificacao': 'Ruim', 'faixa': '0.05 < Disp/VM <= 0.1', 'descricao': 'Disp/VM limitado, indicando liquidez moderada.'}
    elif 0.1 < disp_vm <= 0.2:
        return {'classificacao': 'Moderado', 'faixa': '0.1 < Disp/VM <= 0.2', 'descricao': 'Disp/VM adequado, sugerindo equilíbrio.'}
    elif 0.2 < disp_vm <= 0.5:
        return {'classificacao': 'Ótimo', 'faixa': '0.2 < Disp/VM <= 0.5', 'descricao': 'Disp/VM alto, indicando alta liquidez imediata.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Disp/VM > 0.5', 'descricao': 'Disp/VM extremamente alto, sugerindo liquidez excepcional.'}

def evaluate_divida_liquida_vm(dl_vm):
    """
    Avalia a Dívida Líquida/Valor de Mercado.
    - DL/VM < -0.5: Crítico (caixa excessivo)
    - -0.5 ≤ DL/VM < 0: Ótimo (caixa supera dívida)
    - 0 ≤ DL/VM ≤ 0.3: Moderado (endividamento baixo)
    - 0.3 < DL/VM ≤ 0.6: Ruim (endividamento moderado)
    - 0.6 < DL/VM ≤ 1: Péssimo (endividamento alto)
    - DL/VM > 1: Fora da faixa (endividamento excessivo)
    """
    if not isinstance(dl_vm, (int, float)):
        raise TypeError("DL/VM deve ser um número (int ou float)")
    if dl_vm < -0.5:
        return {'classificacao': 'Crítico', 'faixa': 'DL/VM < -0.5', 'descricao': 'DL/VM extremamente negativa indica caixa excessivo.'}
    elif -0.5 <= dl_vm < 0:
        return {'classificacao': 'Ótimo', 'faixa': '-0.5 <= DL/VM < 0', 'descricao': 'DL/VM negativa indica solidez financeira.'}
    elif 0 <= dl_vm <= 0.3:
        return {'classificacao': 'Moderado', 'faixa': '0 <= DL/VM <= 0.3', 'descricao': 'DL/VM baixa, indicando endividamento controlado.'}
    elif 0.3 < dl_vm <= 0.6:
        return {'classificacao': 'Ruim', 'faixa': '0.3 < DL/VM <= 0.6', 'descricao': 'DL/VM moderada, sugerindo endividamento aceitável.'}
    elif 0.6 < dl_vm <= 1:
        return {'classificacao': 'Péssimo', 'faixa': '0.6 < DL/VM <= 1', 'descricao': 'DL/VM alta, indicando endividamento elevado.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'DL/VM > 1', 'descricao': 'DL/VM extremamente alta, sugerindo endividamento excessivo.'}

def evaluate_valor_mercado_receita(vm_receita):
    """
    Avalia o Valor de Mercado/Receita.
    - VM/Receita < 0: Crítico (receita negativa)
    - 0 ≤ VM/Receita ≤ 0.3: Ótimo (subvalorizado)
    - 0.3 < VM/Receita ≤ 0.8: Moderado (justo)
    - 0.8 < VM/Receita ≤ 1.5: Ruim (sobrevalorizado)
    - 1.5 < VM/Receita ≤ 2.5: Péssimo (muito caro)
    - VM/Receita > 2.5: Fora da faixa (extremamente sobrevalorizado)
    """
    if not isinstance(vm_receita, (int, float)):
        raise TypeError("VM/Receita deve ser um número (int ou float)")
    if vm_receita < 0:
        return {'classificacao': 'Crítico', 'faixa': 'VM/Receita < 0', 'descricao': 'VM/Receita negativo indica receita negativa.'}
    elif 0 <= vm_receita <= 0.3:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= VM/Receita <= 0.3', 'descricao': 'VM/Receita baixo, sugerindo subvalorização.'}
    elif 0.3 < vm_receita <= 0.8:
        return {'classificacao': 'Moderado', 'faixa': '0.3 < VM/Receita <= 0.8', 'descricao': 'VM/Receita indica valuation justo.'}
    elif 0.8 < vm_receita <= 1.5:
        return {'classificacao': 'Ruim', 'faixa': '0.8 < VM/Receita <= 1.5', 'descricao': 'VM/Receita elevado, sugerindo sobrevalorização.'}
    elif 1.5 < vm_receita <= 2.5:
        return {'classificacao': 'Péssimo', 'faixa': '1.5 < VM/Receita <= 2.5', 'descricao': 'VM/Receita muito alto, indicando empresa cara.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'VM/Receita > 2.5', 'descricao': 'VM/Receita extremamente elevado, sugerindo sobrevalorização severa.'}

def evaluate_valor_firma_receita(vf_receita):
    """
    Avalia o Valor de Firma/Receita.
    - VF/Receita < 0: Crítico (receita negativa)
    - 0 ≤ VF/Receita ≤ 0.5: Ótimo (subvalorizado)
    - 0.5 < VF/Receita ≤ 1: Moderado (justo)
    - 1 < VF/Receita ≤ 2: Ruim (sobrevalorizado)
    - 2 < VF/Receita ≤ 3: Péssimo (muito caro)
    - VF/Receita > 3: Fora da faixa (extremamente sobrevalorizado)
    """
    if not isinstance(vf_receita, (int, float)):
        raise TypeError("VF/Receita deve ser um número (int ou float)")
    if vf_receita < 0:
        return {'classificacao': 'Crítico', 'faixa': 'VF/Receita < 0', 'descricao': 'VF/Receita negativo indica receita negativa.'}
    elif 0 <= vf_receita <= 0.5:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= VF/Receita <= 0.5', 'descricao': 'VF/Receita baixo, sugerindo subvalorização.'}
    elif 0.5 < vf_receita <= 1:
        return {'classificacao': 'Moderado', 'faixa': '0.5 < VF/Receita <= 1', 'descricao': 'VF/Receita indica valuation justo.'}
    elif 1 < vf_receita <= 2:
        return {'classificacao': 'Ruim', 'faixa': '1 < VF/Receita <= 2', 'descricao': 'VF/Receita elevado, sugerindo sobrevalorização.'}
    elif 2 < vf_receita <= 3:
        return {'classificacao': 'Péssimo', 'faixa': '2 < VF/Receita <= 3', 'descricao': 'VF/Receita muito alto, indicando empresa cara.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'VF/Receita > 3', 'descricao': 'VF/Receita extremamente elevado, sugerindo sobrevalorização severa.'}

def evaluate_roe(roe):
    """
    Avalia o Retorno sobre Patrimônio (ROE).
    - ROE < 0: Crítico (prejuízo)
    - 0 ≤ ROE ≤ 5: Péssimo (rentabilidade muito baixa)
    - 5 < ROE ≤ 10: Ruim (rentabilidade limitada)
    - 10 < ROE ≤ 15: Moderado (rentabilidade adequada)
    - 15 < ROE ≤ 25: Ótimo (rentabilidade alta)
    - ROE > 25: Fora da faixa (rentabilidade excepcional)
    """
    if not isinstance(roe, (int, float)):
        raise TypeError("ROE deve ser um número (int ou float)")
    if roe < 0:
        return {'classificacao': 'Crítico', 'faixa': 'ROE < 0', 'descricao': 'ROE negativo indica prejuízo.'}
    elif 0 <= roe <= 5:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= ROE <= 5', 'descricao': 'ROE muito baixo, sugerindo baixa rentabilidade.'}
    elif 5 < roe <= 10:
        return {'classificacao': 'Ruim', 'faixa': '5 < ROE ≤ 10', 'descricao': 'ROE limitado, indicando rentabilidade moderada.'}
    elif 10 < roe <= 15:
        return {'classificacao': 'Moderado', 'faixa': '10 < ROE ≤ 15', 'descricao': 'ROE adequado, sugerindo rentabilidade equilibrada.'}
    elif 15 < roe <= 25:
        return {'classificacao': 'Ótimo', 'faixa': '15 < ROE ≤ 25', 'descricao': 'ROE alto, indicando forte rentabilidade.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'ROE > 25', 'descricao': 'ROE extremamente alto, sugerindo rentabilidade excepcional.'}

def evaluate_margem_liquida(ml):
    """
    Avalia a Margem Líquida.
    - ML < 0: Crítico (prejuízo)
    - 0 ≤ ML ≤ 3: Péssimo (margem muito baixa)
    - 3 < ML ≤ 7: Ruim (margem limitada)
    - 7 < ML ≤ 15: Moderado (margem adequada)
    - 15 < ML ≤ 25: Ótimo (margem alta)
    - ML > 25: Fora da faixa (margem excepcional)
    """
    if not isinstance(ml, (int, float)):
        raise TypeError("Margem Líquida deve ser um número (int ou float)")
    if ml < 0:
        return {'classificacao': 'Crítico', 'faixa': 'ML < 0', 'descricao': 'Margem Líquida negativa indica prejuízo.'}
    elif 0 <= ml <= 3:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= ML ≤ 3', 'descricao': 'Margem muito baixa, sugerindo baixa eficiência.'}
    elif 3 < ml <= 7:
        return {'classificacao': 'Ruim', 'faixa': '3 < ML ≤ 7', 'descricao': 'Margem limitada, indicando eficiência moderada.'}
    elif 7 < ml <= 15:
        return {'classificacao': 'Moderado', 'faixa': '7 < ML ≤ 15', 'descricao': 'Margem adequada, sugerindo eficiência equilibrada.'}
    elif 15 < ml <= 25:
        return {'classificacao': 'Ótimo', 'faixa': '15 < ML ≤ 25', 'descricao': 'Margem alta, indicando forte eficiência.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'ML > 25', 'descricao': 'Margem extremamente alta, sugerindo eficiência excepcional.'}

def evaluate_roic(roic):
    """
    Avalia o Retorno sobre Capital Investido (ROIC).
    - ROIC < 0: Crítico (ineficiência)
    - 0 ≤ ROIC ≤ 5: Péssimo (retorno muito baixo)
    - 5 < ROIC ≤ 10: Ruim (retorno limitado)
    - 10 < ROIC ≤ 15: Moderado (retorno adequado)
    - 15 < ROIC ≤ 20: Ótimo (retorno alto)
    - ROIC > 20: Fora da faixa (retorno excepcional)
    """
    if not isinstance(roic, (int, float)):
        raise TypeError("ROIC deve ser um número (int ou float)")
    if roic < 0:
        return {'classificacao': 'Crítico', 'faixa': 'ROIC < 0', 'descricao': 'ROIC negativo indica ineficiência na alocação de capital.'}
    elif 0 <= roic <= 5:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= ROIC ≤ 5', 'descricao': 'ROIC muito baixo, sugerindo baixa eficiência.'}
    elif 5 < roic <= 10:
        return {'classificacao': 'Ruim', 'faixa': '5 < ROIC ≤ 10', 'descricao': 'ROIC limitado, indicando eficiência moderada.'}
    elif 10 < roic <= 15:
        return {'classificacao': 'Moderado', 'faixa': '10 < ROIC ≤ 15', 'descricao': 'ROIC adequado, sugerindo eficiência equilibrada.'}
    elif 15 < roic <= 20:
        return {'classificacao': 'Ótimo', 'faixa': '15 < ROIC ≤ 20', 'descricao': 'ROIC alto, indicando forte eficiência.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'ROIC > 20', 'descricao': 'ROIC extremamente alto, sugerindo eficiência excepcional.'}

class TestEvaluateIndicators(unittest.TestCase):
    """Testes unitários para as funções de avaliação de indicadores."""

    def test_evaluate_pl(self):
        result = evaluate_pl(-5)
        self.assertEqual(result['classificacao'], 'Crítico')
        result = evaluate_pl(5)
        self.assertEqual(result['classificacao'], 'Ótimo')
        result = evaluate_pl(10)
        self.assertEqual(result['classificacao'], 'Moderado')
        result = evaluate_pl(20)
        self.assertEqual(result['classificacao'], 'Ruim')
        result = evaluate_pl(30)
        self.assertEqual(result['classificacao'], 'Péssimo')
        result = evaluate_pl(40)
        self.assertEqual(result['classificacao'], 'Fora da faixa')
        with self.assertRaises(TypeError):
            evaluate_pl("5")

    def test_evaluate_giro_ativos(self):
        result = evaluate_giro_ativos(-0.1)
        self.assertEqual(result['classificacao'], 'Crítico')
        result = evaluate_giro_ativos(0.1)
        self.assertEqual(result['classificacao'], 'Péssimo')
        result = evaluate_giro_ativos(0.3)
        self.assertEqual(result['classificacao'], 'Ruim')
        result = evaluate_giro_ativos(0.7)
        self.assertEqual(result['classificacao'], 'Moderado')
        result = evaluate_giro_ativos(1.5)
        self.assertEqual(result['classificacao'], 'Ótimo')
        result = evaluate_giro_ativos(2.5)
        self.assertEqual(result['classificacao'], 'Fora da faixa')
        with self.assertRaises(TypeError):
            evaluate_giro_ativos("0.5")

    def test_evaluate_divida_liquida_ebitda(self):
        result = evaluate_divida_liquida_ebitda(-3)
        self.assertEqual(result['classificacao'], 'Crítico')
        result = evaluate_divida_liquida_ebitda(-1)
        self.assertEqual(result['classificacao'], 'Ótimo')
        result = evaluate_divida_liquida_ebitda(1)
        self.assertEqual(result['classificacao'], 'Moderado')
        result = evaluate_divida_liquida_ebitda(2)
        self.assertEqual(result['classificacao'], 'Ruim')
        result = evaluate_divida_liquida_ebitda(4)
        self.assertEqual(result['classificacao'], 'Péssimo')
        result = evaluate_divida_liquida_ebitda(5)
        self.assertEqual(result['classificacao'], 'Fora da faixa')
        with self.assertRaises(TypeError):
            evaluate_divida_liquida_ebitda("2")

    def test_evaluate_liquidez_corrente(self):
        result = evaluate_liquidez_corrente(0.5)
        self.assertEqual(result['classificacao'], 'Crítico')
        result = evaluate_liquidez_corrente(0.9)
        self.assertEqual(result['classificacao'], 'Péssimo')
        result = evaluate_liquidez_corrente(1.1)
        self.assertEqual(result['classificacao'], 'Ruim')
        result = evaluate_liquidez_corrente(1.4)
        self.assertEqual(result['classificacao'], 'Moderado')
        result = evaluate_liquidez_corrente(1.8)
        self.assertEqual(result['classificacao'], 'Ótimo')
        result = evaluate_liquidez_corrente(2.5)
        self.assertEqual(result['classificacao'], 'Fora da faixa')
        with self.assertRaises(TypeError):
            evaluate_liquidez_corrente("1.5")

    def test_evaluate_peg_ratio(self):
        result = evaluate_peg_ratio(-1)
        self.assertEqual(result['classificacao'], 'Crítico')
        result = evaluate_peg_ratio(0.3)
        self.assertEqual(result['classificacao'], 'Ótimo')
        result = evaluate_peg_ratio(0.8)
        self.assertEqual(result['classificacao'], 'Moderado')
        result = evaluate_peg_ratio(1.2)
        self.assertEqual(result['classificacao'], 'Ruim')
        result = evaluate_peg_ratio(1.8)
        self.assertEqual(result['classificacao'], 'Péssimo')
        result = evaluate_peg_ratio(2.5)
        self.assertEqual(result['classificacao'], 'Fora da faixa')
        with self.assertRaises(TypeError):
            evaluate_peg_ratio("1")

if __name__ == '__main__':
    unittest.main()