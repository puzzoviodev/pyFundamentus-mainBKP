import unittest

def evaluate_pl(pl):
    """
    Avalia o Preço/Lucro (P/L) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(pl, (int, float)):
        raise TypeError("P/L deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if pl < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/L < 0', 'descricao': 'P/L negativo indica prejuízo, sugerindo problemas financeiros ou cíclicos. Comum em setores voláteis (ex.: commodities). Exige análise detalhada.'}
    elif 0 <= pl <= 5:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/L <= 5', 'descricao': 'P/L baixo sugere subvalorização, com preço atrativo em relação ao lucro. Comum em setores maduros (ex.: bancos). Oportunidade de compra.'}
    elif 5 < pl <= 15:
        return {'classificacao': 'Moderado', 'faixa': '5 < P/L <= 15', 'descricao': 'P/L indica valuation justo, típico de empresas com crescimento moderado. Comum em setores consolidados (ex.: energia).'}
    elif 15 < pl <= 25:
        return {'classificacao': 'Ruim', 'faixa': '15 < P/L <= 25', 'descricao': 'P/L elevado sugere sobrevalorização, com mercado esperando crescimento. Aceitável em setores dinâmicos (ex.: tecnologia).'}
    elif 25 < pl <= 35:
        return {'classificacao': 'Péssimo', 'faixa': '25 < P/L <= 35', 'descricao': 'P/L muito alto indica ação cara, com expectativas de crescimento elevadas. Alto risco de correção.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/L > 35', 'descricao': 'P/L extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas.'}

def evaluate_pebitda(pebitda):
    """
    Avalia o Preço/EBITDA (P/EBITDA) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(pebitda, (int, float)):
        raise TypeError("P/EBITDA deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if pebitda < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/EBITDA < 0', 'descricao': 'P/EBITDA negativo indica EBITDA negativo, sugerindo problemas operacionais graves. Exige análise de fluxo de caixa.'}
    elif 0 <= pebitda <= 5:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/EBITDA <= 5', 'descricao': 'P/EBITDA baixo sugere subvalorização em relação ao fluxo de caixa. Comum em setores maduros (ex.: utilities).'}
    elif 5 < pebitda <= 8:
        return {'classificacao': 'Moderado', 'faixa': '5 < P/EBITDA <= 8', 'descricao': 'P/EBITDA indica valuation justo, típico de empresas com caixa estável (ex.: indústria).'}
    elif 8 < pebitda <= 12:
        return {'classificacao': 'Ruim', 'faixa': '8 < P/EBITDA <= 12', 'descricao': 'P/EBITDA elevado sugere sobrevalorização moderada. Aceitável em setores dinâmicos (ex.: varejo tech).'}
    elif 12 < pebitda <= 15:
        return {'classificacao': 'Péssimo', 'faixa': '12 < P/EBITDA <= 15', 'descricao': 'P/EBITDA muito alto indica ação cara, com alto risco de correção.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/EBITDA > 15', 'descricao': 'P/EBITDA extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas.'}

def evaluate_pvp(pvp):
    """
    Avalia o Preço/Valor Patrimonial (P/VP) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(pvp, (int, float)):
        raise TypeError("P/VP deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if pvp < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/VP < 0', 'descricao': 'P/VP negativo indica patrimônio líquido negativo, sugerindo graves problemas financeiros.'}
    elif 0 <= pvp <= 1:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/VP <= 1', 'descricao': 'P/VP baixo sugere subvalorização, com preço abaixo do patrimônio. Comum em setores maduros (ex.: bancos).'}
    elif 1 < pvp <= 2:
        return {'classificacao': 'Moderado', 'faixa': '1 < P/VP <= 2', 'descricao': 'P/VP indica valuation justo, típico de empresas com estabilidade financeira (ex.: celulose).'}
    elif 2 < pvp <= 3:
        return {'classificacao': 'Ruim', 'faixa': '2 < P/VP <= 3', 'descricao': 'P/VP elevado sugere sobrevalorização moderada, com mercado precificando crescimento.'}
    elif 3 < pvp <= 5:
        return {'classificacao': 'Péssimo', 'faixa': '3 < P/VP <= 5', 'descricao': 'P/VP muito alto indica ação cara, com risco de correção.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/VP > 5', 'descricao': 'P/VP extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas.'}

def evaluate_pebit(pebit):
    """
    Avalia o Preço/EBIT (P/EBIT) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(pebit, (int, float)):
        raise TypeError("P/EBIT deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if pebit < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/EBIT < 0', 'descricao': 'P/EBIT negativo indica prejuízo operacional, sugerindo problemas graves.'}
    elif 0 <= pebit <= 6:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/EBIT <= 6', 'descricao': 'P/EBIT baixo sugere subvalorização em relação ao lucro operacional. Oportunidade de compra.'}
    elif 6 < pebit <= 10:
        return {'classificacao': 'Moderado', 'faixa': '6 < P/EBIT <= 10', 'descricao': 'P/EBIT indica valuation justo, típico de empresas com lucro estável.'}
    elif 10 < pebit <= 15:
        return {'classificacao': 'Ruim', 'faixa': '10 < P/EBIT <= 15', 'descricao': 'P/EBIT elevado sugere sobrevalorização moderada.'}
    elif 15 < pebit <= 20:
        return {'classificacao': 'Péssimo', 'faixa': '15 < P/EBIT <= 20', 'descricao': 'P/EBIT muito alto indica ação cara, com risco de correção.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/EBIT > 20', 'descricao': 'P/EBIT extremamente elevado sugere sobrevalorização severa.'}

def evaluate_evebitda(evebitda):
    """
    Avalia o Valor da Firma/EBITDA (EV/EBITDA) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(evebitda, (int, float)):
        raise TypeError("EV/EBITDA deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if evebitda < 0:
        return {'classificacao': 'Crítico', 'faixa': 'EV/EBITDA < 0', 'descricao': 'EV/EBITDA negativo indica EBITDA negativo, sugerindo problemas operacionais graves.'}
    elif 0 <= evebitda <= 5:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= EV/EBITDA <= 5', 'descricao': 'EV/EBITDA baixo sugere subvalorização em relação ao fluxo de caixa. Oportunidade de compra.'}
    elif 5 < evebitda <= 8:
        return {'classificacao': 'Moderado', 'faixa': '5 < EV/EBITDA <= 8', 'descricao': 'EV/EBITDA indica valuation justo, típico de empresas com caixa estável.'}
    elif 8 < evebitda <= 12:
        return {'classificacao': 'Ruim', 'faixa': '8 < EV/EBITDA <= 12', 'descricao': 'EV/EBITDA elevado sugere sobrevalorização moderada.'}
    elif 12 < evebitda <= 16:
        return {'classificacao': 'Péssimo', 'faixa': '12 < EV/EBITDA <= 16', 'descricao': 'EV/EBITDA muito alto indica empresa cara, com risco de correção.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'EV/EBITDA > 16', 'descricao': 'EV/EBITDA extremamente elevado sugere sobrevalorização severa.'}

def evaluate_evebit(evebit):
    """
    Avalia o Valor da Firma/EBIT (EV/EBIT) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(evebit, (int, float)):
        raise TypeError("EV/EBIT deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if evebit < 0:
        return {'classificacao': 'Crítico', 'faixa': 'EV/EBIT < 0', 'descricao': 'EV/EBIT negativo indica EBIT negativo, sugerindo problemas operacionais graves.'}
    elif 0 <= evebit <= 6:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= EV/EBIT <= 6', 'descricao': 'EV/EBIT baixo sugere subvalorização em relação ao lucro operacional.'}
    elif 6 < evebit <= 10:
        return {'classificacao': 'Moderado', 'faixa': '6 < EV/EBIT <= 10', 'descricao': 'EV/EBIT indica valuation justo, típico de empresas com lucro estável.'}
    elif 10 < evebit <= 15:
        return {'classificacao': 'Ruim', 'faixa': '10 < EV/EBIT <= 15', 'descricao': 'EV/EBIT elevado sugere sobrevalorização moderada.'}
    elif 15 < evebit <= 20:
        return {'classificacao': 'Péssimo', 'faixa': '15 < EV/EBIT <= 20', 'descricao': 'EV/EBIT muito alto indica empresa cara, com risco de correção.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'EV/EBIT > 20', 'descricao': 'EV/EBIT extremamente elevado sugere sobrevalorização severa.'}

def evaluate_giro_ativos(giro):
    """
    Avalia o Giro de Ativos (Receita Líquida/Ativos Totais) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(giro, (int, float)):
        raise TypeError("Giro de Ativos deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if giro < 0:
        return {'classificacao': 'Crítico', 'faixa': 'Giro < 0', 'descricao': 'Giro negativo indica receita negativa, sugerindo problemas operacionais graves.'}
    elif 0 <= giro <= 0.3:
        return {'classificacao': 'Ruim', 'faixa': '0 <= Giro <= 0.3', 'descricao': 'Giro baixo indica baixa eficiência no uso de ativos. Comum em setores intensivos em capital (ex.: infraestrutura).'}
    elif 0.3 < giro <= 0.6:
        return {'classificacao': 'Péssimo', 'faixa': '0.3 < Giro <= 0.6', 'descricao': 'Giro muito baixo sugere eficiência extremamente limitada. Pode indicar ativos ociosos.'}
    elif 0.6 < giro <= 1.0:
        return {'classificacao': 'Moderado', 'faixa': '0.6 < Giro <= 1.0', 'descricao': 'Giro indica eficiência aceitável. Comum em setores consolidados (ex.: celulose).'}
    elif 1.0 < giro <= 1.5:
        return {'classificacao': 'Ótimo', 'faixa': '1.0 < Giro <= 1.5', 'descricao': 'Giro alto sugere alta eficiência na geração de receita. Comum em setores dinâmicos (ex.: varejo).'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Giro > 1.5', 'descricao': 'Giro extremamente elevado indica eficiência excepcional, mas pode sugerir alavancagem.'}

def evaluate_divida_liquida_pl(dl_pl):
    """
    Avalia a Dívida Líquida/Patrimônio Líquido com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(dl_pl, (int, float)):
        raise TypeError("Dívida Líquida/PL deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if dl_pl < -0.5:
        return {'classificacao': 'Crítico', 'faixa': 'Dívida Líquida/PL < -0.5', 'descricao': 'Dívida Líquida/PL extremamente negativa indica caixa excessivo, sugerindo ineficiência.'}
    elif -0.5 <= dl_pl < 0:
        return {'classificacao': 'Ótimo', 'faixa': '-0.5 <= Dívida Líquida/PL < 0', 'descricao': 'Dívida Líquida negativa indica mais caixa que dívida, sugerindo solidez financeira.'}
    elif 0 <= dl_pl <= 0.3:
        return {'classificacao': 'Moderado', 'faixa': '0 <= Dívida Líquida/PL <= 0.3', 'descricao': 'Dívida Líquida/PL baixa indica endividamento controlado. Comum em setores estáveis.'}
    elif 0.3 < dl_pl <= 0.6:
        return {'classificacao': 'Ruim', 'faixa': '0.3 < Dívida Líquida/PL <= 0.6', 'descricao': 'Dívida Líquida/PL moderada sugere endividamento aceitável, mas requer cautela.'}
    elif 0.6 < dl_pl <= 1:
        return {'classificacao': 'Péssimo', 'faixa': '0.6 < Dívida Líquida/PL <= 1', 'descricao': 'Dívida Líquida/PL alta indica endividamento elevado, com risco de dificuldades.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Dívida Líquida/PL > 1', 'descricao': 'Dívida Líquida/PL extremamente alta sugere endividamento excessivo.'}

def evaluate_divida_liquida_ebitda(dl_ebitda):
    """
    Avalia a Dívida Líquida/EBITDA com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(dl_ebitda, (int, float)):
        raise TypeError("Dívida Líquida/EBITDA deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if dl_ebitda < -3:
        return {'classificacao': 'Crítico', 'faixa': 'Dívida Líquida/EBITDA < -3', 'descricao': 'Dívida Líquida/EBITDA extremamente negativa indica caixa excessivo.'}
    elif -3 <= dl_ebitda < 0:
        return {'classificacao': 'Ótimo', 'faixa': '-3 <= Dívida Líquida/EBITDA < 0', 'descricao': 'Dívida Líquida negativa indica solidez financeira.'}
    elif 0 <= dl_ebitda <= 1:
        return {'classificacao': 'Moderado', 'faixa': '0 <= Dívida Líquida/EBITDA <= 1', 'descricao': 'Dívida Líquida/EBITDA baixa indica endividamento controlado.'}
    elif 1 < dl_ebitda <= 2:
        return {'classificacao': 'Ruim', 'faixa': '1 < Dívida Líquida/EBITDA <= 2', 'descricao': 'Dívida Líquida/EBITDA moderada sugere endividamento aceitável.'}
    elif 2 < dl_ebitda <= 3:
        return {'classificacao': 'Péssimo', 'faixa': '2 < Dívida Líquida/EBITDA <= 3', 'descricao': 'Dívida Líquida/EBITDA alta indica endividamento elevado.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Dívida Líquida/EBITDA > 3', 'descricao': 'Dívida Líquida/EBITDA extremamente alta sugere endividamento excessivo.'}

def evaluate_divida_liquida_ebit(dl_ebit):
    """
    Avalia a Dívida Líquida/EBIT com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(dl_ebit, (int, float)):
        raise TypeError("Dívida Líquida/EBIT deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if dl_ebit < -4:
        return {'classificacao': 'Crítico', 'faixa': 'Dívida Líquida/EBIT < -4', 'descricao': 'Dívida Líquida/EBIT extremamente negativa indica caixa excessivo.'}
    elif -4 <= dl_ebit < 0:
        return {'classificacao': 'Ótimo', 'faixa': '-4 <= Dívida Líquida/EBIT < 0', 'descricao': 'Dívida Líquida negativa indica solidez financeira.'}
    elif 0 <= dl_ebit <= 2:
        return {'classificacao': 'Moderado', 'faixa': '0 <= Dívida Líquida/EBIT <= 2', 'descricao': 'Dívida Líquida/EBIT baixa indica endividamento controlado.'}
    elif 2 < dl_ebit <= 4:
        return {'classificacao': 'Ruim', 'faixa': '2 < Dívida Líquida/EBIT <= 4', 'descricao': 'Dívida Líquida/EBIT moderada sugere endividamento aceitável.'}
    elif 4 < dl_ebit <= 6:
        return {'classificacao': 'Péssimo', 'faixa': '4 < Dívida Líquida/EBIT <= 6', 'descricao': 'Dívida Líquida/EBIT alta indica endividamento elevado.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Dívida Líquida/EBIT > 6', 'descricao': 'Dívida Líquida/EBIT extremamente alta sugere endividamento excessivo.'}

def evaluate_pl_ativos(pl_ativos):
    """
    Avalia o Patrimônio Líquido/Ativos com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(pl_ativos, (int, float)):
        raise TypeError("PL/Ativos deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if pl_ativos < 0:
        return {'classificacao': 'Crítico', 'faixa': 'PL/Ativos < 0', 'descricao': 'PL/Ativos negativo indica patrimônio negativo, sugerindo graves problemas financeiros.'}
    elif 0 <= pl_ativos <= 0.2:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= PL/Ativos <= 0.2', 'descricao': 'PL/Ativos baixo indica alta alavancagem, com poucos ativos financiados por patrimônio.'}
    elif 0.2 < pl_ativos <= 0.4:
        return {'classificacao': 'Ruim', 'faixa': '0.2 < PL/Ativos <= 0.4', 'descricao': 'PL/Ativos moderado sugere alavancagem aceitável, mas com riscos.'}
    elif 0.4 < pl_ativos <= 0.6:
        return {'classificacao': 'Moderado', 'faixa': '0.4 < PL/Ativos <= 0.6', 'descricao': 'PL/Ativos indica estrutura de capital equilibrada.'}
    elif 0.6 < pl_ativos <= 0.8:
        return {'classificacao': 'Ótimo', 'faixa': '0.6 < PL/Ativos <= 0.8', 'descricao': 'PL/Ativos alto indica patrimônio sólido, com baixo endividamento.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'PL/Ativos > 0.8', 'descricao': 'PL/Ativos extremamente alto sugere pouco endividamento, mas pode indicar ineficiência.'}

def evaluate_passivos_ativos(passivos_ativos):
    """
    Avalia o Passivos/Ativos com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(passivos_ativos, (int, float)):
        raise TypeError("Passivos/Ativos deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if passivos_ativos < 0:
        return {'classificacao': 'Crítico', 'faixa': 'Passivos/Ativos < 0', 'descricao': 'Passivos/Ativos negativo é impossível e sugere erro contábil.'}
    elif 0 <= passivos_ativos <= 0.2:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= Passivos/Ativos <= 0.2', 'descricao': 'Passivos/Ativos baixo indica endividamento mínimo.'}
    elif 0.2 < passivos_ativos <= 0.4:
        return {'classificacao': 'Moderado', 'faixa': '0.2 < Passivos/Ativos <= 0.4', 'descricao': 'Passivos/Ativos moderado indica endividamento controlado.'}
    elif 0.4 < passivos_ativos <= 0.6:
        return {'classificacao': 'Ruim', 'faixa': '0.4 < Passivos/Ativos <= 0.6', 'descricao': 'Passivos/Ativos elevado sugere endividamento moderado.'}
    elif 0.6 < passivos_ativos <= 0.8:
        return {'classificacao': 'Péssimo', 'faixa': '0.6 < Passivos/Ativos <= 0.8', 'descricao': 'Passivos/Ativos alto indica endividamento elevado.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Passivos/Ativos > 0.8', 'descricao': 'Passivos/Ativos extremamente alto sugere endividamento excessivo.'}

def evaluate_liquidez_corrente(lc):
    """
    Avalia a Liquidez Corrente (Ativo Circulante/Passivo Circulante) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(lc, (int, float)):
        raise TypeError("Liquidez Corrente deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if lc < 0.5:
        return {'classificacao': 'Crítico', 'faixa': 'Liquidez < 0.5', 'descricao': 'Liquidez muito baixa indica alto risco de insolvência de curto prazo.'}
    elif 0.5 <= lc <= 1:
        return {'classificacao': 'Péssimo', 'faixa': '0.5 <= Liquidez <= 1', 'descricao': 'Liquidez baixa sugere dificuldades para cobrir obrigações de curto prazo.'}
    elif 1 < lc <= 1.5:
        return {'classificacao': 'Ruim', 'faixa': '1 < Liquidez <= 1.5', 'descricao': 'Liquidez limitada indica capacidade moderada de honrar obrigações.'}
    elif 1.5 < lc <= 2:
        return {'classificacao': 'Moderado', 'faixa': '1.5 < Liquidez <= 2', 'descricao': 'Liquidez adequada sugere equilíbrio na gestão de obrigações.'}
    elif 2 < lc <= 3:
        return {'classificacao': 'Ótimo', 'faixa': '2 < Liquidez <= 3', 'descricao': 'Liquidez alta indica forte capacidade de cobrir obrigações.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Liquidez > 3', 'descricao': 'Liquidez extremamente alta sugere excesso de ativos circulantes.'}

def evaluate_peg_ratio(peg):
    """
    Avalia o PEG Ratio (P/L dividido pelo crescimento esperado do lucro) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(peg, (int, float)):
        raise TypeError("PEG Ratio deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if peg < 0:
        return {'classificacao': 'Crítico', 'faixa': 'PEG < 0', 'descricao': 'PEG negativo indica P/L negativo ou crescimento esperado negativo.'}
    elif 0 <= peg <= 0.5:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= PEG <= 0.5', 'descricao': 'PEG baixo sugere subvalorização em relação ao crescimento esperado.'}
    elif 0.5 < peg <= 1:
        return {'classificacao': 'Moderado', 'faixa': '0.5 < PEG <= 1', 'descricao': 'PEG indica valuation justo, equilibrando preço e crescimento.'}
    elif 1 < peg <= 1.5:
        return {'classificacao': 'Ruim', 'faixa': '1 < PEG <= 1.5', 'descricao': 'PEG elevado sugere sobrevalorização moderada.'}
    elif 1.5 < peg <= 2:
        return {'classificacao': 'Péssimo', 'faixa': '1.5 < PEG <= 2', 'descricao': 'PEG muito alto indica ação cara em relação ao crescimento.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'PEG > 2', 'descricao': 'PEG extremamente elevado sugere sobrevalorização severa.'}

def evaluate_p_ativo(p_ativo):
    """
    Avalia o Preço/Ativo Total com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(p_ativo, (int, float)):
        raise TypeError("P/Ativo deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if p_ativo < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/Ativo < 0', 'descricao': 'P/Ativo negativo é impossível e sugere erro nos dados.'}
    elif 0 <= p_ativo <= 0.3:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/Ativo <= 0.3', 'descricao': 'P/Ativo baixo sugere subvalorização em relação aos ativos totais.'}
    elif 0.3 < p_ativo <= 0.6:
        return {'classificacao': 'Moderado', 'faixa': '0.3 < P/Ativo <= 0.6', 'descricao': 'P/Ativo indica valuation justo, típico de empresas com ativos sólidos.'}
    elif 0.6 < p_ativo <= 1:
        return {'classificacao': 'Ruim', 'faixa': '0.6 < P/Ativo <= 1', 'descricao': 'P/Ativo elevado sugere sobrevalorização moderada.'}
    elif 1 < p_ativo <= 1.5:
        return {'classificacao': 'Péssimo', 'faixa': '1 < P/Ativo <= 1.5', 'descricao': 'P/Ativo muito alto indica ação cara em relação aos ativos.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/Ativo > 1.5', 'descricao': 'P/Ativo extremamente elevado sugere sobrevalorização severa.'}

def evaluate_vpa(vpa_preco):
    """
    Avalia o VPA/Preço (Valor Patrimonial por Ação dividido pelo preço da ação) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(vpa_preco, (int, float)):
        raise TypeError("VPA/Preço deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if vpa_preco < 0:
        return {'classificacao': 'Crítico', 'faixa': 'VPA/Preço < 0', 'descricao': 'VPA/Preço negativo indica patrimônio líquido negativo.'}
    elif 0 <= vpa_preco <= 0.5:
        return {'classificacao': 'Fora da faixa', 'faixa': '0 <= VPA/Preço <= 0.5', 'descricao': 'VPA/Preço muito baixo indica sobrevalorização severa.'}
    elif 0.5 < vpa_preco <= 1:
        return {'classificacao': 'Péssimo', 'faixa': '0.5 < VPA/Preço <= 1', 'descricao': 'VPA/Preço baixo sugere ação cara em relação ao patrimônio.'}
    elif 1 < vpa_preco <= 1.5:
        return {'classificacao': 'Ruim', 'faixa': '1 < VPA/Preço <= 1.5', 'descricao': 'VPA/Preço moderado indica sobrevalorização.'}
    elif 1.5 < vpa_preco <= 2:
        return {'classificacao': 'Moderado', 'faixa': '1.5 < VPA/Preço <= 2', 'descricao': 'VPA/Preço indica valuation justo.'}
    else:
        return {'classificacao': 'Ótimo', 'faixa': 'VPA/Preço > 2', 'descricao': 'VPA/Preço alto sugere subvalorização em relação ao patrimônio.'}

def evaluate_lpa(lpa):
    """
    Avalia o Lucro por Ação (LPA) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(lpa, (int, float)):
        raise TypeError("LPA deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if lpa < 0:
        return {'classificacao': 'Crítico', 'faixa': 'LPA < 0', 'descricao': 'LPA negativo indica prejuízo por ação.'}
    elif 0 <= lpa <= 0.5:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= LPA <= 0.5', 'descricao': 'LPA muito baixo sugere lucratividade limitada.'}
    elif 0.5 < lpa <= 1:
        return {'classificacao': 'Ruim', 'faixa': '0.5 < LPA <= 1', 'descricao': 'LPA limitado indica lucratividade moderada.'}
    elif 1 < lpa <= 2:
        return {'classificacao': 'Moderado', 'faixa': '1 < LPA <= 2', 'descricao': 'LPA adequado sugere lucratividade equilibrada.'}
    elif 2 < lpa <= 3:
        return {'classificacao': 'Ótimo', 'faixa': '2 < LPA <= 3', 'descricao': 'LPA alto indica forte lucratividade por ação.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'LPA > 3', 'descricao': 'LPA extremamente alto sugere lucratividade excepcional.'}

def evaluate_psr(psr):
    """
    Avalia o Preço/Receita (P/SR) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(psr, (int, float)):
        raise TypeError("P/SR deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if psr < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/SR < 0', 'descricao': 'P/SR negativo indica receita negativa, sugerindo problemas graves.'}
    elif 0 <= psr <= 0.5:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/SR <= 0.5', 'descricao': 'P/SR baixo sugere subvalorização em relação à receita.'}
    elif 0.5 < psr <= 1:
        return {'classificacao': 'Moderado', 'faixa': '0.5 < P/SR <= 1', 'descricao': 'P/SR indica valuation justo.'}
    elif 1 < psr <= 2:
        return {'classificacao': 'Ruim', 'faixa': '1 < P/SR <= 2', 'descricao': 'P/SR elevado sugere sobrevalorização moderada.'}
    elif 2 < psr <= 3:
        return {'classificacao': 'Péssimo', 'faixa': '2 < P/SR <= 3', 'descricao': 'P/SR muito alto indica ação cara.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/SR > 3', 'descricao': 'P/SR extremamente elevado sugere sobrevalorização severa.'}

def evaluate_p_ativo_circ_liq(p_acl):
    """
    Avalia o Preço/Ativo Circulante Líquido com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(p_acl, (int, float)):
        raise TypeError("P/ACL deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if p_acl < 0:
        return {'classificacao': 'Crítico', 'faixa': 'P/ACL < 0', 'descricao': 'P/ACL negativo indica ativo circulante líquido negativo.'}
    elif 0 <= p_acl <= 0.5:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= P/ACL <= 0.5', 'descricao': 'P/ACL baixo sugere subvalorização em relação aos ativos circulantes.'}
    elif 0.5 < p_acl <= 1:
        return {'classificacao': 'Moderado', 'faixa': '0.5 < P/ACL <= 1', 'descricao': 'P/ACL indica valuation justo.'}
    elif 1 < p_acl <= 2:
        return {'classificacao': 'Ruim', 'faixa': '1 < P/ACL <= 2', 'descricao': 'P/ACL elevado sugere sobrevalorização moderada.'}
    elif 2 < p_acl <= 3:
        return {'classificacao': 'Péssimo', 'faixa': '2 < P/ACL <= 3', 'descricao': 'P/ACL muito alto indica ação cara.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'P/ACL > 3', 'descricao': 'P/ACL extremamente elevado sugere sobrevalorização severa.'}

def evaluate_liquidez_media_diaria(lmd):
    """
    Avalia a Liquidez Média Diária (em R$ milhões) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(lmd, (int, float)):
        raise TypeError("Liquidez Média Diária deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if lmd < 0.5:
        return {'classificacao': 'Crítico', 'faixa': 'LMD < 0.5', 'descricao': 'Liquidez muito baixa indica baixa negociabilidade, com alto risco de iliquidez.'}
    elif 0.5 <= lmd <= 2:
        return {'classificacao': 'Péssimo', 'faixa': '0.5 <= LMD <= 2', 'descricao': 'Liquidez baixa sugere dificuldades para negociar ações.'}
    elif 2 < lmd <= 5:
        return {'classificacao': 'Ruim', 'faixa': '2 < LMD <= 5', 'descricao': 'Liquidez limitada indica negociabilidade moderada.'}
    elif 5 < lmd <= 10:
        return {'classificacao': 'Moderado', 'faixa': '5 < LMD <= 10', 'descricao': 'Liquidez adequada sugere boa negociabilidade.'}
    elif 10 < lmd <= 20:
        return {'classificacao': 'Ótimo', 'faixa': '10 < LMD <= 20', 'descricao': 'Liquidez alta indica forte negociabilidade.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'LMD > 20', 'descricao': 'Liquidez extremamente alta sugere excelente negociabilidade.'}

def evaluate_patrimonio_liquido_pl_vm(pl_vm):
    """
    Avalia o Patrimônio Líquido/Valor de Mercado com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(pl_vm, (int, float)):
        raise TypeError("Patrimônio Líquido/VM deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if pl_vm < 0:
        return {'classificacao': 'Crítico', 'faixa': 'PL/VM < 0', 'descricao': 'Patrimônio Líquido negativo indica graves problemas financeiros.'}
    elif 0 <= pl_vm <= 0.5:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= PL/VM <= 0.5', 'descricao': 'PL/VM baixo sugere patrimônio insuficiente em relação ao valor de mercado.'}
    elif 0.5 < pl_vm <= 1:
        return {'classificacao': 'Ruim', 'faixa': '0.5 < PL/VM <= 1', 'descricao': 'PL/VM limitado indica patrimônio moderado.'}
    elif 1 < pl_vm <= 1.5:
        return {'classificacao': 'Moderado', 'faixa': '1 < PL/VM <= 1.5', 'descricao': 'PL/VM adequado sugere equilíbrio entre patrimônio e valor de mercado.'}
    elif 1.5 < pl_vm <= 2:
        return {'classificacao': 'Ótimo', 'faixa': '1.5 < PL/VM <= 2', 'descricao': 'PL/VM alto indica patrimônio sólido.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'PL/VM > 2', 'descricao': 'PL/VM extremamente alto sugere subvalorização ou ineficiência.'}

def evaluate_ativos_vm(ativos_vm):
    """
    Avalia o Ativos/Valor de Mercado com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(ativos_vm, (int, float)):
        raise TypeError("Ativos/VM deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if ativos_vm < 0:
        return {'classificacao': 'Crítico', 'faixa': 'Ativos/VM < 0', 'descricao': 'Ativos/VM negativo é impossível e sugere erro nos dados.'}
    elif 0 <= ativos_vm <= 0.5:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= Ativos/VM <= 0.5', 'descricao': 'Ativos/VM baixo sugere ativos insuficientes em relação ao valor de mercado.'}
    elif 0.5 < ativos_vm <= 1:
        return {'classificacao': 'Ruim', 'faixa': '0.5 < Ativos/VM <= 1', 'descricao': 'Ativos/VM limitado indica ativos moderados.'}
    elif 1 < ativos_vm <= 2:
        return {'classificacao': 'Moderado', 'faixa': '1 < Ativos/VM <= 2', 'descricao': 'Ativos/VM adequado sugere equilíbrio entre ativos e valor de mercado.'}
    elif 2 < ativos_vm <= 3:
        return {'classificacao': 'Ótimo', 'faixa': '2 < Ativos/VM <= 3', 'descricao': 'Ativos/VM alto indica ativos sólidos.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Ativos/VM > 3', 'descricao': 'Ativos/VM extremamente alto sugere subvalorização ou ineficiência.'}

def evaluate_ativo_circulante_vm(ac_vm):
    """
    Avalia o Ativo Circulante/Valor de Mercado com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(ac_vm, (int, float)):
        raise TypeError("Ativo Circulante/VM deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if ac_vm < 0:
        return {'classificacao': 'Crítico', 'faixa': 'AC/VM < 0', 'descricao': 'Ativo Circulante/VM negativo é impossível e sugere erro nos dados.'}
    elif 0 <= ac_vm <= 0.3:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= AC/VM <= 0.3', 'descricao': 'AC/VM baixo sugere ativos circulantes insuficientes.'}
    elif 0.3 < ac_vm <= 0.6:
        return {'classificacao': 'Ruim', 'faixa': '0.3 < AC/VM <= 0.6', 'descricao': 'AC/VM limitado indica ativos circulantes moderados.'}
    elif 0.6 < ac_vm <= 1:
        return {'classificacao': 'Moderado', 'faixa': '0.6 < AC/VM <= 1', 'descricao': 'AC/VM adequado sugere equilíbrio.'}
    elif 1 < ac_vm <= 1.5:
        return {'classificacao': 'Ótimo', 'faixa': '1 < AC/VM <= 1.5', 'descricao': 'AC/VM alto indica ativos circulantes sólidos.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'AC/VM > 1.5', 'descricao': 'AC/VM extremamente alto sugere excesso de liquidez.'}

def evaluate_divida_bruta_vm(db_vm):
    """
    Avalia a Dívida Bruta/Valor de Mercado com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(db_vm, (int, float)):
        raise TypeError("Dívida Bruta/VM deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if db_vm < 0:
        return {'classificacao': 'Crítico', 'faixa': 'DB/VM < 0', 'descricao': 'Dívida Bruta/VM negativa é impossível e sugere erro nos dados.'}
    elif 0 <= db_vm <= 0.2:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= DB/VM <= 0.2', 'descricao': 'Dívida Bruta/VM baixa indica endividamento mínimo.'}
    elif 0.2 < db_vm <= 0.5:
        return {'classificacao': 'Moderado', 'faixa': '0.2 < DB/VM <= 0.5', 'descricao': 'Dívida Bruta/VM moderada indica endividamento controlado.'}
    elif 0.5 < db_vm <= 1:
        return {'classificacao': 'Ruim', 'faixa': '0.5 < DB/VM <= 1', 'descricao': 'Dívida Bruta/VM elevada sugere endividamento moderado.'}
    elif 1 < db_vm <= 1.5:
        return {'classificacao': 'Péssimo', 'faixa': '1 < DB/VM <= 1.5', 'descricao': 'Dívida Bruta/VM alta indica endividamento elevado.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'DB/VM > 1.5', 'descricao': 'Dívida Bruta/VM extremamente alta sugere endividamento excessivo.'}

def evaluate_disponibilidade_vm(disp_vm):
    """
    Avalia a Disponibilidade/Valor de Mercado com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(disp_vm, (int, float)):
        raise TypeError("Disponibilidade/VM deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if disp_vm < 0:
        return {'classificacao': 'Crítico',
                'faixa': 'Disp/VM < 0',
                'descricao': 'Disponibilidade/VM negativa é impossível e sugere erro nos dados.'}
    elif 0 <= disp_vm <= 0.1:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= Disp/VM <= 0.1', 'descricao': 'Disponibilidade/VM baixa sugere pouca liquidez imediata.'}
    elif 0.1 < disp_vm <= 0.3:
        return {'classificacao': 'Ruim', 'faixa': '0.1 < Disp/VM <= 0.3', 'descricao': 'Disponibilidade/VM limitada indica liquidez moderada.'}
    elif 0.3 < disp_vm <= 0.5:
        return {'classificacao': 'Moderado', 'faixa': '0.3 < Disp/VM <= 0.5', 'descricao': 'Disponibilidade/VM adequada sugere equilíbrio.'}
    elif 0.5 < disp_vm <= 1:
        return {'classificacao': 'Ótimo', 'faixa': '0.5 < Disp/VM <= 1', 'descricao': 'Disponibilidade/VM alta indica forte liquidez imediata.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'Disp/VM > 1', 'descricao': 'Disponibilidade/VM extremamente alta sugere excesso de caixa.'}

def evaluate_divida_liquida_vm(dl_vm):
    """
    Avalia a Dívida Líquida/Valor de Mercado com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(dl_vm, (int, float)):
        raise TypeError("Dívida Líquida/VM deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if dl_vm < -0.5:
        return {'classificacao': 'Crítico', 'faixa': 'DL/VM < -0.5', 'descricao': 'Dívida Líquida/VM extremamente negativa indica caixa excessivo.'}
    elif -0.5 <= dl_vm < 0:
        return {'classificacao': 'Ótimo', 'faixa': '-0.5 <= DL/VM < 0', 'descricao': 'Dívida Líquida negativa indica solidez financeira.'}
    elif 0 <= dl_vm <= 0.3:
        return {'classificacao': 'Moderado', 'faixa': '0 <= DL/VM <= 0.3', 'descricao': 'Dívida Líquida/VM baixa indica endividamento controlado.'}
    elif 0.3 < dl_vm <= 0.6:
        return {'classificacao': 'Ruim', 'faixa': '0.3 < DL/VM <= 0.6', 'descricao': 'Dívida Líquida/VM moderada sugere endividamento aceitável.'}
    elif 0.6 < dl_vm <= 1:
        return {'classificacao': 'Péssimo', 'faixa': '0.6 < DL/VM <= 1', 'descricao': 'Dívida Líquida/VM alta indica endividamento elevado.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'DL/VM > 1', 'descricao': 'Dívida Líquida/VM extremamente alta sugere endividamento excessivo.'}

def evaluate_valor_mercado_receita(vm_receita):
    """
    Avalia o Valor de Mercado/Receita com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(vm_receita, (int, float)):
        raise TypeError("Valor de Mercado/Receita deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if vm_receita < 0:
        return {'classificacao': 'Crítico', 'faixa': 'VM/Receita < 0', 'descricao': 'VM/Receita negativo indica receita negativa, sugerindo problemas graves.'}
    elif 0 <= vm_receita <= 0.5:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= VM/Receita <= 0.5', 'descricao': 'VM/Receita baixo sugere subvalorização em relação à receita.'}
    elif 0.5 < vm_receita <= 1:
        return {'classificacao': 'Moderado', 'faixa': '0.5 < VM/Receita <= 1', 'descricao': 'VM/Receita indica valuation justo.'}
    elif 1 < vm_receita <= 2:
        return {'classificacao': 'Ruim', 'faixa': '1 < VM/Receita <= 2', 'descricao': 'VM/Receita elevado sugere sobrevalorização moderada.'}
    elif 2 < vm_receita <= 3:
        return {'classificacao': 'Péssimo', 'faixa': '2 < VM/Receita <= 3', 'descricao': 'VM/Receita muito alto indica empresa cara.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'VM/Receita > 3', 'descricao': 'VM/Receita extremamente elevado sugere sobrevalorização severa.'}

def evaluate_valor_firma_receita(vf_receita):
    """
    Avalia o Valor de Firma/Receita com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(vf_receita, (int, float)):
        raise TypeError("Valor de Firma/Receita deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if vf_receita < 0:
        return {'classificacao': 'Crítico', 'faixa': 'VF/Receita < 0', 'descricao': 'VF/Receita negativo indica receita negativa, sugerindo problemas graves.'}
    elif 0 <= vf_receita <= 0.5:
        return {'classificacao': 'Ótimo', 'faixa': '0 <= VF/Receita <= 0.5', 'descricao': 'VF/Receita baixo sugere subvalorização em relação à receita.'}
    elif 0.5 < vf_receita <= 1:
        return {'classificacao': 'Moderado', 'faixa': '0.5 < VF/Receita <= 1', 'descricao': 'VF/Receita indica valuation justo.'}
    elif 1 < vf_receita <= 2:
        return {'classificacao': 'Ruim', 'faixa': '1 < VF/Receita <= 2', 'descricao': 'VF/Receita elevado sugere sobrevalorização moderada.'}
    elif 2 < vf_receita <= 3:
        return {'classificacao': 'Péssimo', 'faixa': '2 < VF/Receita <= 3', 'descricao': 'VF/Receita muito alto indica empresa cara.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'VF/Receita > 3', 'descricao': 'VF/Receita extremamente elevado sugere sobrevalorização severa.'}

def evaluate_roe(roe):
    """
    Avalia o Retorno sobre Patrimônio (ROE) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(roe, (int, float)):
        raise TypeError("ROE deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if roe < 0:
        return {'classificacao': 'Crítico', 'faixa': 'ROE < 0', 'descricao': 'ROE negativo indica prejuízo, sugerindo problemas financeiros.'}
    elif 0 <= roe <= 5:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= ROE <= 5', 'descricao': 'ROE muito baixo sugere baixa rentabilidade do patrimônio.'}
    elif 5 < roe <= 10:
        return {'classificacao': 'Ruim', 'faixa': '5 < ROE <= 10', 'descricao': 'ROE limitado indica rentabilidade moderada.'}
    elif 10 < roe <= 20:
        return {'classificacao': 'Moderado', 'faixa': '10 < ROE <= 20', 'descricao': 'ROE adequado sugere rentabilidade equilibrada.'}
    elif 20 < roe <= 30:
        return {'classificacao': 'Ótimo', 'faixa': '20 < ROE <= 30', 'descricao': 'ROE alto indica forte rentabilidade do patrimônio.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'ROE > 30', 'descricao': 'ROE extremamente alto sugere rentabilidade excepcional, mas verificar sustentabilidade.'}

def evaluate_margem_liquida(ml):
    """
    Avalia a Margem Líquida com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(ml, (int, float)):
        raise TypeError("Margem Líquida deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if ml < 0:
        return {'classificacao': 'Crítico', 'faixa': 'ML < 0', 'descricao': 'Margem Líquida negativa indica prejuízo, sugerindo problemas operacionais.'}
    elif 0 <= ml <= 5:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= ML <= 5', 'descricao': 'Margem Líquida muito baixa sugere baixa eficiência na geração de lucro.'}
    elif 5 < ml <= 10:
        return {'classificacao': 'Ruim', 'faixa': '5 < ML <= 10', 'descricao': 'Margem Líquida limitada indica eficiência moderada.'}
    elif 10 < ml <= 20:
        return {'classificacao': 'Moderado', 'faixa': '10 < ML <= 20', 'descricao': 'Margem Líquida adequada sugere eficiência equilibrada.'}
    elif 20 < ml <= 30:
        return {'classificacao': 'Ótimo', 'faixa': '20 < ML <= 30', 'descricao': 'Margem Líquida alta indica forte eficiência na geração de lucro.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'ML > 30', 'descricao': 'Margem Líquida extremamente alta sugere eficiência excepcional.'}

def evaluate_roic(roic):
    """
    Avalia o Retorno sobre Capital Investido (ROIC) com base em faixas definidas para o mercado brasileiro.
    """
    if not isinstance(roic, (int, float)):
        raise TypeError("ROIC deve ser um número (int ou float)")
    # TODO: Futura integração com Fundamentus
    if roic < 0:
        return {'classificacao': 'Crítico', 'faixa': 'ROIC < 0', 'descricao': 'ROIC negativo indica ineficiência na alocação de capital.'}
    elif 0 <= roic <= 5:
        return {'classificacao': 'Péssimo', 'faixa': '0 <= ROIC <= 5', 'descricao': 'ROIC muito baixo sugere baixa eficiência no uso do capital.'}
    elif 5 < roic <= 10:
        return {'classificacao': 'Ruim', 'faixa': '5 < ROIC <= 10', 'descricao': 'ROIC limitado indica eficiência moderada.'}
    elif 10 < roic <= 15:
        return {'classificacao': 'Moderado', 'faixa': '10 < ROIC <= 15', 'descricao': 'ROIC adequado sugere eficiência equilibrada.'}
    elif 15 < roic <= 25:
        return {'classificacao': 'Ótimo', 'faixa': '15 < ROIC <= 25', 'descricao': 'ROIC alto indica forte eficiência no uso do capital.'}
    else:
        return {'classificacao': 'Fora da faixa', 'faixa': 'ROIC > 25', 'descricao': 'ROIC extremamente alto sugere eficiência excepcional.'}

class TestEvaluateIndicators(unittest.TestCase):
    """Testes unitários para as funções de avaliação de indicadores."""

    def test_giro_ativos(self):
        result = evaluate_giro_ativos(-0.1)
        self.assertEqual(result['classificacao'], 'Crítico')
        self.assertEqual(result['faixa'], 'Giro < 0')
        result = evaluate_giro_ativos(0.2)
        self.assertEqual(result['classificacao'], 'Ruim')
        result = evaluate_giro_ativos(0.4)
        self.assertEqual(result['classificacao'], 'Péssimo')
        result = evaluate_giro_ativos(0.8)
        self.assertEqual(result['classificacao'], 'Moderado')
        result = evaluate_giro_ativos(1.2)
        self.assertEqual(result['classificacao'], 'Ótimo')
        result = evaluate_giro_ativos(2)
        self.assertEqual(result['classificacao'], 'Fora da faixa')
        with self.assertRaises(TypeError):
            evaluate_giro_ativos("0.5")

    def test_divida_liquida_ebitda(self):
        result = evaluate_divida_liquida_ebitda(-4)
        self.assertEqual(result['classificacao'], 'Crítico')
        result = evaluate_divida_liquida_ebitda(-1)
        self.assertEqual(result['classificacao'], 'Ótimo')
        result = evaluate_divida_liquida_ebitda(0.5)
        self.assertEqual(result['classificacao'], 'Moderado')
        result = evaluate_divida_liquida_ebitda(1.5)
        self.assertEqual(result['classificacao'], 'Ruim')
        result = evaluate_divida_liquida_ebitda(2.5)
        self.assertEqual(result['classificacao'], 'Péssimo')
        result = evaluate_divida_liquida_ebitda(4)
        self.assertEqual(result['classificacao'], 'Fora da faixa')
        with self.assertRaises(TypeError):
            evaluate_divida_liquida_ebitda("1")

    def test_liquidez_corrente(self):
        result = evaluate_liquidez_corrente(0.3)
        self.assertEqual(result['classificacao'], 'Crítico')
        result = evaluate_liquidez_corrente(0.7)
        self.assertEqual(result['classificacao'], 'Péssimo')
        result = evaluate_liquidez_corrente(1.2)
        self.assertEqual(result['classificacao'], 'Ruim')
        result = evaluate_liquidez_corrente(1.8)
        self.assertEqual(result['classificacao'], 'Moderado')
        result = evaluate_liquidez_corrente(2.5)
        self.assertEqual(result['classificacao'], 'Ótimo')
        result = evaluate_liquidez_corrente(4)
        self.assertEqual(result['classificacao'], 'Fora da faixa')
        with self.assertRaises(TypeError):
            evaluate_liquidez_corrente("1.5")

    def test_peg_ratio(self):
        result = evaluate_peg_ratio(-0.1)
        self.assertEqual(result['classificacao'], 'Crítico')
        result = evaluate_peg_ratio(0.3)
        self.assertEqual(result['classificacao'], 'Ótimo')
        result = evaluate_peg_ratio(0.8)
        self.assertEqual(result['classificacao'], 'Moderado')
        result = evaluate_peg_ratio(1.2)
        self.assertEqual(result['classificacao'], 'Ruim')
        result = evaluate_peg_ratio(1.8)
        self.assertEqual(result['classificacao'], 'Péssimo')
        result = evaluate_peg_ratio(3)
        self.assertEqual(result['classificacao'], 'Fora da faixa')
        with self.assertRaises(TypeError):
            evaluate_peg_ratio("1")

    def test_psr(self):
        result = evaluate_psr(-0.1)
        self.assertEqual(result['classificacao'], 'Crítico')
        result = evaluate_psr(0.3)
        self.assertEqual(result['classificacao'], 'Ótimo')
        result = evaluate_psr(0.8)
        self.assertEqual(result['classificacao'], 'Moderado')
        result = evaluate_psr(1.5)
        self.assertEqual(result['classificacao'], 'Ruim')
        result = evaluate_psr(2.5)
        self.assertEqual(result['classificacao'], 'Péssimo')
        result = evaluate_psr(4)
        self.assertEqual(result['classificacao'], 'Fora da faixa')
        with self.assertRaises(TypeError):
            evaluate_psr("1")

if __name__ == '__main__':
    unittest.main()