"""
analisefundamentalista_1.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: Dívida Líquida/EBITDA, Margem EBITDA, ROA, Payout de Dividendos.
"""


def evaluate_divida_liquida_ebitda(divida_liquida_ebitda):
    """
    Avalia a Dívida Líquida/EBITDA com base em faixas definidas para o mercado brasileiro:
    - Dívida Líquida/EBITDA < 0: Fora da faixa (sem dívida líquida ou EBITDA negativo)
    - 0 ≤ Dívida Líquida/EBITDA ≤ 1: Ótimo (endividamento muito baixo)
    - 1 < Dívida Líquida/EBITDA ≤ 2: Moderado (endividamento aceitável)
    - 2 < Dívida Líquida/EBITDA ≤ 3: Ruim (endividamento elevado)
    - 3 < Dívida Líquida/EBITDA ≤ 4: Péssimo (endividamento muito alto)
    - Dívida Líquida/EBITDA > 4: Crítico (endividamento excessivo, risco elevado)
    """
    definicao = """
    A Dívida Líquida/EBITDA mede a capacidade da empresa de pagar sua dívida líquida com base no EBITDA,
    calculada como (Dívida Total - Caixa e Equivalentes) / EBITDA. É um indicador chave de alavancagem
    financeira, mostrando quantos anos a empresa levaria para quitar sua dívida líquida com sua geração
    de caixa operacional. Um valor baixo indica saúde financeira, enquanto um valor alto sugere risco
    financeiro elevado. É amplamente utilizado em setores intensivos em capital, como mineração e energia.
    """
    agrupador = 'Endividamento'
    formula = 'Dívida Líquida/EBITDA = (Dívida Total - Caixa e Equivalentes) / EBITDA'

    try:
        if divida_liquida_ebitda < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Líquida/EBITDA < 0',
                'descricao': """
                Um valor negativo indica que a empresa não possui dívida líquida (caixa excede a dívida)
                ou que o EBITDA é negativo. Empresas como a Totvs (TOTS3), com forte geração de caixa, podem
                apresentar valores negativos em períodos de alta liquidez. Para investidores, isso pode ser
                positivo, sugerindo solidez financeira, mas também pode indicar ineficiência na alocação de
                capital, como excesso de caixa ocioso. Análises complementares, como ROIC e fluxo de caixa livre,
                são recomendadas para avaliar a eficiência do uso do caixa.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_liquida_ebitda <= 1:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida Líquida/EBITDA <= 1',
                'descricao': """
                Um valor entre 0 e 1 reflete endividamento muito baixo, indicando que a empresa pode quitar
                sua dívida líquida rapidamente com sua geração de caixa. Empresas como a Vale (VALE3) em períodos
                de alta nos preços de minério de ferro frequentemente operam nessa faixa. Para investidores,
                essa faixa é atrativa, pois sugere baixo risco financeiro e flexibilidade para investimentos ou
                dividendos. É importante verificar a consistência do EBITDA e a composição da dívida.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < divida_liquida_ebitda <= 2:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Dívida Líquida/EBITDA <= 2',
                'descricao': """
                Um valor entre 1 e 2 indica endividamento aceitável, com a empresa mantendo um equilíbrio entre
                dívida e geração de caixa. No Brasil, empresas como a Ambev (ABEV3) frequentemente operam nessa
                faixa devido à sua gestão financeira eficiente. Para investidores, essa faixa sugere risco moderado,
                com a empresa capaz de suportar oscilações econômicas sem grandes pressões. É importante avaliar
                a estrutura da dívida (curto vs. longo prazo) e a geração de fluxo de caixa livre.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < divida_liquida_ebitda <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '2 < Dívida Líquida/EBITDA <= 3',
                'descricao': """
                Um valor entre 2 e 3 sugere endividamento elevado, indicando que a empresa levaria um tempo
                considerável para quitar sua dívida líquida com o EBITDA. Isso é comum em setores intensivos em
                capital, como a Petrobras (PETR4) em períodos de investimentos pesados. Para investidores, essa
                faixa exige cautela, pois a empresa pode ser vulnerável a aumentos de juros ou quedas na receita.
                Análise de fluxo de caixa e covenants de dívida é recomendada.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < divida_liquida_ebitda <= 4:
            return {
                'classificacao': 'Péssimo',
                'faixa': '3 < Dívida Líquida/EBITDA <= 4',
                'descricao': """
                Um valor entre 3 e 4 reflete endividamento muito alto, indicando risco significativo de pressão
                financeira. Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises, enfrentando dificuldades
                para gerenciar dívidas elevadas. Para investidores, essa faixa é preocupante, exigindo análise detalhada
                da estrutura de capital, planos de desalavancagem e fluxo de caixa operacional.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif divida_liquida_ebitda > 4:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida Líquida/EBITDA > 4',
                'descricao': """
                Um valor acima de 4 indica endividamento excessivo, sugerindo que a empresa depende fortemente de
                dívidas em relação à sua geração de caixa. Isso é alarmante e típico de empresas em dificuldades
                financeiras, como a Gol (GOLL4) em períodos de crise no setor aéreo. Para investidores, essa faixa é
                de altíssimo risco, com possibilidade de reestruturação ou insolvência. A análise deve focar na
                capacidade de geração de caixa, estratégias de redução de dívida e covenants financeiros.
                """,
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f"""
            Ocorreu um erro ao processar a Dívida Líquida/EBITDA: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o EBITDA for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que a dívida líquida e o EBITDA estejam corretos e sejam valores numéricos válidos.
            """,
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_margem_ebitda(margem_ebitda):
    '''
    Avalia a Margem EBITDA com base em faixas definidas para o mercado brasileiro:
    - Margem EBITDA < 0%: Crítico (prejuízo operacional, risco elevado)
    - 0% ≤ Margem EBITDA ≤ 10%: Ruim (rentabilidade operacional baixa)
    - 10% < Margem EBITDA ≤ 20%: Moderado (rentabilidade operacional aceitável)
    - 20% < Margem EBITDA ≤ 30%: Ótimo (rentabilidade operacional robusta)
    - Margem EBITDA > 30%: Fora da faixa (rentabilidade operacional excepcional)
    '''
    definicao = '''
    A Margem EBITDA mede a proporção da receita bruta que se converte em EBITDA, calculada como
    (EBITDA / Receita Bruta). É um indicador de rentabilidade operacional que reflete a eficiência da
    empresa em gerar caixa antes de juros, impostos, depreciação e amortização. Uma margem alta sugere
    forte geração de caixa operacional, enquanto uma margem baixa ou negativa indica ineficiência ou
    prejuízo. É especialmente útil em setores com alta intensidade de capital, como energia e mineração.
    '''
    agrupador = 'Rentabilidade'
    formula = 'Margem EBITDA = EBITDA / Receita Bruta'

    try:
        if margem_ebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Margem EBITDA < 0%',
                'descricao': '''
                Uma Margem EBITDA negativa indica que a empresa está gerando prejuízo operacional, com custos
                superando a receita antes de juros, impostos, depreciação e amortização. Isso é comum em empresas
                em crise, como a Oi (OIBR3) durante períodos de reestruturação. Para investidores, essa faixa é um
                alerta de risco elevado, pois reflete dificuldades operacionais graves. A análise deve focar na
                estrutura de custos, estratégias de recuperação e tendências setoriais.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= margem_ebitda <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Margem EBITDA <= 10%',
                'descricao': '''
                Uma Margem EBITDA entre 0% e 10% reflete rentabilidade operacional baixa, indicando que a empresa
                tem dificuldade em converter receita em caixa operacional significativo. Isso é comum em setores com
                margens apertadas, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere
                risco moderado, pois a empresa pode ser vulnerável a aumentos de custos ou oscilações econômicas.
                Análise de redução de custos e crescimento da receita é recomendada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < margem_ebitda <= 20:
            return {
                'classificacao': 'Moderado',
                'faixa': '10% < Margem EBITDA <= 20%',
                'descricao': '''
                Uma Margem EBITDA entre 10% e 20% indica rentabilidade operacional aceitável, típico de empresas
                com eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa
                devido à sua consistência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio
                entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes. É importante
                avaliar a sustentabilidade da margem e o impacto de fatores macroeconômicos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < margem_ebitda <= 30:
            return {
                'classificacao': 'Ótimo',
                'faixa': '20% < Margem EBITDA <= 30%',
                'descricao': '''
                Uma Margem EBITDA entre 20% e 30% reflete rentabilidade operacional robusta, indicando que a empresa
                converte uma proporção significativa de sua receita em caixa operacional. Empresas como a Ambev (ABEV3),
                com forte controle de custos, frequentemente apresentam margem nessa faixa. Para investidores, essa faixa
                é atrativa, pois sugere solidez financeira e potencial para dividendos ou reinvestimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif margem_ebitda > 30:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Margem EBITDA > 30%',
                'descricao': '''
                Uma Margem EBITDA acima de 30% é excepcional, indicando que a empresa converte uma proporção
                extremamente alta de sua receita em caixa operacional. Isso é raro, mas pode ocorrer em empresas
                com alta eficiência operacional, como a Weg (WEGE3) em períodos de forte desempenho. Para investidores,
                essa faixa é altamente atrativa, mas exige cautela, pois margens tão altas podem não ser sustentáveis
                a longo prazo. A análise deve focar na escalabilidade do modelo de negócios e barreiras de entrada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Margem EBITDA: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que o EBITDA e a receita bruta estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_roa(roa):
    '''
    Avalia o Retorno sobre Ativos (ROA) com base em faixas definidas para o mercado brasileiro:
    - ROA < 0%: Crítico (prejuízo, destruição de valor)
    - 0% ≤ ROA ≤ 5%: Ruim (retorno baixo, ineficiência)
    - 5% < ROA ≤ 10%: Moderado (retorno aceitável)
    - 10% < ROA ≤ 15%: Ótimo (retorno robusto)
    - ROA > 15%: Fora da faixa (retorno excepcional)
    '''
    definicao = '''
    O Retorno sobre Ativos (ROA) mede a eficiência da empresa em gerar lucro com seus ativos totais,
    calculado como (Lucro Líquido / Ativos Totais). É um indicador de rentabilidade que reflete como
    a empresa utiliza seus recursos para gerar retorno. Um ROA alto indica eficiência operacional, enquanto
    um valor baixo ou negativo sugere ineficiência ou prejuízo. É útil para comparar empresas dentro do
    mesmo setor, mas deve ser analisado com margem líquida e giro de ativos.
    '''
    agrupador = 'Rentabilidade'
    formula = 'ROA = Lucro Líquido / Ativos Totais'

    try:
        if roa < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'ROA < 0%',
                'descricao': '''
                Um ROA negativo indica que a empresa está gerando prejuízo, destruindo valor com seus ativos.
                Isso é comum em empresas em crise, como a Gol (GOLL4) durante períodos de baixa demanda no setor
                aéreo. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades financeiras
                graves. A análise deve focar na estrutura de custos, endividamento e estratégias de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= roa <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= ROA <= 5%',
                'descricao': '''
                Um ROA entre 0% e 5% reflete retorno baixo, indicando ineficiência na utilização dos ativos.
                Isso é comum em setores com alta intensidade de capital ou margens apertadas, como varejo
                (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa
                pode ser vulnerável a oscilações econômicas. Análise de giro de ativos e margem líquida é recomendada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < roa <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < ROA <= 10%',
                'descricao': '''
                Um ROA entre 5% e 10% indica retorno aceitável, típico de empresas com eficiência moderada na
                utilização de ativos. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa
                devido à sua consistência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio
                entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < roa <= 15:
            return {
                'classificacao': 'Ótimo',
                'faixa': '10% < ROA <= 15%',
                'descricao': '''
                Um ROA entre 10% e 15% reflete retorno robusto, indicando que a empresa utiliza seus ativos de
                forma eficiente para gerar lucro. Empresas como a Ambev (ABEV3), com forte gestão operacional,
                frequentemente apresentam ROA nessa faixa. Para investidores, essa faixa é atrativa, pois sugere
                solidez financeira e potencial para crescimento sustentável.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif roa > 15:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'ROA > 15%',
                'descricao': '''
                Um ROA acima de 15% é excepcional, indicando que a empresa gera retornos extremamente altos com
                seus ativos. Isso é raro, mas pode ocorrer em empresas com alta eficiência operacional, como a Weg
                (WEGE3) em períodos de forte desempenho. Para investidores, essa faixa é altamente atrativa, mas
                exige cautela, pois retornos tão altos podem não ser sustentáveis. A análise deve focar na
                escalabilidade do modelo de negócios e barreiras de entrada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o ROA: {str(e)}. Isso pode ter acontecido se o valor fornecido não for
            numérico ou se os ativos totais forem zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que o lucro líquido e os ativos totais estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_dividend_payout(payout):
    '''
    Avalia o Payout de Dividendos com base em faixas definidas para o mercado brasileiro:
    - Payout < 0%: Fora da faixa (sem dividendos ou prejuízo)
    - 0% ≤ Payout ≤ 25%: Ruim (distribuição baixa de dividendos)
    - 25% < Payout ≤ 50%: Moderado (distribuição aceitável de dividendos)
    - 50% < Payout ≤ 75%: Ótimo (distribuição robusta de dividendos)
    - Payout > 75%: Crítico (distribuição excessiva, risco de sustentabilidade)
    '''
    definicao = '''
    O Payout de Dividendos mede a proporção do lucro líquido distribuído como dividendos, calculado como
    (Dividendos Pagos / Lucro Líquido). É um indicador que reflete a política de distribuição de lucros da
    empresa, mostrando quanto do lucro é retornado aos acionistas versus reinvestido no negócio. Um payout
    alto é atrativo para investidores focados em renda, mas pode indicar menor reinvestimento. Um payout baixo
    pode sugerir crescimento, mas também insatisfação para investidores de dividendos.
    '''
    agrupador = 'Dividendos'
    formula = 'Payout = Dividendos Pagos / Lucro Líquido'

    try:
        if payout < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Payout < 0%',
                'descricao': '''
                Um Payout negativo ou zero indica que a empresa não distribui dividendos, seja por prejuízo ou
                por reinvestir todo o lucro no negócio. Isso é comum em empresas em crescimento, como o Nubank
                (NUBR33), ou em crise, como a Oi (OIBR3). Para investidores focados em renda, essa faixa é
                desvantajosa, mas pode ser positiva para quem busca crescimento. A análise deve focar no motivo da
                ausência de dividendos (crescimento ou dificuldades financeiras).
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= payout <= 25:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Payout <= 25%',
                'descricao': '''
                Um Payout entre 0% e 25% reflete distribuição baixa de dividendos, indicando que a empresa prioriza
                reinvestimento em vez de retorno aos acionistas. Isso é comum em empresas em expansão, como a Magazine
                Luiza (MGLU3). Para investidores focados em renda, essa faixa é pouco atrativa, mas pode ser positiva
                para quem busca crescimento. É importante analisar o potencial de crescimento e a eficiência do
                reinvestimento (ex.: ROIC).
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 25 < payout <= 50:
            return {
                'classificacao': 'Moderado',
                'faixa': '25% < Payout <= 50%',
                'descricao': '''
                Um Payout entre 25% e 50% indica distribuição aceitável de dividendos, com equilíbrio entre retorno
                aos acionistas e reinvestimento. No Brasil, empresas como a Vale (VALE3) frequentemente operam nessa
                faixa em períodos de lucros estáveis. Para investidores, essa faixa é adequada para quem busca renda
                moderada com potencial de crescimento. É importante avaliar a consistência dos lucros e a política
                de dividendos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 50 < payout <= 75:
            return {
                'classificacao': 'Ótimo',
                'faixa': '50% < Payout <= 75%',
                'descricao': '''
                Um Payout entre 50% e 75% reflete distribuição robusta de dividendos, indicando que a empresa retorna
                uma parte significativa de seus lucros aos acionistas. Empresas como a Engie Brasil (EGIE3), do setor
                de energia, frequentemente apresentam payout nessa faixa. Para investidores focados em renda, essa faixa
                é atrativa, pois sugere estabilidade e retorno consistente. No entanto, é importante verificar a
                sustentabilidade dos dividendos com base no fluxo de caixa livre.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif payout > 75:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Payout > 75%',
                'descricao': '''
                Um Payout acima de 75% indica distribuição excessiva de dividendos, sugerindo que a empresa está
                retornando quase todo o lucro aos acionistas, com pouco reinvestimento. Isso pode ocorrer em empresas
                maduras, como a Taesa (TAEE11), mas é arriscado, pois pode comprometer o crescimento futuro. Para
                investidores, essa faixa exige cautela, pois dividendos altos podem não ser sustentáveis. A análise deve
                focar no fluxo de caixa livre e nas perspectivas de crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Payout de Dividendos: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o lucro líquido for zero, o que impede o cálculo. Verifique os dados
            de entrada, assegurando que os dividendos pagos e o lucro líquido estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

    """
    analisefundamentalista_2.py
    Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
    e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
    Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
    Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
    Indicadores incluídos: Crescimento da Receita, Liquidez Seca, Margem Operacional, P/EBITDA.
    """

    def evaluate_crescimento_receita(crescimento_receita):
        '''
        Avalia o Crescimento da Receita com base em faixas definidas para o mercado brasileiro:
        - Crescimento Receita < 0%: Crítico (redução de receita, risco elevado)
        - 0% ≤ Crescimento Receita ≤ 5%: Ruim (crescimento baixo ou estagnação)
        - 5% < Crescimento Receita ≤ 10%: Moderado (crescimento aceitável)
        - 10% < Crescimento Receita ≤ 20%: Ótimo (crescimento robusto)
        - Crescimento Receita > 20%: Fora da faixa (crescimento excepcional)
        '''
        definicao = '''
        O Crescimento da Receita mede a taxa anual de aumento da receita bruta, calculada como
        ((Receita Final / Receita Inicial)^(1/n) - 1), onde n é o número de anos. É um indicador de
        crescimento que reflete a capacidade da empresa de expandir suas vendas. Um crescimento alto sugere
        expansão bem-sucedida, enquanto um valor baixo ou negativo indica estagnação ou declínio. É especialmente
        relevante em setores de alto crescimento, como tecnologia, mas deve ser analisado com margens de lucro
        e fluxo de caixa.
        '''
        agrupador = 'Crescimento'
        formula = 'Crescimento Receita = ((Receita Final / Receita Inicial)^(1/n) - 1)'

        try:
            if crescimento_receita < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Crescimento Receita < 0%',
                    'descricao': '''
                    Um Crescimento da Receita negativo indica que a empresa está enfrentando uma redução nas vendas,
                    sugerindo dificuldades de mercado ou operacionais. Isso é comum em empresas em crise, como a Gol
                    (GOLL4) durante períodos de baixa demanda. Para investidores, essa faixa é um alerta de risco elevado,
                    pois reflete desafios significativos. A análise deve focar nas causas da queda (ex.: concorrência,
                    crise setorial) e estratégias de recuperação.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= crescimento_receita <= 5:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0% <= Crescimento Receita <= 5%',
                    'descricao': '''
                    Um Crescimento da Receita entre 0% e 5% reflete crescimento baixo ou estagnação, indicando que a
                    empresa tem dificuldade em expandir suas vendas. Isso é comum em setores maduros, como varejo
                    (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa
                    pode ser vulnerável a oscilações econômicas. Análise de estratégias de crescimento e margens de lucro
                    é recomendada.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < crescimento_receita <= 10:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '5% < Crescimento Receita <= 10%',
                    'descricao': '''
                    Um Crescimento da Receita entre 5% e 10% indica crescimento aceitável, típico de empresas com
                    expansão moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido
                    à sua consistência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre
                    crescimento e segurança, sendo adequada para quem busca retornos consistentes.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 10 < crescimento_receita <= 20:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '10% < Crescimento Receita <= 20%',
                    'descricao': '''
                    Um Crescimento da Receita entre 10% e 20% reflete crescimento robusto, indicando que a empresa está
                    expandindo suas vendas de forma significativa. Empresas como a Magazine Luiza (MGLU3), em períodos
                    de forte crescimento no e-commerce, frequentemente apresentam crescimento nessa faixa. Para investidores,
                    essa faixa é atrativa, pois sugere potencial de valorização. É importante verificar a sustentabilidade
                    do crescimento com base em margens e fluxo de caixa.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif crescimento_receita > 20:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Crescimento Receita > 20%',
                    'descricao': '''
                    Um Crescimento da Receita acima de 20% é excepcional, indicando expansão extremamente rápida das
                    vendas. Isso é raro, mas pode ocorrer em empresas em setores de alto crescimento, como o Nubank
                    (NUBR33) em sua fase inicial. Para investidores, essa faixa é altamente atrativa, mas exige cautela,
                    pois crescimentos tão altos podem não ser sustentáveis. A análise deve focar na escalabilidade do
                    modelo de negócios e barreiras de entrada.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
        except Exception as e:
            print(f"Erro inesperado tratamento : {e}")
            return {
                'classificacao': 'Erro',
                'faixa': 'N/A',
                'descricao': f'''
                Ocorreu um erro ao processar o Crescimento da Receita: {str(e)}. Isso pode ter acontecido se o valor
                fornecido não for numérico ou se a receita inicial for zero, o que impede o cálculo. Verifique os dados
                de entrada, assegurando que as receitas inicial e final estejam corretas e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_liquidez_seca(liquidez_seca):
        '''
        Avalia a Liquidez Seca com base em faixas definidas para o mercado brasileiro:
        - Liquidez Seca < 0.3: Crítico (dificuldade extrema em pagar obrigações sem estoques)
        - 0.3 ≤ Liquidez Seca ≤ 0.7: Ruim (capacidade limitada de pagar obrigações sem estoques)
        - 0.7 < Liquidez Seca ≤ 1.2: Moderado (capacidade aceitável de pagar obrigações sem estoques)
        - 1.2 < Liquidez Seca ≤ 1.8: Ótimo (boa capacidade de pagar obrigações sem estoques)
        - Liquidez Seca > 1.8: Fora da faixa (excesso de liquidez, possível ineficiência)
        '''
        definicao = '''
        A Liquidez Seca mede a capacidade da empresa de pagar suas obrigações de curto prazo sem depender da
        venda de estoques, calculada como (Ativo Circulante - Estoques) / Passivo Circulante. É um indicador
        conservador de liquidez, útil em setores onde os estoques são menos líquidos, como indústria pesada.
        Um valor alto sugere solidez financeira, enquanto um valor baixo indica risco de inadimplência.
        '''
        agrupador = 'Liquidez'
        formula = 'Liquidez Seca = (Ativo Circulante - Estoques) / Passivo Circulante'

        try:
            if liquidez_seca < 0.3:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Liquidez Seca < 0.3',
                    'descricao': '''
                    Uma Liquidez Seca abaixo de 0.3 indica dificuldade extrema em pagar obrigações de curto prazo sem
                    depender da venda de estoques, sugerindo risco elevado de inadimplência. Isso é comum em empresas
                    em crise, como a Oi (OIBR3) durante reestruturações. Para investidores, essa faixa é um alerta grave,
                    pois reflete problemas de liquidez severos. A análise deve focar na gestão de caixa e estratégias de
                    recuperação.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0.3 <= liquidez_seca <= 0.7:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0.3 <= Liquidez Seca <= 0.7',
                    'descricao': '''
                    Uma Liquidez Seca entre 0.3 e 0.7 reflete capacidade limitada de pagar obrigações de curto prazo
                    sem estoques, indicando dependência de conversão de ativos em caixa. Isso é comum em setores com
                    estoques elevados, como varejo (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco
                    moderado, exigindo análise da qualidade dos ativos circulantes e do ciclo operacional.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0.7 < liquidez_seca <= 1.2:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '0.7 < Liquidez Seca <= 1.2',
                    'descricao': '''
                    Uma Liquidez Seca entre 0.7 e 1.2 indica capacidade aceitável de pagar obrigações de curto prazo
                    sem depender de estoques. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa
                    devido à sua gestão eficiente de caixa. Para investidores, essa faixa sugere equilíbrio entre liquidez
                    e eficiência, sendo adequada para quem busca segurança financeira de curto prazo.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 1.2 < liquidez_seca <= 1.8:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '1.2 < Liquidez Seca <= 1.8',
                    'descricao': '''
                    Uma Liquidez Seca entre 1.2 e 1.8 reflete boa capacidade de pagar obrigações de curto prazo sem
                    depender de estoques, indicando solidez financeira. Empresas como a Ambev (ABEV3) frequentemente
                    apresentam liquidez nessa faixa devido à sua forte geração de caixa. Para investidores, essa faixa
                    é atrativa, sugerindo resiliência a choques financeiros de curto prazo.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif liquidez_seca > 1.8:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Liquidez Seca > 1.8',
                    'descricao': '''
                    Uma Liquidez Seca acima de 1.8 indica excesso de liquidez, com ativos circulantes (excluindo estoques)
                    muito superiores às obrigações de curto prazo. Isso pode ocorrer em empresas com alta geração de caixa,
                    como a Vale (VALE3) em períodos de preços elevados de commodities. Para investidores, essa faixa pode
                    ser positiva, mas também pode indicar ineficiência na alocação de capital, como excesso de caixa ocioso.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
        except Exception as e:
            print(f"Erro inesperado tratamento : {e}")
            return {
                'classificacao': 'Erro',
                'faixa': 'N/A',
                'descricao': f'''
                Ocorreu um erro ao processar a Liquidez Seca: {str(e)}. Isso pode ter acontecido se o valor fornecido
                não for numérico ou se o passivo circulante for zero, o que impede o cálculo. Verifique os dados de
                entrada, assegurando que o ativo circulante, estoques e passivo circulante estejam corretos e sejam
                valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_margem_operacional(margem_operacional):
        '''
        Avalia a Margem Operacional com base em faixas definidas para o mercado brasileiro:
        - Margem Operacional < 0%: Crítico (prejuízo operacional, risco elevado)
        - 0% ≤ Margem Operacional ≤ 5%: Ruim (rentabilidade operacional baixa)
        - 5% < Margem Operacional ≤ 15%: Moderado (rentabilidade operacional aceitável)
        - 15% < Margem Operacional ≤ 25%: Ótimo (rentabilidade operacional robusta)
        - Margem Operacional > 25%: Fora da faixa (rentabilidade operacional excepcional)
        '''
        definicao = '''
        A Margem Operacional mede a proporção da receita bruta que se converte em lucro operacional,
        calculada como (Lucro Operacional / Receita Bruta). É um indicador de rentabilidade que reflete a
        eficiência da empresa em gerenciar custos operacionais antes de juros e impostos. Uma margem alta
        sugere forte desempenho operacional, enquanto uma margem baixa ou negativa indica ineficiência.
        '''
        agrupador = 'Rentabilidade'
        formula = 'Margem Operacional = Lucro Operacional / Receita Bruta'

        try:
            if margem_operacional < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Margem Operacional < 0%',
                    'descricao': '''
                    Uma Margem Operacional negativa indica prejuízo operacional, sugerindo que a empresa não consegue
                    cobrir seus custos operacionais com a receita. Isso é comum em empresas em crise, como a CSN (CSNA3)
                    durante quedas de preços de commodities. Para investidores, essa faixa é um alerta de risco elevado,
                    exigindo análise detalhada da estrutura de custos e estratégias de recuperação.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= margem_operacional <= 5:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0% <= Margem Operacional <= 5%',
                    'descricao': '''
                    Uma Margem Operacional entre 0% e 5% reflete rentabilidade operacional baixa, indicando dificuldade
                    em gerar lucro significativo a partir das operações. Isso é comum em setores com margens apertadas,
                    como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado,
                    exigindo análise de redução de custos e potencial de melhoria da margem.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < margem_operacional <= 15:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '5% < Margem Operacional <= 15%',
                    'descricao': '''
                    Uma Margem Operacional entre 5% e 15% indica rentabilidade operacional aceitável, típico de empresas
                    com eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa
                    devido à sua consistência no setor de celulose. Para investidores, essa faixa sugere equilíbrio entre
                    rentabilidade e segurança.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 15 < margem_operacional <= 25:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '15% < Margem Operacional <= 25%',
                    'descricao': '''
                    Uma Margem Operacional entre 15% e 25% reflete rentabilidade operacional robusta, indicando que a
                    empresa converte uma proporção significativa de sua receita em lucro operacional. Empresas como a
                    Ambev (ABEV3) frequentemente apresentam margem nessa faixa devido à sua eficiência operacional.
                    Para investidores, essa faixa é atrativa, sugerindo solidez financeira.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif margem_operacional > 25:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Margem Operacional > 25%',
                    'descricao': '''
                    Uma Margem Operacional acima de 25% é excepcional, indicando que a empresa converte uma proporção
                    extremamente alta de sua receita em lucro operacional. Isso pode ocorrer em empresas com alta
                    eficiência, como a Weg (WEGE3). Para investidores, essa faixa é atrativa, mas exige cautela, pois
                    margens tão altas podem não ser sustentáveis. A análise deve focar na escalabilidade e barreiras de
                    entrada.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
        except Exception as e:
            print(f"Erro inesperado tratamento : {e}")
            return {
                'classificacao': 'Erro',
                'faixa': 'N/A',
                'descricao': f'''
                Ocorreu um erro ao processar a Margem Operacional: {str(e)}. Isso pode ter acontecido se o valor
                fornecido não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados
                de entrada, assegurando que o lucro operacional e a receita bruta estejam corretos e sejam valores
                numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_p_ebitda(p_ebitda):
        '''
        Avalia o Preço/EBITDA com base em faixas definidas para o mercado brasileiro:
        - P/EBITDA < 0: Crítico (EBITDA negativo, risco elevado)
        - 0 ≤ P/EBITDA ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
        - 5 < P/EBITDA ≤ 8: Moderado (valuation justo)
        - 8 < P/EBITDA ≤ 12: Ruim (sobrevalorizado, cautela necessária)
        - 12 < P/EBITDA ≤ 15: Péssimo (muito caro, alto risco)
        - P/EBITDA > 15: Fora da faixa (extremamente sobrevalorizado)
        '''
        definicao = '''
        O Preço/EBITDA compara o preço da ação (ou valor de mercado da empresa) ao EBITDA, calculado como
        (Preço da Ação * Número de Ações) / EBITDA ou (Valor de Mercado + Dívida Líquida) / EBITDA para EV/EBITDA.
        É um indicador de valuation que avalia se a empresa está cara ou barata em relação à sua geração de
        caixa operacional. Um valor baixo sugere subvalorização, enquanto um valor alto indica sobrevalorização.
        É útil em setores com alta intensidade de capital, mas menos eficaz em empresas com EBITDA negativo.
        '''
        agrupador = 'Valuation'
        formula = 'P/EBITDA = (Preço da Ação * Número de Ações) / EBITDA'

        try:
            if p_ebitda < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'P/EBITDA < 0',
                    'descricao': '''
                    Um P/EBITDA negativo indica que a empresa tem EBITDA negativo, sugerindo prejuízo operacional.
                    Isso é comum em empresas em crise, como a Oi (OIBR3) durante reestruturações. Para investidores,
                    essa faixa é um alerta de risco elevado, exigindo análise detalhada da saúde financeira e estratégias
                    de recuperação.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= p_ebitda <= 5:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '0 <= P/EBITDA <= 5',
                    'descricao': '''
                    Um P/EBITDA entre 0 e 5 sugere que a ação está subvalorizada em relação à sua geração de caixa,
                    indicando uma potencial oportunidade de compra. Isso é comum em setores cíclicos durante períodos de
                    baixa, como a Vale (VALE3). Para investidores, essa faixa é atrativa, mas é importante verificar a
                    sustentabilidade do EBITDA.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < p_ebitda <= 8:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '5 < P/EBITDA <= 8',
                    'descricao': '''
                    Um P/EBITDA entre 5 e 8 reflete um valuation justo, típico de empresas com geração de caixa estável.
                    No Brasil, empresas como a Ambev (ABEV3) frequentemente operam nessa faixa. Para investidores, essa
                    faixa sugere equilíbrio entre preço e fundamentos, sendo adequada para retornos consistentes.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 8 < p_ebitda <= 12:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '8 < P/EBITDA <= 12',
                    'descricao': '''
                    Um P/EBITDA entre 8 e 12 sugere que a ação está sobrevalorizada, indicando que o mercado espera
                    crescimento significativo. Empresas como a Raia Drogasil (RADL3) podem atingir essa faixa em períodos
                    de expansão. Para investidores, essa faixa exige cautela, pois o preço elevado pode não se sustentar
                    sem crescimento robusto.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 12 < p_ebitda <= 15:
                return {
                    'classificacao': 'Péssimo',
                    'faixa': '12 < P/EBITDA <= 15',
                    'descricao': '''
                    Um P/EBITDA entre 12 e 15 indica que a ação é muito cara, sugerindo que o mercado está pagando um
                    prêmio elevado. Empresas como a Localiza (RENT3) podem apresentar P/EBITDA nessa faixa em momentos
                    de otimismo. Para investidores, essa faixa é de alto risco, exigindo análise de crescimento e
                    escalabilidade do modelo de negócios.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif p_ebitda > 15:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'P/EBITDA > 15',
                    'descricao': '''
                    Um P/EBITDA acima de 15 é extremamente elevado, geralmente associado a empresas com altíssimas
                    expectativas de crescimento, como o Nubank (NUBR33) após sua estreia na bolsa. Para investidores,
                    essa faixa é de altíssimo risco, pois reflete mais especulação do que fundamentos. A análise deve
                    focar em projeções de longo prazo e comparação com peers globais.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
        except Exception as e:
            print(f"Erro inesperado tratamento : {e}")
            return {
                'classificacao': 'Erro',
                'faixa': 'N/A',
                'descricao': f'''
                Ocorreu um erro ao processar o P/EBITDA: {str(e)}. Isso pode ter acontecido se o valor fornecido não
                for numérico ou se o EBITDA for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando
                que o preço da ação, número de ações e EBITDA estejam corretos e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }


"""
analisefundamentalista_3.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: Free Cash Flow Yield, Crescimento do Lucro, Dívida/Patrimônio, Margem Líquida Crescimento.
"""


def evaluate_free_cash_flow_yield(fcf_yield):
    '''
    Avalia o Free Cash Flow Yield com base em faixas definidas para o mercado brasileiro:
    - FCF Yield < 0%: Crítico (fluxo de caixa livre negativo, risco elevado)
    - 0% ≤ FCF Yield ≤ 3%: Ruim (fluxo de caixa livre baixo)
    - 3% < FCF Yield ≤ 6%: Moderado (fluxo de caixa livre aceitável)
    - 6% < FCF Yield ≤ 10%: Ótimo (fluxo de caixa livre robusto)
    - FCF Yield > 10%: Fora da faixa (fluxo de caixa livre excepcional)
    '''
    definicao = '''
    O Free Cash Flow Yield mede o fluxo de caixa livre por ação em relação ao preço da ação, calculado
    como (Fluxo de Caixa Livre / Valor de Mercado). É um indicador que reflete a capacidade da empresa
    de gerar caixa após despesas operacionais e investimentos, em relação ao seu valor de mercado. Um
    yield alto sugere subvalorização, enquanto um valor baixo ou negativo indica ineficiência ou sobrevalorização.
    '''
    agrupador = 'Fluxo de Caixa'
    formula = 'FCF Yield = Fluxo de Caixa Livre / Valor de Mercado'

    try:
        if fcf_yield < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'FCF Yield < 0%',
                'descricao': '''
                Um FCF Yield negativo indica que a empresa não gera fluxo de caixa livre, sugerindo dificuldades
                financeiras ou altos investimentos. Isso é comum em empresas em crise, como a Gol (GOLL4). Para
                investidores, essa faixa é um alerta de risco elevado, exigindo análise de endividamento e estratégias
                de geração de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= fcf_yield <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= FCF Yield <= 3%',
                'descricao': '''
                Um FCF Yield entre 0% e 3% reflete fluxo de caixa livre baixo, indicando que a empresa gera pouco
                caixa em relação ao seu valor de mercado. Isso é comum em setores com margens apertadas, como varejo
                (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, exigindo análise
                de eficiência operacional e potencial de melhoria do fluxo de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < fcf_yield <= 6:
            return {
                'classificacao': 'Moderado',
                'faixa': '3% < FCF Yield <= 6%',
                'descricao': '''
                Um FCF Yield entre 3% e 6% indica fluxo de caixa livre aceitável, típico de empresas com eficiência
                moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa. Para investidores,
                essa faixa sugere equilíbrio entre geração de caixa e valuation, sendo adequada para retornos consistentes.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 6 < fcf_yield <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '6% < FCF Yield <= 10%',
                'descricao': '''
                Um FCF Yield entre 6% e 10% reflete fluxo de caixa livre robusto, indicando que a empresa gera
                caixa significativo em relação ao seu valor de mercado. Empresas como a Ambev (ABEV3) frequentemente
                apresentam yield nessa faixa. Para investidores, essa faixa é atrativa, sugerindo subvalorização e
                solidez financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif fcf_yield > 10:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'FCF Yield > 10%',
                'descricao': '''
                Um FCF Yield acima de 10% é excepcional, indicando que a empresa gera fluxo de caixa livre extremamente
                alto em relação ao seu valor de mercado. Isso pode ocorrer em empresas como a Vale (VALE3) em períodos
                de alta geração de caixa. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois
                yields tão altos podem não ser sustentáveis. A análise deve focar na consistência do fluxo de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o FCF Yield: {str(e)}. Isso pode ter acontecido se o valor fornecido não
            for numérico ou se o valor de mercado for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que o fluxo de caixa livre e o valor de mercado estejam corretos e sejam valores numéricos
            válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_crescimento_lucro(crescimento_lucro):
    '''
    Avalia o Crescimento do Lucro com base em faixas definidas para o mercado brasileiro:
    - Crescimento Lucro < 0%: Crítico (redução de lucro, risco elevado)
    - 0% ≤ Crescimento Lucro ≤ 5%: Ruim (crescimento baixo ou estagnação)
    - 5% < Crescimento Lucro ≤ 15%: Moderado (crescimento aceitável)
    - 15% < Crescimento Lucro ≤ 25%: Ótimo (crescimento robusto)
    - Crescimento Lucro > 25%: Fora da faixa (crescimento excepcional)
    '''
    definicao = '''
    O Crescimento do Lucro mede a taxa anual de aumento do lucro líquido, calculada como
    ((Lucro Final / Lucro Inicial)^(1/n) - 1), onde n é o número de anos. É um indicador de crescimento
    que reflete a capacidade da empresa de aumentar sua rentabilidade. Um crescimento alto sugere sucesso
    operacional, enquanto um valor baixo ou negativo indica dificuldades. É útil em setores de alto crescimento,
    como tecnologia, mas deve ser analisado com margens e fluxo de caixa.
    '''
    agrupador = 'Crescimento'
    formula = 'Crescimento Lucro = ((Lucro Final / Lucro Inicial)^(1/n) - 1)'

    try:
        if crescimento_lucro < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Crescimento Lucro < 0%',
                'descricao': '''
                Um Crescimento do Lucro negativo indica que a empresa está enfrentando uma redução no lucro líquido,
                sugerindo dificuldades operacionais ou financeiras. Isso é comum em empresas em crise, como a Gol
                (GOLL4). Para investidores, essa faixa é um alerta de risco elevado, exigindo análise das causas da
                queda e estratégias de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= crescimento_lucro <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Crescimento Lucro <= 5%',
                'descricao': '''
                Um Crescimento do Lucro entre 0% e 5% reflete crescimento baixo ou estagnação, indicando que a
                empresa tem dificuldade em aumentar sua rentabilidade. Isso é comum em setores maduros, como varejo
                (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, exigindo análise
                de estratégias de crescimento e eficiência operacional.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < crescimento_lucro <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < Crescimento Lucro <= 15%',
                'descricao': '''
                Um Crescimento do Lucro entre 5% e 15% indica crescimento aceitável, típico de empresas com
                rentabilidade estável. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa.
                Para investidores, essa faixa sugere equilíbrio entre crescimento e segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < crescimento_lucro <= 25:
            return {
                'classificacao': 'Ótimo',
                'faixa': '15% < Crescimento Lucro <= 25%',
                'descricao': '''
                Um Crescimento do Lucro entre 15% e 25% reflete crescimento robusto, indicando que a empresa está
                aumentando sua rentabilidade de forma significativa. Empresas como a Magazine Luiza (MGLU3) podem
                apresentar crescimento nessa faixa em períodos de expansão. Para investidores, essa faixa é atrativa,
                sugerindo potencial de valorização.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif crescimento_lucro > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Crescimento Lucro > 25%',
                'descricao': '''
                Um Crescimento do Lucro acima de 25% é excepcional, indicando aumento extremamente rápido da
                rentabilidade. Isso pode ocorrer em empresas em setores de alto crescimento, como o Nubank (NUBR33).
                Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois crescimentos tão altos
                podem não ser sustentáveis. A análise deve focar na escalabilidade e barreiras de entrada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Crescimento do Lucro: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o lucro inicial for zero, o que impede o cálculo. Verifique os dados
            de entrada, assegurando que os lucros inicial e final estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_debt_equity(debt_equity):
    '''
    Avalia a Dívida/Patrimônio Líquido com base em faixas definidas para o mercado brasileiro:
    - Dívida/Patrimônio < 0: Fora da faixa (sem dívida ou patrimônio negativo)
    - 0 ≤ Dívida/Patrimônio ≤ 0.5: Ótimo (endividamento muito baixo)
    - 0.5 < Dívida/Patrimônio ≤ 1: Moderado (endividamento aceitável)
    - 1 < Dívida/Patrimônio ≤ 2: Ruim (endividamento elevado)
    - 2 < Dívida/Patrimônio ≤ 3: Péssimo (endividamento muito alto)
    - Dívida/Patrimônio > 3: Crítico (endividamento excessivo, risco elevado)
    '''
    definicao = '''
    A Dívida/Patrimônio Líquido mede a proporção da dívida total em relação ao patrimônio líquido,
    calculada como (Dívida Total / Patrimônio Líquido). É um indicador de alavancagem financeira que
    avalia o nível de endividamento em relação ao capital próprio. Um valor baixo sugere solidez financeira,
    enquanto um valor alto indica maior risco financeiro devido à dependência de dívidas.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida/Patrimônio = Dívida Total / Patrimônio Líquido'

    try:
        if debt_equity < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida/Patrimônio < 0',
                'descricao': '''
                Uma Dívida/Patrimônio negativa indica que a empresa não tem dívida ou que o patrimônio líquido
                é negativo. Empresas como a Totvs (TOTS3) podem apresentar valores negativos em períodos de alta
                liquidez, enquanto um patrimônio negativo (ex.: Oi - OIBR3) é alarmante. Para investidores, essa
                faixa exige análise detalhada da estrutura de capital e geração de caixa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= debt_equity <= 0.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida/Patrimônio <= 0.5',
                'descricao': '''
                Uma Dívida/Patrimônio entre 0 e 0.5 reflete endividamento muito baixo, indicando solidez financeira.
                Empresas como a Vale (VALE3) em períodos de alta geração de caixa frequentemente operam nessa faixa.
                Para investidores, essa faixa é atrativa, sugerindo baixo risco financeiro e flexibilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < debt_equity <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < Dívida/Patrimônio <= 1',
                'descricao': '''
                Uma Dívida/Patrimônio entre 0.5 e 1 indica endividamento aceitável, com equilíbrio entre dívida e
                capital próprio. Empresas como a Ambev (ABEV3) frequentemente operam nessa faixa. Para investidores,
                essa faixa sugere risco moderado, com a empresa capaz de suportar oscilações econômicas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < debt_equity <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '1 < Dívida/Patrimônio <= 2',
                'descricao': '''
                Uma Dívida/Patrimônio entre 1 e 2 sugere endividamento elevado, indicando que a empresa depende
                significativamente de dívidas. Isso é comum em setores intensivos em capital, como a Petrobras (PETR4).
                Para investidores, essa faixa exige cautela, pois a empresa pode ser vulnerável a aumentos de juros.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < debt_equity <= 3:
            return {
                'classificacao': 'Péssimo',
                'faixa': '2 < Dívida/Patrimônio <= 3',
                'descricao': '''
                Uma Dívida/Patrimônio entre 2 e 3 reflete endividamento muito alto, indicando risco significativo.
                Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises. Para investidores, essa faixa é
                preocupante, exigindo análise detalhada da estrutura de capital e planos de desalavancagem.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif debt_equity > 3:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida/Patrimônio > 3',
                'descricao': '''
                Uma Dívida/Patrimônio acima de 3 indica endividamento excessivo, sugerindo dependência extrema de
                dívidas. Isso é alarmante e típico de empresas em dificuldades, como a Gol (GOLL4) em crises. Para
                investidores, essa faixa é de altíssimo risco, com possibilidade de insolvência. A análise deve focar
                na capacidade de geração de caixa e estratégias de redução de dívida.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Dívida/Patrimônio: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o patrimônio líquido for zero, o que impede o cálculo. Verifique os
            dados de entrada, assegurando que a dívida total e o patrimônio líquido estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_margem_liquida_crescimento(margem_liquida_crescimento):
    '''
    Avalia o Crescimento da Margem Líquida com base em faixas definidas para o mercado brasileiro:
    - Crescimento Margem Líquida < 0%: Crítico (redução da margem, risco elevado)
    - 0% ≤ Crescimento Margem Líquida ≤ 2%: Ruim (crescimento baixo ou estagnação)
    - 2% < Crescimento Margem Líquida ≤ 5%: Moderado (crescimento aceitável)
    - 5% < Crescimento Margem Líquida ≤ 10%: Ótimo (crescimento robusto)
    - Crescimento Margem Líquida > 10%: Fora da faixa (crescimento excepcional)
    '''
    definicao = '''
    O Crescimento da Margem Líquida mede a taxa anual de aumento da margem líquida, calculada como
    ((Margem Líquida Final / Margem Líquida Inicial)^(1/n) - 1), onde n é o número de anos. É um
    indicador que reflete a melhoria na eficiência da empresa em converter receita em lucro líquido.
    Um crescimento alto sugere maior eficiência operacional, enquanto um valor baixo ou negativo indica
    deterioração da rentabilidade.
    '''
    agrupador = 'Rentabilidade'
    formula = 'Crescimento Margem Líquida = ((Margem Líquida Final / Margem Líquida Inicial)^(1/n) - 1)'

    try:
        if margem_liquida_crescimento < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Crescimento Margem Líquida < 0%',
                'descricao': '''
                Um Crescimento da Margem Líquida negativo indica redução da rentabilidade, sugerindo dificuldades
                operacionais ou aumento de custos. Isso é comum em empresas em crise, como a Oi (OIBR3). Para
                investidores, essa faixa é um alerta de risco elevado, exigindo análise da estrutura de custos e
                estratégias de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= margem_liquida_crescimento <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Crescimento Margem Líquida <= 2%',
                'descricao': '''
                Um Crescimento da Margem Líquida entre 0% e 2% reflete crescimento baixo ou estagnação, indicando
                que a empresa tem dificuldade em melhorar sua rentabilidade. Isso é comum em setores maduros, como
                varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, exigindo
                análise de estratégias de redução de custos e eficiência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < margem_liquida_crescimento <= 5:
            return {
                'classificacao': 'Moderado',
                'faixa': '2% < Crescimento Margem Líquida <= 5%',
                'descricao': '''
                Um Crescimento da Margem Líquida entre 2% e 5% indica crescimento aceitável, típico de empresas com
                eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa.
                Para investidores, essa faixa sugere equilíbrio entre rentabilidade e segurança, sendo adequada para
                retornos consistentes.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < margem_liquida_crescimento <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '5% < Crescimento Margem Líquida <= 10%',
                'descricao': '''
                Um Crescimento da Margem Líquida entre 5% e 10% reflete crescimento robusto, indicando que a empresa
                está melhorando significativamente sua eficiência em converter receita em lucro. Empresas como a Ambev
                (ABEV3) podem apresentar crescimento nessa faixa. Para investidores, essa faixa é atrativa, sugerindo
                potencial de valorização sustentável.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif margem_liquida_crescimento > 10:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Crescimento Margem Líquida > 10%',
                'descricao': '''
                Um Crescimento da Margem Líquida acima de 10% é excepcional, indicando melhoria extremamente rápida
                da rentabilidade. Isso pode ocorrer em empresas em setores de alto crescimento, como o Nubank (NUBR33).
                Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois crescimentos tão altos podem
                não ser sustentáveis. A análise deve focar na escalabilidade e barreiras de entrada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Crescimento da Margem Líquida: {str(e)}. Isso pode ter acontecido se o
            valor fornecido não for numérico ou se a margem líquida inicial for zero, o que impede o cálculo.
            Verifique os dados de entrada, assegurando que as margens líquidas inicial e final estejam corretas e
            sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_4.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: ROE, P/L, Liquidez Corrente, Cobertura de Juros.
"""


def evaluate_roe(roe):
    '''
    Avalia o Retorno sobre o Patrimônio Líquido (ROE) com base em faixas definidas para o mercado brasileiro:
    - ROE < 0%: Crítico (prejuízo, destruição de valor)
    - 0% ≤ ROE ≤ 5%: Ruim (retorno baixo, ineficiência)
    - 5% < ROE ≤ 15%: Moderado (retorno aceitável)
    - 15% < ROE ≤ 25%: Ótimo (retorno robusto)
    - ROE > 25%: Fora da faixa (retorno excepcional)
    '''
    definicao = '''
    O Retorno sobre o Patrimônio Líquido (ROE) mede a rentabilidade do capital próprio, calculado como
    (Lucro Líquido / Patrimônio Líquido). É um indicador de eficiência que mostra quanto a empresa gera
    de lucro com o capital dos acionistas. Um ROE alto sugere eficiência, enquanto um valor baixo ou
    negativo indica ineficiência ou prejuízo. É útil para comparar empresas dentro do mesmo setor.
    '''
    agrupador = 'Rentabilidade'
    formula = 'ROE = Lucro Líquido / Patrimônio Líquido'

    try:
        if roe < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'ROE < 0%',
                'descricao': '''
                Um ROE negativo indica que a empresa está gerando prejuízo, destruindo valor para os acionistas.
                Isso é comum em empresas em crise, como a Oi (OIBR3). Para investidores, essa faixa é um alerta de
                risco elevado, exigindo análise detalhada da estrutura de custos e estratégias de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= roe <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= ROE <= 5%',
                'descricao': '''
                Um ROE entre 0% e 5% reflete retorno baixo, indicando ineficiência na geração de lucro com o capital
                próprio. Isso é comum em setores com margens apertadas, como varejo (ex.: Carrefour Brasil - CRFB3).
                Para investidores, essa faixa sugere risco moderado, exigindo análise de estratégias de melhoria da
                rentabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < roe <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < ROE <= 15%',
                'descricao': '''
                Um ROE entre 5% e 15% indica retorno aceitável, típico de empresas com eficiência moderada. No Brasil,
                empresas como a Suzano (SUZB3) frequentemente operam nessa faixa. Para investidores, essa faixa sugere
                equilíbrio entre rentabilidade e segurança, sendo adequada para retornos consistentes.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < roe <= 25:
            return {
                'classificacao': 'Ótimo',
                'faixa': '15% < ROE <= 25%',
                'descricao': '''
                Um ROE entre 15% e 25% reflete retorno robusto, indicando que a empresa utiliza o capital próprio
                de forma eficiente. Empresas como a Ambev (ABEV3) frequentemente apresentam ROE nessa faixa. Para
                investidores, essa faixa é atrativa, sugerindo solidez financeira e potencial de valorização.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif roe > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'ROE > 25%',
                'descricao': '''
                Um ROE acima de 25% é excepcional, indicando retornos extremamente altos com o capital próprio.
                Isso pode ocorrer em empresas como a Weg (WEGE3) em períodos de forte desempenho. Para investidores,
                essa faixa é altamente atrativa, mas exige cautela, pois retornos tão altos podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o ROE: {str(e)}. Isso pode ter acontecido se o valor fornecido não for
            numérico ou se o patrimônio líquido for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que o lucro líquido e o patrimônio líquido estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_p_l(p_l):
    '''
    Avalia o Preço/Lucro (P/L) com base em faixas definidas para o mercado brasileiro:
    - P/L < 0: Crítico (lucro negativo, risco elevado)
    - 0 ≤ P/L ≤ 10: Ótimo (subvalorizado, oportunidade de compra)
    - 10 < P/L ≤ 15: Moderado (valuation justo)
    - 15 < P/L ≤ 20: Ruim (sobrevalorizado, cautela necessária)
    - 20 < P/L ≤ 25: Péssimo (muito caro, alto risco)
    - P/L > 25: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    O Preço/Lucro (P/L) compara o preço da ação ao lucro por ação, calculado como (Preço da Ação / Lucro por Ação).
    É um indicador de valuation que avalia se a ação está cara ou barata em relação aos lucros. Um P/L baixo
    sugere subvalorização, enquanto um valor alto indica sobrevalorização ou expectativas de crescimento.
    '''
    agrupador = 'Valuation'
    formula = 'P/L = Preço da Ação / Lucro por Ação'

    try:
        if p_l < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/L < 0',
                'descricao': '''
                Um P/L negativo indica que a empresa está gerando prejuízo, sugerindo risco elevado. Isso é comum
                em empresas em crise, como a Oi (OIBR3). Para investidores, essa faixa exige análise detalhada da
                saúde financeira e estratégias de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= p_l <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/L <= 10',
                'descricao': '''
                Um P/L entre 0 e 10 sugere que a ação está subvalorizada, indicando uma potencial oportunidade de
                compra. Isso é comum em setores cíclicos, como a Vale (VALE3) em períodos de baixa. Para investidores,
                essa faixa é atrativa, mas é importante verificar a sustentabilidade dos lucros.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < p_l <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '10 < P/L <= 15',
                'descricao': '''
                Um P/L entre 10 e 15 reflete um valuation justo, típico de empresas com lucros estáveis. Empresas
                como a Ambev (ABEV3) frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio
                entre preço e fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < p_l <= 20:
            return {
                'classificacao': 'Ruim',
                'faixa': '15 < P/L <= 20',
                'descricao': '''
                Um P/L entre 15 e 20 sugere que a ação está sobrevalorizada, indicando que o mercado espera
                crescimento significativo. Empresas como a Raia Drogasil (RADL3) podem atingir essa faixa. Para
                investidores, essa faixa exige cautela, pois o preço elevado pode não se sustentar sem crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < p_l <= 25:
            return {
                'classificacao': 'Péssimo',
                'faixa': '20 < P/L <= 25',
                'descricao': '''
                Um P/L entre 20 e 25 indica que a ação é muito cara, sugerindo que o mercado está pagando um
                prêmio elevado. Empresas como a Localiza (RENT3) podem apresentar P/L nessa faixa em momentos de
                otimismo. Para investidores, essa faixa é de alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif p_l > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/L > 25',
                'descricao': '''
                Um P/L acima de 25 é extremamente elevado, geralmente associado a empresas com altíssimas
                expectativas de crescimento, como o Nubank (NUBR33). Para investidores, essa faixa é de altíssimo
                risco, refletindo mais especulação do que fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o P/L: {str(e)}. Isso pode ter acontecido se o valor fornecido não for
            numérico ou se o lucro por ação for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que o preço da ação e o lucro por ação estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_liquidez_corrente(liquidez_corrente):
    '''
    Avalia a Liquidez Corrente com base em faixas definidas para o mercado brasileiro:
    - Liquidez Corrente < 0.5: Crítico (dificuldade extrema em pagar obrigações de curto prazo)
    - 0.5 ≤ Liquidez Corrente ≤ 1: Ruim (capacidade limitada de pagar obrigações de curto prazo)
    - 1 < Liquidez Corrente ≤ 1.5: Moderado (capacidade aceitável de pagar obrigações de curto prazo)
    - 1.5 < Liquidez Corrente ≤ 2: Ótimo (boa capacidade de pagar obrigações de curto prazo)
    - Liquidez Corrente > 2: Fora da faixa (excesso de liquidez, possível ineficiência)
    '''
    definicao = '''
    A Liquidez Corrente mede a capacidade da empresa de pagar suas obrigações de curto prazo com seus
    ativos circulantes, calculada como (Ativo Circulante / Passivo Circulante). É um indicador de liquidez
    que reflete a saúde financeira de curto prazo. Um valor alto sugere solidez, enquanto um valor baixo
    indica risco de inadimplência.
    '''
    agrupador = 'Liquidez'
    formula = 'Liquidez Corrente = Ativo Circulante / Passivo Circulante'

    try:
        if liquidez_corrente < 0.5:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Liquidez Corrente < 0.5',
                'descricao': '''
                Uma Liquidez Corrente abaixo de 0.5 indica dificuldade extrema em pagar obrigações de curto prazo,
                sugerindo risco elevado de inadimplência. Isso é comum em empresas em crise, como a Oi (OIBR3).
                Para investidores, essa faixa é um alerta grave, exigindo análise da gestão de caixa e recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 <= liquidez_corrente <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 <= Liquidez Corrente <= 1',
                'descricao': '''
                Uma Liquidez Corrente entre 0.5 e 1 reflete capacidade limitada de pagar obrigações de curto prazo,
                indicando dependência de conversão de ativos em caixa. Isso é comum em setores com margens apertadas,
                como varejo (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < liquidez_corrente <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Liquidez Corrente <= 1.5',
                'descricao': '''
                Uma Liquidez Corrente entre 1 e 1.5 indica capacidade aceitável de pagar obrigações de curto prazo.
                Empresas como a Suzano (SUZB3) frequentemente operam nessa faixa. Para investidores, essa faixa sugere
                equilíbrio entre liquidez e eficiência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < liquidez_corrente <= 2:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1.5 < Liquidez Corrente <= 2',
                'descricao': '''
                Uma Liquidez Corrente entre 1.5 e 2 reflete boa capacidade de pagar obrigações de curto prazo,
                indicando solidez financeira. Empresas como a Ambev (ABEV3) frequentemente apresentam liquidez nessa
                faixa. Para investidores, essa faixa é atrativa, sugerindo resiliência financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif liquidez_corrente > 2:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Liquidez Corrente > 2',
                'descricao': '''
                Uma Liquidez Corrente acima de 2 indica excesso de liquidez, com ativos circulantes muito superiores
                às obrigações de curto prazo. Isso pode ocorrer em empresas como a Vale (VALE3) em períodos de alta
                geração de caixa. Para investidores, essa faixa pode ser positiva, mas também pode indicar ineficiência
                na alocação de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Liquidez Corrente: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o passivo circulante for zero, o que impede o cálculo. Verifique os
            dados de entrada, assegurando que o ativo circulante e o passivo circulante estejam corretos e sejam
            valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_cobertura_juros(cobertura_juros):
    '''
    Avalia a Cobertura de Juros com base em faixas definidas para o mercado brasileiro:
    - Cobertura de Juros < 1: Crítico (dificuldade em cobrir juros, risco elevado)
    - 1 ≤ Cobertura de Juros ≤ 2: Ruim (capacidade limitada de cobrir juros)
    - 2 < Cobertura de Juros ≤ 4: Moderado (capacidade aceitável de cobrir juros)
    - 4 < Cobertura de Juros ≤ 6: Ótimo (boa capacidade de cobrir juros)
    - Cobertura de Juros > 6: Fora da faixa (excelente capacidade de cobrir juros)
    '''
    definicao = '''
    A Cobertura de Juros mede a capacidade da empresa de pagar os juros de suas dívidas com o lucro
    operacional, calculada como (EBIT / Despesa com Juros). É um indicador de solvência que reflete a
    segurança financeira em relação às obrigações de dívida. Um valor alto sugere solidez, enquanto um
    valor baixo indica risco de inadimplência.
    '''
    agrupador = 'Solvência'
    formula = 'Cobertura de Juros = EBIT / Despesa com Juros'

    try:
        if cobertura_juros < 1:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Cobertura de Juros < 1',
                'descricao': '''
                Uma Cobertura de Juros abaixo de 1 indica que a empresa não gera lucro operacional suficiente
                para cobrir os juros de suas dívidas, sugerindo risco elevado de inadimplência. Isso é comum em
                empresas em crise, como a Gol (GOLL4). Para investidores, essa faixa é um alerta grave, exigindo
                análise da estrutura de dívida e estratégias de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 <= cobertura_juros <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '1 <= Cobertura de Juros <= 2',
                'descricao': '''
                Uma Cobertura de Juros entre 1 e 2 reflete capacidade limitada de cobrir os juros, indicando
                dependência de lucros operacionais apertados. Isso é comum em setores intensivos em capital, como a
                Petrobras (PETR4). Para investidores, essa faixa sugere risco moderado, exigindo análise da gestão
                de dívida.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < cobertura_juros <= 4:
            return {
                'classificacao': 'Moderado',
                'faixa': '2 < Cobertura de Juros <= 4',
                'descricao': '''
                Uma Cobertura de Juros entre 2 e 4 indica capacidade aceitável de cobrir os juros, típico de empresas
                com estabilidade financeira moderada. Empresas como a Suzano (SUZB3) frequentemente operam nessa faixa.
                Para investidores, essa faixa sugere equilíbrio entre solvência e risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 4 < cobertura_juros <= 6:
            return {
                'classificacao': 'Ótimo',
                'faixa': '4 < Cobertura de Juros <= 6',
                'descricao': '''
                Uma Cobertura de Juros entre 4 e 6 reflete boa capacidade de cobrir os juros, indicando solidez
                financeira. Empresas como a Ambev (ABEV3) frequentemente apresentam cobertura nessa faixa. Para
                investidores, essa faixa é atrativa, sugerindo resiliência financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif cobertura_juros > 6:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Cobertura de Juros > 6',
                'descricao': '''
                Uma Cobertura de Juros acima de 6 indica excelente capacidade de cobrir os juros, sugerindo baixa
                dependência de dívidas. Isso pode ocorrer em empresas como a Vale (VALE3) em períodos de alta geração
                de caixa. Para investidores, essa faixa é altamente atrativa, mas pode indicar subalavancagem.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Cobertura de Juros: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se a despesa com juros for zero, o que impede o cálculo. Verifique os
            dados de entrada, assegurando que o EBIT e a despesa com juros estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_5.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: Margem Bruta, Giro de Ativos, Dívida/EBIT, Dividend Yield.
"""


def evaluate_margem_bruta(margem_bruta):
    '''
    Avalia a Margem Bruta com base em faixas definidas para o mercado brasileiro:
    - Margem Bruta < 10%: Crítico (rentabilidade bruta muito baixa, risco elevado)
    - 10% ≤ Margem Bruta ≤ 20%: Ruim (rentabilidade bruta baixa)
    - 20% < Margem Bruta ≤ 30%: Moderado (rentabilidade bruta aceitável)
    - 30% < Margem Bruta ≤ 50%: Ótimo (rentabilidade bruta robusta)
    - Margem Bruta > 50%: Fora da faixa (rentabilidade bruta excepcional)
    '''
    definicao = '''
    A Margem Bruta mede a proporção da receita bruta que permanece após os custos diretos, calculada
    como (Receita Bruta - Custo dos Produtos Vendidos) / Receita Bruta. É um indicador de rentabilidade
    que reflete a eficiência da empresa em gerenciar custos diretos. Uma margem alta sugere forte
    precificação ou controle de custos, enquanto uma margem baixa indica dificuldades operacionais.
    '''
    agrupador = 'Rentabilidade'
    formula = 'Margem Bruta = (Receita Bruta - Custo dos Produtos Vendidos) / Receita Bruta'

    try:
        if margem_bruta < 10:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Margem Bruta < 10%',
                'descricao': '''
                Uma Margem Bruta abaixo de 10% indica rentabilidade bruta muito baixa, sugerindo dificuldades em
                cobrir custos diretos. Isso é comum em setores altamente competitivos, como varejo (ex.: Casas Bahia
                - BHIA3). Para investidores, essa faixa é um alerta de risco elevado, exigindo análise da estrutura
                de custos e concorrência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 <= margem_bruta <= 20:
            return {
                'classificacao': 'Ruim',
                'faixa': '10% <= Margem Bruta <= 20%',
                'descricao': '''
                Uma Margem Bruta entre 10% e 20% reflete rentabilidade bruta baixa, indicando desafios na gestão
                de custos diretos. Isso é comum em setores com margens apertadas, como varejo alimentar (ex.: Carrefour
                Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, exigindo análise de estratégias
                de precificação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < margem_bruta <= 30:
            return {
                'classificacao': 'Moderado',
                'faixa': '20% < Margem Bruta <= 30%',
                'descricao': '''
                Uma Margem Bruta entre 20% e 30% indica rentabilidade bruta aceitável, típico de empresas com
                eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa.
                Para investidores, essa faixa sugere equilíbrio entre rentabilidade e competitividade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 30 < margem_bruta <= 50:
            return {
                'classificacao': 'Ótimo',
                'faixa': '30% < Margem Bruta <= 50%',
                'descricao': '''
                Uma Margem Bruta entre 30% e 50% reflete rentabilidade bruta robusta, indicando forte controle de
                custos ou precificação. Empresas como a Ambev (ABEV3) frequentemente apresentam margem nessa faixa.
                Para investidores, essa faixa é atrativa, sugerindo solidez operacional.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif margem_bruta > 50:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Margem Bruta > 50%',
                'descricao': '''
                Uma Margem Bruta acima de 50% é excepcional, indicando altíssima eficiência na gestão de custos
                diretos. Isso pode ocorrer em empresas como a Weg (WEGE3). Para investidores, essa faixa é altamente
                atrativa, mas exige cautela, pois margens tão altas podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Margem Bruta: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que a receita bruta e o custo dos produtos vendidos estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_giro_ativos(giro_ativos):
    '''
    Avalia o Giro de Ativos com base em faixas definidas para o mercado brasileiro:
    - Giro de Ativos < 0.2: Crítico (baixa eficiência no uso de ativos)
    - 0.2 ≤ Giro de Ativos ≤ 0.5: Ruim (eficiência limitada no uso de ativos)
    - 0.5 < Giro de Ativos ≤ 1: Moderado (eficiência aceitável no uso de ativos)
    - 1 < Giro de Ativos ≤ 1.5: Ótimo (alta eficiência no uso de ativos)
    - Giro de Ativos > 1.5: Fora da faixa (eficiência excepcional no uso de ativos)
    '''
    definicao = '''
    O Giro de Ativos mede a eficiência da empresa em gerar receita com seus ativos totais, calculado
    como (Receita Bruta / Ativos Totais). É um indicador que reflete como a empresa utiliza seus ativos
    para gerar vendas. Um valor alto sugere eficiência, enquanto um valor baixo indica subutilização de
    ativos.
    '''
    agrupador = 'Eficiência'
    formula = 'Giro de Ativos = Receita Bruta / Ativos Totais'

    try:
        if giro_ativos < 0.2:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Giro de Ativos < 0.2',
                'descricao': '''
                Um Giro de Ativos abaixo de 0.2 indica baixa eficiência no uso de ativos, sugerindo subutilização
                ou ativos ociosos. Isso é comum em empresas com grandes investimentos fixos, como a CSN (CSNA3) em
                períodos de baixa demanda. Para investidores, essa faixa é um alerta de risco elevado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 <= giro_ativos <= 0.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.2 <= Giro de Ativos <= 0.5',
                'descricao': '''
                Um Giro de Ativos entre 0.2 e 0.5 reflete eficiência limitada no uso de ativos, indicando que a
                empresa gera receita moderada em relação aos ativos. Isso é comum em setores intensivos em capital,
                como a Petrobras (PETR4). Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < giro_ativos <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < Giro de Ativos <= 1',
                'descricao': '''
                Um Giro de Ativos entre 0.5 e 1 indica eficiência aceitável no uso de ativos. Empresas como a
                Suzano (SUZB3) frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio
                entre eficiência e estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < giro_ativos <= 1.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1 < Giro de Ativos <= 1.5',
                'descricao': '''
                Um Giro de Ativos entre 1 e 1.5 reflete alta eficiência no uso de ativos, indicando que a empresa
                gera receita significativa com seus ativos. Empresas como a Ambev (ABEV3) frequentemente apresentam
                giro nessa faixa. Para investidores, essa faixa é atrativa, sugerindo eficiência operacional.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif giro_ativos > 1.5:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Giro de Ativos > 1.5',
                'descricao': '''
                Um Giro de Ativos acima de 1.5 é excepcional, indicando eficiência extremamente alta no uso de
                ativos. Isso pode ocorrer em empresas como a Magazine Luiza (MGLU3) em períodos de forte crescimento.
                Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois pode não ser sustentável.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Giro de Ativos: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se os ativos totais forem zero, o que impede o cálculo. Verifique os
            dados de entrada, assegurando que a receita bruta e os ativos totais estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_divida_ebit(divida_ebit):
    '''
    Avalia a Dívida/EBIT com base em faixas definidas para o mercado brasileiro:
    - Dívida/EBIT < 0: Fora da faixa (sem dívida ou EBIT negativo)
    - 0 ≤ Dívida/EBIT ≤ 1: Ótimo (endividamento muito baixo)
    - 1 < Dívida/EBIT ≤ 2: Moderado (endividamento aceitável)
    - 2 < Dívida/EBIT ≤ 3: Ruim (endividamento elevado)
    - 3 < Dívida/EBIT ≤ 4: Péssimo (endividamento muito alto)
    - Dívida/EBIT > 4: Crítico (endividamento excessivo, risco elevado)
    '''
    definicao = '''
    A Dívida/EBIT mede a capacidade da empresa de pagar sua dívida total com o lucro antes de juros e
    impostos, calculada como (Dívida Total / EBIT). É um indicador de alavancagem financeira que avalia
    quantos anos a empresa levaria para quitar sua dívida com seu lucro operacional. Um valor baixo
    sugere solidez financeira, enquanto um valor alto indica risco elevado.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida/EBIT = Dívida Total / EBIT'

    try:
        if divida_ebit < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida/EBIT < 0',
                'descricao': '''
                Uma Dívida/EBIT negativa indica que a empresa não tem dívida ou que o EBIT é negativo. Empresas
                como a Totvs (TOTS3) podem apresentar valores negativos em períodos de alta liquidez, enquanto um
                EBIT negativo (ex.: Oi - OIBR3) é alarmante. Para investidores, essa faixa exige análise detalhada
                da estrutura de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_ebit <= 1:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida/EBIT <= 1',
                'descricao': '''
                Uma Dívida/EBIT entre 0 e 1 reflete endividamento muito baixo, indicando que a empresa pode quitar
                sua dívida rapidamente com o lucro operacional. Empresas como a Vale (VALE3) podem operar nessa faixa
                em períodos de alta geração de caixa. Para investidores, essa faixa é atrativa, sugerindo baixo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < divida_ebit <= 2:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Dívida/EBIT <= 2',
                'descricao': '''
                Uma Dívida/EBIT entre 1 e 2 indica endividamento aceitável, com equilíbrio entre dívida e lucro
                operacional. Empresas como a Ambev (ABEV3) frequentemente operam nessa faixa. Para investidores,
                essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < divida_ebit <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '2 < Dívida/EBIT <= 3',
                'descricao': '''
                Uma Dívida/EBIT entre 2 e 3 sugere endividamento elevado, indicando dependência significativa de
                dívidas. Isso é comum em setores intensivos em capital, como a Petrobras (PETR4). Para investidores,
                essa faixa exige cautela, pois a empresa pode ser vulnerável a oscilações econômicas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < divida_ebit <= 4:
            return {
                'classificacao': 'Péssimo',
                'faixa': '3 < Dívida/EBIT <= 4',
                'descricao': '''
                Uma Dívida/EBIT entre 3 e 4 reflete endividamento muito alto, indicando risco significativo.
                Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises. Para investidores, essa faixa
                é preocupante, exigindo análise detalhada da estrutura de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif divida_ebit > 4:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida/EBIT > 4',
                'descricao': '''
                Uma Dívida/EBIT acima de 4 indica endividamento excessivo, sugerindo dependência extrema de dívidas.
                Isso é típico de empresas em dificuldades, como a Gol (GOLL4) em crises. Para investidores, essa
                faixa é de altíssimo risco, com possibilidade de insolvência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Dívida/EBIT: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se o EBIT for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que a dívida total e o EBIT estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_dividend_yield(dividend_yield):
    '''
    Avalia o Dividend Yield com base em faixas definidas para o mercado brasileiro:
    - Dividend Yield < 0%: Fora da faixa (sem dividendos)
    - 0% ≤ Dividend Yield ≤ 2%: Ruim (retorno baixo em dividendos)
    - 2% < Dividend Yield ≤ 5%: Moderado (retorno aceitável em dividendos)
    - 5% < Dividend Yield ≤ 8%: Ótimo (retorno robusto em dividendos)
    - Dividend Yield > 8%: Crítico (retorno muito alto, risco de insustentabilidade)
    '''
    definicao = '''
    O Dividend Yield mede o retorno anual em dividendos em relação ao preço da ação, calculado como
    (Dividendos por Ação / Preço da Ação). É um indicador que reflete o retorno direto para os acionistas
    por meio de dividendos. Um yield alto é atrativo para investidores focados em renda, mas pode indicar
    risco se for insustentável.
    '''
    agrupador = 'Dividendos'
    formula = 'Dividend Yield = Dividendos por Ação / Preço da Ação'

    try:
        if dividend_yield < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dividend Yield < 0%',
                'descricao': '''
                Um Dividend Yield negativo ou zero indica que a empresa não paga dividendos, seja por prejuízo ou
                reinvestimento total dos lucros. Isso é comum em empresas em crescimento, como o Nubank (NUBR33).
                Para investidores focados em renda, essa faixa é desvantajosa, mas pode ser positiva para quem busca
                crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= dividend_yield <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Dividend Yield <= 2%',
                'descricao': '''
                Um Dividend Yield entre 0% e 2% reflete retorno baixo em dividendos, indicando que a empresa
                prioriza reinvestimento. Isso é comum em empresas como a Magazine Luiza (MGLU3). Para investidores
                focados em renda, essa faixa é pouco atrativa, mas pode ser positiva para quem busca crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < dividend_yield <= 5:
            return {
                'classificacao': 'Moderado',
                'faixa': '2% < Dividend Yield <= 5%',
                'descricao': '''
                Um Dividend Yield entre 2% e 5% indica retorno aceitável em dividendos, com equilíbrio entre
                distribuição e reinvestimento. Empresas como a Vale (VALE3) frequentemente operam nessa faixa.
                Para investidores, essa faixa é adequada para quem busca renda moderada com potencial de crescimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < dividend_yield <= 8:
            return {
                'classificacao': 'Ótimo',
                'faixa': '5% < Dividend Yield <= 8%',
                'descricao': '''
                Um Dividend Yield entre 5% e 8% reflete retorno robusto em dividendos, indicando que a empresa
                distribui uma parte significativa dos lucros. Empresas como a Engie Brasil (EGIE3) frequentemente
                apresentam yield nessa faixa. Para investidores, essa faixa é atrativa, sugerindo estabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif dividend_yield > 8:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dividend Yield > 8%',
                'descricao': '''
                Um Dividend Yield acima de 8% indica retorno muito alto, mas pode sugerir insustentabilidade dos
                dividendos. Empresas como a Taesa (TAEE11) podem apresentar yields elevados, mas isso exige cautela,
                pois pode comprometer o crescimento. Para investidores, a análise deve focar no fluxo de caixa livre.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Dividend Yield: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se o preço da ação for zero, o que impede o cálculo. Verifique os dados de entrada,
            assegurando que os dividendos por ação e o preço da ação estejam corretos e sejam valores numéricos
            válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_6.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: P/VP, ROIC, Dívida Líquida/Patrimônio, Crescimento do EBITDA.
"""


def evaluate_p_vp(p_vp):
    '''
    Avalia o Preço/Valor Patrimonial (P/VP) com base em faixas definidas para o mercado brasileiro:
    - P/VP < 0: Fora da faixa (patrimônio líquido negativo)
    - 0 ≤ P/VP ≤ 1: Ótimo (subvalorizado, oportunidade de compra)
    - 1 < P/VP ≤ 1.5: Moderado (valuation justo)
    - 1.5 < P/VP ≤ 2: Ruim (sobrevalorizado, cautela necessária)
    - 2 < P/VP ≤ 3: Péssimo (muito caro, alto risco)
    - P/VP > 3: Crítico (extremamente sobrevalorizado)
    '''
    definicao = '''
    O Preço/Valor Patrimonial (P/VP) compara o preço da ação ao valor patrimonial por ação, calculado
    como (Preço da Ação / Valor Patrimonial por Ação). É um indicador de valuation que avalia se a
    ação está cara ou barata em relação aos ativos líquidos da empresa. Um P/VP baixo sugere
    subvalorização, enquanto um valor alto indica sobrevalorização ou expectativas de crescimento.
    '''
    agrupador = 'Valuation'
    formula = 'P/VP = Preço da Ação / Valor Patrimonial por Ação'

    try:
        if p_vp < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/VP < 0',
                'descricao': '''
                Um P/VP negativo indica que o patrimônio líquido da empresa é negativo, sugerindo sérias
                dificuldades financeiras. Isso é comum em empresas em crise, como a Oi (OIBR3). Para
                investidores, essa faixa é um alerta grave, exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= p_vp <= 1:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/VP <= 1',
                'descricao': '''
                Um P/VP entre 0 e 1 sugere que a ação está subvalorizada, sendo negociada abaixo do seu
                valor patrimonial. Isso é comum em setores cíclicos, como a Vale (VALE3) em períodos de baixa.
                Para investidores, essa faixa é atrativa, mas é importante verificar a qualidade dos ativos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < p_vp <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < P/VP <= 1.5',
                'descricao': '''
                Um P/VP entre 1 e 1.5 reflete um valuation justo, típico de empresas com estabilidade financeira.
                Empresas como a Ambev (ABEV3) frequentemente operam nessa faixa. Para investidores, essa faixa
                sugere equilíbrio entre preço e fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < p_vp <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '1.5 < P/VP <= 2',
                'descricao': '''
                Um P/VP entre 1.5 e 2 sugere que a ação está sobrevalorizada, indicando que o mercado espera
                crescimento. Empresas como a Raia Drogasil (RADL3) podem atingir essa faixa. Para investidores,
                essa faixa exige cautela, pois o preço elevado pode não se sustentar sem crescimento robusto.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < p_vp <= 3:
            return {
                'classificacao': 'Péssimo',
                'faixa': '2 < P/VP <= 3',
                'descricao': '''
                Um P/VP entre 2 e 3 indica que a ação é muito cara, sugerindo que o mercado está pagando um
                prêmio elevado. Empresas como a Localiza (RENT3) podem apresentar P/VP nessa faixa em momentos
                de otimismo. Para investidores, essa faixa é de alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif p_vp > 3:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/VP > 3',
                'descricao': '''
                Um P/VP acima de 3 é extremamente elevado, geralmente associado a empresas com altíssimas
                expectativas de crescimento, como o Nubank (NUBR33). Para investidores, essa faixa reflete
                especulação e alto risco, exigindo análise detalhada dos fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o P/VP: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se o valor patrimonial por ação for zero, o que impede o cálculo.
            Verifique os dados de entrada, assegurando que o preço da ação e o valor patrimonial por ação
            estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_roic(roic):
    '''
    Avalia o Retorno sobre o Capital Investido (ROIC) com base em faixas definidas para o mercado brasileiro:
    - ROIC < 0%: Crítico (destruição de valor, risco elevado)
    - 0% ≤ ROIC ≤ 5%: Ruim (retorno baixo, ineficiência)
    - 5% < ROIC ≤ 10%: Moderado (retorno aceitável)
    - 10% < ROIC ≤ 20%: Ótimo (retorno robusto)
    - ROIC > 20%: Fora da faixa (retorno excepcional)
    '''
    definicao = '''
    O Retorno sobre o Capital Investido (ROIC) mede a eficiência da empresa em gerar lucro com o capital
    total investido (dívida e patrimônio), calculado como (NOPAT / Capital Investido), onde NOPAT é
    o lucro operacional após impostos. É um indicador de rentabilidade que avalia a eficiência do uso
    do capital. Um ROIC alto sugere eficiência, enquanto um valor baixo ou negativo indica ineficiência.
    '''
    agrupador = 'Rentabilidade'
    formula = 'ROIC = NOPAT / Capital Investido'

    try:
        if roic < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'ROIC < 0%',
                'descricao': '''
                Um ROIC negativo indica que a empresa está destruindo valor, gerando prejuízo com o capital
                investido. Isso é comum em empresas em crise, como a Gol (GOLL4). Para investidores, essa
                faixa é um alerta grave, exigindo análise detalhada da gestão de capital e recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= roic <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= ROIC <= 5%',
                'descricao': '''
                Um ROIC entre 0% e 5% reflete retorno baixo, indicando ineficiência no uso do capital investido.
                Isso é comum em setores com margens apertadas, como varejo (ex.: Carrefour Brasil - CRFB3).
                Para investidores, essa faixa sugere risco moderado, exigindo análise de estratégias de melhoria.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < roic <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < ROIC <= 10%',
                'descricao': '''
                Um ROIC entre 5% e 10% indica retorno aceitável, típico de empresas com eficiência moderada.
                No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa. Para investidores,
                essa faixa sugere equilíbrio entre rentabilidade e segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < roic <= 20:
            return {
                'classificacao': 'Ótimo',
                'faixa': '10% < ROIC <= 20%',
                'descricao': '''
                Um ROIC entre 10% e 20% reflete retorno robusto, indicando que a empresa utiliza o capital
                investido de forma eficiente. Empresas como a Ambev (ABEV3) frequentemente apresentam ROIC
                nessa faixa. Para investidores, essa faixa é atrativa, sugerindo solidez financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif roic > 20:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'ROIC > 20%',
                'descricao': '''
                Um ROIC acima de 20% é excepcional, indicando retornos extremamente altos com o capital
                investido. Isso pode ocorrer em empresas como a Weg (WEGE3). Para investidores, essa faixa
                é altamente atrativa, mas exige cautela, pois retornos tão altos podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o ROIC: {str(e)}. Isso pode ter acontecido se o valor fornecido
            não for numérico ou se o capital investido for zero, o que impede o cálculo. Verifique os
            dados de entrada, assegurando que o NOPAT e o capital investido estejam corretos e sejam
            valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_divida_liquida_patrimonio(divida_liquida_patrimonio):
    '''
    Avalia a Dívida Líquida/Patrimônio com base em faixas definidas para o mercado brasileiro:
    - Dívida Líquida/Patrimônio < 0: Fora da faixa (sem dívida líquida ou patrimônio negativo)
    - 0 ≤ Dívida Líquida/Patrimônio ≤ 0.3: Ótimo (endividamento muito baixo)
    - 0.3 < Dívida Líquida/Patrimônio ≤ 0.6: Moderado (endividamento aceitável)
    - 0.6 < Dívida Líquida/Patrimônio ≤ 1: Ruim (endividamento elevado)
    - 1 < Dívida Líquida/Patrimônio ≤ 1.5: Péssimo (endividamento muito alto)
    - Dívida Líquida/Patrimônio > 1.5: Crítico (endividamento excessivo, risco elevado)
    '''
    definicao = '''
    A Dívida Líquida/Patrimônio mede a proporção da dívida líquida (dívida total menos caixa e equivalentes)
    em relação ao patrimônio líquido, calculada como (Dívida Líquida / Patrimônio Líquido). É um indicador
    de alavancagem financeira que avalia o nível de endividamento líquido. Um valor baixo sugere solidez,
    enquanto um valor alto indica maior risco financeiro.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida Líquida/Patrimônio = Dívida Líquida / Patrimônio Líquido'

    try:
        if divida_liquida_patrimonio < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Líquida/Patrimônio < 0',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio negativa indica que a empresa tem mais caixa do que dívida ou
                que o patrimônio líquido é negativo. Empresas como a Totvs (TOTS3) podem apresentar valores
                negativos em períodos de alta liquidez, enquanto um patrimônio negativo (ex.: Oi - OIBR3) é
                alarmante. Para investidores, essa faixa exige análise detalhada da estrutura de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_liquida_patrimonio <= 0.3:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida Líquida/Patrimônio <= 0.3',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio entre 0 e 0.3 reflete endividamento muito baixo, indicando
                solidez financeira. Empresas como a Vale (VALE3) em períodos de alta geração de caixa
                frequentemente operam nessa faixa. Para investidores, essa faixa é atrativa, sugerindo
                baixo risco financeiro.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 < divida_liquida_patrimonio <= 0.6:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.3 < Dívida Líquida/Patrimônio <= 0.6',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio entre 0.3 e 0.6 indica endividamento aceitável, com equilíbrio
                entre dívida líquida e capital próprio. Empresas como a Ambev (ABEV3) frequentemente operam
                nessa faixa. Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.6 < divida_liquida_patrimonio <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.6 < Dívida Líquida/Patrimônio <= 1',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio entre 0.6 e 1 sugere endividamento elevado, indicando
                dependência significativa de dívidas líquidas. Isso é comum em setores intensivos em capital,
                como a Petrobras (PETR4). Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < divida_liquida_patrimonio <= 1.5:
            return {
                'classificacao': 'Péssimo',
                'faixa': '1 < Dívida Líquida/Patrimônio <= 1.5',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio entre 1 e 1.5 reflete endividamento muito alto, indicando
                risco significativo. Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises.
                Para investidores, essa faixa é preocupante, exigindo análise detalhada da estrutura de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif divida_liquida_patrimonio > 1.5:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida Líquida/Patrimônio > 1.5',
                'descricao': '''
                Uma Dívida Líquida/Patrimônio acima de 1.5 indica endividamento excessivo, sugerindo
                dependência extrema de dívidas líquidas. Isso é típico de empresas em dificuldades, como
                a Gol (GOLL4) em crises. Para investidores, essa faixa é de altíssimo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Dívida Líquida/Patrimônio: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se o patrimônio líquido for zero,
            o que impede o cálculo. Verifique os dados de entrada, assegurando que a dívida líquida
            e o patrimônio líquido estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_crescimento_ebitda(crescimento_ebitda):
    '''
    Avalia o Crescimento do EBITDA com base em faixas definidas para o mercado brasileiro:
    - Crescimento EBITDA < 0%: Crítico (redução de lucratividade operacional, risco elevado)
    - 0% ≤ Crescimento EBITDA ≤ 5%: Ruim (crescimento baixo ou estagnação)
    - 5% < Crescimento EBITDA ≤ 15%: Moderado (crescimento aceitável)
    - 15% < Crescimento EBITDA ≤ 25%: Ótimo (crescimento robusto)
    - Crescimento EBITDA > 25%: Fora da faixa (crescimento excepcional)
    '''
    definicao = '''
    O Crescimento do EBITDA mede a taxa anual de aumento do lucro antes de juros, impostos,
    depreciação e amortização, calculada como ((EBITDA Final / EBITDA Inicial)^(1/n) - 1),
    onde n é o número de anos. É um indicador de crescimento operacional que reflete a capacidade
    da empresa de aumentar sua lucratividade antes de encargos financeiros. Um crescimento alto
    sugere sucesso operacional, enquanto um valor baixo ou negativo indica dificuldades.
    '''
    agrupador = 'Crescimento'
    formula = 'Crescimento EBITDA = ((EBITDA Final / EBITDA Inicial)^(1/n) - 1)'

    try:
        if crescimento_ebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Crescimento EBITDA < 0%',
                'descricao': '''
                Um Crescimento do EBITDA negativo indica redução da lucratividade operacional, sugerindo
                dificuldades em gerar receita ou controlar custos. Isso é comum em empresas em crise,
                como a Oi (OIBR3). Para investidores, essa faixa é um alerta de risco elevado, exigindo
                análise das causas da queda.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= crescimento_ebitda <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Crescimento EBITDA <= 5%',
                'descricao': '''
                Um Crescimento do EBITDA entre 0% e 5% reflete crescimento baixo ou estagnação, indicando
                que a empresa tem dificuldade em expandir sua lucratividade operacional. Isso é comum
                em setores maduros, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores,
                essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < crescimento_ebitda <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < Crescimento EBITDA <= 15%',
                'descricao': '''
                Um Crescimento do EBITDA entre 5% e 15% indica crescimento aceitável, típico de empresas
                com estabilidade operacional. No Brasil, empresas como a Suzano (SUZB3) frequentemente
                operam nessa faixa. Para investidores, essa faixa sugere equilíbrio entre crescimento e
                segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < crescimento_ebitda <= 25:
            return {
                'classificacao': 'Ótimo',
                'faixa': '15% < Crescimento EBITDA <= 25%',
                'descricao': '''
                Um Crescimento do EBITDA entre 15% e 25% reflete crescimento robusto, indicando que a
                empresa está expandindo sua lucratividade operacional de forma significativa. Empresas
                como a Magazine Luiza (MGLU3) podem apresentar crescimento nessa faixa em períodos de
                expansão. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif crescimento_ebitda > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Crescimento EBITDA > 25%',
                'descricao': '''
                Um Crescimento do EBITDA acima de 25% é excepcional, indicando aumento extremamente rápido
                da lucratividade operacional. Isso pode ocorrer em empresas como o Nubank (NUBR33) em
                períodos de forte crescimento. Para investidores, essa faixa é altamente atrativa, mas
                exige cautela, pois crescimentos tão altos podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Crescimento do EBITDA: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se o EBITDA inicial for zero,
            o que impede o cálculo. Verifique os dados de entrada, assegurando que os EBITDAs
            inicial e final estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_7.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: Margem EBITDA, P/EBITDA, Liquidez Imediata, Crescimento da Receita.
"""


def evaluate_margem_ebitda(margem_ebitda):
    '''
    Avalia a Margem EBITDA com base em faixas definidas para o mercado brasileiro:
    - Margem EBITDA < 0%: Crítico (lucratividade operacional negativa, risco elevado)
    - 0% ≤ Margem EBITDA ≤ 10%: Ruim (lucratividade operacional baixa)
    - 10% < Margem EBITDA ≤ 20%: Moderado (lucratividade operacional aceitável)
    - 20% < Margem EBITDA ≤ 30%: Ótimo (lucratividade operacional robusta)
    - Margem EBITDA > 30%: Fora da faixa (lucratividade operacional excepcional)
    '''
    definicao = '''
    A Margem EBITDA mede a proporção do lucro antes de juros, impostos, depreciação e amortização
    em relação à receita bruta, calculada como (EBITDA / Receita Bruta). É um indicador de
    rentabilidade operacional que reflete a eficiência da empresa em gerar lucro antes de encargos
    financeiros. Uma margem alta sugere forte desempenho operacional, enquanto uma margem baixa
    indica dificuldades.
    '''
    agrupador = 'Rentabilidade'
    formula = 'Margem EBITDA = EBITDA / Receita Bruta'

    try:
        if margem_ebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Margem EBITDA < 0%',
                'descricao': '''
                Uma Margem EBITDA negativa indica lucratividade operacional negativa, sugerindo que a empresa
                não consegue cobrir custos operacionais com sua receita. Isso é comum em empresas em crise,
                como a Oi (OIBR3). Para investidores, essa faixa é um alerta grave, exigindo análise detalhada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= margem_ebitda <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Margem EBITDA <= 10%',
                'descricao': '''
                Uma Margem EBITDA entre 0% e 10% reflete lucratividade operacional baixa, indicando desafios
                na gestão de custos operacionais. Isso é comum em setores com margens apertadas, como varejo
                (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < margem_ebitda <= 20:
            return {
                'classificacao': 'Moderado',
                'faixa': '10% < Margem EBITDA <= 20%',
                'descricao': '''
                Uma Margem EBITDA entre 10% e 20% indica lucratividade operacional aceitável, típico de
                empresas com eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente
                operam nessa faixa. Para investidores, essa faixa sugere equilíbrio entre rentabilidade e
                competitividade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < margem_ebitda <= 30:
            return {
                'classificacao': 'Ótimo',
                'faixa': '20% < Margem EBITDA <= 30%',
                'descricao': '''
                Uma Margem EBITDA entre 20% e 30% reflete lucratividade operacional robusta, indicando forte
                controle de custos e eficiência. Empresas como a Ambev (ABEV3) frequentemente apresentam
                margem nessa faixa. Para investidores, essa faixa é atrativa, sugerindo solidez operacional.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif margem_ebitda > 30:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Margem EBITDA > 30%',
                'descricao': '''
                Uma Margem EBITDA acima de 30% é excepcional, indicando altíssima eficiência operacional.
                Isso pode ocorrer em empresas como a Weg (WEGE3). Para investidores, essa faixa é altamente
                atrativa, mas exige cautela, pois margens tão altas podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Margem EBITDA: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se a receita bruta for zero, o que impede o cálculo.
            Verifique os dados de entrada, assegurando que o EBITDA e a receita bruta estejam corretos
            e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_p_ebitda(p_ebitda):
    '''
    Avalia o Preço/EBITDA com base em faixas definidas para o mercado brasileiro:
    - P/EBITDA < 0: Crítico (EBITDA negativo, risco elevado)
    - 0 ≤ P/EBITDA ≤ 4: Ótimo (subvalorizado, oportunidade de compra)
    - 4 < P/EBITDA ≤ 8: Moderado (valuation justo)
    - 8 < P/EBITDA ≤ 12: Ruim (sobrevalorizado, cautela necessária)
    - 12 < P/EBITDA ≤ 16: Péssimo (muito caro, alto risco)
    - P/EBITDA > 16: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    O Preço/EBITDA compara o valor da empresa (valor de mercado + dívida líquida) ao EBITDA,
    calculado como (Enterprise Value / EBITDA). É um indicador de valuation que avalia se a
    empresa está cara ou barata em relação à sua lucratividade operacional. Um P/EBITDA baixo
    sugere subvalorização, enquanto um valor alto indica sobrevalorização.
    '''
    agrupador = 'Valuation'
    formula = 'P/EBITDA = Enterprise Value / EBITDA'

    try:
        if p_ebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/EBITDA < 0',
                'descricao': '''
                Um P/EBITDA negativo indica que a empresa tem EBITDA negativo, sugerindo prejuízo
                operacional. Isso é comum em empresas em crise, como a Oi (OIBR3). Para investidores,
                essa faixa é um alerta grave, exigindo análise detalhada da saúde financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= p_ebitda <= 4:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/EBITDA <= 4',
                'descricao': '''
                Um P/EBITDA entre 0 e 4 sugere que a empresa está subvalorizada, sendo uma potencial
                oportunidade de compra. Isso é comum em setores cíclicos, como a Vale (VALE3) em
                períodos de baixa. Para investidores, essa faixa é atrativa, mas exige verificação
                da sustentabilidade do EBITDA.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 4 < p_ebitda <= 8:
            return {
                'classificacao': 'Moderado',
                'faixa': '4 < P/EBITDA <= 8',
                'descricao': '''
                Um P/EBITDA entre 4 e 8 reflete um valuation justo, típico de empresas com lucratividade
                estável. Empresas como a Ambev (ABEV3) frequentemente operam nessa faixa. Para
                investidores, essa faixa sugere equilíbrio entre preço e fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 8 < p_ebitda <= 12:
            return {
                'classificacao': 'Ruim',
                'faixa': '8 < P/EBITDA <= 12',
                'descricao': '''
                Um P/EBITDA entre 8 e 12 sugere que a empresa está sobrevalorizada, indicando que o
                mercado espera crescimento significativo. Empresas como a Raia Drogasil (RADL3) podem
                atingir essa faixa. Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 12 < p_ebitda <= 16:
            return {
                'classificacao': 'Péssimo',
                'faixa': '12 < P/EBITDA <= 16',
                'descricao': '''
                Um P/EBITDA entre 12 e 16 indica que a empresa é muito cara, sugerindo que o mercado
                está pagando um prêmio elevado. Empresas como a Localiza (RENT3) podem apresentar
                P/EBITDA nessa faixa em momentos de otimismo. Para investidores, essa faixa é de alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif p_ebitda > 16:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/EBITDA > 16',
                'descricao': '''
                Um P/EBITDA acima de 16 é extremamente elevado, geralmente associado a empresas com
                altíssimas expectativas de crescimento, como o Nubank (NUBR33). Para investidores,
                essa faixa reflete especulação e alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o P/EBITDA: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o EBITDA for zero, o que impede o cálculo. Verifique
            os dados de entrada, assegurando que o enterprise value e o EBITDA estejam corretos
            e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_liquidez_imediata(liquidez_imediata):
    '''
    Avalia a Liquidez Imediata com base em faixas definidas para o mercado brasileiro:
    - Liquidez Imediata < 0.2: Crítico (dificuldade extrema em pagar obrigações imediatas)
    - 0.2 ≤ Liquidez Imediata ≤ 0.5: Ruim (capacidade limitada de pagar obrigações imediatas)
    - 0.5 < Liquidez Imediata ≤ 1: Moderado (capacidade aceitável de pagar obrigações imediatas)
    - 1 < Liquidez Imediata ≤ 1.5: Ótimo (boa capacidade de pagar obrigações imediatas)
    - Liquidez Imediata > 1.5: Fora da faixa (excesso de liquidez, possível ineficiência)
    '''
    definicao = '''
    A Liquidez Imediata mede a capacidade da empresa de pagar suas obrigações de curto prazo
    apenas com caixa e equivalentes, calculada como (Caixa e Equivalentes / Passivo Circulante).
    É um indicador de liquidez que reflete a saúde financeira imediata. Um valor alto sugere
    solidez, enquanto um valor baixo indica risco de inadimplência.
    '''
    agrupador = 'Liquidez'
    formula = 'Liquidez Imediata = Caixa e Equivalentes / Passivo Circulante'

    try:
        if liquidez_imediata < 0.2:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Liquidez Imediata < 0.2',
                'descricao': '''
                Uma Liquidez Imediata abaixo de 0.2 indica dificuldade extrema em pagar obrigações de
                curto prazo com caixa disponível, sugerindo risco elevado. Isso é comum em empresas
                em crise, como a Gol (GOLL4). Para investidores, essa faixa é um alerta grave.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 <= liquidez_imediata <= 0.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.2 <= Liquidez Imediata <= 0.5',
                'descricao': '''
                Uma Liquidez Imediata entre 0.2 e 0.5 reflete capacidade limitada de pagar obrigações
                imediatas, indicando dependência de conversão de outros ativos. Isso é comum em setores
                com margens apertadas, como varejo (ex.: Casas Bahia - BHIA3). Para investidores,
                essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 < liquidez_imediata <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < Liquidez Imediata <= 1',
                'descricao': '''
                Uma Liquidez Imediata entre 0.5 e 1 indica capacidade aceitável de pagar obrigações
                imediatas. Empresas como a Suzano (SUZB3) frequentemente operam nessa faixa. Para
                investidores, essa faixa sugere equilíbrio entre liquidez e eficiência.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < liquidez_imediata <= 1.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1 < Liquidez Imediata <= 1.5',
                'descricao': '''
                Uma Liquidez Imediata entre 1 e 1.5 reflete boa capacidade de pagar obrigações imediatas,
                indicando solidez financeira. Empresas como a Ambev (ABEV3) frequentemente apresentam
                liquidez nessa faixa. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif liquidez_imediata > 1.5:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Liquidez Imediata > 1.5',
                'descricao': '''
                Uma Liquidez Imediata acima de 1.5 indica excesso de liquidez, com caixa muito superior
                às obrigações de curto prazo. Isso pode ocorrer em empresas como a Vale (VALE3) em
                períodos de alta geração de caixa. Para investidores, essa faixa pode indicar
                ineficiência na alocação de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Liquidez Imediata: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se o passivo circulante for zero, o que
            impede o cálculo. Verifique os dados de entrada, assegurando que o caixa e o passivo
            circulante estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_crescimento_receita(crescimento_receita):
    '''
    Avalia o Crescimento da Receita com base em faixas definidas para o mercado brasileiro:
    - Crescimento Receita < 0%: Crítico (redução de receita, risco elevado)
    - 0% ≤ Crescimento Receita ≤ 5%: Ruim (crescimento baixo ou estagnação)
    - 5% < Crescimento Receita ≤ 15%: Moderado (crescimento aceitável)
    - 15% < Crescimento Receita ≤ 25%: Ótimo (crescimento robusto)
    - Crescimento Receita > 25%: Fora da faixa (crescimento excepcional)
    '''
    definicao = '''
    O Crescimento da Receita mede a taxa anual de aumento da receita bruta, calculada como
    ((Receita Final / Receita Inicial)^(1/n) - 1), onde n é o número de anos. É um indicador
    de crescimento que reflete a capacidade da empresa de expandir suas vendas. Um crescimento
    alto sugere sucesso comercial, enquanto um valor baixo ou negativo indica dificuldades.
    '''
    agrupador = 'Crescimento'
    formula = 'Crescimento Receita = ((Receita Final / Receita Inicial)^(1/n) - 1)'

    try:
        if crescimento_receita < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Crescimento Receita < 0%',
                'descricao': '''
                Um Crescimento da Receita negativo indica redução nas vendas, sugerindo dificuldades
                comerciais ou de mercado. Isso é comum em empresas em crise, como a Gol (GOLL4).
                Para investidores, essa faixa é um alerta de risco elevado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= crescimento_receita <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Crescimento Receita <= 5%',
                'descricao': '''
                Um Crescimento da Receita entre 0% e 5% reflete crescimento baixo ou estagnação,
                indicando dificuldade em expandir as vendas. Isso é comum em setores maduros, como
                varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco
                moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < crescimento_receita <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < Crescimento Receita <= 15%',
                'descricao': '''
                Um Crescimento da Receita entre 5% e 15% indica crescimento aceitável, típico de
                empresas com estabilidade comercial. Empresas como a Suzano (SUZB3) frequentemente
                operam nessa faixa. Para investidores, essa faixa sugere equilíbrio entre crescimento
                e segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < crescimento_receita <= 25:
            return {
                'classificacao': 'Ótimo',
                'faixa': '15% < Crescimento Receita <= 25%',
                'descricao': '''
                Um Crescimento da Receita entre 15% e 25% reflete crescimento robusto, indicando
                forte expansão das vendas. Empresas como a Magazine Luiza (MGLU3) podem apresentar
                crescimento nessa faixa em períodos de expansão. Para investidores, essa faixa é
                atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif crescimento_receita > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Crescimento Receita > 25%',
                'descricao': '''
                Um Crescimento da Receita acima de 25% é excepcional, indicando aumento extremamente
                rápido das vendas. Isso pode ocorrer em empresas como o Nubank (NUBR33) em períodos
                de forte crescimento. Para investidores, essa faixa é altamente atrativa, mas exige
                cautela, pois crescimentos tão altos podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Crescimento da Receita: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se a receita inicial for zero,
            o que impede o cálculo. Verifique os dados de entrada, assegurando que as receitas
            inicial e final estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_8.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: Margem Operacional, Dívida/Ativo, EV/EBIT, Payout Ratio.
"""


def evaluate_margem_operacional(margem_operacional):
    '''
    Avalia a Margem Operacional com base em faixas definidas para o mercado brasileiro:
    - Margem Operacional < 0%: Crítico (lucratividade operacional negativa, risco elevado)
    - 0% ≤ Margem Operacional ≤ 5%: Ruim (lucratividade operacional baixa)
    - 5% < Margem Operacional ≤ 15%: Moderado (lucratividade operacional aceitável)
    - 15% < Margem Operacional ≤ 25%: Ótimo (lucratividade operacional robusta)
    - Margem Operacional > 25%: Fora da faixa (lucratividade operacional excepcional)
    '''
    definicao = '''
    A Margem Operacional mede a proporção do lucro operacional em relação à receita bruta,
    calculada como (EBIT / Receita Bruta). É um indicador de rentabilidade que reflete a
    eficiência da empresa em gerar lucro a partir de suas operações principais. Uma margem
    alta sugere forte desempenho operacional, enquanto uma margem baixa indica dificuldades.
    '''
    agrupador = 'Rentabilidade'
    formula = 'Margem Operacional = EBIT / Receita Bruta'

    try:
        if margem_operacional < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Margem Operacional < 0%',
                'descricao': '''
                Uma Margem Operacional negativa indica prejuízo operacional, sugerindo que a empresa
                não consegue cobrir custos operacionais com sua receita. Isso é comum em empresas em
                crise, como a Oi (OIBR3). Para investidores, essa faixa é um alerta grave.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= margem_operacional <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Margem Operacional <= 5%',
                'descricao': '''
                Uma Margem Operacional entre 0% e 5% reflete lucratividade operacional baixa,
                indicando desafios na gestão de custos. Isso é comum em setores com margens apertadas,
                como varejo (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco
                moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < margem_operacional <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < Margem Operacional <= 15%',
                'descricao': '''
                Uma Margem Operacional entre 5% e 15% indica lucratividade operacional aceitável,
                típico de empresas com eficiência moderada. No Brasil, empresas como a Suzano (SUZB3)
                frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < margem_operacional <= 25:
            return {
                'classificacao': 'Ótimo',
                'faixa': '15% < Margem Operacional <= 25%',
                'descricao': '''
                Uma Margem Operacional entre 15% e 25% reflete lucratividade operacional robusta,
                indicando forte controle de custos e eficiência. Empresas como a Ambev (ABEV3)
                frequentemente apresentam margem nessa faixa. Para investidores, essa faixa é
                atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif margem_operacional > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Margem Operacional > 25%',
                'descricao': '''
                Uma Margem Operacional acima de 25% é excepcional, indicando altíssima eficiência
                operacional. Isso pode ocorrer em empresas como a Weg (WEGE3). Para investidores,
                essa faixa é altamente atrativa, mas exige cautela, pois margens tão altas podem
                não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Margem Operacional: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se a receita bruta for zero, o que impede
            o cálculo. Verifique os dados de entrada, assegurando que o EBIT e a receita bruta
            estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_divida_ativo(divida_ativo):
    '''
    Avalia a Dívida/Ativo com base em faixas definidas para o mercado brasileiro:
    - Dívida/Ativo < 0: Fora da faixa (sem dívida ou ativo negativo)
    - 0 ≤ Dívida/Ativo ≤ 0.2: Ótimo (endividamento muito baixo)
    - 0.2 < Dívida/Ativo ≤ 0.4: Moderado (endividamento aceitável)
    - 0.4 < Dívida/Ativo ≤ 0.6: Ruim (endividamento elevado)
    - 0.6 < Dívida/Ativo ≤ 0.8: Péssimo (endividamento muito alto)
    - Dívida/Ativo > 0.8: Crítico (endividamento excessivo, risco elevado)
    '''
    definicao = '''
    A Dívida/Ativo mede a proporção da dívida total em relação aos ativos totais, calculada
    como (Dívida Total / Ativos Totais). É um indicador de alavancagem financeira que avalia
    o nível de endividamento em relação aos ativos da empresa. Um valor baixo sugere solidez
    financeira, enquanto um valor alto indica maior risco financeiro.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida/Ativo = Dívida Total / Ativos Totais'

    try:
        if divida_ativo < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida/Ativo < 0',
                'descricao': '''
                Uma Dívida/Ativo negativa indica que a empresa não tem dívida ou que os ativos totais
                são negativos, o que é extremamente raro e alarmante. Para investidores, essa faixa
                exige análise detalhada da estrutura de capital.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_ativo <= 0.2:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida/Ativo <= 0.2',
                'descricao': '''
                Uma Dívida/Ativo entre 0 e 0.2 reflete endividamento muito baixo, indicando solidez
                financeira. Empresas como a Vale (VALE3) em períodos de alta geração de caixa podem
                operar nessa faixa. Para investidores, essa faixa é atrativa, sugerindo baixo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.2 < divida_ativo <= 0.4:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.2 < Dívida/Ativo <= 0.4',
                'descricao': '''
                Uma Dívida/Ativo entre 0.2 e 0.4 indica endividamento aceitável, com equilíbrio entre
                dívida e ativos. Empresas como a Ambev (ABEV3) frequentemente operam nessa faixa.
                Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.4 < divida_ativo <= 0.6:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.4 < Dívida/Ativo <= 0.6',
                'descricao': '''
                Uma Dívida/Ativo entre 0.4 e 0.6 sugere endividamento elevado, indicando dependência
                significativa de dívidas. Isso é comum em setores intensivos em capital, como a
                Petrobras (PETR4). Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.6 < divida_ativo <= 0.8:
            return {
                'classificacao': 'Péssimo',
                'faixa': '0.6 < Dívida/Ativo <= 0.8',
                'descricao': '''
                Uma Dívida/Ativo entre 0.6 e 0.8 reflete endividamento muito alto, indicando risco
                significativo. Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises.
                Para investidores, essa faixa é preocupante.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif divida_ativo > 0.8:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida/Ativo > 0.8',
                'descricao': '''
                Uma Dívida/Ativo acima de 0.8 indica endividamento excessivo, sugerindo dependência
                extrema de dívidas. Isso é típico de empresas em dificuldades, como a Gol (GOLL4)
                em crises. Para investidores, essa faixa é de altíssimo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Dívida/Ativo: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se os ativos totais forem zero, o que
            impede o cálculo. Verifique os dados de entrada, assegurando que a dívida total
            e os ativos totais estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_ev_ebit(ev_ebit):
    '''
    Avalia o Enterprise Value/EBIT com base em faixas definidas para o mercado brasileiro:
    - EV/EBIT < 0: Crítico (EBIT negativo, risco elevado)
    - 0 ≤ EV/EBIT ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
    - 5 < EV/EBIT ≤ 10: Moderado (valuation justo)
    - 10 < EV/EBIT ≤ 15: Ruim (sobrevalorizado, cautela necessária)
    - 15 < EV/EBIT ≤ 20: Péssimo (muito caro, alto risco)
    - EV/EBIT > 20: Fora da faixa (extremamente sobrevalorizado)
    '''
    definicao = '''
    O Enterprise Value/EBIT compara o valor da empresa (valor de mercado + dívida líquida)
    ao lucro operacional antes de juros e impostos, calculado como (Enterprise Value / EBIT).
    É um indicador de valuation que avalia se a empresa está cara ou barata em relação à sua
    lucratividade operacional. Um EV/EBIT baixo sugere subvalorização, enquanto um valor alto
    indica sobrevalorização.
    '''
    agrupador = 'Valuation'
    formula = 'EV/EBIT = Enterprise Value / EBIT'

    try:
        if ev_ebit < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'EV/EBIT < 0',
                'descricao': '''
                Um EV/EBIT negativo indica que a empresa tem EBIT negativo, sugerindo prejuízo
                operacional. Isso é comum em empresas em crise, como a Oi (OIBR3). Para investidores,
                essa faixa é um alerta grave.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= ev_ebit <= 5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= EV/EBIT <= 5',
                'descricao': '''
                Um EV/EBIT entre 0 e 5 sugere que a empresa está subvalorizada, sendo uma potencial
                oportunidade de compra. Isso é comum em setores cíclicos, como a Vale (VALE3) em
                períodos de baixa. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < ev_ebit <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '5 < EV/EBIT <= 10',
                'descricao': '''
                Um EV/EBIT entre 5 e 10 reflete um valuation justo, típico de empresas com
                lucratividade estável. Empresas como a Ambev (ABEV3) frequentemente operam nessa
                faixa. Para investidores, essa faixa sugere equilíbrio entre preço e fundamentos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < ev_ebit <= 15:
            return {
                'classificacao': 'Ruim',
                'faixa': '10 < EV/EBIT <= 15',
                'descricao': '''
                Um EV/EBIT entre 10 e 15 sugere que a empresa está sobrevalorizada, indicando
                que o mercado espera crescimento significativo. Empresas como a Raia Drogasil
                (RADL3) podem atingir essa faixa. Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < ev_ebit <= 20:
            return {
                'classificacao': 'Péssimo',
                'faixa': '15 < EV/EBIT <= 20',
                'descricao': '''
                Um EV/EBIT entre 15 e 20 indica que a empresa é muito cara, sugerindo que o
                mercado está pagando um prêmio elevado. Empresas como a Localiza (RENT3) podem
                apresentar EV/EBIT nessa faixa em momentos de otimismo. Para investidores, essa
                faixa é de alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif ev_ebit > 20:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'EV/EBIT > 20',
                'descricao': '''
                Um EV/EBIT acima de 20 é extremamente elevado, geralmente associado a empresas com
                altíssimas expectativas de crescimento, como o Nubank (NUBR33). Para investidores,
                essa faixa reflete especulação e alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o EV/EBIT: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se o EBIT for zero, o que impede o cálculo. Verifique
            os dados de entrada, assegurando que o enterprise value e o EBIT estejam corretos
            e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_payout_ratio(payout_ratio):
    '''
    Avalia o Payout Ratio com base em faixas definidas para o mercado brasileiro:
    - Payout Ratio < 0%: Fora da faixa (sem dividendos ou prejuízo)
    - 0% ≤ Payout Ratio ≤ 30%: Ruim (baixa distribuição de dividendos)
    - 30% < Payout Ratio ≤ 60%: Moderado (distribuição equilibrada de dividendos)
    - 60% < Payout Ratio ≤ 80%: Ótimo (alta distribuição de dividendos)
    - Payout Ratio > 80%: Crítico (distribuição muito alta, risco de insustentabilidade)
    '''
    definicao = '''
    O Payout Ratio mede a proporção do lucro líquido distribuído como dividendos, calculada
    como (Dividendos / Lucro Líquido). É um indicador que reflete a política de dividendos da
    empresa. Um payout alto é atrativo para investidores focados em renda, mas pode indicar
    risco se for insustentável.
    '''
    agrupador = 'Dividendos'
    formula = 'Payout Ratio = Dividendos / Lucro Líquido'

    try:
        if payout_ratio < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Payout Ratio < 0%',
                'descricao': '''
                Um Payout Ratio negativo ou zero indica que a empresa não paga dividendos, seja por
                prejuízo ou reinvestimento total dos lucros. Isso é comum em empresas em crescimento,
                como o Nubank (NUBR33). Para investidores focados em renda, essa faixa é desvantajosa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= payout_ratio <= 30:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Payout Ratio <= 30%',
                'descricao': '''
                Um Payout Ratio entre 0% e 30% reflete baixa distribuição de dividendos, indicando que
                a empresa prioriza reinvestimento. Isso é comum em empresas como a Magazine Luiza
                (MGLU3). Para investidores focados em renda, essa faixa é pouco atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 30 < payout_ratio <= 60:
            return {
                'classificacao': 'Moderado',
                'faixa': '30% < Payout Ratio <= 60%',
                'descricao': '''
                Um Payout Ratio entre 30% e 60% indica distribuição equilibrada de dividendos, com
                equilíbrio entre distribuição e reinvestimento. Empresas como a Vale (VALE3)
                frequentemente operam nessa faixa. Para investidores, essa faixa é adequada para
                quem busca renda moderada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 60 < payout_ratio <= 80:
            return {
                'classificacao': 'Ótimo',
                'faixa': '60% < Payout Ratio <= 80%',
                'descricao': '''
                Um Payout Ratio entre 60% e 80% reflete alta distribuição de dividendos, indicando
                que a empresa distribui uma parte significativa dos lucros. Empresas como a Engie
                Brasil (EGIE3) frequentemente apresentam payout nessa faixa. Para investidores,
                essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif payout_ratio > 80:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Payout Ratio > 80%',
                'descricao': '''
                Um Payout Ratio acima de 80% indica distribuição muito alta, sugerindo risco de
                insustentabilidade dos dividendos. Empresas como a Taesa (TAEE11) podem apresentar
                payouts elevados, mas isso exige cautela, pois pode comprometer o crescimento.
                Para investidores, a análise deve focar no fluxo de caixa livre.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Payout Ratio: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se o lucro líquido for zero, o que impede
            o cálculo. Verifique os dados de entrada, assegurando que os dividendos e o lucro
            líquido estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_9.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: ROA, CAPEX/Receita, Dívida Bruta/EBITDA, Crescimento da Margem de Lucro Bruto.
"""


def evaluate_roa(roa):
    '''
    Avalia o Retorno sobre Ativos (ROA) com base em faixas definidas para o mercado brasileiro:
    - ROA < 0%: Crítico (prejuízo, destruição de valor)
    - 0% ≤ ROA ≤ 3%: Ruim (retorno baixo, ineficiência)
    - 3% < ROA ≤ 8%: Moderado (retorno aceitável)
    - 8% < ROA ≤ 15%: Ótimo (retorno robusto)
    - ROA > 15%: Fora da faixa (retorno excepcional)
    '''
    definicao = '''
    O Retorno sobre Ativos (ROA) mede a rentabilidade dos ativos totais, calculado como
    (Lucro Líquido / Ativos Totais). É um indicador de eficiência que mostra quanto a empresa
    gera de lucro com seus ativos. Um ROA alto sugere eficiência, enquanto um valor baixo ou
    negativo indica ineficiência ou prejuízo.
    '''
    agrupador = 'Rentabilidade'
    formula = 'ROA = Lucro Líquido / Ativos Totais'

    try:
        if roa < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'ROA < 0%',
                'descricao': '''
                Um ROA negativo indica que a empresa está gerando prejuízo, destruindo valor com
                seus ativos. Isso é comum em empresas em crise, como a Oi (OIBR3). Para investidores,
                essa faixa é um alerta grave, exigindo análise detalhada da gestão de ativos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= roa <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= ROA <= 3%',
                'descricao': '''
                Um ROA entre 0% e 3% reflete retorno baixo, indicando ineficiência no uso dos ativos.
                Isso é comum em setores com margens apertadas, como varejo (ex.: Carrefour Brasil - CRFB3).
                Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < roa <= 8:
            return {
                'classificacao': 'Moderado',
                'faixa': '3% < ROA <= 8%',
                'descricao': '''
                Um ROA entre 3% e 8% indica retorno aceitável, típico de empresas com eficiência
                moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa.
                Para investidores, essa faixa sugere equilíbrio entre rentabilidade e segurança.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 8 < roa <= 15:
            return {
                'classificacao': 'Ótimo',
                'faixa': '8% < ROA <= 15%',
                'descricao': '''
                Um ROA entre 8% e 15% reflete retorno robusto, indicando que a empresa utiliza seus
                ativos de forma eficiente. Empresas como a Ambev (ABEV3) frequentemente apresentam
                ROA nessa faixa. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif roa > 15:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'ROA > 15%',
                'descricao': '''
                Um ROA acima de 15% é excepcional, indicando retornos extremamente altos com os ativos.
                Isso pode ocorrer em empresas como a Weg (WEGE3). Para investidores, essa faixa é
                altamente atrativa, mas exige cautela, pois retornos tão altos podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o ROA: {str(e)}. Isso pode ter acontecido se o valor
            fornecido não for numérico ou se os ativos totais forem zero, o que impede o cálculo.
            Verifique os dados de entrada, assegurando que o lucro líquido e os ativos totais
            estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_capex_receita(capex_receita):
    '''
    Avalia o CAPEX/Receita com base em faixas definidas para o mercado brasileiro:
    - CAPEX/Receita < 5%: Ruim (baixo investimento em ativos fixos)
    - 5% ≤ CAPEX/Receita ≤ 10%: Moderado (investimento equilibrado)
    - 10% < CAPEX/Receita ≤ 20%: Ótimo (investimento robusto)
    - 20% < CAPEX/Receita ≤ 30%: Crítico (investimento elevado, risco de alavancagem)
    - CAPEX/Receita > 30%: Fora da faixa (investimento excessivo, alto risco)
    '''
    definicao = '''
    O CAPEX/Receita mede a proporção dos gastos de capital (CAPEX) em relação à receita bruta,
    calculada como (CAPEX / Receita Bruta). É um indicador de investimento que reflete quanto a
    empresa está investindo em ativos fixos para crescimento futuro. Um valor equilibrado sugere
    planejamento estratégico, enquanto valores muito altos ou baixos podem indicar problemas.t
    '''
    agrupador = 'Investimento'
    formula = 'CAPEX/Receita = CAPEX / Receita Bruta'

    try:
        if capex_receita < 5:
            return {
                'classificacao': 'Ruim',
                'faixa': 'CAPEX/Receita < 5%',
                'descricao': '''
                Um CAPEX/Receita abaixo de 5% indica baixo investimento em ativos fixos, sugerindo
                que a empresa pode estar negligenciando crescimento futuro. Isso é comum em empresas
                maduras com baixa necessidade de expansão, como a Engie Brasil (EGIE3). Para
                investidores, essa faixa pode indicar estagnação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 <= capex_receita <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% <= CAPEX/Receita <= 10%',
                'descricao': '''
                Um CAPEX/Receita entre 5% e 10% reflete investimento equilibrado, indicando que a
                empresa está mantendo ativos sem comprometer a liquidez. Empresas como a Ambev (ABEV3)
                frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < capex_receita <= 20:
            return {
                'classificacao': 'Ótimo',
                'faixa': '10% < CAPEX/Receita <= 20%',
                'descricao': '''
                Um CAPEX/Receita entre 10% e 20% indica investimento robusto, sugerindo que a empresa
                está focada em crescimento futuro sem comprometer a saúde financeira. Empresas como a
                Vale (VALE3) podem apresentar CAPEX nessa faixa em períodos de expansão. Para
                investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < capex_receita <= 30:
            return {
                'classificacao': 'Crítico',
                'faixa': '20% < CAPEX/Receita <= 30%',
                'descricao': '''
                Um CAPEX/Receita entre 20% e 30% reflete investimento elevado, indicando risco de
                alavancagem financeira para sustentar expansões. Isso é comum em setores intensivos
                em capital, como a Petrobras (PETR4). Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif capex_receita > 30:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'CAPEX/Receita > 30%',
                'descricao': '''
                Um CAPEX/Receita acima de 30% indica investimento excessivo, sugerindo que a empresa
                pode estar comprometendo sua saúde financeira. Isso pode ocorrer em empresas como a
                CSN (CSNA3) em grandes projetos. Para investidores, essa faixa é de alto risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o CAPEX/Receita: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se a receita bruta for zero, o que impede
            o cálculo. Verifique os dados de entrada, assegurando que o CAPEX e a receita bruta
            estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_divida_bruta_ebitda(divida_bruta_ebitda):
    '''
    Avalia a Dívida Bruta/EBITDA com base em faixas definidas para o mercado brasileiro:
    - Dívida Bruta/EBITDA < 0: Fora da faixa (sem dívida ou EBITDA negativo)
    - 0 ≤ Dívida Bruta/EBITDA ≤ 1: Ótimo (endividamento muito baixo)
    - 1 < Dívida Bruta/EBITDA ≤ 2: Moderado (endividamento aceitável)
    - 2 < Dívida Bruta/EBITDA ≤ 3: Ruim (endividamento elevado)
    - 3 < Dívida Bruta/EBITDA ≤ 4: Péssimo (endividamento muito alto)
    - Dívida Bruta/EBITDA > 4: Crítico (endividamento excessivo, risco elevado)
    '''
    definicao = '''
    A Dívida Bruta/EBITDA mede a proporção da dívida bruta em relação ao lucro antes de juros,
    impostos, depreciação e amortização, calculada como (Dívida Bruta / EBITDA). É um indicador
    de alavancagem financeira que avalia a capacidade da empresa de pagar sua dívida com base em
    sua geração de caixa operacional. Um valor baixo sugere solidez, enquanto um valor alto indica
    maior risco financeiro.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida Bruta/EBITDA = Dívida Bruta / EBITDA'

    try:
        if divida_bruta_ebitda < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Bruta/EBITDA < 0',
                'descricao': '''
                Uma Dívida Bruta/EBITDA negativa indica que a empresa não tem dívida ou que o EBITDA
                é negativo, o que é alarmante. Empresas como a Oi (OIBR3) podem apresentar EBITDA
                negativo em crises. Para investidores, essa faixa exige análise detalhada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= divida_bruta_ebitda <= 1:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= Dívida Bruta/EBITDA <= 1',
                'descricao': '''
                Uma Dívida Bruta/EBITDA entre 0 e 1 reflete endividamento muito baixo, indicando
                forte capacidade de pagamento da dívida. Empresas como a Vale (VALE3) em períodos
                de alta geração de caixa operam nessa faixa. Para investidores, essa faixa é
                atrativa, sugerindo baixo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < divida_bruta_ebitda <= 2:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Dívida Bruta/EBITDA <= 2',
                'descricao': '''
                Uma Dívida Bruta/EBITDA entre 1 e 2 indica endividamento aceitável, com equilíbrio
                entre dívida e geração de caixa. Empresas como a Ambev (ABEV3) frequentemente operam
                nessa faixa. Para investidores, essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < divida_bruta_ebitda <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '2 < Dívida Bruta/EBITDA <= 3',
                'descricao': '''
                Uma Dívida Bruta/EBITDA entre 2 e 3 sugere endividamento elevado, indicando maior
                dependência de dívidas. Isso é comum em setores intensivos em capital, como a
                Petrobras (PETR4). Para investidores, essa faixa exige cautela.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < divida_bruta_ebitda <= 4:
            return {
                'classificacao': 'Péssimo',
                'faixa': '3 < Dívida Bruta/EBITDA <= 4',
                'descricao': '''
                Uma Dívida Bruta/EBITDA entre 3 e 4 reflete endividamento muito alto, indicando
                risco significativo. Empresas como a Gol (GOLL4) já estiveram nessa faixa durante
                crises. Para investidores, essa faixa é preocupante.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif divida_bruta_ebitda > 4:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dívida Bruta/EBITDA > 4',
                'descricao': '''
                Uma Dívida Bruta/EBITDA acima de 4 indica endividamento excessivo, sugerindo
                dificuldades em pagar dívidas com a geração de caixa. Isso é típico de empresas em
                dificuldades, como a Oi (OIBR3). Para investidores, essa faixa é de altíssimo risco.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar a Dívida Bruta/EBITDA: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se o EBITDA for zero, o que
            impede o cálculo. Verifique os dados de entrada, assegurando que a dívida bruta
            e o EBITDA estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_crescimento_margem_lucro_bruto(crescimento_margem_lucro_bruto):
    '''
    Avalia o Crescimento da Margem de Lucro Bruto com base em faixas definidas para o mercado brasileiro:
    - Crescimento Margem Bruta < 0%: Crítico (redução da margem, risco elevado)
    - 0% ≤ Crescimento Margem Bruta ≤ 2%: Ruim (crescimento baixo ou estagnação)
    - 2% < Crescimento Margem Bruta ≤ 5%: Moderado (crescimento aceitável)
    - 5% < Crescimento Margem Bruta ≤ 10%: Ótimo (crescimento robusto)
    - Crescimento Margem Bruta > 10%: Fora da faixa (crescimento excepcional)
    '''
    definicao = '''
    O Crescimento da Margem de Lucro Bruto mede a taxa anual de aumento da margem de lucro bruto,
    calculada como ((Margem Bruta Final / Margem Bruta Inicial)^(1/n) - 1), onde n é o número
    de anos. É um indicador de eficiência operacional que reflete a capacidade da empresa de
    melhorar a relação entre receita e custo dos bens vendidos. Um crescimento alto sugere
    melhoria na eficiência, enquanto um valor baixo ou negativo indica dificuldades.
    '''
    agrupador = 'Crescimento'
    formula = 'Crescimento Margem Bruta = ((Margem Bruta Final / Margem Bruta Inicial)^(1/n) - 1)'

    try:
        if crescimento_margem_lucro_bruto < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Crescimento Margem Bruta < 0%',
                'descricao': '''
                Um Crescimento da Margem Bruta negativo indica redução na margem de lucro bruto,
                sugerindo aumento nos custos ou queda nos preços de venda. Isso é comum em empresas
                em setores competitivos, como a Casas Bahia (BHIA3). Para investidores, essa faixa
                é um alerta de risco elevado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= crescimento_margem_lucro_bruto <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Crescimento Margem Bruta <= 2%',
                'descricao': '''
                Um Crescimento da Margem Bruta entre 0% e 2% reflete crescimento baixo ou estagnação,
                indicando dificuldade em melhorar a eficiência operacional. Isso é comum em setores
                maduros, como o varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa
                faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < crescimento_margem_lucro_bruto <= 5:
            return {
                'classificacao': 'Moderado',
                'faixa': '2% < Crescimento Margem Bruta <= 5%',
                'descricao': '''
                Um Crescimento da Margem Bruta entre 2% e 5% indica crescimento aceitável, típico
                de empresas com melhorias graduais na eficiência. Empresas como a Suzano (SUZB3)
                frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < crescimento_margem_lucro_bruto <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '5% < Crescimento Margem Bruta <= 10%',
                'descricao': '''
                Um Crescimento da Margem Bruta entre 5% e 10% reflete crescimento robusto, indicando
                forte melhoria na eficiência operacional. Empresas como a Magazine Luiza (MGLU3)
                podem apresentar crescimento nessa faixa em períodos de expansão. Para investidores,
                essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif crescimento_margem_lucro_bruto > 10:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Crescimento Margem Bruta > 10%',
                'descricao': '''
                Um Crescimento da Margem Bruta acima de 10% é excepcional, indicando aumento
                extremamente rápido na eficiência operacional. Isso pode ocorrer em empresas como
                o Nubank (NUBR33) em períodos de forte otimização. Para investidores, essa faixa
                é altamente atrativa, mas exige cautela, pois crescimentos tão altos podem não
                ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Crescimento da Margem Bruta: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se a margem bruta inicial for
            zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que as
            margens brutas inicial e final estejam corretas e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


"""
analisefundamentalista_10.py
Módulo para análise fundamentalista de empresas, com funções que avaliam indicadores financeiros
e retornam classificações, faixas, definições e descrições detalhadas adaptadas ao mercado brasileiro.
Cada função avalia um indicador específico, categorizando-o em faixas como Crítico, Ruim, Moderado,
Ótimo ou Fora da faixa, com exemplos de empresas brasileiras e implicações para investidores.
Indicadores incluídos: Dividend Yield, Free Cash Flow Yield, Giro de Ativos, Crescimento do Lucro Líquido.
"""


def evaluate_dividend_yield(dividend_yield):
    '''
    Avalia o Dividend Yield com base em faixas definidas para o mercado brasileiro:
    - Dividend Yield < 0%: Fora da faixa (sem dividendos)
    - 0% ≤ Dividend Yield ≤ 2%: Ruim (retorno baixo com dividendos)
    - 2% < Dividend Yield ≤ 5%: Moderado (retorno aceitável com dividendos)
    - 5% < Dividend Yield ≤ 8%: Ótimo (retorno robusto com dividendos)
    - Dividend Yield > 8%: Crítico (retorno muito alto, risco de insustentabilidade)
    '''
    definicao = '''
    O Dividend Yield mede o retorno anual dos dividendos em relação ao preço da ação, calculado
    como (Dividendos por Ação / Preço da Ação). É um indicador que reflete a atratividade da
    empresa para investidores focados em renda passiva. Um yield alto é atrativo, mas pode indicar
    risco se for insustentável.
    '''
    agrupador = 'Dividendos'
    formula = 'Dividend Yield = Dividendos por Ação / Preço da Ação'

    try:
        if dividend_yield < 0:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dividend Yield < 0%',
                'descricao': '''
                Um Dividend Yield negativo ou zero indica que a empresa não paga dividendos, seja
                por prejuízo ou reinvestimento total dos lucros. Isso é comum em empresas em
                crescimento, como o Nubank (NUBR33). Para investidores focados em renda, essa faixa
                é desvantajosa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= dividend_yield <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Dividend Yield <= 2%',
                'descricao': '''
                Um Dividend Yield entre 0% e 2% reflete retorno baixo com dividendos, indicando que
                a empresa prioriza reinvestimento. Isso é comum em empresas como a Magazine Luiza
                (MGLU3). Para investidores focados em renda, essa faixa é pouco atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < dividend_yield <= 5:
            return {
                'classificacao': 'Moderado',
                'faixa': '2% < Dividend Yield <= 5%',
                'descricao': '''
                Um Dividend Yield entre 2% e 5% indica retorno aceitável com dividendos, com equilíbrio
                entre distribuição e reinvestimento. Empresas como a Vale (VALE3) frequentemente
                operam nessa faixa. Para investidores, essa faixa é adequada para quem busca renda
                moderada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < dividend_yield <= 8:
            return {
                'classificacao': 'Ótimo',
                'faixa': '5% < Dividend Yield <= 8%',
                'descricao': '''
                Um Dividend Yield entre 5% e 8% reflete retorno robusto com dividendos, indicando
                que a empresa distribui uma parte significativa dos lucros. Empresas como a Engie
                Brasil (EGIE3) frequentemente apresentam yield nessa faixa. Para investidores, essa
                faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif dividend_yield > 8:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dividend Yield > 8%',
                'descricao': '''
                Um Dividend Yield acima de 8% indica retorno muito alto, mas pode sugerir risco de
                insustentabilidade dos dividendos. Empresas como a Taesa (TAEE11) podem apresentar
                yields elevados, mas isso exige cautela, pois pode comprometer o crescimento. Para
                investidores, a análise deve focar no fluxo de caixa livre.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Dividend Yield: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se o preço da ação for zero, o que impede
            o cálculo. Verifique os dados de entrada, assegurando que os dividendos por ação
            e o preço da ação estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_free_cash_flow_yield(free_cash_flow_yield):
    '''
    Avalia o Free Cash Flow Yield com base em faixas definidas para o mercado brasileiro:
    - Free Cash Flow Yield < 0%: Crítico (fluxo de caixa livre negativo, risco elevado)
    - 0% ≤ Free Cash Flow Yield ≤ 3%: Ruim (geração de caixa baixa)
    - 3% < Free Cash Flow Yield ≤ 6%: Moderado (geração de caixa aceitável)
    - 6% < Free Cash Flow Yield ≤ 10%: Ótimo (geração de caixa robusta)
    - Free Cash Flow Yield > 10%: Fora da faixa (geração de caixa excepcional)
    '''
    definicao = '''
    O Free Cash Flow Yield mede o fluxo de caixa livre por ação em relação ao preço da ação,
    calculado como (Fluxo de Caixa Livre por Ação / Preço da Ação). É um indicador que reflete
    a capacidade da empresa de gerar caixa disponível após despesas operacionais e investimentos.
    Um yield alto sugere solidez financeira, enquanto um valor baixo ou negativo indica dificuldades.
    '''
    agrupador = 'Fluxo de Caixa'
    formula = 'Free Cash Flow Yield = Fluxo de Caixa Livre por Ação / Preço da Ação'

    try:
        if free_cash_flow_yield < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Free Cash Flow Yield < 0%',
                'descricao': '''
                Um Free Cash Flow Yield negativo indica que a empresa não gera fluxo de caixa livre,
                sugerindo dificuldades financeiras. Isso é comum em empresas em crise, como a Gol
                (GOLL4). Para investidores, essa faixa é um alerta grave.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= free_cash_flow_yield <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Free Cash Flow Yield <= 3%',
                'descricao': '''
                Um Free Cash Flow Yield entre 0% e 3% reflete geração de caixa baixa, indicando
                desafios na geração de fluxo de caixa livre. Isso é comum em setores com altos
                investimentos, como a Petrobras (PETR4). Para investidores, essa faixa sugere
                risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < free_cash_flow_yield <= 6:
            return {
                'classificacao': 'Moderado',
                'faixa': '3% < Free Cash Flow Yield <= 6%',
                'descricao': '''
                Um Free Cash Flow Yield entre 3% e 6% indica geração de caixa aceitável, típico
                de empresas com eficiência moderada. Empresas como a Suzano (SUZB3) frequentemente
                operam nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 6 < free_cash_flow_yield <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '6% < Free Cash Flow Yield <= 10%',
                'descricao': '''
                Um Free Cash Flow Yield entre 6% e 10% reflete geração de caixa robusta, indicando
                forte saúde financeira. Empresas como a Ambev (ABEV3) frequentemente apresentam
                yield nessa faixa. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif free_cash_flow_yield > 10:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Free Cash Flow Yield > 10%',
                'descricao': '''
                Um Free Cash Flow Yield acima de 10% é excepcional, indicando geração de caixa
                extremamente alta. Isso pode ocorrer em empresas como a Vale (VALE3) em períodos
                de alta lucratividade. Para investidores, essa faixa é altamente atrativa, mas
                exige cautela, pois yields tão altos podem não ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Free Cash Flow Yield: {str(e)}. Isso pode ter
            acontecido se o valor fornecido não for numérico ou se o preço da ação for zero,
            o que impede o cálculo. Verifique os dados de entrada, assegurando que o fluxo
            de caixa livre por ação e o preço da ação estejam corretos e sejam valores
            numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_giro_ativos(giro_ativos):
    '''
    Avalia o Giro de Ativos com base em faixas definidas para o mercado brasileiro:
    - Giro de Ativos < 0.3: Crítico (baixa eficiência no uso de ativos)
    - 0.3 ≤ Giro de Ativos ≤ 0.6: Ruim (eficiência baixa)
    - 0.6 < Giro de Ativos ≤ 1: Moderado (eficiência aceitável)
    - 1 < Giro de Ativos ≤ 1.5: Ótimo (eficiência robusta)
    - Giro de Ativos > 1.5: Fora da faixa (eficiência excepcional)
    '''
    definicao = '''
    O Giro de Ativos mede a eficiência com que a empresa utiliza seus ativos para gerar receita,
    calculado como (Receita Bruta / Ativos Totais). É um indicador de eficiência operacional
    que reflete a capacidade da empresa de maximizar o uso de seus ativos. Um giro alto sugere
    eficiência, enquanto um giro baixo indica subutilização.
    '''
    agrupador = 'Eficiência'
    formula = 'Giro de Ativos = Receita Bruta / Ativos Totais'

    try:
        if giro_ativos < 0.3:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Giro de Ativos < 0.3',
                'descricao': '''
                Um Giro de Ativos abaixo de 0.3 indica baixa eficiência no uso dos ativos, sugerindo
                subutilização ou ativos ociosos. Isso é comum em empresas em crise, como a Oi (OIBR3).
                Para investidores, essa faixa é um alerta grave.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.3 <= giro_ativos <= 0.6:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.3 <= Giro de Ativos <= 0.6',
                'descricao': '''
                Um Giro de Ativos entre 0.3 e 0.6 reflete eficiência baixa, indicando que a empresa
                tem dificuldade em gerar receita com seus ativos. Isso é comum em setores intensivos
                em capital, como a Petrobras (PETR4). Para investidores, essa faixa sugere risco
                moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.6 < giro_ativos <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.6 < Giro de Ativos <= 1',
                'descricao': '''
                Um Giro de Ativos entre 0.6 e 1 indica eficiência aceitável, típico de empresas com
                utilização moderada de ativos. Empresas como a Suzano (SUZB3) frequentemente operam
                nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < giro_ativos <= 1.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '1 < Giro de Ativos <= 1.5',
                'descricao': '''
                Um Giro de Ativos entre 1 e 1.5 reflete eficiência robusta, indicando que a empresa
                utiliza seus ativos de forma eficaz. Empresas como a Ambev (ABEV3) frequentemente
                apresentam giro nessa faixa. Para investidores, essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif giro_ativos > 1.5:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Giro de Ativos > 1.5',
                'descricao': '''
                Um Giro de Ativos acima de 1.5 é excepcional, indicando eficiência extremamente alta
                no uso dos ativos. Isso pode ocorrer em empresas como a Magazine Luiza (MGLU3) em
                períodos de alta rotatividade. Para investidores, essa faixa é altamente atrativa,
                mas exige análise da sustentabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Giro de Ativos: {str(e)}. Isso pode ter acontecido
            se o valor fornecido não for numérico ou se os ativos totais forem zero, o que
            impede o cálculo. Verifique os dados de entrada, assegurando que a receita bruta
            e os ativos totais estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_crescimento_lucro_liquido(crescimento_lucro_liquido):
    '''
    Avalia o Crescimento do Lucro Líquido com base em faixas definidas para o mercado brasileiro:
    - Crescimento Lucro Líquido < 0%: Crítico (redução do lucro, risco elevado)
    - 0% ≤ Crescimento Lucro Líquido ≤ 5%: Ruim (crescimento baixo ou estagnação)
    - 5% < Crescimento Lucro Líquido ≤ 15%: Moderado (crescimento aceitável)
    - 15% < Crescimento Lucro Líquido ≤ 25%: Ótimo (crescimento robusto)
    - Crescimento Lucro Líquido > 25%: Fora da faixa (crescimento excepcional)
    '''
    definicao = '''
    O Crescimento do Lucro Líquido mede a taxa anual de aumento do lucro líquido, calculada
    como ((Lucro Líquido Final / Lucro Líquido Inicial)^(1/n) - 1), onde n é o número de anos.
    É um indicador de crescimento que reflete a capacidade da empresa de aumentar sua
    lucratividade final. Um crescimento alto sugere sucesso financeiro, enquanto um valor baixo
    ou negativo indica dificuldades.
    '''
    agrupador = 'Crescimento'
    formula = 'Crescimento Lucro Líquido = ((Lucro Líquido Final / Lucro Líquido Inicial)^(1/n) - 1)'

    try:
        if crescimento_lucro_liquido < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Crescimento Lucro Líquido < 0%',
                'descricao': '''
                Um Crescimento do Lucro Líquido negativo indica redução nos lucros, sugerindo
                dificuldades financeiras ou operacionais. Isso é comum em empresas em crise, como
                a Gol (GOLL4). Para investidores, essa faixa é um alerta de risco elevado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= crescimento_lucro_liquido <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0% <= Crescimento Lucro Líquido <= 5%',
                'descricao': '''
                Um Crescimento do Lucro Líquido entre 0% e 5% reflete crescimento baixo ou
                estagnação, indicando dificuldade em expandir a lucratividade. Isso é comum em
                setores maduros, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores,
                essa faixa sugere risco moderado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < crescimento_lucro_liquido <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '5% < Crescimento Lucro Líquido <= 15%',
                'descricao': '''
                Um Crescimento do Lucro Líquido entre 5% e 15% indica crescimento aceitável,
                típico de empresas com estabilidade financeira. Empresas como a Suzano (SUZB3)
                frequentemente operam nessa faixa. Para investidores, essa faixa sugere equilíbrio.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < crescimento_lucro_liquido <= 25:
            return {
                'classificacao': 'Ótimo',
                'faixa': '15% < Crescimento Lucro Líquido <= 25%',
                'descricao': '''
                Um Crescimento do Lucro Líquido entre 15% e 25% reflete crescimento robusto,
                indicando forte expansão da lucratividade. Empresas como a Magazine Luiza (MGLU3)
                podem apresentar crescimento nessa faixa em períodos de expansão. Para investidores,
                essa faixa é atrativa.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif crescimento_lucro_liquido > 25:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Crescimento Lucro Líquido > 25%',
                'descricao': '''
                Um Crescimento do Lucro Líquido acima de 25% é excepcional, indicando aumento
                extremamente rápido da lucratividade. Isso pode ocorrer em empresas como o Nubank
                (NUBR33) em períodos de forte crescimento. Para investidores, essa faixa é
                altamente atrativa, mas exige cautela, pois crescimentos tão altos podem não
                ser sustentáveis.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
            Ocorreu um erro ao processar o Crescimento do Lucro Líquido: {str(e)}. Isso pode
            ter acontecido se o valor fornecido não for numérico ou se o lucro líquido inicial
            for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que
            os lucros líquidos inicial e final estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }
