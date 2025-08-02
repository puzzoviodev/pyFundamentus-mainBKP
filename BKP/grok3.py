import unittest

# Funções já implementadas anteriormente
def evaluate_pl(pl):
    """
    Avalia o Preço/Lucro (P/L) com base em faixas definidas para o mercado brasileiro:
    - P/L < 0: Crítico (prejuízo, risco extremo)
    - 0 ≤ P/L ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
    - 5 < P/L ≤ 15: Moderado (valuation justo, crescimento moderado)
    - 15 < P/L ≤ 25: Ruim (sobrevalorizado, cautela necessária)
    - 25 < P/L ≤ 35: Péssimo (muito caro, alto risco)
    - P/L > 35: Fora da faixa (extremamente sobrevalorizado, risco elevado)

    Args:
        pl (float or int): Valor do índice Preço/Lucro.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do P/L.

    Raises:
        TypeError: Se P/L não for um número (int ou float).
    """
    if not isinstance(pl, (int, float)):
        raise TypeError("P/L deve ser um número (int ou float)")

    if pl < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'P/L < 0',
            'descricao': 'P/L negativo indica prejuízo, sugerindo problemas financeiros ou cíclicos. Comum em empresas em crise ou setores voláteis (ex.: commodities). Exige análise detalhada.'
        }
    elif 0 <= pl <= 5:
        return {
            'classificacao': 'Ótimo',
            'faixa': '0 <= P/L <= 5',
            'descricao': 'P/L baixo sugere subvalorização, com preço atrativo em relação ao lucro. Comum em setores maduros (ex.: bancos, utilities) ou empresas em recuperação. Oportunidade de compra.'
        }
    elif 5 < pl <= 15:
        return {
            'classificacao': 'Moderado',
            'faixa': '5 < P/L <= 15',
            'descricao': 'P/L indica valuation justo, típico de empresas com crescimento moderado. Comum em setores consolidados (ex.: indústria, energia). Equilíbrio entre risco e retorno.'
        }
    elif 15 < pl <= 25:
        return {
            'classificacao': 'Ruim',
            'faixa': '15 < P/L <= 25',
            'descricao': 'P/L elevado sugere sobrevalorização, com mercado esperando crescimento. Aceitável em setores dinâmicos (ex.: tecnologia), mas exige cautela.'
        }
    elif 25 < pl <= 35:
        return {
            'classificacao': 'Péssimo',
            'faixa': '25 < P/L <= 35',
            'descricao': 'P/L muito alto indica que a ação está cara, com expectativas de crescimento elevadas. Comum em setores de alto crescimento, mas com risco significativo.'
        }
    else:  # pl > 35
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'P/L > 35',
            'descricao': 'P/L extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas. Exige análise detalhada de crescimento futuro.'
        }

def evaluate_pebitda(pebitda):
    """
    Avalia o Preço/EBITDA (P/EBITDA) com base em faixas definidas para o mercado brasileiro:
    - P/EBITDA < 0: Crítico (EBITDA negativo, risco extremo)
    - 0 ≤ P/EBITDA ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
    - 5 < P/EBITDA ≤ 8: Moderado (valuation justo, crescimento moderado)
    - 8 < P/EBITDA ≤ 12: Ruim (sobrevalorizado, cautela necessária)
    - 12 < P/EBITDA ≤ 15: Péssimo (muito caro, alto risco)
    - P/EBITDA > 15: Fora da faixa (extremamente sobrevalorizado, risco elevado)

    Args:
        pebitda (float or int): Valor do índice Preço/EBITDA.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do P/EBITDA.

    Raises:
        TypeError: Se P/EBITDA não for um número (int ou float).
    """
    if not isinstance(pebitda, (int, float)):
        raise TypeError("P/EBITDA deve ser um número (int ou float)")

    if pebitda < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'P/EBITDA < 0',
            'descricao': 'P/EBITDA negativo indica EBITDA negativo, sugerindo problemas operacionais graves. Raro, exige análise detalhada de fluxo de caixa e recuperação.'
        }
    elif 0 <= pebitda <= 5:
        return {
            'classificacao': 'Ótimo',
            'faixa': '0 <= P/EBITDA <= 5',
            'descricao': 'P/EBITDA baixo sugere que a ação está subvalorizada em relação ao fluxo de caixa operacional. Comum em setores maduros (ex.: bancos, utilities) ou em recuperação. Oportunidade de compra.'
        }
    elif 5 < pebitda <= 8:
        return {
            'classificacao': 'Moderado',
            'faixa': '5 < P/EBITDA <= 8',
            'descricao': 'P/EBITDA indica valuation justo, típico de empresas com geração de caixa estável. Comum em setores consolidados (ex.: indústria, celulose). Equilíbrio entre risco e retorno.'
        }
    elif 8 < pebitda <= 12:
        return {
            'classificacao': 'Ruim',
            'faixa': '8 < P/EBITDA <= 12',
            'descricao': 'P/EBITDA elevado sugere sobrevalorização moderada, com mercado esperando crescimento. Aceitável em setores dinâmicos (ex.: varejo tech), mas exige cautela.'
        }
    elif 12 < pebitda <= 15:
        return {
            'classificacao': 'Péssimo',
            'faixa': '12 < P/EBITDA <= 15',
            'descricao': 'P/EBITDA muito alto indica que a ação está cara, com expectativas de crescimento elevadas. Alto risco de correção, salvo em setores de crescimento.'
        }
    else:  # pebitda > 15
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'P/EBITDA > 15',
            'descricao': 'P/EBITDA extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas. Pode ser justificado em setores de crescimento excepcional (ex.: tecnologia).'
        }

def evaluate_pvp(pvp):
    """
    Avalia o Preço/Valor Patrimonial (P/VP) com base em faixas definidas para o mercado brasileiro:
    - P/VP < 0: Crítico (patrimônio líquido negativo, risco extremo)
    - 0 ≤ P/VP ≤ 1: Ótimo (subvalorizado, oportunidade de compra)
    - 1 < P/VP ≤ 2: Moderado (valuation justo, crescimento moderado)
    - 2 < P/VP ≤ 3: Ruim (sobrevalorizado, cautela necessária)
    - 3 < P/VP ≤ 5: Péssimo (muito caro, alto risco)
    - P/VP > 5: Fora da faixa (extremamente sobrevalorizado, risco elevado)

    Args:
        pvp (float or int): Valor do índice Preço/Valor Patrimonial.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do P/VP.

    Raises:
        TypeError: Se P/VP não for um número (int ou float).
    """
    if not isinstance(pvp, (int, float)):
        raise TypeError("P/VP deve ser um número (int ou float)")

    if pvp < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'P/VP < 0',
            'descricao': 'P/VP negativo indica patrimônio líquido negativo, sugerindo graves problemas financeiros, como dívidas elevadas ou prejuízos recorrentes. Extremamente raro, exige análise cuidadosa de ativos e passivos.'
        }
    elif 0 <= pvp <= 1:
        return {
            'classificacao': 'Ótimo',
            'faixa': '0 <= P/VP <= 1',
            'descricao': 'P/VP baixo sugere que a ação está subvalorizada, negociada abaixo de seu valor patrimonial. Comum em setores maduros (ex.: bancos, siderurgia) ou empresas com desafios temporários. Oportunidade de compra.'
        }
    elif 1 < pvp <= 2:
        return {
            'classificacao': 'Moderado',
            'faixa': '1 < P/VP <= 2',
            'descricao': 'P/VP indica valuation justo, típico de empresas com estabilidade financeira e crescimento moderado. Comum em setores consolidados (ex.: energia, celulose). Equilíbrio entre risco e retorno.'
        }
    elif 2 < pvp <= 3:
        return {
            'classificacao': 'Ruim',
            'faixa': '2 < P/VP <= 3',
            'descricao': 'P/VP elevado sugere sobrevalorização moderada, com mercado precificando crescimento ou intangíveis (ex.: marca, tecnologia). Exige análise de perspectivas de lucro.'
        }
    elif 3 < pvp <= 5:
        return {
            'classificacao': 'Péssimo',
            'faixa': '3 < P/VP <= 5',
            'descricao': 'P/VP muito alto indica que a ação está cara, com expectativas de crescimento elevadas que podem não se concretizar. Comum em setores de alto crescimento, com risco de correção.'
        }
    else:  # pvp > 5
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'P/VP > 5',
            'descricao': 'P/VP extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas. Pode ser justificado em setores de crescimento excepcional (ex.: tecnologia).'
        }

def evaluate_pebit(pebit):
    """
    Avalia o Preço/EBIT (P/EBIT) com base em faixas definidas para o mercado brasileiro:
    - P/EBIT < 0: Crítico (prejuízo operacional, risco extremo)
    - 0 ≤ P/EBIT ≤ 6: Ótimo (subvalorizado, oportunidade de compra)
    - 6 < P/EBIT ≤ 10: Moderado (valuation justo, crescimento moderado)
    - 10 < P/EBIT ≤ 15: Ruim (sobrevalorizado, cautela necessária)
    - 15 < P/EBIT ≤ 20: Péssimo (muito caro, alto risco)
    - P/EBIT > 20: Fora da faixa (extremamente sobrevalorizado, risco elevado)

    Args:
        pebit (float or int): Valor do índice Preço/EBIT.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do P/EBIT.

    Raises:
        TypeError: Se P/EBIT não for um número (int ou float).
    """
    if not isinstance(pebit, (int, float)):
        raise TypeError("P/EBIT deve ser um número (int ou float)")

    if pebit < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'P/EBIT < 0',
            'descricao': 'P/EBIT negativo indica prejuízo operacional, sugerindo problemas graves na geração de lucro antes de juros e impostos. Raro, exige análise detalhada de recuperação.'
        }
    elif 0 <= pebit <= 6:
        return {
            'classificacao': 'Ótimo',
            'faixa': '0 <= P/EBIT <= 6',
            'descricao': 'P/EBIT baixo sugere que a ação está subvalorizada em relação ao lucro operacional. Comum em setores maduros (ex.: bancos, utilities) ou em recuperação. Oportunidade de compra.'
        }
    elif 6 < pebit <= 10:
        return {
            'classificacao': 'Moderado',
            'faixa': '6 < P/EBIT <= 10',
            'descricao': 'P/EBIT indica valuation justo, típico de empresas com lucro operacional estável. Comum em setores consolidados (ex.: indústria, celulose). Equilíbrio entre risco e retorno.'
        }
    elif 10 < pebit <= 15:
        return {
            'classificacao': 'Ruim',
            'faixa': '10 < P/EBIT <= 15',
            'descricao': 'P/EBIT elevado sugere sobrevalorização moderada, com mercado esperando crescimento. Aceitável em setores dinâmicos (ex.: varejo tech), mas exige cautela.'
        }
    elif 15 < pebit <= 20:
        return {
            'classificacao': 'Péssimo',
            'faixa': '15 < P/EBIT <= 20',
            'descricao': 'P/EBIT muito alto indica que a ação está cara, com expectativas de crescimento elevadas que podem não se concretizar. Alto risco de correção.'
        }
    else:  # pebit > 20
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'P/EBIT > 20',
            'descricao': 'P/EBIT extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas. Pode ser justificado em setores de crescimento excepcional (ex.: tecnologia).'
        }

def evaluate_evebitda(evebitda):
    """
    Avalia o Valor da Firma/EBITDA (EV/EBITDA) com base em faixas definidas para o mercado brasileiro:
    - EV/EBITDA < 0: Crítico (EBITDA negativo, risco extremo)
    - 0 ≤ EV/EBITDA ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
    - 5 < EV/EBITDA ≤ 8: Moderado (valuation justo, crescimento moderado)
    - 8 < EV/EBITDA ≤ 12: Ruim (sobrevalorizado, cautela necessária)
    - 12 < EV/EBITDA ≤ 16: Péssimo (muito caro, alto risco)
    - EV/EBITDA > 16: Fora da faixa (extremamente sobrevalorizado, risco elevado)

    Args:
        evebitda (float or int): Valor do índice EV/EBITDA.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do EV/EBITDA.

    Raises:
        TypeError: Se EV/EBITDA não for um número (int ou float).
    """
    if not isinstance(evebitda, (int, float)):
        raise TypeError("EV/EBITDA deve ser um número (int ou float)")

    if evebitda < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'EV/EBITDA < 0',
            'descricao': 'EV/EBITDA negativo indica EBITDA negativo, sugerindo graves problemas operacionais ou crise financeira. Raro, exige análise detalhada de fluxo de caixa.'
        }
    elif 0 <= evebitda <= 5:
        return {
            'classificacao': 'Ótimo',
            'faixa': '0 <= EV/EBITDA <= 5',
            'descricao': 'EV/EBITDA baixo sugere que a empresa está subvalorizada em relação à geração de caixa. Comum em setores maduros (ex.: bancos, utilities) ou em recuperação. Oportunidade de compra.'
        }
    elif 5 < evebitda <= 8:
        return {
            'classificacao': 'Moderado',
            'faixa': '5 < EV/EBITDA <= 8',
            'descricao': 'EV/EBITDA indica valuation justo, típico de empresas com geração de caixa estável. Comum em setores consolidados (ex.: indústria, celulose). Equilíbrio entre risco e retorno.'
        }
    elif 8 < evebitda <= 12:
        return {
            'classificacao': 'Ruim',
            'faixa': '8 < EV/EBITDA <= 12',
            'descricao': 'EV/EBITDA elevado sugere sobrevalorização moderada, com mercado esperando crescimento. Aceitável em setores dinâmicos (ex.: varejo tech), mas exige cautela.'
        }
    elif 12 < evebitda <= 16:
        return {
            'classificacao': 'Péssimo',
            'faixa': '12 < EV/EBITDA <= 16',
            'descricao': 'EV/EBITDA muito alto indica que a empresa está cara, com expectativas de crescimento elevadas. Alto risco de correção, salvo em setores de crescimento.'
        }
    else:  # evebitda > 16
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'EV/EBITDA > 16',
            'descricao': 'EV/EBITDA extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas. Pode ser justificado em setores de crescimento excepcional (ex.: tecnologia).'
        }

def evaluate_evebit(evebit):
    """
    Avalia o Valor da Firma/EBIT (EV/EBIT) com base em faixas definidas para o mercado brasileiro:
    - EV/EBIT < 0: Crítico (EBIT negativo, risco extremo)
    - 0 ≤ EV/EBIT ≤ 6: Ótimo (subvalorizado, oportunidade de compra)
    - 6 < EV/EBIT ≤ 10: Moderado (valuation justo, crescimento moderado)
    - 10 < EV/EBIT ≤ 15: Ruim (sobrevalorizado, cautela necessária)
    - 15 < EV/EBIT ≤ 20: Péssimo (muito caro, alto risco)
    - EV/EBIT > 20: Fora da faixa (extremamente sobrevalorizado, risco elevado)

    Args:
        evebit (float or int): Valor do índice EV/EBIT.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do EV/EBIT.

    Raises:
        TypeError: Se EV/EBIT não for um número (int ou float).
    """
    if not isinstance(evebit, (int, float)):
        raise TypeError("EV/EBIT deve ser um número (int ou float)")

    if evebit < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'EV/EBIT < 0',
            'descricao': 'EV/EBIT negativo indica EBIT negativo, sugerindo problemas operacionais graves. Raro, exige análise detalhada de recuperação.'
        }
    elif 0 <= evebit <= 6:
        return {
            'classificacao': 'Ótimo',
            'faixa': '0 <= EV/EBIT <= 6',
            'descricao': 'EV/EBIT baixo sugere que a empresa está subvalorizada em relação ao lucro operacional. Comum em setores maduros (ex.: bancos, utilities). Oportunidade de compra.'
        }
    elif 6 < evebit <= 10:
        return {
            'classificacao': 'Moderado',
            'faixa': '6 < EV/EBIT <= 10',
            'descricao': 'EV/EBIT indica valuation justo, típico de empresas com lucro operacional estável. Comum em setores consolidados (ex.: indústria, celulose). Equilíbrio entre risco e retorno.'
        }
    elif 10 < evebit <= 15:
        return {
            'classificacao': 'Ruim',
            'faixa': '10 < EV/EBIT <= 15',
            'descricao': 'EV/EBIT elevado sugere sobrevalorização moderada, com mercado esperando crescimento. Aceitável em setores dinâmicos (ex.: varejo tech), mas exige cautela.'
        }
    elif 15 < evebit <= 20:
        return {
            'classificacao': 'Péssimo',
            'faixa': '15 < EV/EBIT <= 20',
            'descricao': 'EV/EBIT muito alto indica que a empresa está cara, com expectativas de crescimento elevadas. Alto risco de correção.'
        }
    else:  # evebit > 20
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'EV/EBIT > 20',
            'descricao': 'EV/EBIT extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas. Pode ser justificado em setores de crescimento excepcional (ex.: tecnologia).'
        }

# Novas funções para os indicadores fornecidos
def evaluate_giro_ativos(giro):
    """
    Avalia o Giro de Ativos (Receita Líquida/Ativos Totais) com base em faixas definidas para o mercado brasileiro:
    - Giro < 0: Crítico (receita negativa, risco extremo)
    - 0 ≤ Giro ≤ 0.3: Ruim (baixa eficiência no uso de ativos)
    - 0.3 < Giro ≤ 0.6: Péssimo (eficiência muito baixa)
    - 0.6 < Giro ≤ 1.0: Moderado (eficiência aceitável)
    - 1.0 < Giro ≤ 1.5: Ótimo (alta eficiência)
    - Giro > 1.5: Fora da faixa (eficiência excepcional, mas pode indicar alavancagem)

    Args:
        giro (float or int): Valor do índice Giro de Ativos.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do Giro de Ativos.

    Raises:
        TypeError: Se Giro não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter Giro de Ativos automaticamente
    if not isinstance(giro, (int, float)):
        raise TypeError("Giro de Ativos deve ser um número (int ou float)")

    if giro < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'Giro < 0',
            'descricao': 'Giro de Ativos negativo indica receita negativa, sugerindo graves problemas operacionais ou contábeis. Extremamente raro, exige análise detalhada da saúde financeira.'
        }
    elif 0 <= giro <= 0.3:
        return {
            'classificacao': 'Ruim',
            'faixa': '0 <= Giro <= 0.3',
            'descricao': 'Giro baixo indica baixa eficiência no uso de ativos para gerar receita. Comum em setores intensivos em capital (ex.: infraestrutura) ou empresas com problemas operacionais.'
        }
    elif 0.3 < giro <= 0.6:
        return {
            'classificacao': 'Péssimo',
            'faixa': '0.3 < Giro <= 0.6',
            'descricao': 'Giro muito baixo sugere eficiência operacional extremamente limitada. Pode ocorrer em empresas com ativos ociosos ou em setores com margens apertadas.'
        }
    elif 0.6 < giro <= 1.0:
        return {
            'classificacao': 'Moderado',
            'faixa': '0.6 < Giro <= 1.0',
            'descricao': 'Giro indica eficiência aceitável no uso de ativos. Comum em setores consolidados (ex.: indústria, celulose). Oferece equilíbrio, mas há espaço para melhorias.'
        }
    elif 1.0 < giro <= 1.5:
        return {
            'classificacao': 'Ótimo',
            'faixa': '1.0 < Giro <= 1.5',
            'descricao': 'Giro alto sugere alta eficiência na geração de receita com ativos. Comum em setores dinâmicos (ex.: varejo, tecnologia). Representa uma empresa bem gerida.'
        }
    else:  # giro > 1.5
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'Giro > 1.5',
            'descricao': 'Giro extremamente elevado indica eficiência excepcional, mas pode sugerir alavancagem ou subinvestimento em ativos. Comum em empresas leves em ativos (ex.: tecnologia).'
        }

def evaluate_divida_liquida_pl(dl_pl):
    """
    Avalia a Dívida Líquida/Patrimônio Líquido com base em faixas definidas para o mercado brasileiro:
    - Dívida Líquida/PL < -0.5: Crítico (caixa excessivo, ineficiência)
    - -0.5 ≤ Dívida Líquida/PL < 0: Ótimo (caixa supera dívida)
    - 0 ≤ Dívida Líquida/PL ≤ 0.3: Moderado (endividamento baixo)
    - 0.3 < Dívida Líquida/PL ≤ 0.6: Ruim (endividamento moderado)
    - 0.6 < Dívida Líquida/PL ≤ 1: Péssimo (endividamento alto)
    - Dívida Líquida/PL > 1: Fora da faixa (endividamento excessivo)

    Args:
        dl_pl (float or int): Valor do índice Dívida Líquida/PL.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do Dívida Líquida/PL.

    Raises:
        TypeError: Se Dívida Líquida/PL não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter Dívida Líquida/PL automaticamente
    if not isinstance(dl_pl, (int, float)):
        raise TypeError("Dívida Líquida/PL deve ser um número (int ou float)")

    if dl_pl < -0.5:
        return {
            'classificacao': 'Crítico',
            'faixa': 'Dívida Líquida/PL < -0.5',
            'descricao': 'Dívida Líquida/PL extremamente negativa indica caixa excessivo, sugerindo ineficiência na alocação de capital. Pode ser positivo em crises, mas exige análise de estratégia.'
        }
    elif -0.5 <= dl_pl < 0:
        return {
            'classificacao': 'Ótimo',
            'faixa': '-0.5 <= Dívida Líquida/PL < 0',
            'descricao': 'Dívida Líquida negativa indica mais caixa que dívida, sugerindo solidez financeira. Comum em empresas maduras (ex.: tecnologia, utilities). Oportunidade se bem gerida.'
        }
    elif 0 <= dl_pl <= 0.3:
        return {
            'classificacao': 'Moderado',
            'faixa': '0 <= Dívida Líquida/PL <= 0.3',
            'descricao': 'Dívida Líquida/PL baixa indica endividamento controlado. Comum em setores estáveis (ex.: energia, celulose). Equilíbrio entre risco e retorno.'
        }
    elif 0.3 < dl_pl <= 0.6:
        return {
            'classificacao': 'Ruim',
            'faixa': '0.3 < Dívida Líquida/PL <= 0.6',
            'descricao': 'Dívida Líquida/PL moderada sugere endividamento aceitável, mas requer cautela. Comum em setores cíclicos (ex.: mineração). Análise de fluxo de caixa é necessária.'
        }
    elif 0.6 < dl_pl <= 1:
        return {
            'classificacao': 'Péssimo',
            'faixa': '0.6 < Dívida Líquida/PL <= 1',
            'descricao': 'Dívida Líquida/PL alta indica endividamento elevado, com risco de dificuldades financeiras. Pode ser justificado em investimentos, mas há risco de insolvência.'
        }
    else:  # dl_pl > 1
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'Dívida Líquida/PL > 1',
            'descricao': 'Dívida Líquida/PL extremamente alta sugere endividamento excessivo, com alto risco de inadimplência. Comum em empresas alavancadas ou em crise.'
        }

def evaluate_divida_liquida_ebitda(dl_ebitda):
    """
    Avalia a Dívida Líquida/EBITDA com base em faixas definidas para o mercado brasileiro:
    - Dívida Líquida/EBITDA < -3: Crítico (caixa excessivo, ineficiência)
    - -3 ≤ Dívida Líquida/EBITDA < 0: Ótimo (caixa supera dívida)
    - 0 ≤ Dívida Líquida/EBITDA ≤ 1: Moderado (endividamento baixo)
    - 1 < Dívida Líquida/EBITDA ≤ 2: Ruim (endividamento moderado)
    - 2 < Dívida Líquida/EBITDA ≤ 3: Péssimo (endividamento alto)
    - Dívida Líquida/EBITDA > 3: Fora da faixa (endividamento excessivo)

    Args:
        dl_ebitda (float or int): Valor do índice Dívida Líquida/EBITDA.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do Dívida Líquida/EBITDA.

    Raises:
        TypeError: Se Dívida Líquida/EBITDA não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter Dívida Líquida/EBITDA automaticamente
    if not isinstance(dl_ebitda, (int, float)):
        raise TypeError("Dívida Líquida/EBITDA deve ser um número (int ou float)")

    if dl_ebitda < -3:
        return {
            'classificacao': 'Crítico',
            'faixa': 'Dívida Líquida/EBITDA < -3',
            'descricao': 'Dívida Líquida/EBITDA extremamente negativa indica caixa excessivo, sugerindo ineficiência na alocação de capital. Pode ser positivo em crises, mas exige análise.'
        }
    elif -3 <= dl_ebitda < 0:
        return {
            'classificacao': 'Ótimo',
            'faixa': '-3 <= Dívida Líquida/EBITDA < 0',
            'descricao': 'Dívida Líquida negativa indica mais caixa que dívida, sugerindo solidez financeira. Comum em empresas maduras (ex.: tecnologia, utilities). Oportunidade se bem gerida.'
        }
    elif 0 <= dl_ebitda <= 1:
        return {
            'classificacao': 'Moderado',
            'faixa': '0 <= Dívida Líquida/EBITDA <= 1',
            'descricao': 'Dívida Líquida/EBITDA baixa indica endividamento controlado e capacidade de pagamento confortável. Comum em setores estáveis (ex.: energia, celulose).'
        }
    elif 1 < dl_ebitda <= 2:
        return {
            'classificacao': 'Ruim',
            'faixa': '1 < Dívida Líquida/EBITDA <= 2',
            'descricao': 'Dívida Líquida/EBITDA moderada sugere endividamento aceitável, mas requer cautela. Comum em setores cíclicos (ex.: mineração). Análise de fluxo de caixa é necessária.'
        }
    elif 2 < dl_ebitda <= 3:
        return {
            'classificacao': 'Péssimo',
            'faixa': '2 < Dívida Líquida/EBITDA <= 3',
            'descricao': 'Dívida Líquida/EBITDA alta indica endividamento elevado, com risco de dificuldades financeiras. Pode ser justificado em investimentos, mas há risco de insolvência.'
        }
    else:  # dl_ebitda > 3
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'Dívida Líquida/EBITDA > 3',
            'descricao': 'Dívida Líquida/EBITDA extremamente alta sugere endividamento excessivo, com alto risco de inadimplência. Comum em empresas alavancadas ou em crise.'
        }

def evaluate_divida_liquida_ebit(dl_ebit):
    """
    Avalia a Dívida Líquida/EBIT com base em faixas definidas para o mercado brasileiro:
    - Dívida Líquida/EBIT < -4: Crítico (caixa excessivo, ineficiência)
    - -4 ≤ Dívida Líquida/EBIT < 0: Ótimo (caixa supera dívida)
    - 0 ≤ Dívida Líquida/EBIT ≤ 2: Moderado (endividamento baixo)
    - 2 < Dívida Líquida/EBIT ≤ 4: Ruim (endividamento moderado)
    - 4 < Dívida Líquida/EBIT ≤ 6: Péssimo (endividamento alto)
    - Dívida Líquida/EBIT > 6: Fora da faixa (endividamento excessivo)

    Args:
        dl_ebit (float or int): Valor do índice Dívida Líquida/EBIT.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do Dívida Líquida/EBIT.

    Raises:
        TypeError: Se Dívida Líquida/EBIT não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter Dívida Líquida/EBIT automaticamente
    if not isinstance(dl_ebit, (int, float)):
        raise TypeError("Dívida Líquida/EBIT deve ser um número (int ou float)")

    if dl_ebit < -4:
        return {
            'classificacao': 'Crítico',
            'faixa': 'Dívida Líquida/EBIT < -4',
            'descricao': 'Dívida Líquida/EBIT extremamente negativa indica caixa excessivo, sugerindo ineficiência na alocação de capital. Pode ser positivo em crises, mas exige análise.'
        }
    elif -4 <= dl_ebit < 0:
        return {
            'classificacao': 'Ótimo',
            'faixa': '-4 <= Dívida Líquida/EBIT < 0',
            'descricao': 'Dívida Líquida negativa indica mais caixa que dívida, sugerindo solidez financeira. Comum em empresas maduras (ex.: tecnologia, utilities). Oportunidade se bem gerida.'
        }
    elif 0 <= dl_ebit <= 2:
        return {
            'classificacao': 'Moderado',
            'faixa': '0 <= Dívida Líquida/EBIT <= 2',
            'descricao': 'Dívida Líquida/EBIT baixa indica endividamento controlado e capacidade de pagamento confortável. Comum em setores estáveis (ex.: energia, celulose).'
        }
    elif 2 < dl_ebit <= 4:
        return {
            'classificacao': 'Ruim',
            'faixa': '2 < Dívida Líquida/EBIT <= 4',
            'descricao': 'Dívida Líquida/EBIT moderada sugere endividamento aceitável, mas requer cautela. Comum em setores cíclicos (ex.: mineração). Análise de fluxo de caixa é necessária.'
        }
    elif 4 < dl_ebit <= 6:
        return {
            'classificacao': 'Péssimo',
            'faixa': '4 < Dívida Líquida/EBIT <= 6',
            'descricao': 'Dívida Líquida/EBIT alta indica endividamento elevado, com risco de dificuldades financeiras. Pode ser justificado em investimentos, mas há risco de insolvência.'
        }
    else:  # dl_ebit > 6
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'Dívida Líquida/EBIT > 6',
            'descricao': 'Dívida Líquida/EBIT extremamente alta sugere endividamento excessivo, com alto risco de inadimplência. Comum em empresas alavancadas ou em crise.'
        }

def evaluate_pl_ativos(pl_ativos):
    """
    Avalia o Patrimônio Líquido/Ativos com base em faixas definidas para o mercado brasileiro:
    - PL/Ativos < 0: Crítico (patrimônio negativo)
    - 0 ≤ PL/Ativos ≤ 0.2: Péssimo (alta alavancagem)
    - 0.2 < PL/Ativos ≤ 0.4: Ruim (alavancagem moderada)
    - 0.4 < PL/Ativos ≤ 0.6: Moderado (estrutura equilibrada)
    - 0.6 < PL/Ativos ≤ 0.8: Ótimo (patrimônio sólido)
    - PL/Ativos > 0.8: Fora da faixa (pouco endividamento, possível ineficiência)

    Args:
        pl_ativos (float or int): Valor do índice PL/Ativos.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do PL/Ativos.

    Raises:
        TypeError: Se PL/Ativos não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter PL/Ativos automaticamente
    if not isinstance(pl_ativos, (int, float)):
        raise TypeError("PL/Ativos deve ser um número (int ou float)")

    if pl_ativos < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'PL/Ativos < 0',
            'descricao': 'PL/Ativos negativo indica patrimônio líquido negativo, sugerindo graves problemas financeiros, como dívidas elevadas. Exige análise de solvência.'
        }
    elif 0 <= pl_ativos <= 0.2:
        return {
            'classificacao': 'Péssimo',
            'faixa': '0 <= PL/Ativos <= 0.2',
            'descricao': 'PL/Ativos baixo indica alta alavancagem, com poucos ativos financiados por patrimônio. Comum em setores intensivos em dívida (ex.: infraestrutura). Alto risco.'
        }
    elif 0.2 < pl_ativos <= 0.4:
        return {
            'classificacao': 'Ruim',
            'faixa': '0.2 < PL/Ativos <= 0.4',
            'descricao': 'PL/Ativos moderado sugere alavancagem aceitável, mas com riscos. Comum em setores cíclicos (ex.: mineração, celulose). Análise de endividamento é necessária.'
        }
    elif 0.4 < pl_ativos <= 0.6:
        return {
            'classificacao': 'Moderado',
            'faixa': '0.4 < PL/Ativos <= 0.6',
            'descricao': 'PL/Ativos indica estrutura de capital equilibrada, com bom nível de patrimônio. Comum em setores estáveis (ex.: energia, indústria). Boa saúde financeira.'
        }
    elif 0.6 < pl_ativos <= 0.8:
        return {
            'classificacao': 'Ótimo',
            'faixa': '0.6 < PL/Ativos <= 0.8',
            'descricao': 'PL/Ativos alto indica patrimônio sólido, com baixo endividamento. Comum em empresas maduras (ex.: tecnologia, utilities). Representa segurança financeira.'
        }
    else:  # pl_ativos > 0.8
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'PL/Ativos > 0.8',
            'descricao': 'PL/Ativos extremamente alto sugere pouco endividamento, mas pode indicar ineficiência na alocação de capital. Análise de investimentos é recomendada.'
        }

def evaluate_passivos_ativos(passivos_ativos):
    """
    Avalia o Passivos/Ativos com base em faixas definidas para o mercado brasileiro:
    - Passivos/Ativos < 0: Crítico (impossível, erro contábil)
    - 0 ≤ Passivos/Ativos ≤ 0.2: Ótimo (baixo endividamento)
    - 0.2 < Passivos/Ativos ≤ 0.4: Moderado (endividamento controlado)
    - 0.4 < Passivos/Ativos ≤ 0.6: Ruim (endividamento moderado)
    - 0.6 < Passivos/Ativos ≤ 0.8: Péssimo (endividamento alto)
    - Passivos/Ativos > 0.8: Fora da faixa (endividamento excessivo)

    Args:
        passivos_ativos (float or int): Valor do índice Passivos/Ativos.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do Passivos/Ativos.

    Raises:
        TypeError: Se Passivos/Ativos não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter Passivos/Ativos automaticamente
    if not isinstance(passivos_ativos, (int, float)):
        raise TypeError("Passivos/Ativos deve ser um número (int ou float)")

    if passivos_ativos < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'Passivos/Ativos < 0',
            'descricao': 'Passivos/Ativos negativo é impossível e sugere erro contábil. Exige verificação imediata dos dados financeiros.'
        }
    elif 0 <= passivos_ativos <= 0.2:
        return {
            'classificacao': 'Ótimo',
            'faixa': '0 <= Passivos/Ativos <= 0.2',
            'descricao': 'Passivos/Ativos baixo indica endividamento mínimo, sugerindo solidez financeira. Comum em empresas maduras (ex.: tecnologia, utilities).'
        }
    elif 0.2 < passivos_ativos <= 0.4:
        return {
            'classificacao': 'Moderado',
            'faixa': '0.2 < Passivos/Ativos <= 0.4',
            'descricao': 'Passivos/Ativos moderado indica endividamento controlado. Comum em setores estáveis (ex.: energia, celulose). Equilíbrio entre risco e retorno.'
        }
    elif 0.4 < passivos_ativos <= 0.6:
        return {
            'classificacao': 'Ruim',
            'faixa': '0.4 < Passivos/Ativos <= 0.6',
            'descricao': 'Passivos/Ativos elevado sugere endividamento moderado, com riscos. Comum em setores cíclicos (ex.: mineração). Análise de fluxo de caixa é necessária.'
        }
    elif 0.6 < passivos_ativos <= 0.8:
        return {
            'classificacao': 'Péssimo',
            'faixa': '0.6 < Passivos/Ativos <= 0.8',
            'descricao': 'Passivos/Ativos alto indica endividamento elevado, com risco de dificuldades financeiras. Pode ser justificado em investimentos, mas há risco de insolvência.'
        }
    else:  # passivos_ativos > 0.8
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'Passivos/Ativos > 0.8',
            'descricao': 'Passivos/Ativos extremamente alto sugere endividamento excessivo, com alto risco de inadimplência. Comum em empresas alavancadas ou em crise.'
        }

def evaluate_liquidez_corrente(lc):
    """
    Avalia a Liquidez Corrente (Ativo Circulante/Passivo Circulante) com base em faixas definidas para o mercado brasileiro:
    - Liquidez < 0.5: Crítico (alta insolvência de curto prazo)
    - 0.5 ≤ Liquidez ≤ 1: Péssimo (liquidez muito baixa)
    - 1 < Liquidez ≤ 1.5: Ruim (liquidez limitada)
    - 1.5 < Liquidez ≤ 2: Moderado (liquidez adequada)
    - 2 < Liquidez ≤ 3: Ótimo (alta liquidez)
    - Liquidez > 3: Fora da faixa (liquidez excessiva, possível ineficiência)

    Args:
        lc (float or int): Valor do índice Liquidez Corrente.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do Liquidez Corrente.

    Raises:
        TypeError: Se Liquidez Corrente não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter Liquidez Corrente automaticamente
    if not isinstance(lc, (int, float)):
        raise TypeError("Liquidez Corrente deve ser um número (int ou float)")

    if lc < 0.5:
        return {
            'classificacao': 'Crítico',
            'faixa': 'Liquidez < 0.5',
            'descricao': 'Liquidez Corrente muito baixa indica alto risco de insolvência de curto prazo, com dificuldades para honrar obrigações. Exige análise urgente de fluxo de caixa.'
        }
    elif 0.5 <= lc <= 1:
        return {
            'classificacao': 'Péssimo',
            'faixa': '0.5 <= Liquidez <= 1',
            'descricao': 'Liquidez Corrente baixa sugere dificuldades para cobrir obrigações de curto prazo. Comum em setores alavancados ou em crise. Alto risco financeiro.'
        }
    elif 1 < lc <= 1.5:
        return {
            'classificacao': 'Ruim',
            'faixa': '1 < Liquidez <= 1.5',
            'descricao': 'Liquidez Corrente limitada indica capacidade moderada de honrar obrigações. Comum em setores cíclicos (ex.: celulose). Exige cautela.'
        }
    elif 1.5 < lc <= 2:
        return {
            'classificacao': 'Moderado',
            'faixa': '1.5 < Liquidez <= 2',
            'descricao': 'Liquidez Corrente adequada sugere equilíbrio na gestão de obrigações de curto prazo. Comum em setores estáveis (ex.: energia, indústria).'
        }
    elif 2 < lc <= 3:
        return {
            'classificacao': 'Ótimo',
            'faixa': '2 < Liquidez <= 3',
            'descricao': 'Liquidez Corrente alta indica forte capacidade de cobrir obrigações de curto prazo. Comum em empresas sólidas (ex.: tecnologia).'
        }
    else:  # lc > 3
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'Liquidez > 3',
            'descricao': 'Liquidez Corrente extremamente alta sugere excesso de ativos circulantes, podendo indicar ineficiência na alocação de capital.'
        }

def evaluate_peg_ratio(peg):
    """
    Avalia o PEG Ratio (P/L dividido pelo crescimento esperado do lucro) com base em faixas definidas para o mercado brasileiro:
    - PEG < 0: Crítico (crescimento negativo ou P/L negativo)
    - 0 ≤ PEG ≤ 0.5: Ótimo (subvalorizado com alto crescimento)
    - 0.5 < PEG ≤ 1: Moderado (valuation justo)
    - 1 < PEG ≤ 1.5: Ruim (sobrevalorizado)
    - 1.5 < PEG ≤ 2: Péssimo (muito caro)
    - PEG > 2: Fora da faixa (extremamente sobrevalorizado)

    Args:
        peg (float or int): Valor do índice PEG Ratio.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do PEG Ratio.

    Raises:
        TypeError: Se PEG Ratio não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter PEG Ratio automaticamente
    if not isinstance(peg, (int, float)):
        raise TypeError("PEG Ratio deve ser um número (int ou float)")

    if peg < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'PEG < 0',
            'descricao': 'PEG negativo indica P/L negativo ou crescimento esperado negativo, sugerindo prejuízo ou estagnação. Exige análise detalhada de perspectivas de lucro.'
        }
    elif 0 <= peg <= 0.5:
        return {
            'classificacao': 'Ótimo',
            'faixa': '0 <= PEG <= 0.5',
            'descricao': 'PEG baixo sugere que a ação está subvalorizada em relação ao crescimento esperado. Comum em empresas com alto potencial (ex.: tecnologia, varejo). Oportunidade de compra.'
        }
    elif 0.5 < peg <= 1:
        return {
            'classificacao': 'Moderado',
            'faixa': '0.5 < PEG <= 1',
            'descricao': 'PEG indica valuation justo, equilibrando preço com crescimento esperado. Comum em setores consolidados (ex.: indústria, energia).'
        }
    elif 1 < peg <= 1.5:
        return {
            'classificacao': 'Ruim',
            'faixa': '1 < PEG <= 1.5',
            'descricao': 'PEG elevado sugere sobrevalorização moderada, com preço superando o crescimento esperado. Exige análise de fundamentos e comparação com o setor.'
        }
    elif 1.5 < peg <= 2:
        return {
            'classificacao': 'Péssimo',
            'faixa': '1.5 < PEG <= 2',
            'descricao': 'PEG muito alto indica que a ação está cara em relação ao crescimento. Comum em setores de hype (ex.: tecnologia), com risco de correção.'
        }
    else:  # peg > 2
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'PEG > 2',
            'descricao': 'PEG extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas. Pode ser justificado em setores de alto crescimento.'
        }

def evaluate_psr(psr):
    """
    Avalia o Preço/Receita (P/SR) com base em faixas definidas para o mercado brasileiro:
    - P/SR < 0: Crítico (receita negativa, risco extremo)
    - 0 ≤ P/SR ≤ 0.5: Ótimo (subvalorizado)
    - 0.5 < P/SR ≤ 1: Moderado (valuation justo)
    - 1 < P/SR ≤ 2: Ruim (sobrevalorizado)
    - 2 < P/SR ≤ 3: Péssimo (muito caro)
    - P/SR > 3: Fora da faixa (extremamente sobrevalorizado)

    Args:
        psr (float or int): Valor do índice Preço/Receita.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do P/SR.

    Raises:
        TypeError: Se P/SR não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter P/SR automaticamente
    if not isinstance(psr, (int, float)):
        raise TypeError("P/SR deve ser um número (int ou float)")

    if psr < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'P/SR < 0',
            'descricao': 'P/SR negativo indica receita negativa, sugerindo problemas operacionais graves. Extremamente raro, exige análise detalhada da saúde financeira.'
        }
    elif 0 <= psr <= 0.5:
        return {
            'classificacao': 'Ótimo',
            'faixa': '0 <= P/SR <= 0.5',
            'descricao': 'P/SR baixo sugere que a ação está subvalorizada em relação à receita. Comum em setores maduros (ex.: siderurgia, varejo) ou em recuperação. Oportunidade de compra.'
        }
    elif 0.5 < psr <= 1:
        return {
            'classificacao': 'Moderado',
            'faixa': '0.5 < P/SR <= 1',
            'descricao': 'P/SR indica valuation justo, típico de empresas com receita estável. Comum em setores consolidados (ex.: indústria, energia).'
        }
    elif 1 < psr <= 2:
        return {
            'classificacao': 'Ruim',
            'faixa': '1 < P/SR <= 2',
            'descricao': 'P/SR elevado sugere sobrevalorização moderada, com mercado esperando crescimento de receita. Aceitável em setores dinâmicos (ex.: tecnologia), mas exige cautela.'
        }
    elif 2 < psr <= 3:
        return {
            'classificacao': 'Péssimo',
            'faixa': '2 < P/SR <= 3',
            'descricao': 'P/SR muito alto indica que a ação está cara em relação à receita. Comum em setores de crescimento, mas há risco de correção.'
        }
    else:  # psr > 3
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'P/SR > 3',
            'descricao': 'P/SR extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas. Pode ser justificado em setores de alto crescimento (ex.: tecnologia).'
        }

def evaluate_p_ativo(p_ativo):
    """
    Avalia o Preço/Ativo Total (P/Ativo) com base em faixas definidas para o mercado brasileiro:
    - P/Ativo < 0: Crítico (impossível, erro)
    - 0 ≤ P/Ativo ≤ 0.3: Ótimo (subvalorizado)
    - 0.3 < P/Ativo ≤ 0.6: Moderado (valuation justo)
    - 0.6 < P/Ativo ≤ 1: Ruim (sobrevalorizado)
    - 1 < P/Ativo ≤ 1.5: Péssimo (muito caro)
    - P/Ativo > 1.5: Fora da faixa (extremamente caroColabora caro)

    Args:
        p_ativo (float or int): Valor do índice Preço/Ativo Total.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do P/Ativo.

    Raises:
        TypeError: Se P/Ativo não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter P/Ativo automaticamente
    if not isinstance(p_ativo, (int, float)):
        raise TypeError("P/Ativo deve ser um número (int ou float)")

    if p_ativo < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'P/Ativo < 0',
            'descricao': 'P/Ativo negativo é impossível e sugere erro nos dados financeiros. Exige verificação imediata.'
        }
    elif 0 <= p_ativo <= 0.3:
        return {
            'classificacao': 'Ótimo',
            'faixa': '0 <= P/Ativo <= 0.3',
            'descricao': 'P/Ativo baixo sugere que a ação está subvalorizada em relação aos ativos totais. Comum em setores intensivos em capital (ex.: siderurgia, infraestrutura). Oportunidade de compra.'
        }
    elif 0.3 < p_ativo <= 0.6:
        return {
            'classificacao': 'Moderado',
            'faixa': '0.3 < P/Ativo <= 0.6',
            'descricao': 'P/Ativo indica valuation justo, típico de empresas com ativos sólidos. Comum em setores consolidados (ex.: indústria, energia).'
        }
    elif 0.6 < p_ativo <= 1:
        return {
            'classificacao': 'Ruim',
            'faixa': '0.6 < P/Ativo <= 1',
            'descricao': 'P/Ativo elevado sugere sobrevalorização moderada, com mercado precificando intangíveis ou crescimento. Exige análise de fundamentos.'
        }
    elif 1 < p_ativo <= 1.5:
        return {
            'classificacao': 'Péssimo',
            'faixa': '1 < P/Ativo <= 1.5',
            'descricao': 'P/Ativo muito alto indica que a ação está cara em relação aos ativos. Comum em setores de crescimento, com risco de correção.'
        }
    else:  # p_ativo > 1.5
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'P/Ativo > 1.5',
            'descricao': 'P/Ativo extremamente elevado sugere sobrevalorização severa, típica de empresas com intangíveis fortes (ex.: tecnologia). Análise de crescimento é essencial.'
        }

def evaluate_vpa(vpa_preco):
    """
    Avalia o VPA/Preço (Valor Patrimonial por Ação dividido pelo preço da ação) com base em faixas definidas para o mercado brasileiro:
    - VPA/Preço < 0: Crítico (patrimônio negativo)
    - 0 ≤ VPA/Preço ≤ 0.5: Fora da faixa (sobrevalorizado)
    - 0.5 < VPA/Preço ≤ 1: Péssimo (muito caro)
    - 1 < VPA/Preço ≤ 1.5: Ruim (sobrevalorizado)
    - 1.5 < VPA/Preço ≤ 2: Moderado (valuation justo)
    - VPA/Preço > 2: Ótimo (subvalorizado)

    Args:
        vpa_preco (float or int): Valor do índice VPA/Preço.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do VPA/Preço.

    Raises:
        TypeError: Se VPA/Preço não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter VPA automaticamente
    if not isinstance(vpa_preco, (int, float)):
        raise TypeError("VPA/Preço deve ser um número (int ou float)")

    if vpa_preco < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'VPA/Preço < 0',
            'descricao': 'VPA/Preço negativo indica patrimônio líquido negativo, sugerindo graves problemas financeiros. Exige análise de solvência.'
        }
    elif 0 <= vpa_preco <= 0.5:
        return {
            'classificacao': 'Fora da faixa',
            'faixa': '0 <= VPA/Preço <= 0.5',
            'descricao': 'VPA/Preço muito baixo indica sobrevalorização severa, com preço muito acima do patrimônio. Comum em setores de intangíveis (ex.: tecnologia). Alto risco.'
        }
    elif 0.5 < vpa_preco <= 1:
        return {
            'classificacao': 'Péssimo',
            'faixa': '0.5 < VPA/Preço <= 1',
            'descricao': 'VPA/Preço baixo sugere que a ação está cara em relação ao patrimônio. Comum em setores de crescimento, com risco de correção.'
        }
    elif 1 < vpa_preco <= 1.5:
        return {
            'classificacao': 'Ruim',
            'faixa': '1 < VPA/Preço <= 1.5',
            'descricao': 'VPA/Preço moderado indica sobrevalorização, com mercado precificando crescimento. Exige análise de fundamentos.'
        }
    elif 1.5 < vpa_preco <= 2:
        return {
            'classificacao': 'Moderado',
            'faixa': '1.5 < VPA/Preço <= 2',
            'descricao': 'VPA/Preço indica valuation justo, típico de empresas com patrimônio sólido. Comum em setores consolidados (ex.: energia, celulose).'
        }
    else:  # vpa_preco > 2
        return {
            'classificacao': 'Ótimo',
            'faixa': 'VPA/Preço > 2',
            'descricao': 'VPA/Preço alto sugere que a ação está subvalorizada em relação ao patrimônio. Comum em setores maduros (ex.: bancos, siderurgia). Oportunidade de compra.'
        }

def evaluate_lpa(lpa):
    """
    Avalia o Lucro por Ação (LPA) com base em faixas definidas para o mercado brasileiro:
    - LPA < 0: Crítico (prejuízo por ação)
    - 0 ≤ LPA ≤ 0.5: Péssimo (lucro muito baixo)
    - 0.5 < LPA ≤ 1: Ruim (lucro limitado)
    - 1 < LPA ≤ 2: Moderado (lucro adequado)
    - 2 < LPA ≤ 3: Ótimo (lucro alto)
    - LPA > 3: Fora da faixa (lucro excepcional, verificar sustentabilidade)

    Args:
        lpa (float or int): Valor do índice Lucro por Ação.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do LPA.

    Raises:
        TypeError: Se LPA não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter LPA automaticamente
    if not isinstance(lpa, (int, float)):
        raise TypeError("LPA deve ser um número (int ou float)")

    if lpa < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'LPA < 0',
            'descricao': 'LPA negativo indica prejuízo por ação, sugerindo problemas financeiros ou cíclicos. Exige análise detalhada de recuperação.'
        }
    elif 0 <= lpa <= 0.5:
        return {
            'classificacao': 'Péssimo',
            'faixa': '0 <= LPA <= 0.5',
            'descricao': 'LPA muito baixo sugere lucratividade limitada, comum em empresas em crise ou setores com margens apertadas. Alto risco.'
        }
    elif 0.5 < lpa <= 1:
        return {
            'classificacao': 'Ruim',
            'faixa': '0.5 < LPA <= 1',
            'descricao': 'LPA limitado indica lucratividade moderada, comum em setores cíclicos (ex.: celulose). Exige análise de crescimento.'
        }
    elif 1 < lpa <= 2:
        return {
            'classificacao': 'Moderado',
            'faixa': '1 < LPA <= 2',
            'descricao': 'LPA adequado sugere lucratividade equilibrada. Comum em setores consolidados (ex.: energia, indústria).'
        }
    elif 2 < lpa <= 3:
        return {
            'classificacao': 'Ótimo',
            'faixa': '2 < LPA <= 3',
            'descricao': 'LPA alto indica forte lucratividade por ação. Comum em empresas sólidas (ex.: tecnologia, bancos). Oportunidade se sustentável.'
        }
    else:  # lpa > 3
        return {
            'classificacao': 'Fora da faixa',
            'faixa': 'LPA > 3',
            'descricao': 'LPA extremamente alto sugere lucratividade excepcional, mas pode ser insustentável. Comum em setores de crescimento (ex.: tecnologia). Verificar consistência.'
        }

def evaluate_p_ativo_circ_liq(p_acl):
    """
    Avalia o Preço/Ativo Circulante Líquido com base em faixas definidas para o mercado brasileiro:
    - P/ACL < 0: Crítico (ativo circulante líquido negativo)
    - 0 ≤ P/ACL ≤ 0.5: Ótimo (subvalorizado)
    - 0.5 < P/ACL ≤ 1: Moderado (valuation justo)
    - 1 < P/ACL ≤ 2: Ruim (sobrevalorizado)
    - 2 < P/ACL ≤ 3: Péssimo (muito caro)
    - P/ACL > 3: Fora da faixa (extremamente sobrevalorizado)

    Args:
        p_acl (float or int): Valor do índice Preço/Ativo Circulante Líquido.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do P/ACL.

    Raises:
        TypeError: Se P/ACL não for um número (int ou float).
    """
    # TODO: Futura integração com Fundamentus para obter P/ACL automaticamente
    if not isinstance(p_acl, (int, float)):
        raise TypeError("P/ACL deve ser um número (int ou float)")

    if p_acl < 0:
        return {
            'classificacao': 'Crítico',
            'faixa': 'P/ACL < 0',
            'descricao': 'P/ACL negativo indica ativo circulante líquido negativo, sugerindo problemas de liquidez de curto prazo. Exige análise urgente.'
        }
    elif 0 <= p_acl <= 0.5:
        return {
            'classificacao': 'Ótimo',
            'faixa': '0 <= P/ACL <= 0.5',
            'descricao': 'P/ACL baixo sugere que a ação está subvalorizada em relação aos ativos circulantes líquidos. Comum em empresas com alta liquidez. Oportunidade de compra.'
        }
    elif 0.5 < p_acl <= 1:
        return {
            'classificacao': 'Moderado',
            'faixa': '0.5 < P/ACL <= 1',
            'descricao': 'P/ACL indica valuation justo, típico de empresas com liquidez equilibrada. Comum em setores consolidados (ex.: indústria, energia).'
        }
    elif 1 < p_acl <= 2:
        return {
            'classificacao': 'Ruim',
            'faixa': '1 < P/ACL <= 2',
            'descricao': 'P/ACL elevado sugere sobrevalorização moderada, com mercado precificando crescimento. Exige análise de fundamentos.'
        }
    elif 2 < p_acl <= 3:
        return {
            'classificacao': 'Péssimo',
            'faixa': '2 < P/ACL <= 3',
            'descricao': 'P/ACL muito alto indica que a ação está cara em relação aos ativos circulantes. Comum em setores de crescimento, com risco de correção.'
        }
    else:  # p_acl > 3
        return {
            'classificacao': 'Fora da faixa',
            'fa