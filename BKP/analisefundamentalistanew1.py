def evaluate_pl(PL):
    '''
    Avalia o Preço/Lucro (P/L) com base em faixas definidas para o mercado brasileiro:
    - P/L < 0: Crítico (prejuízo, risco elevado)
    - 0 ≤ P/L ≤ 10: Ótimo (subvalorizado, oportunidade de compra)
    - 10 < P/L ≤ 15: Moderado (valuation justo, crescimento moderado)
    - 15 < P/L ≤ 20: Ruim (sobrevalorizado, cautela necessária)
    - 20 < P/L ≤ 30: Péssimo (muito caro, alto risco)
    - P/L > 30: Fora da faixa (extremamente sobrevalorizado, risco elevado)
    '''
    definicao = '''
    O Preço/Lucro (P/L) é um dos indicadores mais amplamente utilizados na análise fundamentalista de ações. Ele é calculado dividindo o preço atual da ação pelo lucro por ação (LPA) dos últimos 12 meses, refletindo quantos anos seriam necessários para recuperar o investimento inicial com base nos lucros atuais, assumindo que eles permaneçam constantes. Esse indicador é essencial para avaliar se uma ação está cara ou barata em relação aos seus lucros, mas sua interpretação exige cautela. Fatores como expectativas de crescimento futuro, risco setorial, política de dividendos e estrutura de capital da empresa podem influenciar significativamente o P/L. Por exemplo, empresas em setores de alto crescimento, como tecnologia, frequentemente apresentam P/L mais alto devido às expectativas de lucros futuros, enquanto setores maduros, como utilities, tendem a ter P/L mais baixo por causa da estabilidade de seus ganhos.
    '''
    agrupador = 'Valuation'
    formula = 'P/L = Preço da Ação / Lucro por Ação'

    try:
        if PL < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/L < 0',
                'descricao': '''
                Um P/L negativo ocorre quando a empresa registra prejuízo, ou seja, seu lucro líquido é negativo. Isso pode ser um sinal de alerta para investidores, pois indica que a empresa não está gerando retorno positivo em suas operações no período analisado. Esse cenário é comum em setores cíclicos, como mineração ou celulose, durante quedas de preço das commodities, ou em empresas em reestruturação financeira. Por exemplo, a Oi (OIBR3) já apresentou P/L negativo em períodos de crise, refletindo dificuldades operacionais e alto endividamento. Para avaliar uma empresa nessa faixa, é fundamental analisar outros indicadores, como o EBITDA (para verificar a geração de caixa operacional), o fluxo de caixa livre e a dívida líquida, a fim de entender se o prejuízo é temporário ou estrutural. Startups ou empresas em fase de expansão também podem ter P/L negativo devido a investimentos pesados, mas nesse caso o foco deve estar no potencial de crescimento futuro e na capacidade de atingir lucratividade. Investidores conservadores geralmente evitam empresas nessa faixa devido ao elevado risco, enquanto investidores de valor podem enxergar oportunidades se houver sinais claros de recuperação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= PL <= 10:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/L <= 10',
                'descricao': '''
                Um P/L entre 0 e 10 geralmente indica que a ação está subvalorizada em relação aos lucros atuais da empresa, o que pode representar uma oportunidade de compra para investidores. Isso ocorre com frequência em setores maduros e estáveis, como bancos, utilities ou varejo tradicional, onde o crescimento é limitado, mas os lucros são consistentes. Por exemplo, o Banco do Brasil (BBAS3) já exibiu P/L baixo em períodos de alta taxa de juros, quando o mercado subestima seu potencial de geração de receita. Essa faixa também pode surgir em empresas enfrentando desafios temporários, como aumento de custos ou queda nas vendas, mas que mantêm fundamentos sólidos. Para confirmar se é realmente uma boa oportunidade, é necessário verificar a sustentabilidade dos lucros, a qualidade da gestão e o posicionamento competitivo da empresa no mercado. Um P/L baixo isoladamente não garante um bom investimento, pois pode refletir pessimismo justificado do mercado em relação ao futuro da companhia. Assim, a análise deve ser complementada com indicadores como margem líquida, retorno sobre o patrimônio líquido (ROE) e perspectivas setoriais.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < PL <= 15:
            return {
                'classificacao': 'Moderado',
                'faixa': '10 < P/L <= 15',
                'descricao': '''
                Um P/L entre 10 e 15 é considerado uma zona de valuation justo, onde o preço da ação reflete um equilíbrio razoável entre os lucros atuais e as expectativas de crescimento moderado. Empresas nessa faixa geralmente pertencem a setores com estabilidade e potencial de expansão controlada, como consumo básico ou energia. Um exemplo seria a Ambev (ABEV3), que historicamente opera com P/L nessa faixa devido à sua posição dominante no mercado de bebidas e à previsibilidade de seus resultados. Para investidores, esse nível sugere que a ação não está excessivamente cara nem subvalorizada, mas ainda requer análise detalhada. Fatores como consistência nos lucros, política de dividendos e riscos macroeconômicos (como inflação ou taxa de juros) devem ser considerados. Um P/L nessa faixa pode ser atrativo para quem busca um meio-termo entre segurança e retorno, mas não elimina a necessidade de avaliar se o preço já incorpora todo o potencial de upside da empresa no curto e médio prazo.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < PL <= 20:
            return {
                'classificacao': 'Ruim',
                'faixa': '15 < P/L <= 20',
                'descricao': '''
                Um P/L entre 15 e 20 sugere que a ação está começando a entrar em um território de sobrevalorização, onde o preço pago excede significativamente os lucros atuais da empresa. Isso pode ocorrer em setores com expectativas de crescimento acima da média, como varejo online ou tecnologia, ou em empresas específicas que o mercado acredita terem um futuro promissor. Um exemplo seria a Magazine Luiza (MGLU3) em períodos de otimismo com o e-commerce, quando seu P/L refletia apostas em expansão futura mais do que lucros presentes. Para investidores, essa faixa exige cautela, pois o preço elevado aumenta o risco de correção caso as expectativas não se concretizem. É importante analisar se o crescimento projetado justifica o P/L, examinando indicadores como taxa de crescimento anual composta (CAGR) dos lucros, investimentos em inovação e condições de mercado. Se a empresa não entregar resultados consistentes com essas expectativas, o investimento pode se tornar menos atrativo, especialmente em cenários de alta volatilidade ou aumento nas taxas de juros.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 20 < PL <= 30:
            return {
                'classificacao': 'Péssimo',
                'faixa': '20 < P/L <= 30',
                'descricao': '''
                Um P/L entre 20 e 30 indica que a ação está muito cara em relação aos lucros atuais, sugerindo um nível elevado de otimismo ou especulação por parte do mercado. Esse patamar é típico de empresas em setores de alto crescimento ou em momentos de hype, como tecnologia ou saúde durante avanços disruptivos. Por exemplo, empresas como a Weg (WEGE3) podem atingir essa faixa em picos de valorização devido à sua reputação de inovação e eficiência, mas isso também reflete expectativas irreais ou insustentáveis de crescimento. Para investidores, essa classificação representa um risco considerável, pois qualquer decepção nos resultados financeiros ou mudanças no cenário econômico (como aumento de juros ou recessão) pode levar a quedas significativas no preço da ação. É crucial avaliar se os fundamentos da empresa – como margens de lucro, barreiras de entrada no mercado e capacidade de execução – suportam o valuation elevado. Investidores de longo prazo devem pesar cuidadosamente o potencial de upside contra a possibilidade de perdas expressivas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif PL > 30:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/L > 30',
                'descricao': '''
                Um P/L acima de 30 é um indicativo de extrema sobrevalorização, onde o preço da ação está completamente desalinhado dos lucros atuais, refletindo especulação intensa ou expectativas de crescimento excepcionalmente altas. Esse nível é comum em empresas de tecnologia em estágios iniciais ou em bolhas de mercado, como ocorreu com algumas ações de e-commerce durante a pandemia. Um exemplo hipotético seria uma empresa como a Nubank (NUBR33) sendo avaliada com P/L elevado devido ao entusiasmo com sua expansão no setor financeiro digital. Para investidores, essa faixa representa um risco altíssimo, pois depende quase inteiramente de projeções futuras que podem não se materializar. A análise deve focar em fatores como inovação disruptiva, liderança de mercado e capacidade de escalar lucros rapidamente. No entanto, mesmo com fundamentos sólidos, o preço elevado deixa pouco espaço para erros, tornando a ação vulnerável a correções bruscas em resposta a resultados abaixo do esperado ou mudanças no humor do mercado. Investidores agressivos podem se interessar, mas a maioria deve evitar essa faixa a menos que haja uma tese de investimento muito robusta.
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
            Ocorreu um erro ao processar o P/L: {str(e)}. Isso pode ter acontecido devido a um valor inválido fornecido (como texto em vez de número) ou a um lucro por ação igual a zero, o que tornaria o cálculo impossível. Verifique os dados de entrada e tente novamente. Certifique-se de que o preço da ação e o lucro por ação estejam corretamente informados e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_pebitda(pebitda):
    '''
    Avalia o Preço/EBITDA com base em faixas definidas para o mercado brasileiro:
    - P/EBITDA < 0: Crítico (EBITDA negativo, risco elevado)
    - 0 ≤ P/EBITDA ≤ 4: Ótimo (subvalorizado, oportunidade de compra)
    - 4 < P/EBITDA ≤ 7: Moderado (valuation justo, crescimento moderado)
    - 7 < P/EBITDA ≤ 10: Ruim (sobrevalorizado, cautela necessária)
    - 10 < P/EBITDA ≤ 15: Péssimo (muito caro, alto risco)
    - P/EBITDA > 15: Fora da faixa (extremamente sobrevalorizado, risco elevado)
    '''
    definicao = '''
    O Preço/EBITDA é um indicador de valuation que compara o preço da ação ao EBITDA (Lucro Antes de Juros, Impostos, Depreciação e Amortização) por ação. Ele mede a capacidade da empresa de gerar caixa operacional em relação ao seu valor de mercado, sendo especialmente útil para comparar empresas de diferentes setores ou com estruturas de capital distintas, pois exclui os efeitos de financiamentos e políticas contábeis. Um P/EBITDA baixo pode indicar subvalorização, enquanto um valor alto sugere que a ação está cara. No entanto, como o EBITDA não considera investimentos em capital ou depreciação, ele deve ser usado em conjunto com outros indicadores, como fluxo de caixa livre e margens operacionais, para uma análise mais completa.
    '''
    agrupador = 'Valuation'
    formula = 'P/EBITDA = Preço da Ação / EBITDA por Ação'

    try:
        if pebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/EBITDA < 0',
                'descricao': '''
                Um P/EBITDA negativo indica que a empresa possui EBITDA negativo, o que significa que ela não está gerando caixa suficiente em suas operações para cobrir custos operacionais, antes mesmo de considerar despesas financeiras ou impostos. Isso pode ser um sinal de ineficiência grave ou de um modelo de negócios insustentável. Setores cíclicos, como siderurgia ou mineração, podem apresentar EBITDA negativo durante crises de preços de commodities, como visto na Gerdau (GGBR4) em períodos de baixa demanda global. Para empresas nessa faixa, é crucial analisar a estrutura de custos, a capacidade de reverter o cenário (por exemplo, através de cortes de despesas ou reestruturação) e o nível de endividamento, pois a falta de geração de caixa pode levar a dificuldades financeiras severas. Investidores devem ter extrema cautela, pois o risco de insolvência ou reestruturação de dívidas é elevado.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= pebitda <= 4:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/EBITDA <= 4',
                'descricao': '''
                Um P/EBITDA entre 0 e 4 é considerado baixo, sugerindo que a ação está subvalorizada em relação à sua capacidade de gerar caixa operacional. Isso é comum em empresas de setores maduros ou com margens temporariamente pressionadas, como utilities ou indústrias pesadas. Por exemplo, a Copel (CPLE6), uma empresa de energia, pode apresentar P/EBITDA baixo em momentos de alta regulação ou baixos investimentos em infraestrutura. Para investidores, essa faixa pode representar uma oportunidade de compra, especialmente se houver perspectivas de melhora nas margens ou de crescimento futuro. No entanto, é importante verificar se o baixo valuation não está associado a problemas estruturais, como obsolescência tecnológica ou alta concorrência. Análises complementares de fluxo de caixa livre e endividamento são recomendadas para confirmar a atratividade do investimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 4 < pebitda <= 7:
            return {
                'classificacao': 'Moderado',
                'faixa': '4 < P/EBITDA <= 7',
                'descricao': '''
                Um P/EBITDA entre 4 e 7 reflete um valuation justo, típico de empresas com geração de caixa estável e crescimento moderado. No Brasil, empresas como a Engie Brasil (EGIE3) frequentemente operam nessa faixa, devido à consistência de suas operações no setor de energia. Para investidores, essa faixa indica um equilíbrio entre preço e fundamentos, sendo adequada para quem busca retornos consistentes sem exposição a grandes riscos de sobrevalorização. Ainda assim, é necessário avaliar se o P/EBITDA está alinhado ao ciclo econômico e às perspectivas do setor, complementando a análise com indicadores como margem EBITDA e retorno sobre ativos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 7 < pebitda <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '7 < P/EBITDA <= 10',
                'descricao': '''
                Um P/EBITDA entre 7 e 10 sugere que a ação está sobrevalorizada em relação ao caixa operacional gerado, indicando expectativas de crescimento ou otimismo do mercado. Empresas como a Localiza (RENT3) podem atingir essa faixa em períodos de alta demanda por aluguel de veículos e expansão de frota. Para investidores, essa faixa exige cautela, pois o preço elevado pode não se sustentar se a geração de caixa não acompanhar as expectativas. Riscos incluem aumento da concorrência ou custos operacionais, que podem erodir as margens. Análise de tendências setoriais e comparação com peers são recomendadas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < pebitda <= 15:
            return {
                'classificacao': 'Péssimo',
                'faixa': '10 < P/EBITDA <= 15',
                'descricao': '''
                Um P/EBITDA entre 10 e 15 indica que a ação é muito cara em relação à geração de caixa operacional, sugerindo que o mercado está pagando um prêmio elevado por expectativas futuras. Empresas como a Totvs (TOTS3) já atingiram essa faixa em momentos de forte valorização, refletindo otimismo sobre sua expansão no setor de tecnologia. Para investidores, essa faixa representa alto risco, pois o preço elevado pode não ser justificado se os resultados futuros não corresponderem às expectativas. É essencial analisar o histórico de crescimento da receita, a escalabilidade do modelo de negócios e o contexto competitivo para avaliar a sustentabilidade desse valuation.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif pebitda > 15:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/EBITDA > 15',
                'descricao': '''
                Um P/EBITDA acima de 15 é extremamente elevado, geralmente associado a empresas com altíssimas expectativas de crescimento ou especulação de mercado. No Brasil, o Nubank (NUBR33) já apresentou P/EBITDA nessa faixa após sua estreia na bolsa, devido ao hype em torno de sua disrupção no setor financeiro. Para investidores, essa faixa é de altíssimo risco, pois o preço reflete mais especulação do que fundamentos atuais, tornando a ação vulnerável a correções bruscas. A análise deve focar em projeções de longo prazo, execução estratégica e comparação com peers globais, mas mesmo assim, é uma escolha apenas para investidores tolerantes a risco elevado.
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
            Ocorreu um erro ao processar o P/EBITDA: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o EBITDA por ação for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o preço da ação e o EBITDA por ação estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_pvp(pvp):
    '''
    Avalia o Preço/Valor Patrimonial (P/VP) com base em faixas definidas para o mercado brasileiro:
    - P/VP < 0: Crítico (patrimônio líquido negativo, risco elevado)
    - 0 ≤ P/VP ≤ 0.8: Ótimo (subvalorizado, oportunidade de compra)
    - 0.8 < P/VP ≤ 1.5: Moderado (valuation justo, crescimento moderado)
    - 1.5 < P/VP ≤ 2.5: Ruim (sobrevalorizado, cautela necessária)
    - 2.5 < P/VP ≤ 4: Péssimo (muito caro, alto risco)
    - P/VP > 4: Fora da faixa (extremamente sobrevalorizado, risco elevado)
    '''
    definicao = '''
    O Preço/Valor Patrimonial (P/VP) compara o preço da ação ao valor patrimonial por ação, que representa o valor contábil dos ativos líquidos da empresa dividido pelo número de ações. É um indicador especialmente útil para avaliar empresas em setores onde o patrimônio líquido é significativo, como bancos, seguradoras e holdings. Um P/VP baixo pode indicar subvalorização, enquanto um valor alto sugere que o mercado está pagando um prêmio pelos ativos intangíveis ou pelo potencial de crescimento da empresa. No entanto, o P/VP deve ser interpretado com cuidado, pois ativos contábeis podem estar desatualizados ou não refletir o valor real de mercado, especialmente em setores intensivos em tecnologia ou marcas.
    '''
    agrupador = 'Valuation'
    formula = 'P/VP = Preço da Ação / Valor Patrimonial por Ação'

    try:
        if pvp < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/VP < 0',
                'descricao': '''
                Um P/VP negativo indica que o patrimônio líquido da empresa é negativo, ou seja, suas dívidas superam o valor de seus ativos. Esse é um sinal grave de problemas financeiros, frequentemente associado a empresas em crise ou em processo de recuperação judicial, como a Oi (OIBR3) em períodos de dificuldades. Para investidores, essa faixa representa um risco extremamente elevado, com alta probabilidade de insolvência. A análise deve focar em planos de reestruturação, geração de caixa operacional e a possibilidade de recuperação do patrimônio. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas se houver uma tese de recuperação muito robusta, apoiada por indicadores como fluxo de caixa livre ou vendas de ativos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= pvp <= 0.8:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/VP <= 0.8',
                'descricao': '''
                Um P/VP entre 0 e 0.8 sugere que a ação está sendo negociada abaixo de seu valor patrimonial, indicando subvalorização. Isso é comum em setores como bancos ou seguradoras durante períodos de pessimismo no mercado, como o Banco do Brasil (BBAS3) em momentos de alta taxa de juros. Para investidores, essa faixa pode representar uma oportunidade de compra, especialmente se a empresa possui ativos de qualidade e boa gestão. No entanto, é importante verificar se o baixo P/VP não reflete problemas como ativos obsoletos ou baixa rentabilidade. Análises complementares, como retorno sobre o patrimônio líquido (ROE) e qualidade dos ativos, são essenciais para confirmar a atratividade do investimento.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.8 < pvp <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.8 < P/VP <= 1.5',
                'descricao': '''
                Um P/VP entre 0.8 e 1.5 reflete um valuation justo, onde o preço da ação está próximo ou ligeiramente acima do valor patrimonial. Empresas como a Suzano (SUZB3), do setor de celulose, frequentemente operam nessa faixa devido à estabilidade de seus ativos e geração de caixa consistente. Para investidores, essa faixa indica um equilíbrio entre preço e fundamentos, sendo adequada para quem busca retornos moderados sem grande exposição a riscos de sobrevalorização. É importante avaliar a qualidade do patrimônio (ex.: ativos intangíveis vs. tangíveis) e a capacidade da empresa de gerar retorno sobre seus ativos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < pvp <= 2.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '1.5 < P/VP <= 2.5',
                'descricao': '''
                Um P/VP entre 1.5 e 2.5 sugere que a ação está sobrevalorizada em relação ao seu patrimônio líquido, indicando que o mercado está pagando um prêmio por ativos intangíveis, como marca ou potencial de crescimento. Empresas como a Lojas Renner (LREN3) podem atingir essa faixa em períodos de otimismo com o varejo. Para investidores, essa faixa exige cautela, pois o preço elevado pode não ser justificado se a empresa não entregar crescimento consistente ou se os ativos forem supervalorizados. Análises de margens, crescimento de receita e contexto setorial são recomendadas para avaliar a sustentabilidade do valuation.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2.5 < pvp <= 4:
            return {
                'classificacao': 'Péssimo',
                'faixa': '2.5 < P/VP <= 4',
                'descricao': '''
                Um P/VP entre 2.5 e 4 indica que a ação é muito cara em relação ao seu patrimônio líquido, sugerindo que o mercado está atribuindo um valor elevado a ativos intangíveis ou expectativas de crescimento futuro. Empresas como a Totvs (TOTS3) podem apresentar P/VP nessa faixa devido à sua liderança em tecnologia e inovação. Para investidores, essa faixa representa alto risco, pois o preço elevado deixa pouco espaço para erros. É essencial analisar a qualidade dos ativos intangíveis (ex.: patentes, software) e o potencial de crescimento para justificar o valuation. Riscos macroeconômicos, como aumento de juros, também podem pressionar o preço da ação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif pvp > 4:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/VP > 4',
                'descricao': '''
                Um P/VP acima de 4 é extremamente elevado, indicando que a ação está sendo negociada a um múltiplo muito alto em relação ao seu patrimônio líquido. Isso é comum em empresas com forte valor de marca ou expectativas de crescimento excepcionais, como a Weg (WEGE3) em períodos de hype no mercado. Para investidores, essa faixa é de altíssimo risco, pois o preço reflete mais especulação do que fundamentos contábeis sólidos. A análise deve focar em fatores como liderança de mercado, inovação disruptiva e capacidade de gerar retorno sobre o capital investido. Mesmo com fundamentos fortes, o valuation elevado torna a ação vulnerável a correções bruscas, especialmente em cenários de volatilidade ou mudanças no humor do mercado.
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
            Ocorreu um erro ao processar o P/VP: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o valor patrimonial por ação for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o preço da ação e o valor patrimonial por ação estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_pebit(pebit):
    '''
    Avalia o Preço/EBIT com base em faixas definidas para o mercado brasileiro:
    - P/EBIT < 0: Crítico (EBIT negativo, risco elevado)
    - 0 ≤ P/EBIT ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
    - 5 < P/EBIT ≤ 10: Moderado (valuation justo, crescimento moderado)
    - 10 < P/EBIT ≤ 15: Ruim (sobrevalorizado, cautela necessária)
    - 15 < P/EBIT ≤ 20: Péssimo (muito caro, alto risco)
    - P/EBIT > 20: Fora da faixa (extremamente sobrevalorizado, risco elevado)
    '''
    definicao = '''
    O Preço/EBIT compara o preço da ação ao EBIT (Lucro Antes de Juros e Impostos) por ação, medindo a capacidade da empresa de gerar lucro operacional em relação ao seu valor de mercado. Diferentemente do P/EBITDA, o P/EBIT considera depreciação e amortização, sendo útil para avaliar a eficiência operacional em setores com altos investimentos em ativos fixos, como indústria ou infraestrutura. Um P/EBIT baixo pode indicar subvalorização, enquanto um valor alto sugere que a ação está cara. A análise deve ser complementada com indicadores como margem operacional e fluxo de caixa para confirmar a saúde financeira da empresa.
    '''
    agrupador = 'Valuation'
    formula = 'P/EBIT = Preço da Ação / EBIT por Ação'

    try:
        if pebit < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'P/EBIT < 0',
                'descricao': '''
                Um P/EBIT negativo indica que a empresa possui EBIT negativo, ou seja, não está gerando lucro operacional antes de juros e impostos. Isso pode refletir ineficiência operacional ou dificuldades setoriais, como visto na Usiminas (USIM5) durante crises no setor siderúrgico. Para investidores, essa faixa é um alerta de risco elevado, pois a empresa pode estar enfrentando problemas estruturais ou cíclicos. A análise deve focar na estrutura de custos, na capacidade de reverter o prejuízo operacional e no nível de endividamento. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar se houver sinais claros de recuperação ou reestruturação.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= pebit <= 5:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= P/EBIT <= 5',
                'descricao': '''
                Um P/EBIT entre 0 e 5 sugere que a ação está subvalorizada em relação ao seu lucro operacional, indicando uma potencial oportunidade de compra. Isso é comum em setores cíclicos durante períodos de baixa, como a Vale (VALE3) em momentos de preços de minério de ferro deprimidos. Para investidores, essa faixa pode ser atrativa, especialmente se a empresa possui fundamentos sólidos e perspectivas de recuperação. No entanto, é importante verificar a sustentabilidade do EBIT e a qualidade dos ativos operacionais. Análises complementares de fluxo de caixa livre e margem operacional são recomendadas para confirmar a oportunidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 5 < pebit <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '5 < P/EBIT <= 10',
                'descricao': '''
                Um P/EBIT entre 5 e 10 reflete um valuation justo, típico de empresas com operações estáveis e crescimento moderado. No Brasil, empresas como a EDP Brasil (ENBR3), do setor elétrico, frequentemente operam nessa faixa devido à consistência de seus lucros operacionais. Para investidores, essa faixa indica um equilíbrio entre preço e fundamentos, sendo adequada para quem busca retornos consistentes sem grande exposição a riscos de sobrevalorização. É importante avaliar a consistência do EBIT e o contexto setorial para garantir que o valuation seja sustentável.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < pebit <= 15:
            return {
                'classificacao': 'Ruim',
                'faixa': '10 < P/EBIT <= 15',
                'descricao': '''
                Um P/EBIT entre 10 e 15 sugere que a ação está sobrevalorizada em relação ao seu lucro operacional, indicando que o mercado espera crescimento significativo. Empresas como a Raia Drogasil (RADL3) podem atingir essa faixa em períodos de expansão agressiva no varejo farmacêutico. Para investidores, essa faixa exige cautela, pois o preço elevado pode não se sustentar se os lucros operacionais não acompanharem as expectativas. Riscos como aumento de custos ou concorrência devem ser monitorados. Análise de tendências setoriais e margens operacionais é recomendada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 15 < pebit <= 20:
            return {
                'classificacao': 'Péssimo',
                'faixa': '15 < P/EBIT <= 20',
                'descricao': '''
                Um P/EBIT entre 15 e 20 indica que a ação é muito cara em relação ao seu lucro operacional, sugerindo que o mercado está pagando um prêmio elevado por expectativas futuras. Empresas como a Localiza (RENT3) podem apresentar P/EBIT nessa faixa em momentos de otimismo com expansão de frota ou novos mercados. Para investidores, essa faixa representa alto risco, pois o preço elevado pode não ser justificado se os resultados operacionais não corresponderem às expectativas. É essencial analisar o histórico de crescimento, a escalabilidade do modelo de negócios e o contexto competitivo.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif pebit > 20:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/EBIT > 20',
                'descricao': '''
                Um P/EBIT acima de 20 é extremamente elevado, geralmente associado a empresas com altíssimas expectativas de crescimento ou especulação de mercado. No Brasil, o Nubank (NUBR33) já apresentou P/EBIT nessa faixa após sua estreia na bolsa, devido ao entusiasmo com sua disrupção no setor financeiro. Para investidores, essa faixa é de altíssimo risco, pois o preço reflete mais especulação do que fundamentos operacionais sólidos. A análise deve focar em projeções de longo prazo, execução estratégica e comparação com peers globais, mas mesmo assim, é uma escolha apenas para investidores tolerantes a risco elevado.
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
            Ocorreu um erro ao processar o P/EBIT: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o EBIT por ação for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o preço da ação e o EBIT por ação estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_divida_liquida_ebitda(dl_ebitda):
    '''
    Avalia a Dívida Líquida/EBITDA com base em faixas definidas:
    - DL/EBITDA < -2: Crítico (caixa excessivo, possível ineficiência)
    - -2 ≤ DL/EBITDA < 0: Ótimo (caixa supera dívida)
    - 0 ≤ DL/EBITDA ≤ 1.5: Moderado (endividamento baixo)
    - 1.5 < DL/EBITDA ≤ 3: Ruim (endividamento moderado)
    - 3 < DL/EBITDA ≤ 4.5: Péssimo (endividamento alto)
    - DL/EBITDA > 4.5: Fora da faixa (endividamento excessivo)
    '''
    definicao = '''
    A Dívida Líquida/EBITDA é um indicador de endividamento que mede quantos anos de EBITDA (Lucro Antes de Juros, Impostos, Depreciação e Amortização) seriam necessários para quitar a dívida líquida da empresa. Ele é amplamente utilizado para avaliar a capacidade de uma empresa de pagar suas obrigações financeiras com base em sua geração de caixa operacional. Um valor baixo indica que a empresa pode quitar sua dívida rapidamente, enquanto um valor alto sugere maior risco financeiro. Esse indicador é particularmente útil para comparar empresas de diferentes tamanhos ou setores, pois normaliza a dívida em relação à capacidade de geração de caixa. No entanto, ele deve ser interpretado com cuidado em empresas com EBITDA volátil ou em setores com alta necessidade de reinvestimento, como telecomunicações ou infraestrutura.
    '''
    agrupador = 'Endividamento'
    formula = 'Dívida Líquida/EBITDA = Dívida Líquida / EBITDA'

    try:
        if dl_ebitda < -2:
            return {
                'classificacao': 'Crítico',
                'faixa': 'DL/EBITDA < -2',
                'descricao': '''
                Um DL/EBITDA abaixo de -2 indica que a empresa possui um nível de caixa e equivalentes muito superior à sua dívida bruta, resultando em uma dívida líquida negativa expressiva. Embora isso possa parecer positivo à primeira vista, um valor tão baixo pode sinalizar ineficiência na alocação de capital, pois a empresa está mantendo recursos ociosos que poderiam ser investidos em crescimento, recompra de ações ou pagamento de dividendos. Empresas de tecnologia, como a Totvs (TOTS3), podem apresentar essa característica em períodos de alta liquidez, especialmente após captações ou vendas de ativos. Para investidores, essa faixa exige uma análise da estratégia de gestão de caixa da empresa: se o excesso de liquidez está sendo usado para aquisições ou inovação, pode ser positivo; caso contrário, pode indicar falta de oportunidades de investimento ou aversão ao risco excessiva. Comparar com o retorno sobre o capital investido (ROIC) pode ajudar a entender se a empresa está utilizando seus recursos de forma eficiente.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif -2 <= dl_ebitda < 0:
            return {
                'classificacao': 'Ótimo',
                'faixa': '-2 <= DL/EBITDA < 0',
                'descricao': '''
                Um DL/EBITDA entre -2 e 0 indica que a empresa possui mais caixa do que dívida, ou seja, sua dívida líquida é negativa, mas não de forma excessiva. Isso sugere uma posição financeira sólida, com a empresa capaz de cobrir suas obrigações financeiras imediatamente, se necessário. Esse cenário é comum em empresas com forte geração de caixa e baixo endividamento, como a Vale (VALE3) em períodos de alta nos preços de minério de ferro. Para investidores, essa faixa é atrativa, pois indica baixo risco financeiro e flexibilidade para investir em crescimento ou retornar capital aos acionistas. No entanto, é importante verificar se a empresa está utilizando seu caixa de forma eficiente, seja em expansões, aquisições ou recompra de ações, para evitar que o excesso de liquidez se torne um peso no balanço. Análises de fluxo de caixa e planos estratégicos da empresa são recomendadas para entender o uso futuro desses recursos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= dl_ebitda <= 1.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0 <= DL/EBITDA <= 1.5',
                'descricao': '''
                Um DL/EBITDA entre 0 e 1.5 reflete um nível de endividamento baixo, indicando que a empresa pode quitar sua dívida líquida em até 1,5 anos com base em sua geração de caixa operacional. Esse é um patamar confortável, comum em empresas com finanças saudáveis, como a Ambev (ABEV3), que mantém um balanço sólido graças à sua forte geração de caixa. Para investidores, essa faixa sugere baixo risco financeiro e boa capacidade de suportar oscilações econômicas ou investimentos sem comprometer a saúde financeira. Ainda assim, é útil analisar a composição da dívida (curto ou longo prazo) e a consistência do EBITDA para garantir que o indicador reflete uma situação sustentável.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1.5 < dl_ebitda <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '1.5 < DL/EBITDA <= 3',
                'descricao': '''
                Um DL/EBITDA entre 1,5 e 3 indica um endividamento moderado, onde a empresa levaria entre 1,5 e 3 anos para quitar sua dívida líquida com o EBITDA atual. Esse nível é aceitável para muitas empresas, mas exige atenção, especialmente em setores sensíveis a juros ou ciclos econômicos. A Petrobras (PETR4), por exemplo, já operou nessa faixa em períodos de recuperação, equilibrando dívida elevada com forte geração de caixa. Para investidores, essa faixa sugere um risco moderado, mas é importante monitorar a tendência da dívida, os custos de financiamento e a volatilidade do EBITDA para evitar surpresas negativas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 3 < dl_ebitda <= 4.5:
            return {
                'classificacao': 'Péssimo',
                'faixa': '3 < DL/EBITDA <= 4.5',
                'descricao': '''
                Um DL/EBITDA entre 3 e 4,5 reflete um endividamento alto, indicando que a empresa levaria entre 3 e 4,5 anos para pagar sua dívida líquida com o EBITDA atual. Esse nível é preocupante, especialmente em cenários de alta de juros ou instabilidade econômica. Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises, evidenciando os desafios de gerenciar dívidas elevadas com geração de caixa limitada. Para investidores, essa faixa representa risco significativo, exigindo análise detalhada da estrutura de capital, covenants de dívida e planos de desalavancagem para avaliar a viabilidade financeira.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif dl_ebitda > 4.5:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'DL/EBITDA > 4.5',
                'descricao': '''
                Um DL/EBITDA acima de 4,5 indica endividamento excessivo, sugerindo que a empresa levaria mais de 4,5 anos para quitar sua dívida líquida com o EBITDA atual. Esse nível é alarmante e típico de empresas em dificuldades financeiras ou em setores com alta alavancagem, como infraestrutura. A Gol (GOLL4), por exemplo, já apresentou DL/EBITDA elevado em períodos de crise no setor aéreo, refletindo os desafios de margens apertadas e dívidas altas. Para investidores, essa faixa é de altíssimo risco, com possibilidade de reestruturação ou insolvência, exigindo análise profunda da capacidade de geração de caixa e estratégias de redução de dívida.
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
            Ocorreu um erro ao processar o DL/EBITDA: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico, se o EBITDA for zero (o que impede a divisão), ou se houver erro nos dados de dívida líquida. Verifique os dados de entrada e certifique-se de que a dívida líquida e o EBITDA estejam corretamente informados e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

def evaluate_evebit(evebit):
        '''
        Avalia o EV/EBIT com base em faixas definidas para o mercado brasileiro:
        - EV/EBIT < 0: Crítico (EBIT negativo, risco elevado)
        - 0 ≤ EV/EBIT ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
        - 5 < EV/EBIT ≤ 10: Moderado (valuation justo, crescimento moderado)
        - 10 < EV/EBIT ≤ 15: Ruim (sobrevalorizado, cautela necessária)
        - 15 < EV/EBIT ≤ 20: Péssimo (muito caro, alto risco)
        - EV/EBIT > 20: Fora da faixa (extremamente sobrevalorizado, risco elevado)
        '''
        definicao = '''
        O EV/EBIT compara o valor da empresa (Enterprise Value, ou valor de mercado + dívida líquida) ao EBIT (Lucro Antes de Juros e Impostos), medindo a capacidade de geração de lucro operacional em relação ao valor total da empresa. É especialmente útil em análises de fusões e aquisições, pois considera a dívida líquida, oferecendo uma visão mais completa do valuation do que o P/EBIT. Um EV/EBIT baixo pode indicar subvalorização, enquanto um valor alto sugere que a empresa está cara. Deve ser usado com cautela em setores com alta depreciação ou necessidade de reinvestimento, como infraestrutura, e complementado com indicadores como fluxo de caixa livre e margem operacional.
        '''
        agrupador = 'Valuation'
        formula = 'EV/EBIT = (Valor de Mercado + Dívida Líquida) / EBIT'

        try:
            if evebit < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'EV/EBIT < 0',
                    'descricao': '''
                    Um EV/EBIT negativo indica que a empresa possui EBIT negativo, ou seja, não está gerando lucro operacional antes de juros e impostos. Isso reflete ineficiência operacional ou dificuldades setoriais, como observado na CSN (CSNA3) durante crises no setor siderúrgico. Para investidores, essa faixa é um alerta de risco elevado, pois pode indicar problemas estruturais ou cíclicos. A análise deve focar na estrutura de custos, na capacidade de reverter o prejuízo operacional e no nível de endividamento, já que o EV inclui a dívida líquida. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de recuperação, apoiada por indicadores como fluxo de caixa livre ou vendas de ativos.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= evebit <= 5:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '0 <= EV/EBIT <= 5',
                    'descricao': '''
                    Um EV/EBIT entre 0 e 5 sugere que a empresa está subvalorizada em relação ao seu lucro operacional, indicando uma potencial oportunidade de compra. Isso é comum em setores cíclicos durante períodos de baixa, como a Vale (VALE3) em momentos de preços de minério de ferro deprimidos. Para investidores, essa faixa é atrativa, especialmente se a empresa possui fundamentos sólidos e perspectivas de recuperação. No entanto, é importante verificar a sustentabilidade do EBIT e a qualidade dos ativos operacionais, considerando que o EV inclui a dívida líquida. Análises complementares de fluxo de caixa livre, margem operacional e endividamento são recomendadas para confirmar a oportunidade.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < evebit <= 10:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '5 < EV/EBIT <= 10',
                    'descricao': '''
                    Um EV/EBIT entre 5 e 10 reflete um valuation justo, típico de empresas com operações estáveis e crescimento moderado. No Brasil, empresas como a EDP Brasil (ENBR3), do setor elétrico, frequentemente operam nessa faixa devido à consistência de seus lucros operacionais. Para investidores, essa faixa indica um equilíbrio entre preço e fundamentos, sendo adequada para quem busca retornos consistentes sem grande exposição a riscos de sobrevalorização. É importante avaliar a consistência do EBIT, a composição da dívida líquida (curto ou longo prazo) e o contexto setorial para garantir que o valuation seja sustentável.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 10 < evebit <= 15:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '10 < EV/EBIT <= 15',
                    'descricao': '''
                    Um EV/EBIT entre 10 e 15 sugere que a empresa está sobrevalorizada em relação ao seu lucro operacional, indicando que o mercado espera crescimento significativo. Empresas como a Raia Drogasil (RADL3) podem atingir essa faixa em períodos de expansão agressiva no varejo farmacêutico. Para investidores, essa faixa exige cautela, pois o preço elevado (que inclui a dívida líquida) pode não se sustentar se os lucros operacionais não acompanharem as expectativas. Riscos como aumento de custos ou concorrência devem ser monitorados. Análise de tendências setoriais, margens operacionais e estrutura de capital é recomendada.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 15 < evebit <= 20:
                return {
                    'classificacao': 'Péssimo',
                    'faixa': '15 < EV/EBIT <= 20',
                    'descricao': '''
                    Um EV/EBIT entre 15 e 20 indica que a empresa é muito cara em relação ao seu lucro operacional, sugerindo que o mercado está pagando um prêmio elevado por expectativas futuras. Empresas como a Localiza (RENT3) podem apresentar EV/EBIT nessa faixa em momentos de otimismo com expansão de frota ou novos mercados. Para investidores, essa faixa representa alto risco, pois o preço elevado (que considera a dívida líquida) pode não ser justificado se os resultados operacionais não corresponderem às expectativas. É essencial analisar o histórico de crescimento, a escalabilidade do modelo de negócios e o contexto competitivo para avaliar a sustentabilidade do valuation.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif evebit > 20:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'EV/EBIT > 20',
                    'descricao': '''
                    Um EV/EBIT acima de 20 é extremamente elevado, geralmente associado a empresas com altíssimas expectativas de crescimento ou especulação de mercado. No Brasil, o Nubank (NUBR33) já apresentou EV/EBIT nessa faixa após sua estreia na bolsa, devido ao entusiasmo com sua disrupção no setor financeiro. Para investidores, essa faixa é de altíssimo risco, pois o preço reflete mais especulação do que fundamentos operacionais sólidos, especialmente considerando a inclusão da dívida líquida no cálculo do EV. A análise deve focar em projeções de longo prazo, execução estratégica e comparação com peers globais, mas mesmo assim, é uma escolha apenas para investidores tolerantes a risco elevado.
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
                Ocorreu um erro ao processar o EV/EBIT: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o EBIT for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o valor da empresa (valor de mercado + dívida líquida) e o EBIT estejam corretos e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_margem_bruta(margem_bruta):
        '''
        Avalia a Margem Bruta com base em faixas definidas para o mercado brasileiro:
        - Margem Bruta < 10%: Crítico (baixa rentabilidade operacional, risco elevado)
        - 10% ≤ Margem Bruta ≤ 20%: Ruim (rentabilidade operacional limitada)
        - 20% < Margem Bruta ≤ 40%: Moderado (rentabilidade operacional aceitável)
        - 40% < Margem Bruta ≤ 60%: Ótimo (alta rentabilidade operacional)
        - Margem Bruta > 60%: Fora da faixa (rentabilidade operacional excepcional, avaliar sustentabilidade)
        '''
        definicao = '''
        A Margem Bruta é um indicador de rentabilidade que mede a porcentagem da receita que resta após a dedução dos custos diretos de produção (como matérias-primas e mão de obra direta). É calculada como (Receita Bruta - Custo dos Produtos Vendidos) / Receita Bruta. Esse indicador reflete a eficiência da empresa em gerenciar seus custos diretos e é especialmente importante em setores com alta concorrência ou margens apertadas, como varejo e indústria. Uma margem bruta alta sugere que a empresa tem poder de precificação ou eficiência na produção, enquanto uma margem baixa pode indicar pressão competitiva ou custos elevados. Deve ser analisada em conjunto com outros indicadores de rentabilidade, como margem líquida e retorno sobre ativos.
        '''
        agrupador = 'Rentabilidade'
        formula = 'Margem Bruta = (Receita Bruta - Custo dos Produtos Vendidos) / Receita Bruta'

        try:
            if margem_bruta < 10:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Margem Bruta < 10%',
                    'descricao': '''
                    Uma Margem Bruta abaixo de 10% indica baixa rentabilidade operacional, sugerindo que a empresa tem dificuldades em cobrir os custos diretos de produção ou enfrenta forte pressão competitiva. Isso é comum em setores com margens apertadas, como varejo de baixa margem (ex.: Casas Bahia - BHIA3 durante crises de consumo). Para investidores, essa faixa é um alerta de risco elevado, pois a empresa pode ter dificuldades em gerar lucro após cobrir outros custos operacionais e financeiros. A análise deve focar na estrutura de custos, estratégias de precificação e posicionamento competitivo. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar se houver sinais de melhoria operacional ou redução de custos.
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
                    Uma Margem Bruta entre 10% e 20% reflete rentabilidade operacional limitada, indicando que a empresa consegue cobrir os custos diretos, mas com pouca folga para despesas operacionais ou investimentos. Isso é comum em setores competitivos, como varejo alimentar (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a aumentos de custos ou oscilações na receita. É importante analisar a capacidade da empresa de melhorar a eficiência operacional ou aumentar preços sem perder mercado. Análises complementares de margem líquida e fluxo de caixa operacional são recomendadas.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 20 < margem_bruta <= 40:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '20% < Margem Bruta <= 40%',
                    'descricao': '''
                    Uma Margem Bruta entre 20% e 40% indica rentabilidade operacional aceitável, típica de empresas com boa gestão de custos e poder de precificação moderado. No Brasil, empresas como a Ambev (ABEV3) frequentemente operam nessa faixa devido à sua eficiência na produção de bebidas. Para investidores, essa faixa sugere um equilíbrio entre rentabilidade e resiliência, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência da margem bruta ao longo do tempo e o contexto setorial para confirmar a sustentabilidade.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 40 < margem_bruta <= 60:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '40% < Margem Bruta <= 60%',
                    'descricao': '''
                    Uma Margem Bruta entre 40% e 60% reflete alta rentabilidade operacional, indicando que a empresa tem forte controle sobre custos diretos e/ou poder de precificação significativo. Empresas como a Weg (WEGE3), com produtos de alto valor agregado, frequentemente apresentam margens nessa faixa. Para investidores, essa faixa é atrativa, pois sugere eficiência operacional e potencial para cobrir despesas adicionais ou investir em crescimento. No entanto, é importante verificar se a margem é sustentável, analisando fatores como concorrência, custos de insumos e tendências de mercado.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif margem_bruta > 60:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Margem Bruta > 60%',
                    'descricao': '''
                    Uma Margem Bruta acima de 60% é excepcional, indicando que a empresa tem um poder de precificação extremamente alto ou custos diretos muito baixos. Isso é raro, mas pode ocorrer em empresas de tecnologia ou com marcas fortes, como a Totvs (TOTS3) em soluções de software. Para investidores, essa faixa é atraente, mas exige cautela, pois margens tão altas podem não ser sustentáveis a longo prazo, especialmente em setores com entrada de novos concorrentes ou mudanças regulatórias. A análise deve focar na escalabilidade do modelo de negócios, barreiras de entrada e consistência histórica da margem.
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
                Ocorreu um erro ao processar a Margem Bruta: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que a receita bruta e o custo dos produtos vendidos estejam corretos e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_margem_liquida(margem_liquida):
        '''
        Avalia a Margem Líquida com base em faixas definidas para o mercado brasileiro:
        - Margem Líquida < 0%: Crítico (prejuízo líquido, risco elevado)
        - 0% ≤ Margem Líquida ≤ 5%: Ruim (rentabilidade líquida baixa)
        - 5% < Margem Líquida ≤ 15%: Moderado (rentabilidade líquida aceitável)
        - 15% < Margem Líquida ≤ 25%: Ótimo (alta rentabilidade líquida)
        - Margem Líquida > 25%: Fora da faixa (rentabilidade líquida excepcional, avaliar sustentabilidade)
        '''
        definicao = '''
        A Margem Líquida mede a porcentagem da receita que resta como lucro líquido após a dedução de todos os custos, despesas, impostos e juros. É calculada como (Lucro Líquido / Receita Bruta). Esse indicador reflete a eficiência geral da empresa em converter receita em lucro, considerando todos os custos operacionais e financeiros. Uma margem líquida alta sugere boa gestão e controle de custos, enquanto uma margem baixa ou negativa pode indicar ineficiência ou pressões externas. É especialmente importante em setores com alta carga tributária ou financeira, como varejo e bancos, e deve ser analisada em conjunto com outros indicadores de rentabilidade, como ROE e margem bruta.
        '''
        agrupador = 'Rentabilidade'
        formula = 'Margem Líquida = Lucro Líquido / Receita Bruta'

        try:
            if margem_liquida < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Margem Líquida < 0%',
                    'descricao': '''
                    Uma Margem Líquida negativa indica que a empresa está operando com prejuízo, ou seja, os custos totais superam a receita. Isso é comum em empresas em crise, como a Oi (OIBR3) durante períodos de reestruturação, ou em setores cíclicos, como aviação (ex.: Gol - GOLL4) em momentos de baixa demanda. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades financeiras graves. A análise deve focar na estrutura de custos, endividamento e estratégias de recuperação. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= margem_liquida <= 5:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0% <= Margem Líquida <= 5%',
                    'descricao': '''
                    Uma Margem Líquida entre 0% e 5% reflete rentabilidade líquida baixa, indicando que a empresa tem pouca capacidade de converter receita em lucro após todos os custos. Isso é comum em setores com margens apertadas, como varejo alimentar (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a aumentos de custos, juros ou impostos. É importante analisar a capacidade de melhorar a eficiência operacional ou reduzir despesas financeiras. Análises complementares de fluxo de caixa e endividamento são recomendadas.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < margem_liquida <= 15:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '5% < Margem Líquida <= 15%',
                    'descricao': '''
                    Uma Margem Líquida entre 5% e 15% indica rentabilidade líquida aceitável, típica de empresas com boa gestão de custos e resiliência financeira. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua eficiência operacional no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência da margem líquida ao longo do tempo e o impacto de fatores externos, como carga tributária e custos financeiros.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 15 < margem_liquida <= 25:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '15% < Margem Líquida <= 25%',
                    'descricao': '''
                    Uma Margem Líquida entre 15% e 25% reflete alta rentabilidade líquida, indicando que a empresa é eficiente em converter receita em lucro após todos os custos. Empresas como a Ambev (ABEV3), com forte controle de custos e poder de precificação, frequentemente apresentam margens nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e potencial para reinvestimento ou pagamento de dividendos. No entanto, é importante verificar a sustentabilidade da margem, analisando fatores como concorrência, custos operacionais e tendências de mercado.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif margem_liquida > 25:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Margem Líquida > 25%',
                    'descricao': '''
                    Uma Margem Líquida acima de 25% é excepcional, indicando que a empresa tem uma capacidade extraordinária de gerar lucro líquido. Isso é raro, mas pode ocorrer em empresas com forte poder de precificação ou baixos custos, como a Weg (WEGE3) em períodos de alta eficiência. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois margens tão altas podem não ser sustentáveis a longo prazo, especialmente em setores com entrada de novos concorrentes ou mudanças regulatórias. A análise deve focar na escalabilidade do modelo de negócios, barreiras de entrada e consistência histórica da margem.
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
                Ocorreu um erro ao processar a Margem Líquida: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o lucro líquido e a receita bruta estejam corretos e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_roe(roe):
        '''
        Avalia o Retorno sobre o Patrimônio Líquido (ROE) com base em faixas definidas para o mercado brasileiro:
        - ROE < 0%: Crítico (prejuízo sobre o patrimônio, risco elevado)
        - 0% ≤ ROE ≤ 10%: Ruim (retorno baixo sobre o patrimônio)
        - 10% < ROE ≤ 20%: Moderado (retorno aceitável sobre o patrimônio)
        - 20% < ROE ≤ 30%: Ótimo (alto retorno sobre o patrimônio)
        - ROE > 30%: Fora da faixa (retorno excepcional, avaliar sustentabilidade)
        '''
        definicao = '''
        O Retorno sobre o Patrimônio Líquido (ROE) mede a rentabilidade da empresa em relação ao patrimônio líquido dos acionistas, calculado como (Lucro Líquido / Patrimônio Líquido). É um indicador chave para avaliar a eficiência com que a empresa utiliza o capital dos acionistas para gerar lucros. Um ROE alto sugere boa gestão e alta rentabilidade, enquanto um ROE baixo ou negativo pode indicar ineficiência ou prejuízo. É especialmente útil em setores como bancos e seguradoras, mas deve ser interpretado com cuidado, pois um ROE alto pode ser impulsionado por alavancagem financeira, aumentando o risco.
        '''
        agrupador = 'Rentabilidade'
        formula = 'ROE = Lucro Líquido / Patrimônio Líquido'

        try:
            if roe < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'ROE < 0%',
                    'descricao': '''
                    Um ROE negativo indica que a empresa está gerando prejuízo em relação ao patrimônio líquido, ou seja, destruindo valor para os acionistas. Isso é comum em empresas em crise, como a Oi (OIBR3) durante períodos de reestruturação, ou em setores cíclicos, como aviação (ex.: Gol - GOLL4) em momentos de baixa demanda. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades financeiras graves. A análise deve focar na estrutura de custos, endividamento e estratégias de recuperação. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= roe <= 10:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0% <= ROE <= 10%',
                    'descricao': '''
                    Um ROE entre 0% e 10% reflete um retorno baixo sobre o patrimônio líquido, indicando que a empresa tem dificuldade em gerar valor significativo para os acionistas. Isso é comum em setores com margens apertadas ou alta concorrência, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a oscilações econômicas ou custos elevados. É importante analisar a eficiência operacional, a alavancagem financeira e o potencial de melhoria do ROE. Análises complementares de margem líquida e fluxo de caixa são recomendadas.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 10 < roe <= 20:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '10% < ROE <= 20%',
                    'descricao': '''
                    Um ROE entre 10% e 20% indica um retorno aceitável sobre o patrimônio líquido, típico de empresas com boa gestão e eficiência operacional moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua solidez financeira no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência do ROE ao longo do tempo e o impacto da alavancagem financeira, que pode inflar o indicador.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 20 < roe <= 30:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '20% < ROE <= 30%',
                    'descricao': '''
                    Um ROE entre 20% e 30% reflete um alto retorno sobre o patrimônio líquido, indicando que a empresa é eficiente em gerar valor para os acionistas. Empresas como a Ambev (ABEV3), com forte controle de custos e liderança de mercado, frequentemente apresentam ROE nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e potencial para reinvestimento ou pagamento de dividendos. No entanto, é importante verificar se o ROE é impulsionado por alavancagem financeira, que pode aumentar o risco. Análises de endividamento e fluxo de caixa são recomendadas.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif roe > 30:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'ROE > 30%',
                    'descricao': '''
                    Um ROE acima de 30% é excepcional, indicando que a empresa gera retornos extraordinários sobre o patrimônio líquido. Isso é raro, mas pode ocorrer em empresas com alta eficiência operacional ou forte alavancagem, como a Weg (WEGE3) em períodos de crescimento robusto. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois um ROE muito alto pode ser impulsionado por dívidas elevadas, aumentando o risco financeiro. A análise deve focar na sustentabilidade do ROE, barreiras de entrada e alavancagem financeira para garantir que o retorno seja consistente a longo prazo.
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
                Ocorreu um erro ao processar o ROE: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o patrimônio líquido for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o lucro líquido e o patrimônio líquido estejam corretos e sejam valores numéricos válidos.
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
        - 1 < Giro de Ativos ≤ 2: Ótimo (alta eficiência no uso de ativos)
        - Giro de Ativos > 2: Fora da faixa (eficiência excepcional, avaliar sustentabilidade)
        '''
        definicao = '''
        O Giro de Ativos mede a eficiência com que a empresa utiliza seus ativos totais para gerar receita, calculado como (Receita Bruta / Ativos Totais). Um giro alto indica que a empresa gera muita receita com poucos ativos, sugerindo eficiência operacional, enquanto um giro baixo pode indicar subutilização de ativos ou ineficiência. É especialmente útil em setores intensivos em capital, como indústria e infraestrutura, mas deve ser interpretado considerando o modelo de negócios da empresa, pois setores com ativos intangíveis (ex.: tecnologia) podem ter giros diferentes de setores com ativos fixos pesados (ex.: mineração).
        '''
        agrupador = 'Eficiência'
        formula = 'Giro de Ativos = Receita Bruta / Ativos Totais'

        try:
            if giro_ativos < 0.2:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Giro de Ativos < 0.2',
                    'descricao': '''
                    Um Giro de Ativos abaixo de 0.2 indica baixa eficiência no uso dos ativos para gerar receita, sugerindo subutilização de recursos ou ineficiência operacional. Isso é comum em empresas com ativos pesados e baixa receita, como a CSN (CSNA3) em períodos de crise no setor siderúrgico. Para investidores, essa faixa é um alerta de risco elevado, pois a empresa pode estar desperdiçando capital ou enfrentando dificuldades operacionais. A análise deve focar na gestão de ativos, estratégias de aumento de receita e potencial de reestruturação. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar com uma tese robusta de melhoria operacional.
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
                    Um Giro de Ativos entre 0.2 e 0.5 reflete eficiência limitada no uso de ativos, indicando que a empresa gera receita moderada em relação ao seu capital investido. Isso é comum em setores com ativos pesados, como infraestrutura (ex.: CCR - CCRO3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode estar subutilizando seus ativos ou enfrentando concorrência. É importante analisar a capacidade de otimizar operações ou desinvestir ativos ociosos. Análises complementares de ROA (Retorno sobre Ativos) e fluxo de caixa operacional são recomendadas.
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
                    Um Giro de Ativos entre 0.5 e 1 indica eficiência aceitável no uso de ativos, típico de empresas com operações equilibradas. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua capacidade de gerar receita com ativos industriais. Para investidores, essa faixa sugere um equilíbrio entre eficiência e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência do giro ao longo do tempo e o contexto setorial para confirmar a sustentabilidade.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 1 < giro_ativos <= 2:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '1 < Giro de Ativos <= 2',
                    'descricao': '''
                    Um Giro de Ativos entre 1 e 2 reflete alta eficiência no uso de ativos, indicando que a empresa gera receita significativa em relação ao seu capital investido. Empresas como a Ambev (ABEV3), com operações enxutas e forte geração de receita, frequentemente apresentam giros nessa faixa. Para investidores, essa faixa é atrativa, pois sugere eficiência operacional e potencial para reinvestimento ou retorno aos acionistas. No entanto, é importante verificar se o giro é sustentável, analisando fatores como concorrência e necessidade de reinvestimento em ativos.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif giro_ativos > 2:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Giro de Ativos > 2',
                    'descricao': '''
                    Um Giro de Ativos acima de 2 é excepcional, indicando que a empresa gera receita muito alta com poucos ativos. Isso é raro, mas pode ocorrer em empresas de tecnologia ou varejo com modelos enxutos, como a Magazine Luiza (MGLU3) em períodos de forte crescimento no e-commerce. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois giros tão altos podem não ser sustentáveis a longo prazo, especialmente em setores com entrada de novos concorrentes. A análise deve focar na escalabilidade do modelo de negócios, barreiras de entrada e consistência histórica do giro.
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
                Ocorreu um erro ao processar o Giro de Ativos: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se os ativos totais forem zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que a receita bruta e os ativos totais estejam corretos e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

        def evaluate_liquidez_corrente(liquidez_corrente):
            '''
            Avalia a Liquidez Corrente com base em faixas definidas para o mercado brasileiro:
            - Liquidez Corrente < 0.5: Crítico (alta dificuldade em pagar obrigações de curto prazo)
            - 0.5 ≤ Liquidez Corrente ≤ 1: Ruim (capacidade limitada de pagar obrigações de curto prazo)
            - 1 < Liquidez Corrente ≤ 1.5: Moderado (capacidade aceitável de pagar obrigações de curto prazo)
            - 1.5 < Liquidez Corrente ≤ 2: Ótimo (boa capacidade de pagar obrigações de curto prazo)
            - Liquidez Corrente > 2: Fora da faixa (excesso de liquidez, possível ineficiência)
            '''
            definicao = '''
            A Liquidez Corrente mede a capacidade da empresa de pagar suas obrigações de curto prazo com seus ativos circulantes, calculada como (Ativo Circulante / Passivo Circulante). É um indicador fundamental para avaliar a saúde financeira de curto prazo, especialmente em setores com alta necessidade de capital de giro, como varejo e indústria. Uma liquidez corrente alta sugere boa capacidade de honrar compromissos imediatos, enquanto um valor baixo indica risco de inadimplência. Deve ser analisada em conjunto com outros indicadores de liquidez, como Liquidez Imediata, e considerando o ciclo operacional da empresa, pois setores com longos ciclos de recebimento (ex.: infraestrutura) podem exigir maior liquidez.
            '''
            agrupador = 'Liquidez'
            formula = 'Liquidez Corrente = Ativo Circulante / Passivo Circulante'

            try:
                if liquidez_corrente < 0.5:
                    return {
                        'classificacao': 'Crítico',
                        'faixa': 'Liquidez Corrente < 0.5',
                        'descricao': '''
                        Uma Liquidez Corrente abaixo de 0.5 indica que a empresa tem menos da metade dos ativos circulantes necessários para cobrir suas obrigações de curto prazo, sugerindo alta dificuldade financeira. Isso é comum em empresas em crise, como a Oi (OIBR3) durante períodos de reestruturação, ou em setores com margens apertadas, como aviação (ex.: Gol - GOLL4). Para investidores, essa faixa é um alerta de risco elevado, pois a empresa pode enfrentar inadimplência ou necessidade de captações emergenciais. A análise deve focar na composição do ativo circulante (ex.: recebíveis vs. caixa), na estrutura do passivo circulante e em estratégias de gestão de capital de giro. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de recuperação.
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
                        Uma Liquidez Corrente entre 0.5 e 1 indica capacidade limitada de pagar obrigações de curto prazo, pois os ativos circulantes são insuficientes para cobrir integralmente o passivo circulante. Isso é comum em setores com alta rotatividade, como varejo (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode enfrentar dificuldades em cenários de aperto financeiro. É importante analisar a qualidade do ativo circulante (ex.: recebíveis inadimplentes) e a gestão de fluxos de caixa para avaliar a sustentabilidade. Análises complementares de Liquidez Imediata e fluxo de caixa operacional são recomendadas.
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
                        Uma Liquidez Corrente entre 1 e 1.5 indica capacidade aceitável de pagar obrigações de curto prazo, com ativos circulantes suficientes para cobrir o passivo circulante. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua gestão equilibrada de capital de giro no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre liquidez e eficiência, sendo adequada para quem busca segurança financeira de curto prazo. É importante avaliar a composição do ativo circulante e a consistência do fluxo de caixa para confirmar a robustez financeira.
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
                        Uma Liquidez Corrente entre 1.5 e 2 reflete boa capacidade de pagar obrigações de curto prazo, com ativos circulantes excedendo confortavelmente o passivo circulante. Empresas como a Ambev (ABEV3), com forte geração de caixa e gestão eficiente, frequentemente apresentam liquidez nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e resiliência a choques de curto prazo. No entanto, é importante verificar se a liquidez elevada não reflete ineficiência na alocação de recursos, como excesso de estoques ou recebíveis. Análises de ciclo operacional e fluxo de caixa são recomendadas.
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
                        Uma Liquidez Corrente acima de 2 indica excesso de liquidez, com ativos circulantes muito superiores às obrigações de curto prazo. Isso pode ocorrer em empresas com alta geração de caixa, como a Vale (VALE3) em períodos de preços elevados de commodities. Para investidores, essa faixa pode ser positiva, pois sugere segurança financeira, mas também pode indicar ineficiência na alocação de capital, como excesso de caixa ocioso ou estoques acumulados. A análise deve focar na estratégia de uso do ativo circulante (ex.: reinvestimento, dividendos) e no retorno sobre o capital investido (ROIC) para avaliar a eficiência.
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
                    Ocorreu um erro ao processar a Liquidez Corrente: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o passivo circulante for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o ativo circulante e o passivo circulante estejam corretos e sejam valores numéricos válidos.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }

        def evaluate_liquidez_imediata(liquidez_imediata):
            '''
            Avalia a Liquidez Imediata com base em faixas definidas para o mercado brasileiro:
            - Liquidez Imediata < 0.2: Crítico (dificuldade extrema em pagar obrigações de curto prazo)
            - 0.2 ≤ Liquidez Imediata ≤ 0.5: Ruim (capacidade muito limitada de pagar obrigações imediatas)
            - 0.5 < Liquidez Imediata ≤ 1: Moderado (capacidade aceitável de pagar obrigações imediatas)
            - 1 < Liquidez Imediata ≤ 1.5: Ótimo (boa capacidade de pagar obrigações imediatas)
            - Liquidez Imediata > 1.5: Fora da faixa (excesso de liquidez imediata, possível ineficiência)
            '''
            definicao = '''
            A Liquidez Imediata mede a capacidade da empresa de pagar suas obrigações de curto prazo usando apenas caixa, equivalentes de caixa e investimentos de curto prazo, calculada como (Caixa e Equivalentes / Passivo Circulante). É um indicador mais conservador que a Liquidez Corrente, pois exclui ativos menos líquidos, como estoques e recebíveis. É especialmente útil para avaliar a solidez financeira em cenários de crise, onde o acesso imediato a recursos é crucial. Uma liquidez imediata alta sugere segurança financeira, enquanto um valor baixo indica risco de inadimplência. Deve ser analisada considerando o setor e o ciclo operacional da empresa.
            '''
            agrupador = 'Liquidez'
            formula = 'Liquidez Imediata = (Caixa e Equivalentes) / Passivo Circulante'

            try:
                if liquidez_imediata < 0.2:
                    return {
                        'classificacao': 'Crítico',
                        'faixa': 'Liquidez Imediata < 0.2',
                        'descricao': '''
                        Uma Liquidez Imediata abaixo de 0.2 indica dificuldade extrema em pagar obrigações de curto prazo com recursos imediatamente disponíveis, sugerindo risco elevado de inadimplência. Isso é comum em empresas em crise financeira, como a Gol (GOLL4) durante períodos de baixa demanda no setor aéreo. Para investidores, essa faixa é um alerta grave, pois a empresa pode precisar de captações emergenciais ou vendas de ativos. A análise deve focar na gestão de caixa, estrutura do passivo circulante e estratégias de liquidez. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de recuperação.
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
                        Uma Liquidez Imediata entre 0.2 e 0.5 reflete capacidade muito limitada de pagar obrigações imediatas, indicando que a empresa depende de outros ativos circulantes (ex.: recebíveis) para cumprir compromissos. Isso é comum em setores com alta rotatividade, como varejo (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode enfrentar dificuldades em cenários de aperto financeiro. É importante analisar a qualidade do caixa e a velocidade de conversão de recebíveis em dinheiro. Análises complementares de Liquidez Corrente e fluxo de caixa são recomendadas.
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
                        Uma Liquidez Imediata entre 0.5 e 1 indica capacidade aceitável de pagar obrigações imediatas, com caixa e equivalentes cobrindo parcialmente o passivo circulante. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua gestão eficiente de caixa no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre liquidez e eficiência, sendo adequada para quem busca segurança financeira de curto prazo. É importante avaliar a consistência do fluxo de caixa e a composição do passivo circulante para confirmar a robustez financeira.
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
                        Uma Liquidez Imediata entre 1 e 1.5 reflete boa capacidade de pagar obrigações imediatas, com caixa e equivalentes excedendo confortavelmente o passivo circulante. Empresas como a Ambev (ABEV3), com forte geração de caixa, frequentemente apresentam liquidez nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e resiliência a choques de curto prazo. No entanto, é importante verificar se a liquidez elevada não reflete ineficiência na alocação de caixa, como recursos ociosos. Análises de ciclo operacional e ROIC são recomendadas.
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
                        Uma Liquidez Imediata acima de 1.5 indica excesso de liquidez imediata, com caixa e equivalentes muito superiores às obrigações de curto prazo. Isso pode ocorrer em empresas com alta geração de caixa, como a Vale (VALE3) em períodos de preços elevados de commodities. Para investidores, essa faixa pode ser positiva, pois sugere segurança financeira, mas também pode indicar ineficiência na alocação de capital, como excesso de caixa ocioso. A análise deve focar na estratégia de uso do caixa (ex.: reinvestimento, dividendos) e no retorno sobre o capital investido (ROIC) para avaliar a eficiência.
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
                    Ocorreu um erro ao processar a Liquidez Imediata: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o passivo circulante for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o caixa e equivalentes e o passivo circulante estejam corretos e sejam valores numéricos válidos.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }

        def evaluate_divida_bruta_patrimonio(divida_bruta_patrimonio):
            '''
            Avalia a Dívida Bruta/Patrimônio Líquido com base em faixas definidas para o mercado brasileiro:
            - Dívida Bruta/PL < 0.1: Fora da faixa (endividamento extremamente baixo, possível ineficiência)
            - 0.1 ≤ Dívida Bruta/PL ≤ 0.5: Ótimo (endividamento baixo)
            - 0.5 < Dívida Bruta/PL ≤ 1: Moderado (endividamento aceitável)
            - 1 < Dívida Bruta/PL ≤ 2: Ruim (endividamento elevado)
            - 2 < Dívida Bruta/PL ≤ 3: Péssimo (endividamento muito alto)
            - Dívida Bruta/PL > 3: Crítico (endividamento excessivo, risco elevado)
            '''
            definicao = '''
            A Dívida Bruta/Patrimônio Líquido mede o nível de endividamento da empresa em relação ao seu patrimônio líquido, calculado como (Dívida Bruta / Patrimônio Líquido). É um indicador chave para avaliar a alavancagem financeira, mostrando quanto a empresa depende de dívidas em relação ao capital dos acionistas. Um valor baixo sugere solidez financeira, enquanto um valor alto indica maior risco financeiro devido à dependência de financiamento externo. É especialmente útil em setores com alta alavancagem, como infraestrutura e utilities, mas deve ser analisado em conjunto com indicadores como Dívida Líquida/EBITDA e fluxo de caixa livre.
            '''
            agrupador = 'Endividamento'
            formula = 'Dívida Bruta/Patrimônio Líquido = Dívida Bruta / Patrimônio Líquido'

            try:
                if divida_bruta_patrimonio < 0.1:
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'Dívida Bruta/PL < 0.1',
                        'descricao': '''
                        Uma Dívida Bruta/Patrimônio Líquido abaixo de 0.1 indica endividamento extremamente baixo, sugerindo que a empresa depende muito pouco de financiamento externo. Isso pode ocorrer em empresas com alta geração de caixa, como a Totvs (TOTS3) em períodos de forte liquidez. Para investidores, essa faixa pode ser positiva, pois indica baixa alavancagem, mas também pode sugerir ineficiência na alocação de capital, como falta de investimentos em crescimento. A análise deve focar na estratégia de uso do capital próprio e no retorno sobre o capital investido (ROIC) para avaliar a eficiência.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 0.1 <= divida_bruta_patrimonio <= 0.5:
                    return {
                        'classificacao': 'Ótimo',
                        'faixa': '0.1 <= Dívida Bruta/PL <= 0.5',
                        'descricao': '''
                        Uma Dívida Bruta/Patrimônio Líquido entre 0.1 e 0.5 reflete endividamento baixo, indicando que a empresa mantém uma estrutura financeira sólida com dependência limitada de dívidas. Empresas como a Vale (VALE3) em períodos de alta nos preços de minério de ferro frequentemente operam nessa faixa. Para investidores, essa faixa é atrativa, pois sugere baixo risco financeiro e flexibilidade para investimentos ou retorno aos acionistas. É importante verificar a consistência da geração de caixa e a composição da dívida (curto vs. longo prazo) para confirmar a sustentabilidade.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 0.5 < divida_bruta_patrimonio <= 1:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '0.5 < Dívida Bruta/PL <= 1',
                        'descricao': '''
                        Uma Dívida Bruta/Patrimônio Líquido entre 0.5 e 1 indica endividamento aceitável, com equilíbrio entre capital próprio e dívidas. No Brasil, empresas como a Ambev (ABEV3) frequentemente operam nessa faixa devido à sua gestão financeira eficiente. Para investidores, essa faixa sugere risco moderado, com a empresa capaz de suportar oscilações econômicas sem grandes pressões financeiras. É importante avaliar a estrutura da dívida e a capacidade de geração de caixa para confirmar a saúde financeira.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 1 < divida_bruta_patrimonio <= 2:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '1 < Dívida Bruta/PL <= 2',
                        'descricao': '''
                        Uma Dívida Bruta/Patrimônio Líquido entre 1 e 2 sugere endividamento elevado, indicando que a empresa depende significativamente de financiamento externo. Isso é comum em setores com alta alavancagem, como a Petrobras (PETR4) em períodos de investimentos pesados. Para investidores, essa faixa exige cautela, pois a empresa pode ser vulnerável a aumentos de juros ou quedas na receita. A análise deve focar na capacidade de pagamento da dívida, custos de financiamento e tendências do fluxo de caixa.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 2 < divida_bruta_patrimonio <= 3:
                    return {
                        'classificacao': 'Péssimo',
                        'faixa': '2 < Dívida Bruta/PL <= 3',
                        'descricao': '''
                        Uma Dívida Bruta/Patrimônio Líquido entre 2 e 3 reflete endividamento muito alto, indicando risco significativo de pressão financeira. Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises, enfrentando dificuldades para gerenciar dívidas elevadas. Para investidores, essa faixa representa alto risco, exigindo análise detalhada da estrutura de capital, covenants de dívida e planos de desalavancagem para avaliar a viabilidade financeira.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif divida_bruta_patrimonio > 3:
                    return {
                        'classificacao': 'Crítico',
                        'faixa': 'Dívida Bruta/PL > 3',
                        'descricao': '''
                        Uma Dívida Bruta/Patrimônio Líquido acima de 3 indica endividamento excessivo, sugerindo que a empresa depende fortemente de dívidas em relação ao seu capital próprio. Isso é alarmante e típico de empresas em dificuldades financeiras, como a Gol (GOLL4) em períodos de crise no setor aéreo. Para investidores, essa faixa é de altíssimo risco, com possibilidade de reestruturação ou insolvência. A análise deve focar na capacidade de geração de caixa, estratégias de redução de dívida e covenants financeiros para avaliar a viabilidade.
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
                    Ocorreu um erro ao processar a Dívida Bruta/Patrimônio Líquido: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o patrimônio líquido for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que a dívida bruta e o patrimônio líquido estejam corretos e sejam valores numéricos válidos.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }

        def evaluate_margem_ebitda(margem_ebitda):
            '''
            Avalia a Margem EBITDA com base em faixas definidas para o mercado brasileiro:
            - Margem EBITDA < 0%: Crítico (EBITDA negativo, risco elevado)
            - 0% ≤ Margem EBITDA ≤ 10%: Ruim (rentabilidade operacional baixa)
            - 10% < Margem EBITDA ≤ 20%: Moderado (rentabilidade operacional aceitável)
            - 20% < Margem EBITDA ≤ 40%: Ótimo (alta rentabilidade operacional)
            - Margem EBITDA > 40%: Fora da faixa (rentabilidade operacional excepcional, avaliar sustentabilidade)
            '''
            definicao = '''
            A Margem EBITDA mede a porcentagem da receita que resta como EBITDA (Lucro Antes de Juros, Impostos, Depreciação e Amortização), calculada como (EBITDA / Receita Bruta). É um indicador de rentabilidade operacional que reflete a capacidade da empresa de gerar caixa antes de despesas financeiras, impostos e depreciação. É especialmente útil para comparar empresas de diferentes setores ou com estruturas de capital distintas, pois exclui efeitos de financiamento e políticas contábeis. Uma margem EBITDA alta sugere eficiência operacional, enquanto um valor baixo ou negativo pode indicar ineficiência ou pressão de custos. Deve ser analisada em conjunto com outros indicadores, como margem líquida e fluxo de caixa livre.
            '''
            agrupador = 'Rentabilidade'
            formula = 'Margem EBITDA = EBITDA / Receita Bruta'

            try:
                if margem_ebitda < 0:
                    return {
                        'classificacao': 'Crítico',
                        'faixa': 'Margem EBITDA < 0%',
                        'descricao': '''
                        Uma Margem EBITDA negativa indica que a empresa não está gerando caixa operacional suficiente para cobrir custos antes de despesas financeiras, impostos e depreciação. Isso é comum em empresas em crise, como a CSN (CSNA3) durante quedas de preços de commodities. Para investidores, essa faixa é um alerta de risco elevado, pois reflete ineficiência operacional ou dificuldades setoriais. A análise deve focar na estrutura de custos, estratégias de recuperação e endividamento. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
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
                        Uma Margem EBITDA entre 0% e 10% reflete rentabilidade operacional baixa, indicando que a empresa tem pouca capacidade de gerar caixa após custos operacionais. Isso é comum em setores com margens apertadas, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a aumentos de custos ou oscilações na receita. É importante analisar a capacidade de melhorar a eficiência operacional ou reduzir custos. Análises complementares de margem líquida e fluxo de caixa operacional são recomendadas.
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
                        Uma Margem EBITDA entre 10% e 20% indica rentabilidade operacional aceitável, típica de empresas com boa gestão de custos e eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua eficiência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência da margem EBITDA ao longo do tempo e o impacto de fatores externos, como custos de insumos e concorrência.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 20 < margem_ebitda <= 40:
                    return {
                        'classificacao': 'Ótimo',
                        'faixa': '20% < Margem EBITDA <= 40%',
                        'descricao': '''
                        Uma Margem EBITDA entre 20% e 40% reflete alta rentabilidade operacional, indicando que a empresa é eficiente em gerar caixa antes de despesas financeiras e impostos. Empresas como a Ambev (ABEV3), com forte controle de custos e liderança de mercado, frequentemente apresentam margens nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e potencial para reinvestimento ou pagamento de dividendos. No entanto, é importante verificar a sustentabilidade da margem, analisando fatores como concorrência, custos operacionais e tendências de mercado.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif margem_ebitda > 40:
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'Margem EBITDA > 40%',
                        'descricao': '''
                        Uma Margem EBITDA acima de 40% é excepcional, indicando que a empresa tem uma capacidade extraordinária de gerar caixa operacional. Isso é raro, mas pode ocorrer em empresas com forte poder de precificação ou baixos custos, como a Weg (WEGE3) em períodos de alta eficiência. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois margens tão altas podem não ser sustentáveis a longo prazo, especialmente em setores com entrada de novos concorrentes. A análise deve focar na escalabilidade do modelo de negócios, barreiras de entrada e consistência histórica da margem.
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
                    Ocorreu um erro ao processar a Margem EBITDA: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o EBITDA e a receita bruta estejam corretos e sejam valores numéricos válidos.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }

        def evaluate_margem_ebit(margem_ebit):
            '''
            Avalia a Margem EBIT com base em faixas definidas para o mercado brasileiro:
            - Margem EBIT < 0%: Crítico (EBIT negativo, risco elevado)
            - 0% ≤ Margem EBIT ≤ 5%: Ruim (rentabilidade operacional baixa)
            - 5% < Margem EBIT ≤ 15%: Moderado (rentabilidade operacional aceitável)
            - 15% < Margem EBIT ≤ 25%: Ótimo (alta rentabilidade operacional)
            - Margem EBIT > 25%: Fora da faixa (rentabilidade operacional excepcional, avaliar sustentabilidade)
            '''
            definicao = '''
            A Margem EBIT mede a porcentagem da receita que resta como EBIT (Lucro Antes de Juros e Impostos), calculada como (EBIT / Receita Bruta). É um indicador de rentabilidade operacional que reflete a eficiência da empresa em gerar lucro antes de despesas financeiras e impostos, considerando depreciação e amortização. É útil para comparar empresas em setores com diferentes níveis de investimento em ativos fixos, como indústria e infraestrutura. Uma margem EBIT alta sugere eficiência operacional, enquanto um valor baixo ou negativo pode indicar ineficiência ou pressão de custos. Deve ser analisada em conjunto com outros indicadores, como margem EBITDA e fluxo de caixa livre.
            '''
            agrupador = 'Rentabilidade'
            formula = 'Margem EBIT = EBIT / Receita Bruta'

            try:
                if margem_ebit < 0:
                    return {
                        'classificacao': 'Crítico',
                        'faixa': 'Margem EBIT < 0%',
                        'descricao': '''
                        Uma Margem EBIT negativa indica que a empresa não está gerando lucro operacional antes de juros e impostos, refletindo ineficiência operacional ou dificuldades setoriais. Isso é comum em empresas em crise, como a Usiminas (USIM5) durante quedas de preços no setor siderúrgico. Para investidores, essa faixa é um alerta de risco elevado, pois pode indicar problemas estruturais ou cíclicos. A análise deve focar na estrutura de custos, estratégias de recuperação e endividamento. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 0 <= margem_ebit <= 5:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '0% <= Margem EBIT <= 5%',
                        'descricao': '''
                        Uma Margem EBIT entre 0% e 5% reflete rentabilidade operacional baixa, indicando que a empresa tem pouca capacidade de gerar lucro após custos operacionais, incluindo depreciação. Isso é comum em setores com margens apertadas, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a aumentos de custos ou oscilações na receita. É importante analisar a capacidade de melhorar a eficiência operacional ou reduzir custos fixos. Análises complementares de margem EBITDA e fluxo de caixa operacional são recomendadas.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 5 < margem_ebit <= 15:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '5% < Margem EBIT <= 15%',
                        'descricao': '''
                        Uma Margem EBIT entre 5% e 15% indica rentabilidade operacional aceitável, típica de empresas com boa gestão de custos e eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua eficiência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência da margem EBIT ao longo do tempo e o impacto de fatores externos, como custos de insumos e concorrência.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 15 < margem_ebit <= 25:
                    return {
                        'classificacao': 'Ótimo',
                        'faixa': '15% < Margem EBIT <= 25%',
                        'descricao': '''
                        Uma Margem EBIT entre 15% e 25% reflete alta rentabilidade operacional, indicando que a empresa é eficiente em gerar lucro antes de despesas financeiras e impostos. Empresas como a Ambev (ABEV3), com forte controle de custos e liderança de mercado, frequentemente apresentam margens nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e potencial para reinvestimento ou pagamento de dividendos. No entanto, é importante verificar a sustentabilidade da margem, analisando fatores como concorrência, custos operacionais e tendências de mercado.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif margem_ebit > 25:
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'Margem EBIT > 25%',
                        'descricao': '''
                        Uma Margem EBIT acima de 25% é excepcional, indicando que a empresa tem uma capacidade extraordinária de gerar lucro operacional. Isso é raro, mas pode ocorrer em empresas com forte poder de precificação ou baixos custos, como a Weg (WEGE3) em períodos de alta eficiência. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois margens tão altas podem não ser sustentáveis a longo prazo, especialmente em setores com entrada de novos concorrentes. A análise deve focar na escalabilidade do modelo de negócios, barreiras de entrada e consistência histórica da margem.
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
                    Ocorreu um erro ao processar a Margem EBIT: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o EBIT e a receita bruta estejam corretos e sejam valores numéricos válidos.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }


def evaluate_dy(dividend_yield):
    '''
    Avalia o Dividend Yield (DY) com base em faixas definidas para o mercado brasileiro:
    - Dividend Yield < 2%: Ruim (retorno baixo via dividendos)
    - 2% ≤ Dividend Yield ≤ 5%: Moderado (retorno aceitável via dividendos)
    - 5% < Dividend Yield ≤ 8%: Ótimo (alto retorno via dividendos)
    - Dividend Yield > 8%: Fora da faixa (retorno excepcional, avaliar sustentabilidade)
    - Dividend Yield = 0%: Crítico (sem pagamento de dividendos)
    '''
    definicao = '''
    O Dividend Yield (DY) mede o retorno anual em dividendos em relação ao preço da ação, calculado como (Dividendos por Ação / Preço da Ação). É um indicador essencial para investidores focados em renda passiva, pois reflete o quanto a empresa retorna aos acionistas em forma de dividendos. Um DY alto pode indicar uma boa oportunidade de renda, mas também pode sinalizar risco se os dividendos não forem sustentáveis. É particularmente relevante em setores estáveis, como utilities e bancos, mas deve ser analisado em conjunto com a política de dividendos, fluxo de caixa livre e crescimento da empresa.
    '''
    agrupador = 'Dividendos'
    formula = 'Dividend Yield = Dividendos por Ação / Preço da Ação'

    try:
        if dividend_yield == 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'Dividend Yield = 0%',
                'descricao': '''
                Um Dividend Yield de 0% indica que a empresa não pagou dividendos no período analisado, o que pode ocorrer em empresas em crescimento, como a Nubank (NUBR33), que reinvestem todo o lucro em expansão, ou em empresas em crise, como a Oi (OIBR3) durante reestruturações. Para investidores focados em renda, essa faixa é desvantajosa, mas pode ser aceitável para quem busca crescimento de capital. A análise deve focar na estratégia da empresa (reinvestimento vs. dificuldades financeiras), fluxo de caixa livre e perspectivas de pagamento futuro de dividendos. Investidores conservadores devem evitar empresas nessa faixa, a menos que haja forte potencial de valorização.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 < dividend_yield < 2:
            return {
                'classificacao': 'Ruim',
                'faixa': 'Dividend Yield < 2%',
                'descricao': '''
                Um Dividend Yield abaixo de 2% reflete um retorno baixo via dividendos, indicando que a empresa paga dividendos modestos em relação ao preço da ação. Isso é comum em empresas com foco em crescimento, como a Magazine Luiza (MGLU3) durante expansões no e-commerce. Para investidores focados em renda, essa faixa é pouco atrativa, pois o retorno via dividendos é limitado. É importante analisar a política de dividendos, o crescimento dos lucros e o fluxo de caixa livre para avaliar se a empresa pode aumentar os dividendos no futuro. Análises complementares de P/L e ROE são recomendadas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 <= dividend_yield <= 5:
            return {
                'classificacao': 'Moderado',
                'faixa': '2% <= Dividend Yield <= 5%',
                'descricao': '''
                Um Dividend Yield entre 2% e 5% indica um retorno aceitável via dividendos, típico de empresas com estabilidade financeira e política de dividendos equilibrada. No Brasil, empresas como a Engie Brasil (EGIE3) frequentemente operam nessa faixa devido à consistência no setor de energia. Para investidores, essa faixa sugere um equilíbrio entre renda passiva e potencial de valorização, sendo adequada para quem busca retornos moderados. É importante avaliar a sustentabilidade dos dividendos, analisando o payout ratio e o fluxo de caixa livre.
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
                Um Dividend Yield entre 5% e 8% reflete um alto retorno via dividendos, indicando que a empresa distribui uma parcela significativa de seus lucros aos acionistas. Empresas como a Taesa (TAEE11), do setor de energia, frequentemente apresentam DY nessa faixa devido à sua estabilidade e fluxo de caixa previsível. Para investidores, essa faixa é atrativa, especialmente para quem busca renda passiva. No entanto, é crucial verificar a sustentabilidade dos dividendos, analisando o payout ratio, a geração de caixa e a consistência dos lucros.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif dividend_yield > 8:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dividend Yield > 8%',
                'descricao': '''
                Um Dividend Yield acima de 8% é excepcional, mas pode indicar tanto uma oportunidade quanto um risco. Empresas como a Banco do Brasil (BBAS3) podem atingir essa faixa em momentos de preços de ações deprimidos ou alta distribuição de lucros. Para investidores, essa faixa é atrativa, mas exige cautela, pois dividendos muito altos podem não ser sustentáveis, especialmente se o payout ratio for elevado ou a empresa enfrentar desafios financeiros. A análise deve focar na saúde financeira, fluxo de caixa livre e histórico de pagamento de dividendos para avaliar a sustentabilidade.
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
            Ocorreu um erro ao processar o Dividend Yield: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o preço da ação for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que os dividendos por ação e o preço da ação estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_psr(psr):
    '''
    Avalia o Preço/Sales Ratio (P/S) com base em faixas definidas para o mercado brasileiro:
    - P/S < 0.5: Ótimo (subvalorizado, oportunidade de compra)
    - 0.5 ≤ P/S ≤ 1: Moderado (valuation justo, crescimento moderado)
    - 1 < P/S ≤ 2: Ruim (sobrevalorizado, cautela necessária)
    - 2 < P/S ≤ 3: Péssimo (muito caro, alto risco)
    - P/S > 3: Fora da faixa (extremamente sobrevalorizado, risco elevado)
    '''
    definicao = '''
    O Preço/Sales Ratio (P/S) compara o preço da ação à receita bruta por ação, calculado como (Preço da Ação / Receita por Ação). É um indicador de valuation útil para avaliar empresas com lucros baixos ou negativos, como startups ou empresas em crescimento, pois foca na receita em vez do lucro. Um P/S baixo pode indicar subvalorização, enquanto um valor alto sugere que a ação está cara. É particularmente relevante em setores com margens reduzidas, como varejo, mas deve ser analisado em conjunto com margens de lucro e crescimento da receita.
    '''
    agrupador = 'Valuation'
    formula = 'P/S = Preço da Ação / Receita por Ação'

    try:
        if psr < 0.5:
            return {
                'classificacao': 'Ótimo',
                'faixa': 'P/S < 0.5',
                'descricao': '''
                Um P/S abaixo de 0.5 sugere que a ação está subvalorizada em relação à sua receita, indicando uma potencial oportunidade de compra. Isso é comum em setores cíclicos durante períodos de baixa, como a Vale (VALE3) em momentos de preços deprimidos de commodities. Para investidores, essa faixa é atrativa, especialmente se a empresa tem potencial de crescimento de receita ou melhoria de margens. No entanto, é importante verificar se o baixo P/S não reflete problemas estruturais, como margens negativas ou concorrência intensa. Análises complementares de margem líquida e fluxo de caixa são recomendadas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0.5 <= psr <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 <= P/S <= 1',
                'descricao': '''
                Um P/S entre 0.5 e 1 reflete um valuation justo, típico de empresas com receita estável e crescimento moderado. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua consistência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre preço e fundamentos, sendo adequada para quem busca retornos consistentes sem grande exposição a riscos de sobrevalorização. É importante avaliar o crescimento da receita e as margens operacionais para confirmar a sustentabilidade do valuation.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 1 < psr <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '1 < P/S <= 2',
                'descricao': '''
                Um P/S entre 1 e 2 sugere que a ação está sobrevalorizada em relação à sua receita, indicando que o mercado espera crescimento significativo. Empresas como a Raia Drogasil (RADL3) podem atingir essa faixa em períodos de expansão agressiva no varejo farmacêutico. Para investidores, essa faixa exige cautela, pois o preço elevado pode não se sustentar se o crescimento da receita não acompanhar as expectativas. Análise de tendências setoriais, margens operacionais e concorrência é recomendada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 2 < psr <= 3:
            return {
                'classificacao': 'Péssimo',
                'faixa': '2 < P/S <= 3',
                'descricao': '''
                Um P/S entre 2 e 3 indica que a ação é muito cara em relação à sua receita, sugerindo que o mercado está pagando um prêmio elevado por expectativas futuras. Empresas como a Localiza (RENT3) podem apresentar P/S nessa faixa em momentos de otimismo com expansão de frota. Para investidores, essa faixa representa alto risco, pois o preço elevado pode não ser justificado se o crescimento da receita não corresponder às expectativas. É essencial analisar o histórico de crescimento, a escalabilidade do modelo de negócios e o contexto competitivo.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif psr > 3:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/S > 3',
                'descricao': '''
                Um P/S acima de 3 é extremamente elevado, geralmente associado a empresas com altíssimas expectativas de crescimento ou especulação de mercado. No Brasil, o Nubank (NUBR33) já apresentou P/S nessa faixa após sua estreia na bolsa, devido ao entusiasmo com sua disrupção no setor financeiro. Para investidores, essa faixa é de altíssimo risco, pois o preço reflete mais especulação do que fundamentos atuais. A análise deve focar em projeções de longo prazo, execução estratégica e comparação com peers globais, mas mesmo assim, é uma escolha apenas para investidores tolerantes a risco elevado.
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
            Ocorreu um erro ao processar o P/S: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se a receita por ação for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o preço da ação e a receita por ação estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_evebitda(evebitda):
    '''
    Avalia o EV/EBITDA com base em faixas definidas para o mercado brasileiro:
    - EV/EBITDA < 0: Crítico (EBITDA negativo, risco elevado)
    - 0 ≤ EV/EBITDA ≤ 4: Ótimo (subvalorizado, oportunidade de compra)
    - 4 < EV/EBITDA ≤ 7: Moderado (valuation justo, crescimento moderado)
    - 7 < EV/EBITDA ≤ 10: Ruim (sobrevalorizado, cautela necessária)
    - 10 < EV/EBITDA ≤ 15: Péssimo (muito caro, alto risco)
    - EV/EBITDA > 15: Fora da faixa (extremamente sobrevalorizado, risco elevado)
    '''
    definicao = '''
    O EV/EBITDA compara o valor da empresa (Enterprise Value, ou valor de mercado + dívida líquida) ao EBITDA (Lucro Antes de Juros, Impostos, Depreciação e Amortização), medindo a capacidade de geração de caixa operacional em relação ao valor total da empresa. É amplamente utilizado em análises de fusões e aquisições, pois considera a dívida líquida, oferecendo uma visão mais completa do valuation do que o P/EBITDA. Um EV/EBITDA baixo pode indicar subvalorização, enquanto um valor alto sugere que a empresa está cara. Deve ser usado com cautela em setores com alta volatilidade no EBITDA, como commodities, e complementado com indicadores como fluxo de caixa livre e margem EBITDA.
    '''
    agrupador = 'Valuation'
    formula = 'EV/EBITDA = (Valor de Mercado + Dívida Líquida) / EBITDA'

    try:
        if evebitda < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'EV/EBITDA < 0',
                'descricao': '''
                Um EV/EBITDA negativo indica que a empresa possui EBITDA negativo, ou seja, não está gerando caixa operacional suficiente antes de despesas financeiras, impostos e depreciação. Isso é comum em empresas em crise, como a CSN (CSNA3) durante quedas de preços de commodities. Para investidores, essa faixa é um alerta de risco elevado, pois reflete ineficiência operacional ou dificuldades setoriais. A análise deve focar na estrutura de custos, estratégias de recuperação e endividamento, considerando que o EV inclui a dívida líquida. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 0 <= evebitda <= 4:
            return {
                'classificacao': 'Ótimo',
                'faixa': '0 <= EV/EBITDA <= 4',
                'descricao': '''
                Um EV/EBITDA entre 0 e 4 sugere que a empresa está subvalorizada em relação à sua geração de caixa operacional, indicando uma potencial oportunidade de compra. Isso é comum em setores cíclicos durante períodos de baixa, como a Vale (VALE3) em momentos de preços deprimidos de minério de ferro. Para investidores, essa faixa é atrativa, especialmente se a empresa tem potencial de melhoria nas margens ou crescimento de receita. No entanto, é importante verificar a sustentabilidade do EBITDA e a composição da dívida líquida. Análises complementares de fluxo de caixa livre e margem EBITDA são recomendadas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 4 < evebitda <= 7:
            return {
                'classificacao': 'Moderado',
                'faixa': '4 < EV/EBITDA <= 7',
                'descricao': '''
                Um EV/EBITDA entre 4 e 7 reflete um valuation justo, típico de empresas com geração de caixa estável e crescimento moderado. No Brasil, empresas como a Engie Brasil (EGIE3) frequentemente operam nessa faixa devido à consistência no setor de energia. Para investidores, essa faixa sugere um equilíbrio entre preço e fundamentos, sendo adequada para quem busca retornos consistentes sem grande exposição a riscos de sobrevalorização. É importante avaliar a consistência do EBITDA, a composição da dívida líquida e o contexto setorial para confirmar a sustentabilidade.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 7 < evebitda <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '7 < EV/EBITDA <= 10',
                'descricao': '''
                Um EV/EBITDA entre 7 e 10 sugere que a empresa está sobrevalorizada em relação à sua geração de caixa operacional, indicando que o mercado espera crescimento significativo. Empresas como a Localiza (RENT3) podem atingir essa faixa em períodos de expansão agressiva. Para investidores, essa faixa exige cautela, pois o preço elevado (que inclui a dívida líquida) pode não se sustentar se o crescimento do EBITDA não acompanhar as expectativas. Análise de tendências setoriais, margens operacionais e endividamento é recomendada.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < evebitda <= 15:
            return {
                'classificacao': 'Péssimo',
                'faixa': '10 < EV/EBITDA <= 15',
                'descricao': '''
                Um EV/EBITDA entre 10 e 15 indica que a empresa é muito cara em relação à sua geração de caixa operacional, sugerindo que o mercado está pagando um prêmio elevado por expectativas futuras. Empresas como a Totvs (TOTS3) podem apresentar EV/EBITDA nessa faixa em momentos de otimismo com tecnologia. Para investidores, essa faixa representa alto risco, pois o preço elevado pode não ser justificado se os resultados não corresponderem às expectativas. É essencial analisar o histórico de crescimento, a escalabilidade do modelo de negócios e o contexto competitivo.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif evebitda > 15:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'EV/EBITDA > 15',
                'descricao': '''
                Um EV/EBITDA acima de 15 é extremamente elevado, geralmente associado a empresas com altíssimas expectativas de crescimento ou especulação de mercado. No Brasil, o Nubank (NUBR33) já apresentou EV/EBITDA nessa faixa após sua estreia na bolsa, devido ao entusiasmo com sua disrupção no setor financeiro. Para investidores, essa faixa é de altíssimo risco, pois o preço reflete mais especulação do que fundamentos atuais, especialmente considerando a inclusão da dívida líquida. A análise deve focar em projeções de longo prazo, execução estratégica e comparação com peers globais, mas é uma escolha apenas para investidores tolerantes a risco elevado.
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
            Ocorreu um erro ao processar o EV/EBITDA: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o EBITDA for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o valor da empresa (valor de mercado + dívida líquida) e o EBITDA estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_roa(roa):
    '''
    Avalia o Retorno sobre Ativos (ROA) com base em faixas definidas para o mercado brasileiro:
    - ROA < 0%: Crítico (prejuízo sobre os ativos, risco elevado)
    - 0% ≤ ROA ≤ 5%: Ruim (retorno baixo sobre os ativos)
    - 5% < ROA ≤ 10%: Moderado (retorno aceitável sobre os ativos)
    - 10% < ROA ≤ 15%: Ótimo (alto retorno sobre os ativos)
    - ROA > 15%: Fora da faixa (retorno excepcional, avaliar sustentabilidade)
    '''
    definicao = '''
    O Retorno sobre Ativos (ROA) mede a rentabilidade da empresa em relação aos seus ativos totais, calculado como (Lucro Líquido / Ativos Totais). É um indicador chave para avaliar a eficiência com que a empresa utiliza seus ativos para gerar lucros. Um ROA alto sugere boa gestão operacional, enquanto um valor baixo ou negativo pode indicar ineficiência ou prejuízo. É especialmente útil em setores intensivos em capital, como indústria e infraestrutura, mas deve ser interpretado considerando o nível de endividamento, pois o ROA não distingue entre capital próprio e dívidas.
    '''
    agrupador = 'Rentabilidade'
    formula = 'ROA = Lucro Líquido / Ativos Totais'

    try:
        if roa < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'ROA < 0%',
                'descricao': '''
                Um ROA negativo indica que a empresa está gerando prejuízo em relação aos seus ativos totais, destruindo valor. Isso é comum em empresas em crise, como a Oi (OIBR3) durante períodos de reestruturação, ou em setores cíclicos, como aviação (ex.: Gol - GOLL4) em momentos de baixa demanda. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades financeiras graves. A análise deve focar na estrutura de custos, endividamento e estratégias de recuperação. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
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
                Um ROA entre 0% e 5% reflete um retorno baixo sobre os ativos, indicando que a empresa tem dificuldade em gerar lucros significativos com seus recursos. Isso é comum em setores com margens apertadas ou alta concorrência, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a oscilações econômicas ou custos elevados. É importante analisar a eficiência operacional, a utilização de ativos e o potencial de melhoria do ROA. Análises complementares de margem líquida e giro de ativos são recomendadas.
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
                Um ROA entre 5% e 10% indica um retorno aceitável sobre os ativos, típico de empresas com boa gestão e eficiência operacional moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua solidez no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência do ROA ao longo do tempo e o impacto da alavancagem financeira, que pode influenciar o indicador.
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
                Um ROA entre 10% e 15% reflete um alto retorno sobre os ativos, indicando que a empresa é eficiente em gerar lucros com seus recursos. Empresas como a Ambev (ABEV3), com forte controle de custos e liderança de mercado, frequentemente apresentam ROA nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e potencial para reinvestimento ou retorno aos acionistas. No entanto, é importante verificar se o ROA é impulsionado por eficiência operacional ou por fatores temporários, como venda de ativos. Análises de giro de ativos e fluxo de caixa são recomendadas.
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
                Um ROA acima de 15% é excepcional, indicando que a empresa gera retornos extraordinários sobre seus ativos. Isso é raro, mas pode ocorrer em empresas com alta eficiência operacional, como a Weg (WEGE3) em períodos de crescimento robusto. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois retornos tão altos podem não ser sustentáveis a longo prazo, especialmente em setores competitivos. A análise deve focar na sustentabilidade do ROA, barreiras de entrada e eficiência operacional para garantir a consistência do retorno.
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
            Ocorreu um erro ao processar o ROA: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se os ativos totais forem zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o lucro líquido e os ativos totais estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }


def evaluate_roic(roic):
    '''
    Avalia o Retorno sobre o Capital Investido (ROIC) com base em faixas definidas para o mercado brasileiro:
    - ROIC < 0%: Crítico (prejuízo sobre o capital investido, risco elevado)
    - 0% ≤ ROIC ≤ 5%: Ruim (retorno baixo sobre o capital investido)
    - 5% < ROIC ≤ 10%: Moderado (retorno aceitável sobre o capital investido)
    - 10% < ROIC ≤ 15%: Ótimo (alto retorno sobre o capital investido)
    - ROIC > 15%: Fora da faixa (retorno excepcional, avaliar sustentabilidade)
    '''
    definicao = '''
    O Retorno sobre o Capital Investido (ROIC) mede a rentabilidade da empresa em relação ao capital total investido (patrimônio líquido + dívida líquida), calculado como (EBIT Líquido de Impostos / Capital Investido). É um indicador chave para avaliar a eficiência com que a empresa utiliza o capital de acionistas e credores para gerar lucros operacionais. Um ROIC alto sugere boa alocação de capital, enquanto um valor baixo ou negativo pode indicar ineficiência ou prejuízo. É especialmente útil para comparar empresas em setores com diferentes níveis de alavancagem, mas deve ser analisado em conjunto com indicadores como ROE e fluxo de caixa livre.
    '''
    agrupador = 'Rentabilidade'
    formula = 'ROIC = EBIT Líquido de Impostos / (Patrimônio Líquido + Dívida Líquida)'

    try:
        if roic < 0:
            return {
                'classificacao': 'Crítico',
                'faixa': 'ROIC < 0%',
                'descricao': '''
                Um ROIC negativo indica que a empresa está gerando prejuízo em relação ao capital investido, destruindo valor para acionistas e credores. Isso é comum em empresas em crise, como a Oi (OIBR3) durante períodos de reestruturação, ou em setores cíclicos, como aviação (ex.: Gol - GOLL4) em momentos de baixa demanda. Para investidores, essa faixa é um alerta de risco elevado, pois reflete ineficiência na alocação de capital. A análise deve focar na estrutura de custos, endividamento e estratégias de recuperação. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
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
                Um ROIC entre 0% e 5% reflete um retorno baixo sobre o capital investido, indicando que a empresa tem dificuldade em gerar lucros significativos com seus recursos. Isso é comum em setores com margens apertadas ou alta concorrência, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a oscilações econômicas ou custos elevados. É importante analisar a eficiência na alocação de capital, a utilização de ativos e o potencial de melhoria do ROIC. Análises complementares de margem líquida e giro de ativos são recomendadas.
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
                Um ROIC entre 5% e 10% indica um retorno aceitável sobre o capital investido, típico de empresas com boa gestão e eficiência moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua solidez no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência do ROIC ao longo do tempo e o impacto da alavancagem financeira, que pode influenciar o indicador.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif 10 < roic <= 15:
            return {
                'classificacao': 'Ótimo',
                'faixa': '10% < ROIC <= 15%',
                'descricao': '''
                Um ROIC entre 10% e 15% reflete um alto retorno sobre o capital investido, indicando que a empresa é eficiente em gerar lucros com seus recursos. Empresas como a Ambev (ABEV3), com forte controle de custos e liderança de mercado, frequentemente apresentam ROIC nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e potencial para reinvestimento ou retorno aos acionistas. No entanto, é importante verificar se o ROIC é impulsionado por eficiência operacional ou por fatores temporários, como alavancagem. Análises de fluxo de caixa e endividamento são recomendadas.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }
        elif roic > 15:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'ROIC > 15%',
                'descricao': '''
                Um ROIC acima de 15% é excepcional, indicando que a empresa gera retornos extraordinários sobre o capital investido. Isso é raro, mas pode ocorrer em empresas com alta eficiência operacional, como a Weg (WEGE3) em períodos de crescimento robusto. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois retornos tão altos podem não ser sustentáveis a longo prazo, especialmente em setores competitivos. A análise deve focar na sustentabilidade do ROIC, barreiras de entrada e eficiência na alocação de capital para garantir a consistência do retorno.
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
            Ocorreu um erro ao processar o ROIC: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o capital investido (patrimônio líquido + dívida líquida) for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o EBIT líquido de impostos e o capital investido estejam corretos e sejam valores numéricos válidos.
            ''',
            'definicao': definicao,
            'agrupador': agrupador,
            'formula': formula
        }

    def evaluate_cagr_receita(cagr_receita):
        '''
        Avalia o Crescimento Anual Composto da Receita (CAGR Receita) com base em faixas definidas para o mercado brasileiro:
        - CAGR Receita < 0%: Crítico (redução de receita, risco elevado)
        - 0% ≤ CAGR Receita ≤ 5%: Ruim (crescimento baixo ou estagnação)
        - 5% < CAGR Receita ≤ 10%: Moderado (crescimento aceitável)
        - 10% < CAGR Receita ≤ 20%: Ótimo (crescimento robusto)
        - CAGR Receita > 20%: Fora da faixa (crescimento excepcional, avaliar sustentabilidade)
        '''
        definicao = '''
        O Crescimento Anual Composto da Receita (CAGR Receita) mede a taxa anual de crescimento da receita bruta da empresa ao longo de um período, calculado como ((Receita Final / Receita Inicial)^(1/n) - 1), onde n é o número de anos. É um indicador chave para avaliar a capacidade da empresa de expandir suas vendas, refletindo a saúde do modelo de negócios e a demanda por seus produtos ou serviços. Um CAGR alto sugere crescimento robusto, enquanto um valor baixo ou negativo pode indicar estagnação ou declínio. É especialmente útil em setores dinâmicos, como tecnologia e varejo, mas deve ser analisado em conjunto com margens de lucro e fluxo de caixa.
        '''
        agrupador = 'Crescimento'
        formula = 'CAGR Receita = ((Receita Final / Receita Inicial)^(1/n) - 1)'

        try:
            if cagr_receita < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'CAGR Receita < 0%',
                    'descricao': '''
                    Um CAGR Receita negativo indica que a empresa está enfrentando uma redução em sua receita ao longo do tempo, sugerindo problemas como perda de mercado, concorrência intensa ou dificuldades operacionais. Isso é comum em empresas em crise, como a Oi (OIBR3) durante períodos de reestruturação, ou em setores cíclicos, como aviação (ex.: Gol - GOLL4) em momentos de baixa demanda. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades fundamentais no modelo de negócios. A análise deve focar em estratégias de recuperação, posicionamento competitivo e tendências setoriais. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= cagr_receita <= 5:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0% <= CAGR Receita <= 5%',
                    'descricao': '''
                    Um CAGR Receita entre 0% e 5% reflete crescimento baixo ou estagnação, indicando que a empresa tem dificuldade em expandir suas vendas. Isso é comum em setores maduros ou com alta concorrência, como varejo alimentar (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a oscilações econômicas ou perda de participação de mercado. É importante analisar a capacidade de inovação, estratégias de marketing e potencial de crescimento futuro. Análises complementares de margem bruta e fluxo de caixa são recomendadas.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < cagr_receita <= 10:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '5% < CAGR Receita <= 10%',
                    'descricao': '''
                    Um CAGR Receita entre 5% e 10% indica crescimento aceitável, típico de empresas com operações estáveis e expansão moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à consistência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre crescimento e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a sustentabilidade do crescimento, considerando fatores como concorrência, inovação e condições macroeconômicas.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 10 < cagr_receita <= 20:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '10% < CAGR Receita <= 20%',
                    'descricao': '''
                    Um CAGR Receita entre 10% e 20% reflete crescimento robusto, indicando que a empresa está expandindo suas vendas de forma significativa. Empresas como a Magazine Luiza (MGLU3), durante períodos de forte crescimento no e-commerce, frequentemente apresentam CAGR nessa faixa. Para investidores, essa faixa é atrativa, pois sugere dinamismo e potencial de valorização. No entanto, é importante verificar se o crescimento é sustentável, analisando margens de lucro, escalabilidade do modelo de negócios e barreiras à entrada de concorrentes.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif cagr_receita > 20:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'CAGR Receita > 20%',
                    'descricao': '''
                    Um CAGR Receita acima de 20% é excepcional, indicando crescimento extremamente rápido nas vendas. Isso é raro, mas pode ocorrer em empresas disruptivas, como a Nubank (NUBR33) durante sua fase de expansão no setor financeiro. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois crescimentos tão altos podem não ser sustentáveis a longo prazo, especialmente em setores competitivos. A análise deve focar na escalabilidade do modelo de negócios, barreiras de entrada e consistência do crescimento para garantir sua continuidade.
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
                Ocorreu um erro ao processar o CAGR Receita: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se a receita inicial for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que a receita inicial, a receita final e o número de anos estejam corretos e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_cagr_lucro(cagr_lucro):
        '''
        Avalia o Crescimento Anual Composto do Lucro (CAGR Lucro) com base em faixas definidas para o mercado brasileiro:
        - CAGR Lucro < 0%: Crítico (redução de lucros, risco elevado)
        - 0% ≤ CAGR Lucro ≤ 5%: Ruim (crescimento baixo ou estagnação)
        - 5% < CAGR Lucro ≤ 10%: Moderado (crescimento aceitável)
        - 10% < CAGR Lucro ≤ 20%: Ótimo (crescimento robusto)
        - CAGR Lucro > 20%: Fora da faixa (crescimento excepcional, avaliar sustentabilidade)
        '''
        definicao = '''
        O Crescimento Anual Composto do Lucro (CAGR Lucro) mede a taxa anual de crescimento do lucro líquido da empresa ao longo de um período, calculado como ((Lucro Final / Lucro Inicial)^(1/n) - 1), onde n é o número de anos. É um indicador fundamental para avaliar a capacidade da empresa de aumentar sua rentabilidade, refletindo a eficiência operacional e a saúde financeira. Um CAGR alto sugere crescimento sustentável, enquanto um valor baixo ou negativo pode indicar problemas operacionais ou financeiros. É especialmente relevante em setores com alta volatilidade nos lucros, como tecnologia e commodities, mas deve ser analisado em conjunto com margem líquida e fluxo de caixa.
        '''
        agrupador = 'Crescimento'
        formula = 'CAGR Lucro = ((Lucro Final / Lucro Inicial)^(1/n) - 1)'

        try:
            if cagr_lucro < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'CAGR Lucro < 0%',
                    'descricao': '''
                    Um CAGR Lucro negativo indica que a empresa está enfrentando uma redução em seus lucros ao longo do tempo, sugerindo problemas como aumento de custos, perda de mercado ou dificuldades financeiras. Isso é comum em empresas em crise, como a Usiminas (USIM5) durante quedas de preços no setor siderúrgico. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades fundamentais na geração de lucro. A análise deve focar na estrutura de custos, estratégias de recuperação e endividamento. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 <= cagr_lucro <= 5:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0% <= CAGR Lucro <= 5%',
                    'descricao': '''
                    Um CAGR Lucro entre 0% e 5% reflete crescimento baixo ou estagnação, indicando que a empresa tem dificuldade em aumentar seus lucros. Isso é comum em setores maduros ou com margens apertadas, como varejo (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a oscilações econômicas ou aumento de custos. É importante analisar a capacidade de melhorar a eficiência operacional ou expandir margens. Análises complementares de margem líquida e fluxo de caixa são recomendadas.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 5 < cagr_lucro <= 10:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '5% < CAGR Lucro <= 10%',
                    'descricao': '''
                    Um CAGR Lucro entre 5% e 10% indica crescimento aceitável, típico de empresas com operações estáveis e rentabilidade moderada. No Brasil, empresas como a Ambev (ABEV3) frequentemente operam nessa faixa devido à sua consistência no setor de bebidas. Para investidores, essa faixa sugere um equilíbrio entre crescimento e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a sustentabilidade do crescimento, considerando fatores como concorrência, custos operacionais e condições macroeconômicas.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 10 < cagr_lucro <= 20:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '10% < CAGR Lucro <= 20%',
                    'descricao': '''
                    Um CAGR Lucro entre 10% e 20% reflete crescimento robusto, indicando que a empresa está aumentando seus lucros de forma significativa. Empresas como a Weg (WEGE3), com forte eficiência operacional, frequentemente apresentam CAGR nessa faixa. Para investidores, essa faixa é atrativa, pois sugere dinamismo e potencial de valorização. No entanto, é importante verificar se o crescimento é sustentável, analisando margens de lucro, escalabilidade do modelo de negócios e barreiras à entrada de concorrentes.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif cagr_lucro > 20:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'CAGR Lucro > 20%',
                    'descricao': '''
                    Um CAGR Lucro acima de 20% é excepcional, indicando crescimento extremamente rápido nos lucros. Isso é raro, mas pode ocorrer em empresas disruptivas, como a Nubank (NUBR33) durante sua fase de expansão no setor financeiro. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois crescimentos tão altos podem não ser sustentáveis a longo prazo, especialmente em setores competitivos. A análise deve focar na escalabilidade do modelo de negócios, barreiras de entrada e consistência do crescimento para garantir sua continuidade.
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
                Ocorreu um erro ao processar o CAGR Lucro: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o lucro inicial for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o lucro inicial, o lucro final e o número de anos estejam corretos e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_liquidez_seca(liquidez_seca):
        '''
        Avalia a Liquidez Seca com base em faixas definidas para o mercado brasileiro:
        - Liquidez Seca < 0.2: Crítico (dificuldade extrema em pagar obrigações sem estoques)
        - 0.2 ≤ Liquidez Seca ≤ 0.5: Ruim (capacidade limitada de pagar obrigações sem estoques)
        - 0.5 < Liquidez Seca ≤ 1: Moderado (capacidade aceitável de pagar obrigações sem estoques)
        - 1 < Liquidez Seca ≤ 1.5: Ótimo (boa capacidade de pagar obrigações sem estoques)
        - Liquidez Seca > 1.5: Fora da faixa (excesso de liquidez, possível ineficiência)
        '''
        definicao = '''
        A Liquidez Seca mede a capacidade da empresa de pagar suas obrigações de curto prazo usando ativos circulantes, excluindo estoques, calculada como ((Ativo Circulante - Estoques) / Passivo Circulante). É um indicador mais conservador que a Liquidez Corrente, pois considera apenas ativos mais líquidos, como caixa e recebíveis. É especialmente útil em setores com estoques de baixa liquidez, como varejo e indústria. Uma liquidez seca alta sugere solidez financeira, enquanto um valor baixo indica risco de inadimplência. Deve ser analisada em conjunto com Liquidez Corrente e fluxo de caixa operacional.
        '''
        agrupador = 'Liquidez'
        formula = 'Liquidez Seca = (Ativo Circulante - Estoques) / Passivo Circulante'

        try:
            if liquidez_seca < 0.2:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Liquidez Seca < 0.2',
                    'descricao': '''
                    Uma Liquidez Seca abaixo de 0.2 indica dificuldade extrema em pagar obrigações de curto prazo sem depender de estoques, sugerindo risco elevado de inadimplência. Isso é comum em empresas com estoques de baixa liquidez, como varejo em crise (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa é um alerta grave, pois a empresa pode precisar de captações emergenciais. A análise deve focar na gestão de caixa, qualidade dos recebíveis e estratégias de liquidez. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de recuperação.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0.2 <= liquidez_seca <= 0.5:
                return {
                    'classificacao': 'Ruim',
                    'faixa': '0.2 <= Liquidez Seca <= 0.5',
                    'descricao': '''
                    Uma Liquidez Seca entre 0.2 e 0.5 reflete capacidade limitada de pagar obrigações de curto prazo sem estoques, indicando dependência de outros ativos circulantes. Isso é comum em setores com estoques elevados, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode enfrentar dificuldades em cenários de aperto financeiro. É importante analisar a qualidade dos recebíveis e a velocidade de conversão em caixa. Análises complementares de Liquidez Corrente e fluxo de caixa são recomendadas.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0.5 < liquidez_seca <= 1:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '0.5 < Liquidez Seca <= 1',
                    'descricao': '''
                    Uma Liquidez Seca entre 0.5 e 1 indica capacidade aceitável de pagar obrigações de curto prazo sem depender de estoques, com ativos líquidos cobrindo parcialmente o passivo circulante. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua gestão eficiente de caixa. Para investidores, essa faixa sugere um equilíbrio entre liquidez e eficiência, sendo adequada para quem busca segurança financeira de curto prazo. É importante avaliar a composição dos ativos circulantes e a consistência do fluxo de caixa.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 1 < liquidez_seca <= 1.5:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '1 < Liquidez Seca <= 1.5',
                    'descricao': '''
                    Uma Liquidez Seca entre 1 e 1.5 reflete boa capacidade de pagar obrigações de curto prazo sem depender de estoques, com ativos líquidos excedendo confortavelmente o passivo circulante. Empresas como a Ambev (ABEV3), com forte geração de caixa, frequentemente apresentam liquidez nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e resiliência a choques de curto prazo. No entanto, é importante verificar se a liquidez elevada não reflete ineficiência na alocação de recursos. Análises de ciclo operacional e ROIC são recomendadas.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif liquidez_seca > 1.5:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Liquidez Seca > 1.5',
                    'descricao': '''
                    Uma Liquidez Seca acima de 1.5 indica excesso de liquidez, com ativos líquidos muito superiores às obrigações de curto prazo. Isso pode ocorrer em empresas com alta geração de caixa, como a Vale (VALE3) em períodos de preços elevados de commodities. Para investidores, essa faixa pode ser positiva, pois sugere segurança financeira, mas também pode indicar ineficiência na alocação de capital, como excesso de caixa ocioso. A análise deve focar na estratégia de uso dos ativos líquidos (ex.: reinvestimento, dividendos) e no ROIC para avaliar a eficiência.
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
                Ocorreu um erro ao processar a Liquidez Seca: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o passivo circulante for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o ativo circulante, os estoques e o passivo circulante estejam corretos e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_payout_ratio(payout_ratio):
        '''
        Avalia o Payout Ratio com base em faixas definidas para o mercado brasileiro:
        - Payout Ratio < 20%: Ruim (distribuição muito baixa de dividendos)
        - 20% ≤ Payout Ratio ≤ 50%: Moderado (distribuição equilibrada de dividendos)
        - 50% < Payout Ratio ≤ 80%: Ótimo (distribuição generosa de dividendos)
        - Payout Ratio > 80%: Fora da faixa (distribuição excessiva, avaliar sustentabilidade)
        - Payout Ratio = 0%: Crítico (sem pagamento de dividendos)
        '''
        definicao = '''
        O Payout Ratio mede a proporção do lucro líquido distribuído como dividendos, calculado como (Dividendos Totais / Lucro Líquido). É um indicador essencial para avaliar a política de dividendos da empresa, indicando quanto do lucro é retornado aos acionistas versus reinvestido no negócio. Um payout alto sugere foco em renda para acionistas, enquanto um valor baixo pode indicar reinvestimento para crescimento. É particularmente relevante em setores estáveis, como utilities e bancos, mas deve ser analisado em conjunto com fluxo de caixa livre e crescimento dos lucros.
        '''
        agrupador = 'Dividendos'
        formula = 'Payout Ratio = Dividendos Totais / Lucro Líquido'

        try:
            if payout_ratio == 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'Payout Ratio = 0%',
                    'descricao': '''
                    Um Payout Ratio de 0% indica que a empresa não pagou dividendos no período analisado, o que pode ocorrer em empresas em crescimento, como a Nubank (NUBR33), que reinvestem todo o lucro em expansão, ou em empresas em crise, como a Oi (OIBR3) durante reestruturações. Para investidores focados em renda, essa faixa é desvantajosa, mas pode ser aceitável para quem busca crescimento de capital. A análise deve focar na estratégia da empresa (reinvestimento vs. dificuldades financeiras), fluxo de caixa livre e perspectivas de pagamento futuro de dividendos.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 0 < payout_ratio < 20:
                return {
                    'classificacao': 'Ruim',
                    'faixa': 'Payout Ratio < 20%',
                    'descricao': '''
                    Um Payout Ratio abaixo de 20% reflete uma distribuição muito baixa de dividendos, indicando que a empresa retém a maior parte do lucro para reinvestimento. Isso é comum em empresas com foco em crescimento, como a Magazine Luiza (MGLU3) durante expansões no e-commerce. Para investidores focados em renda, essa faixa é pouco atrativa, pois o retorno via dividendos é limitado. É importante analisar o potencial de crescimento, o ROIC e o fluxo de caixa livre para avaliar se o reinvestimento será eficaz.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 20 <= payout_ratio <= 50:
                return {
                    'classificacao': 'Moderado',
                    'faixa': '20% <= Payout Ratio <= 50%',
                    'descricao': '''
                    Um Payout Ratio entre 20% e 50% indica uma distribuição equilibrada de dividendos, típica de empresas que balanceiam retorno aos acionistas com reinvestimento. No Brasil, empresas como a Engie Brasil (EGIE3) frequentemente operam nessa faixa devido à estabilidade no setor de energia. Para investidores, essa faixa sugere um equilíbrio entre renda passiva e crescimento, sendo adequada para quem busca retornos consistentes. É importante avaliar a sustentabilidade dos dividendos, analisando o fluxo de caixa livre e a consistência dos lucros.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif 50 < payout_ratio <= 80:
                return {
                    'classificacao': 'Ótimo',
                    'faixa': '50% < Payout Ratio <= 80%',
                    'descricao': '''
                    Um Payout Ratio entre 50% e 80% reflete uma distribuição generosa de dividendos, indicando que a empresa retorna uma parcela significativa de seus lucros aos acionistas. Empresas como a Taesa (TAEE11), do setor de energia, frequentemente apresentam payout nessa faixa devido à sua estabilidade e fluxo de caixa previsível. Para investidores, essa faixa é atrativa, especialmente para quem busca renda passiva. No entanto, é crucial verificar a sustentabilidade dos dividendos, analisando o fluxo de caixa livre e a consistência dos lucros.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }
            elif payout_ratio > 80:
                return {
                    'classificacao': 'Fora da faixa',
                    'faixa': 'Payout Ratio > 80%',
                    'descricao': '''
                    Um Payout Ratio acima de 80% indica uma distribuição excessiva de dividendos, sugerindo que a empresa está retornando quase todo o lucro aos acionistas, com pouco reinvestimento. Isso pode ocorrer em empresas maduras, como a Banco do Brasil (BBAS3) em períodos de lucros elevados. Para investidores, essa faixa é atrativa para renda, mas exige cautela, pois payout ratios muito altos podem não ser sustentáveis, especialmente se a empresa enfrentar desafios financeiros. A análise deve focar na saúde financeira, fluxo de caixa livre e histórico de pagamento de dividendos.
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
                Ocorreu um erro ao processar o Payout Ratio: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o lucro líquido for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que os dividendos totais e o lucro líquido estejam corretos e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

    def evaluate_free_cash_flow_yield(fcf_yield):
        '''
        Avalia o Free Cash Flow Yield com base em faixas definidas para o mercado brasileiro:
        - FCF Yield < 0%: Crítico (fluxo de caixa livre negativo, risco elevado)
        - 0% ≤ FCF Yield ≤ 3%: Ruim (fluxo de caixa livre baixo)
        - 3% < FCF Yield ≤ 6%: Moderado (fluxo de caixa livre aceitável)
        - 6% < FCF Yield ≤ 10%: Ótimo (fluxo de caixa livre robusto)
        - FCF Yield > 10%: Fora da faixa (fluxo de caixa livre excepcional, avaliar sustentabilidade)
        '''
        definicao = '''
        O Free Cash Flow Yield mede o fluxo de caixa livre por ação em relação ao preço da ação, calculado como (Fluxo de Caixa Livre por Ação / Preço da Ação). É um indicador essencial para avaliar a capacidade da empresa de gerar caixa disponível após investimentos, refletindo sua saúde financeira e flexibilidade para pagar dividendos, reduzir dívidas ou reinvestir. Um FCF Yield alto sugere undervaluation ou forte geração de caixa, enquanto um valor baixo ou negativo pode indicar problemas financeiros. É especialmente relevante em setores intensivos em capital, como indústria e infraestrutura, mas deve ser analisado em conjunto com endividamento e crescimento.
        '''
        agrupador = 'Fluxo de Caixa'
        formula = 'FCF Yield = Fluxo de Caixa Livre por Ação / Preço da Ação'

        try:
            if fcf_yield < 0:
                return {
                    'classificacao': 'Crítico',
                    'faixa': 'FCF Yield < 0%',
                    'descricao': '''
                    Um FCF Yield negativo indica que a empresa não está gerando fluxo de caixa livre, sugerindo que os investimentos operacionais e de capital superam o caixa gerado pelas operações. Isso é comum em empresas em crise, como a Gol (GOLL4) durante períodos de baixa demanda no setor aéreo. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades financeiras graves. A análise deve focar na estrutura de custos, endividamento e estratégias de recuperação. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
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
                    Um FCF Yield entre 0% e 3% reflete um fluxo de caixa livre baixo, indicando que a empresa tem pouca flexibilidade financeira após seus investimentos. Isso é comum em setores com alta necessidade de capital, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a oscilações econômicas ou aumento de custos. É importante analisar a capacidade de melhorar a geração de caixa e reduzir despesas de capital. Análises complementares de margem EBITDA e endividamento são recomendadas.
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
                    Um FCF Yield entre 3% e 6% indica um fluxo de caixa livre aceitável, típico de empresas com boa gestão financeira e flexibilidade moderada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua eficiência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre geração de caixa e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência do fluxo de caixa livre e o impacto de investimentos de capital.
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
                    Um FCF Yield entre 6% e 10% reflete um fluxo de caixa livre robusto, indicando que a empresa gera caixa significativo após investimentos. Empresas como a Ambev (ABEV3), com forte controle de custos e liderança de mercado, frequentemente apresentam FCF Yield nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e potencial para dividendos ou reinvestimento. No entanto, é importante verificar a sustentabilidade do fluxo de caixa, analisando fatores como concorrência, custos operacionais e necessidade de investimentos futuros.
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
                    Um FCF Yield acima de 10% é excepcional, indicando que a empresa gera um fluxo de caixa livre extremamente alto em relação ao preço da ação. Isso pode ocorrer em empresas com alta eficiência operacional, como a Vale (VALE3) em períodos de preços elevados de commodities. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois valores tão altos podem não ser sustentáveis a longo prazo, especialmente em setores cíclicos. A análise deve focar na escalabilidade do modelo de negócios, barreiras de entrada e consistência do fluxo de caixa.
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
                Ocorreu um erro ao processar o FCF Yield: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o preço da ação for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o fluxo de caixa livre por ação e o preço da ação estejam corretos e sejam valores numéricos válidos.
                ''',
                'definicao': definicao,
                'agrupador': agrupador,
                'formula': formula
            }

        def evaluate_pl(pl):
            '''
            Avalia o Preço/Lucro (P/L) com base em faixas definidas para o mercado brasileiro:
            - P/L < 0: Crítico (lucro negativo, risco elevado)
            - 0 ≤ P/L ≤ 10: Ótimo (subvalorizado, oportunidade de compra)
            - 10 < P/L ≤ 15: Moderado (valuation justo, crescimento moderado)
            - 15 < P/L ≤ 20: Ruim (sobrevalorizado, cautela necessária)
            - 20 < P/L ≤ 30: Péssimo (muito caro, alto risco)
            - P/L > 30: Fora da faixa (extremamente sobrevalorizado, risco elevado)
            '''
            definicao = '''
            O Preço/Lucro (P/L) compara o preço da ação ao lucro por ação, calculado como (Preço da Ação / Lucro por Ação). É um indicador de valuation amplamente utilizado para avaliar se uma ação está cara ou barata em relação aos lucros da empresa. Um P/L baixo pode indicar subvalorização, enquanto um valor alto sugere que o mercado espera crescimento significativo. É especialmente útil em setores estáveis, mas menos eficaz em empresas com lucros voláteis ou negativos. Deve ser analisado em conjunto com o crescimento dos lucros (PEG Ratio) e outros indicadores de valuation, como P/S e EV/EBITDA.
            '''
            agrupador = 'Valuation'
            formula = 'P/L = Preço da Ação / Lucro por Ação'

            try:
                if pl < 0:
                    return {
                        'classificacao': 'Crítico',
                        'faixa': 'P/L < 0',
                        'descricao': '''
                        Um P/L negativo indica que a empresa está gerando prejuízo, tornando o indicador inválido para avaliar valuation. Isso é comum em empresas em crise, como a Oi (OIBR3) durante reestruturações, ou em empresas em fase inicial, como startups de tecnologia. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades financeiras. A análise deve focar na estrutura de custos, endividamento e estratégias de recuperação. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 0 <= pl <= 10:
                    return {
                        'classificacao': 'Ótimo',
                        'faixa': '0 <= P/L <= 10',
                        'descricao': '''
                        Um P/L entre 0 e 10 sugere que a ação está subvalorizada em relação aos seus lucros, indicando uma potencial oportunidade de compra. Isso é comum em setores cíclicos durante períodos de baixa, como a Vale (VALE3) em momentos de preços deprimidos de commodities. Para investidores, essa faixa é atrativa, especialmente se a empresa tem potencial de crescimento de lucros. No entanto, é importante verificar se o baixo P/L não reflete problemas estruturais, como margens decrescentes. Análises complementares de fluxo de caixa livre e margem líquida são recomendadas.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 10 < pl <= 15:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '10 < P/L <= 15',
                        'descricao': '''
                        Um P/L entre 10 e 15 reflete um valuation justo, típico de empresas com lucros estáveis e crescimento moderado. No Brasil, empresas como a Ambev (ABEV3) frequentemente operam nessa faixa devido à sua consistência no setor de bebidas. Para investidores, essa faixa sugere um equilíbrio entre preço e fundamentos, sendo adequada para quem busca retornos consistentes sem grande exposição a riscos de sobrevalorização. É importante avaliar o crescimento dos lucros e o contexto setorial para confirmar a sustentabilidade do valuation.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 15 < pl <= 20:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '15 < P/L <= 20',
                        'descricao': '''
                        Um P/L entre 15 e 20 sugere que a ação está sobrevalorizada em relação aos seus lucros, indicando que o mercado espera crescimento significativo. Empresas como a Raia Drogasil (RADL3) podem atingir essa faixa em períodos de expansão agressiva no varejo farmacêutico. Para investidores, essa faixa exige cautela, pois o preço elevado pode não se sustentar se o crescimento dos lucros não acompanhar as expectativas. Análise de tendências setoriais, margens operacionais e PEG Ratio é recomendada.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 20 < pl <= 30:
                    return {
                        'classificacao': 'Péssimo',
                        'faixa': '20 < P/L <= 30',
                        'descricao': '''
                        Um P/L entre 20 e 30 indica que a ação é muito cara em relação aos seus lucros, sugerindo que o mercado está pagando um prêmio elevado por expectativas futuras. Empresas como a Localiza (RENT3) podem apresentar P/L nessa faixa em momentos de otimismo com expansão. Para investidores, essa faixa representa alto risco, pois o preço elevado pode não ser justificado se os lucros não corresponderem às expectativas. É essencial analisar o histórico de crescimento, a escalabilidade do modelo de negócios e o contexto competitivo.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif pl > 30:
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'P/L > 30',
                        'descricao': '''
                        Um P/L acima de 30 é extremamente elevado, geralmente associado a empresas com altíssimas expectativas de crescimento ou especulação de mercado. No Brasil, o Nubank (NUBR33) já apresentou P/L nessa faixa após sua estreia na bolsa, devido ao entusiasmo com sua disrupção no setor financeiro. Para investidores, essa faixa é de altíssimo risco, pois o preço reflete mais especulação do que fundamentos atuais. A análise deve focar em projeções de longo prazo, execução estratégica e comparação com peers globais, mas é uma escolha apenas para investidores tolerantes a risco elevado.
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
                    Ocorreu um erro ao processar o P/L: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o lucro por ação for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o preço da ação e o lucro por ação estejam corretos e sejam valores numéricos válidos.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }

        def evaluate_peg_ratio(peg_ratio):
            '''
            Avalia o PEG Ratio (P/L ajustado pelo crescimento) com base em faixas definidas para o mercado brasileiro:
            - PEG Ratio < 0: Crítico (lucro ou crescimento negativo, risco elevado)
            - 0 ≤ PEG Ratio ≤ 0.5: Ótimo (subvalorizado em relação ao crescimento)
            - 0.5 < PEG Ratio ≤ 1: Moderado (valuation justo em relação ao crescimento)
            - 1 < PEG Ratio ≤ 1.5: Ruim (sobrevalorizado em relação ao crescimento)
            - 1.5 < PEG Ratio ≤ 2: Péssimo (muito caro em relação ao crescimento)
            - PEG Ratio > 2: Fora da faixa (extremamente sobrevalorizado, risco elevado)
            '''
            definicao = '''
            O PEG Ratio ajusta o P/L pela taxa de crescimento esperada dos lucros, calculado como (P/L / Crescimento Anual Esperado do Lucro). É um indicador de valuation que considera o crescimento futuro, sendo útil para avaliar se uma ação cara (alto P/L) é justificada pelo seu potencial de crescimento. Um PEG baixo sugere subvalorização, enquanto um valor alto indica que a ação pode estar cara em relação ao crescimento esperado. É especialmente relevante para empresas em crescimento, como tecnologia, mas depende da confiabilidade das projeções de crescimento.
            '''
            agrupador = 'Valuation'
            formula = 'PEG Ratio = P/L / Crescimento Anual Esperado do Lucro (%)'

            try:
                if peg_ratio < 0:
                    return {
                        'classificacao': 'Crítico',
                        'faixa': 'PEG Ratio < 0',
                        'descricao': '''
                        Um PEG Ratio negativo indica que a empresa tem lucro ou crescimento esperado negativo, tornando o indicador inválido para avaliar valuation. Isso é comum em empresas em crise, como a Gol (GOLL4) durante períodos de baixa demanda, ou em startups com prejuízos, como a Nubank (NUBR33) em fases iniciais. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades financeiras ou incerteza nas projeções. A análise deve focar na estrutura de custos, endividamento e confiabilidade das projeções de crescimento.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 0 <= peg_ratio <= 0.5:
                    return {
                        'classificacao': 'Ótimo',
                        'faixa': '0 <= PEG Ratio <= 0.5',
                        'descricao': '''
                        Um PEG Ratio entre 0 e 0.5 sugere que a ação está subvalorizada em relação ao seu crescimento esperado, indicando uma potencial oportunidade de compra. Isso pode ocorrer em empresas com lucros estáveis e projeções de crescimento robustas, como a Weg (WEGE3) em períodos de expansão. Para investidores, essa faixa é atrativa, especialmente se as projeções de crescimento são confiáveis. No entanto, é importante verificar a qualidade das estimativas de crescimento e a sustentabilidade dos lucros. Análises complementares de P/L e fluxo de caixa livre são recomendadas.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 0.5 < peg_ratio <= 1:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '0.5 < PEG Ratio <= 1',
                        'descricao': '''
                        Um PEG Ratio entre 0.5 e 1 reflete um valuation justo em relação ao crescimento esperado, típico de empresas com lucros e crescimento equilibrados. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua consistência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre preço e potencial de crescimento, sendo adequada para quem busca retornos consistentes. É importante avaliar a confiabilidade das projeções de crescimento e o contexto setorial.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 1 < peg_ratio <= 1.5:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '1 < PEG Ratio <= 1.5',
                        'descricao': '''
                        Um PEG Ratio entre 1 e 1.5 sugere que a ação está sobrevalorizada em relação ao seu crescimento esperado, indicando que o mercado pode estar pagando um prêmio elevado. Empresas como a Magazine Luiza (MGLU3) podem atingir essa faixa em períodos de otimismo com o e-commerce. Para investidores, essa faixa exige cautela, pois o preço elevado pode não se sustentar se o crescimento dos lucros não acompanhar as expectativas. Análise de tendências setoriais, margens operacionais e confiabilidade das projeções é recomendada.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 1.5 < peg_ratio <= 2:
                    return {
                        'classificacao': 'Péssimo',
                        'faixa': '1.5 < PEG Ratio <= 2',
                        'descricao': '''
                        Um PEG Ratio entre 1.5 e 2 indica que a ação é muito cara em relação ao seu crescimento esperado, sugerindo que o mercado está pagando um prêmio excessivo. Empresas como a Localiza (RENT3) podem apresentar PEG nessa faixa em momentos de expansão agressiva. Para investidores, essa faixa representa alto risco, pois o preço elevado pode não ser justificado se o crescimento dos lucros não corresponder às expectativas. É essencial analisar o histórico de crescimento, a escalabilidade do modelo de negócios e o contexto competitivo.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif peg_ratio > 2:
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'PEG Ratio > 2',
                        'descricao': '''
                        Um PEG Ratio acima de 2 é extremamente elevado, geralmente associado a empresas com altíssimas expectativas de crescimento ou especulação de mercado. No Brasil, o Nubank (NUBR33) já apresentou PEG nessa faixa após sua estreia na bolsa, devido ao entusiasmo com sua disrupção no setor financeiro. Para investidores, essa faixa é de altíssimo risco, pois o preço reflete mais especulação do que fundamentos atuais. A análise deve focar em projeções de longo prazo, execução estratégica e comparação com peers globais, mas é uma escolha apenas para investidores tolerantes a risco elevado.
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
                    Ocorreu um erro ao processar o PEG Ratio: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o crescimento anual esperado do lucro for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o P/L e o crescimento esperado estejam corretos e sejam valores numéricos válidos.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }

        def evaluate_ebitda_margin_growth(ebitda_margin_growth):
            '''
            Avalia o Crescimento da Margem EBITDA com base em faixas definidas para o mercado brasileiro:
            - Crescimento Margem EBITDA < 0%: Crítico (redução da margem, risco elevado)
            - 0% ≤ Crescimento Margem EBITDA ≤ 2%: Ruim (crescimento baixo ou estagnação)
            - 2% < Crescimento Margem EBITDA ≤ 5%: Moderado (crescimento aceitável)
            - 5% < Crescimento Margem EBITDA ≤ 10%: Ótimo (crescimento robusto)
            - Crescimento Margem EBITDA > 10%: Fora da faixa (crescimento excepcional, avaliar sustentabilidade)
            '''
            definicao = '''
            O Crescimento da Margem EBITDA mede a taxa anual de aumento da margem EBITDA (EBITDA / Receita Bruta) ao longo de um período, calculado como ((Margem EBITDA Final / Margem EBITDA Inicial)^(1/n) - 1), onde n é o número de anos. É um indicador que reflete a melhoria na eficiência operacional da empresa, mostrando se ela está conseguindo aumentar a proporção de receita que se converte em caixa operacional. Um crescimento alto sugere maior eficiência, enquanto um valor baixo ou negativo pode indicar aumento de custos ou pressão competitiva. Deve ser analisado em conjunto com margem EBITDA absoluta e fluxo de caixa.
            '''
            agrupador = 'Rentabilidade'
            formula = 'Crescimento Margem EBITDA = ((Margem EBITDA Final / Margem EBITDA Inicial)^(1/n) - 1)'

            try:
                if ebitda_margin_growth < 0:
                    return {
                        'classificacao': 'Crítico',
                        'faixa': 'Crescimento Margem EBITDA < 0%',
                        'descricao': '''
                        Um Crescimento da Margem EBITDA negativo indica que a margem operacional da empresa está diminuindo, sugerindo aumento de custos ou pressão competitiva. Isso é comum em empresas em crise, como a CSN (CSNA3) durante quedas de preços de commodities. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades na eficiência operacional. A análise deve focar na estrutura de custos, estratégias de redução de despesas e tendências setoriais. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de recuperação.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 0 <= ebitda_margin_growth <= 2:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '0% <= Crescimento Margem EBITDA <= 2%',
                        'descricao': '''
                        Um Crescimento da Margem EBITDA entre 0% e 2% reflete crescimento baixo ou estagnação, indicando que a empresa tem dificuldade em melhorar sua eficiência operacional. Isso é comum em setores maduros ou com alta concorrência, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a aumentos de custos ou perda de mercado. É importante analisar estratégias de redução de custos e potencial de melhoria da margem. Análises complementares de margem EBITDA absoluta e fluxo de caixa são recomendadas.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 2 < ebitda_margin_growth <= 5:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '2% < Crescimento Margem EBITDA <= 5%',
                        'descricao': '''
                        Um Crescimento da Margem EBITDA entre 2% e 5% indica melhoria aceitável na eficiência operacional, típico de empresas com boa gestão de custos. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua consistência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre eficiência e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a sustentabilidade do crescimento, considerando fatores como concorrência e condições macroeconômicas.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 5 < ebitda_margin_growth <= 10:
                    return {
                        'classificacao': 'Ótimo',
                        'faixa': '5% < Crescimento Margem EBITDA <= 10%',
                        'descricao': '''
                        Um Crescimento da Margem EBITDA entre 5% e 10% reflete melhoria robusta na eficiência operacional, indicando que a empresa está aumentando significativamente a proporção de receita convertida em caixa operacional. Empresas como a Ambev (ABEV3), com forte controle de custos, frequentemente apresentam crescimento nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e potencial para aumento de lucros. No entanto, é importante verificar a sustentabilidade do crescimento, analisando fatores como concorrência e custos operacionais.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif ebitda_margin_growth > 10:
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'Crescimento Margem EBITDA > 10%',
                        'descricao': '''
                        Um Crescimento da Margem EBITDA acima de 10% é excepcional, indicando melhoria extremamente rápida na eficiência operacional. Isso é raro, mas pode ocorrer em empresas com forte inovação ou redução de custos, como a Weg (WEGE3) em períodos de alta eficiência. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois crescimentos tão altos podem não ser sustentáveis a longo prazo. A análise deve focar na escalabilidade do modelo de negócios, barreiras de entrada e consistência do crescimento.
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
                    Ocorreu um erro ao processar o Crescimento da Margem EBITDA: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se a margem EBITDA inicial for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que a margem EBITDA inicial, final e o número de anos estejam corretos e sejam valores numéricos válidos.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }

        def evaluate_net_debt_ebit(net_debt_ebit):
            '''
            Avalia a Dívida Líquida/EBIT com base em faixas definidas para o mercado brasileiro:
            - Dívida Líquida/EBIT < 0: Fora da faixa (sem dívida líquida ou EBIT negativo)
            - 0 ≤ Dívida Líquida/EBIT ≤ 1: Ótimo (endividamento muito baixo)
            - 1 < Dívida Líquida/EBIT ≤ 2: Moderado (endividamento aceitável)
            - 2 < Dívida Líquida/EBIT ≤ 3: Ruim (endividamento elevado)
            - 3 < Dívida Líquida/EBIT ≤ 4: Péssimo (endividamento muito alto)
            - Dívida Líquida/EBIT > 4: Crítico (endividamento excessivo, risco elevado)
            '''
            definicao = '''
            A Dívida Líquida/EBIT mede o nível de endividamento líquido da empresa em relação ao seu EBIT (Lucro Antes de Juros e Impostos), calculado como (Dívida Líquida / EBIT). É um indicador de alavancagem financeira que avalia quanto tempo a empresa levaria para pagar sua dívida líquida com base em sua geração de lucro operacional. Um valor baixo sugere solidez financeira, enquanto um valor alto indica maior risco financeiro devido à dependência de dívidas. É especialmente útil em setores intensivos em capital, como infraestrutura, mas deve ser analisado em conjunto com Dívida Líquida/EBITDA e fluxo de caixa livre.
            '''
            agrupador = 'Endividamento'
            formula = 'Dívida Líquida/EBIT = Dívida Líquida / EBIT'

            try:
                if net_debt_ebit < 0:
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'Dívida Líquida/EBIT < 0',
                        'descricao': '''
                        Uma Dívida Líquida/EBIT negativa pode indicar que a empresa não tem dívida líquida (caixa excede a dívida) ou que o EBIT é negativo. Empresas como a Totvs (TOTS3), com alta geração de caixa, podem apresentar valores negativos em períodos de forte liquidez. Para investidores, essa faixa pode ser positiva, mas também pode sugerir ineficiência na alocação de capital, como excesso de caixa ocioso. A análise deve focar na estratégia de uso do caixa e no retorno sobre o capital investido (ROIC) para avaliar a eficiência.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 0 <= net_debt_ebit <= 1:
                    return {
                        'classificacao': 'Ótimo',
                        'faixa': '0 <= Dívida Líquida/EBIT <= 1',
                        'descricao': '''
                        Uma Dívida Líquida/EBIT entre 0 e 1 reflete endividamento muito baixo, indicando que a empresa poderia quitar sua dívida líquida rapidamente com seu lucro operacional. Empresas como a Vale (VALE3) em períodos de alta nos preços de minério de ferro frequentemente operam nessa faixa. Para investidores, essa faixa é atrativa, pois sugere baixo risco financeiro e flexibilidade para investimentos ou retorno aos acionistas. É importante verificar a consistência da geração de EBIT e a composição da dívida.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 1 < net_debt_ebit <= 2:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '1 < Dívida Líquida/EBIT <= 2',
                        'descricao': '''
                        Uma Dívida Líquida/EBIT entre 1 e 2 indica endividamento aceitável, com equilíbrio entre dívida e geração de lucro operacional. No Brasil, empresas como a Ambev (ABEV3) frequentemente operam nessa faixa devido à sua gestão financeira eficiente. Para investidores, essa faixa sugere risco moderado, com a empresa capaz de suportar oscilações econômicas sem grandes pressões financeiras. É importante avaliar a estrutura da dívida e a capacidade de geração de caixa para confirmar a saúde financeira.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 2 < net_debt_ebit <= 3:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '2 < Dívida Líquida/EBIT <= 3',
                        'descricao': '''
                        Uma Dívida Líquida/EBIT entre 2 e 3 sugere endividamento elevado, indicando que a empresa levaria um tempo considerável para quitar sua dívida com seu lucro operacional. Isso é comum em setores com alta alavancagem, como a Petrobras (PETR4) em períodos de investimentos pesados. Para investidores, essa faixa exige cautela, pois a empresa pode ser vulnerável a aumentos de juros ou quedas na receita. A análise deve focar na capacidade de pagamento da dívida e custos de financiamento.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 3 < net_debt_ebit <= 4:
                    return {
                        'classificacao': 'Péssimo',
                        'faixa': '3 < Dívida Líquida/EBIT <= 4',
                        'descricao': '''
                        Uma Dívida Líquida/EBIT entre 3 e 4 reflete endividamento muito alto, indicando risco significativo de pressão financeira. Empresas como a Oi (OIBR3) já estiveram nessa faixa durante crises, enfrentando dificuldades para gerenciar dívidas elevadas. Para investidores, essa faixa representa alto risco, exigindo análise detalhada da estrutura de capital, covenants de dívida e planos de desalavancagem para avaliar a viabilidade financeira.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif net_debt_ebit > 4:
                    return {
                        'classificacao': 'Crítico',
                        'faixa': 'Dívida Líquida/EBIT > 4',
                        'descricao': '''
                        Uma Dívida Líquida/EBIT acima de 4 indica endividamento excessivo, sugerindo que a empresa depende fortemente de dívidas em relação ao seu lucro operacional. Isso é alarmante e típico de empresas em dificuldades financeiras, como a Gol (GOLL4) em períodos de crise no setor aéreo. Para investidores, essa faixa é de altíssimo risco, com possibilidade de reestruturação ou insolvência. A análise deve focar na capacidade de geração de caixa, estratégias de redução de dívida e covenants financeiros para avaliar a viabilidade.
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
                    Ocorreu um erro ao processar a Dívida Líquida/EBIT: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o EBIT for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que a dívida líquida e o EBIT estejam corretos e sejam valores numéricos válidos.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula
                }

        def evaluate_beta(beta):
            '''
            Avalia o Beta com base em faixas definidas para o mercado brasileiro:
            - Beta < 0.5: Ótimo (baixa volatilidade, defensivo)
            - 0.5 ≤ Beta ≤ 0.8: Moderado (volatilidade abaixo do mercado)
            - 0.8 < Beta ≤ 1.2: Neutro (volatilidade alinhada ao mercado)
            - 1.2 < Beta ≤ 1.5: Ruim (volatilidade acima do mercado)
            - 1.5 < Beta ≤ 2: Péssimo (alta volatilidade, risco elevado)
            - Beta > 2: Fora da faixa (volatilidade extrema, risco muito elevado)
            '''
            definicao = '''
            O Beta mede a volatilidade da ação em relação ao mercado, calculado como a covariância entre os retornos da ação e do mercado dividida pela variância do mercado. Um Beta de 1 indica que a ação se move em linha com o mercado (ex.: Ibovespa), enquanto valores acima ou abaixo de 1 indicam maior ou menor volatilidade, respectivamente. É um indicador de risco sistemático, útil para avaliar o comportamento da ação em diferentes cenários econômicos. Empresas com Beta baixo são defensivas, enquanto as com Beta alto são mais arriscadas. Deve ser analisado em conjunto com outros indicadores de risco, como endividamento e fluxo de caixa.
            '''
            agrupador = 'Risco'
            formula = 'Beta = Covariância(Retornos da Ação, Retornos do Mercado) / Variância(Retornos do Mercado)'

            try:
                if beta < 0.5:
                    return {
                        'classificacao': 'Ótimo',
                        'faixa': 'Beta < 0.5',
                        'descricao': '''
                        Um Beta abaixo de 0.5 indica que a ação é pouco volátil em relação ao mercado, sugerindo um perfil defensivo. Empresas como a Engie Brasil (EGIE3), do setor de energia, frequentemente apresentam Beta baixo devido à estabilidade de suas receitas. Para investidores, essa faixa é atrativa para quem busca proteção contra oscilações do mercado, especialmente em períodos de incerteza econômica. No entanto, é importante verificar se o baixo Beta não reflete estagnação no crescimento. Análises complementares de Dividend Yield e ROE são recomendadas.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 0.5 <= beta <= 0.8:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '0.5 <= Beta <= 0.8',
                        'descricao': '''
                        Um Beta entre 0.5 e 0.8 reflete volatilidade abaixo do mercado, indicando que a ação é menos sensível a movimentos do mercado. Empresas como a Ambev (ABEV3) frequentemente operam nessa faixa devido à sua estabilidade no setor de bebidas. Para investidores, essa faixa sugere um equilíbrio entre segurança e potencial de retorno, sendo adequada para quem busca retornos consistentes com risco moderado. É importante avaliar a consistência dos lucros e o contexto setorial para confirmar a robustez financeira.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 0.8 < beta <= 1.2:
                    return {
                        'classificacao': 'Neutro',
                        'faixa': '0.8 < Beta <= 1.2',
                        'descricao': '''
                        Um Beta entre 0.8 e 1.2 indica que a ação tem volatilidade alinhada ao mercado, movendo-se de forma semelhante ao Ibovespa. Empresas como a Vale (VALE3) frequentemente operam nessa faixa, refletindo sua exposição ao mercado de commodities. Para investidores, essa faixa é neutra, adequada para quem busca acompanhar o desempenho geral do mercado. É importante avaliar o impacto de fatores setoriais e macroeconômicos no desempenho da ação.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 1.2 < beta <= 1.5:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '1.2 < Beta <= 1.5',
                        'descricao': '''
                        Um Beta entre 1.2 e 1.5 sugere que a ação é mais volátil que o mercado, indicando maior risco em períodos de queda. Empresas como a Magazine Luiza (MGLU3) podem apresentar Beta nessa faixa em momentos de expansão agressiva no e-commerce. Para investidores, essa faixa exige cautela, pois a ação pode sofrer quedas mais acentuadas em cenários adversos. Análise de fundamentos, como margens operacionais e endividamento, é recomendada para avaliar a resiliência da empresa.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif 1.5 < beta <= 2:
                    return {
                        'classificacao': 'Péssimo',
                        'faixa': '1.5 < Beta <= 2',
                        'descricao': '''
                        Um Beta entre 1.5 e 2 reflete alta volatilidade, indicando que a ação é significativamente mais sensível a movimentos do mercado. Empresas como a Petrobras (PETR4) podem apresentar Beta nessa faixa devido à sua exposição a preços de petróleo e riscos regulatórios. Para investidores, essa faixa representa alto risco, exigindo análise detalhada da exposição setorial, endividamento e estratégias de mitigação de risco.
                        ''',
                        'definicao': definicao,
                        'agrupador': agrupador,
                        'formula': formula
                    }
                elif beta > 2:
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'Beta > 2',
                        'descricao': '''
                        Um Beta acima de 2 indica volatilidade extrema, sugerindo que a ação é altamente sensível a movimentos do mercado. Isso é comum em empresas com alto risco operacional ou financeiro, como a Gol (GOLL4) em períodos de crise no setor aéreo. Para investidores, essa faixa é de altíssimo risco, adequada apenas para quem tolera grandes oscilações. A análise deve focar na saúde financeira, exposição setorial e estratégias de gestão de risco para avaliar a viabilidade do investimento.
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
                    Ocorreu um erro ao processar o Beta: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se os dados de retornos da ação ou do mercado forem inválidos. Verifique os dados de entrada, assegurando que o Beta esteja correto e seja um valor numérico válido.
                    ''',
                    'definicao': definicao,
                    'agrupador': agrupador,
                    'formula': formula

                def evaluate_giro_ativos(giro_ativos):
                    '''
                    Avalia o Giro de Ativos com base em faixas definidas para o mercado brasileiro:
                    - Giro de Ativos < 0.2: Crítico (baixa eficiência na utilização de ativos)
                    - 0.2 ≤ Giro de Ativos ≤ 0.5: Ruim (eficiência limitada na utilização de ativos)
                    - 0.5 < Giro de Ativos ≤ 1: Moderado (eficiência aceitável na utilização de ativos)
                    - 1 < Giro de Ativos ≤ 1.5: Ótimo (alta eficiência na utilização de ativos)
                    - Giro de Ativos > 1.5: Fora da faixa (eficiência excepcional, avaliar sustentabilidade)
                    '''
                    definicao = '''
                    O Giro de Ativos mede a eficiência com que a empresa utiliza seus ativos para gerar receita, calculado como (Receita Bruta / Ativos Totais). Um valor alto indica que a empresa gera muita receita por unidade de ativo, refletindo eficiência operacional. Um valor baixo pode indicar subutilização de ativos ou baixa demanda. É especialmente útil em setores intensivos em capital, como indústria e varejo, mas deve ser analisado em conjunto com ROA e margem líquida para avaliar a rentabilidade global.
                    '''
                    agrupador = 'Eficiência'
                    formula = 'Giro de Ativos = Receita Bruta / Ativos Totais'

                    try:
                        if giro_ativos < 0.2:
                            return {
                                'classificacao': 'Crítico',
                                'faixa': 'Giro de Ativos < 0.2',
                                'descricao': '''
                                Um Giro de Ativos abaixo de 0.2 indica baixa eficiência na utilização dos ativos, sugerindo que a empresa gera pouca receita em relação aos seus recursos. Isso é comum em empresas com ativos ociosos ou em crise, como a Oi (OIBR3) durante períodos de reestruturação. Para investidores, essa faixa é um alerta de risco elevado, pois reflete ineficiência operacional grave. A análise deve focar na gestão de ativos, estratégias de aumento de receita e redução de custos. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de recuperação.
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
                                Um Giro de Ativos entre 0.2 e 0.5 reflete eficiência limitada na utilização dos ativos, indicando que a empresa gera receita moderada em relação aos seus recursos. Isso é comum em setores com ativos pesados, como siderurgia (ex.: Usiminas - USIM5). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a oscilações econômicas ou ineficiência operacional. É importante analisar estratégias de otimização de ativos e potencial de aumento de receita. Análises complementares de ROA e margem líquida são recomendadas.
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
                                Um Giro de Ativos entre 0.5 e 1 indica eficiência aceitável na utilização dos ativos, típico de empresas com boa gestão operacional. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua eficiência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre eficiência e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência do giro de ativos e o impacto de investimentos em novos ativos.
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
                                Um Giro de Ativos entre 1 e 1.5 reflete alta eficiência na utilização dos ativos, indicando que a empresa gera receita significativa com seus recursos. Empresas como a Ambev (ABEV3), com forte controle operacional, frequentemente apresentam giro nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez operacional e potencial para aumento de lucros. No entanto, é importante verificar se o alto giro não reflete subinvestimento em ativos. Análises de ROIC e fluxo de caixa são recomendadas.
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
                                Um Giro de Ativos acima de 1.5 é excepcional, indicando que a empresa gera receita extremamente alta em relação aos seus ativos. Isso é raro, mas pode ocorrer em empresas com modelos de negócios enxutos, como a Weg (WEGE3) em períodos de alta eficiência. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois giros tão altos podem não ser sustentáveis a longo prazo, especialmente se dependerem de condições de mercado favoráveis. A análise deve focar na sustentabilidade do modelo de negócios e barreiras de entrada.
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
                            Ocorreu um erro ao processar o Giro de Ativos: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se os ativos totais forem zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que a receita bruta e os ativos totais estejam corretos e sejam valores numéricos válidos.
                            ''',
                            'definicao': definicao,
                            'agrupador': agrupador,
                            'formula': formula
                        }

                def evaluate_margem_liquida(margem_liquida):
                    '''
                    Avalia a Margem Líquida com base em faixas definidas para o mercado brasileiro:
                    - Margem Líquida < 0%: Crítico (prejuízo, risco elevado)
                    - 0% ≤ Margem Líquida ≤ 5%: Ruim (rentabilidade baixa)
                    - 5% < Margem Líquida ≤ 10%: Moderado (rentabilidade aceitável)
                    - 10% < Margem Líquida ≤ 20%: Ótimo (rentabilidade robusta)
                    - Margem Líquida > 20%: Fora da faixa (rentabilidade excepcional, avaliar sustentabilidade)
                    '''
                    definicao = '''
                    A Margem Líquida mede a proporção do lucro líquido em relação à receita bruta, calculada como (Lucro Líquido / Receita Bruta). É um indicador de rentabilidade que reflete a eficiência da empresa em converter receita em lucro após todas as despesas, incluindo impostos e juros. Uma margem alta sugere boa gestão de custos e precificação, enquanto uma margem baixa ou negativa indica dificuldades financeiras. É especialmente útil para comparar empresas dentro do mesmo setor, mas deve ser analisado em conjunto com crescimento da receita e ROE.
                    '''
                    agrupador = 'Rentabilidade'
                    formula = 'Margem Líquida = Lucro Líquido / Receita Bruta'

                    try:
                        if margem_liquida < 0:
                            return {
                                'classificacao': 'Crítico',
                                'faixa': 'Margem Líquida < 0%',
                                'descricao': '''
                                Uma Margem Líquida negativa indica que a empresa está gerando prejuízo, com despesas superando a receita. Isso é comum em empresas em crise, como a Gol (GOLL4) durante períodos de baixa demanda no setor aéreo. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades financeiras graves. A análise deve focar na estrutura de custos, endividamento e estratégias de recuperação. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 0 <= margem_liquida <= 5:
                            return {
                                'classificacao': 'Ruim',
                                'faixa': '0% <= Margem Líquida <= 5%',
                                'descricao': '''
                                Uma Margem Líquida entre 0% e 5% reflete rentabilidade baixa, indicando que a empresa tem dificuldade em converter receita em lucro significativo. Isso é comum em setores com margens apertadas, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a aumentos de custos ou oscilações econômicas. É importante analisar estratégias de redução de custos e potencial de melhoria da margem. Análises complementares de giro de ativos e fluxo de caixa são recomendadas.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 5 < margem_liquida <= 10:
                            return {
                                'classificacao': 'Moderado',
                                'faixa': '5% < Margem Líquida <= 10%',
                                'descricao': '''
                                Uma Margem Líquida entre 5% e 10% indica rentabilidade aceitável, típico de empresas com boa gestão de custos e operações estáveis. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua eficiência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência da margem e o impacto de fatores macroeconômicos.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 10 < margem_liquida <= 20:
                            return {
                                'classificacao': 'Ótimo',
                                'faixa': '10% < Margem Líquida <= 20%',
                                'descricao': '''
                                Uma Margem Líquida entre 10% e 20% reflete rentabilidade robusta, indicando que a empresa converte uma proporção significativa de sua receita em lucro. Empresas como a Ambev (ABEV3), com forte controle de custos, frequentemente apresentam margem nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e potencial para dividendos ou reinvestimento. No entanto, é importante verificar a sustentabilidade da margem, analisando concorrência e custos operacionais.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif margem_liquida > 20:
                            return {
                                'classificacao': 'Fora da faixa',
                                'faixa': 'Margem Líquida > 20%',
                                'descricao': '''
                                Uma Margem Líquida acima de 20% é excepcional, indicando que a empresa converte uma proporção extremamente alta de sua receita em lucro. Isso é raro, mas pode ocorrer em empresas com alta eficiência operacional, como a Weg (WEGE3) em períodos de forte desempenho. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois margens tão altas podem não ser sustentáveis a longo prazo. A análise deve focar na escalabilidade do modelo de negócios, barreiras de entrada e consistência da rentabilidade.
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
                            Ocorreu um erro ao processar a Margem Líquida: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o lucro líquido e a receita bruta estejam corretos e sejam valores numéricos válidos.
                            ''',
                            'definicao': definicao,
                            'agrupador': agrupador,
                            'formula': formula
                        }

                def evaluate_debt_coverage(debt_coverage):
                    '''
                    Avalia a Cobertura de Juros com base em faixas definidas para o mercado brasileiro:
                    - Cobertura de Juros < 1: Crítico (incapacidade de cobrir juros, risco elevado)
                    - 1 ≤ Cobertura de Juros ≤ 2: Ruim (cobertura limitada de juros)
                    - 2 < Cobertura de Juros ≤ 4: Moderado (cobertura aceitável de juros)
                    - 4 < Cobertura de Juros ≤ 6: Ótimo (cobertura robusta de juros)
                    - Cobertura de Juros > 6: Fora da faixa (cobertura excepcional, baixo risco financeiro)
                    '''
                    definicao = '''
                    A Cobertura de Juros mede a capacidade da empresa de pagar os juros de suas dívidas com base no EBIT, calculada como (EBIT / Despesas com Juros). É um indicador de saúde financeira que avalia o risco de inadimplência em relação às obrigações de dívida. Um valor alto sugere que a empresa tem folga para cobrir seus juros, enquanto um valor baixo indica dificuldades financeiras. É especialmente relevante em setores com alta alavancagem, como infraestrutura, mas deve ser analisado em conjunto com Dívida Líquida/EBITDA e fluxo de caixa livre.
                    '''
                    agrupador = 'Endividamento'
                    formula = 'Cobertura de Juros = EBIT / Despesas com Juros'

                    try:
                        if debt_coverage < 1:
                            return {
                                'classificacao': 'Crítico',
                                'faixa': 'Cobertura de Juros < 1',
                                'descricao': '''
                                Uma Cobertura de Juros abaixo de 1 indica que a empresa não gera EBIT suficiente para cobrir suas despesas com juros, sugerindo alto risco de inadimplência. Isso é comum em empresas em crise, como a Oi (OIBR3) durante períodos de reestruturação. Para investidores, essa faixa é um alerta grave, pois reflete dificuldades financeiras severas. A análise deve focar na estrutura de dívida, planos de desalavancagem e geração de caixa. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de recuperação.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 1 <= debt_coverage <= 2:
                            return {
                                'classificacao': 'Ruim',
                                'faixa': '1 <= Cobertura de Juros <= 2',
                                'descricao': '''
                                Uma Cobertura de Juros entre 1 e 2 reflete capacidade limitada de cobrir despesas com juros, indicando que a empresa opera com margem de segurança estreita. Isso é comum em setores com alta alavancagem, como a Petrobras (PETR4) em períodos de investimentos pesados. Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a aumentos de juros ou quedas na receita. É importante analisar a estrutura da dívida e a geração de caixa operacional.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 2 < debt_coverage <= 4:
                            return {
                                'classificacao': 'Moderado',
                                'faixa': '2 < Cobertura de Juros <= 4',
                                'descricao': '''
                                Uma Cobertura de Juros entre 2 e 4 indica capacidade aceitável de cobrir despesas com juros, com uma margem de segurança razoável. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua gestão financeira equilibrada. Para investidores, essa faixa sugere um equilíbrio entre risco e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência do EBIT e a composição da dívida.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 4 < debt_coverage <= 6:
                            return {
                                'classificacao': 'Ótimo',
                                'faixa': '4 < Cobertura de Juros <= 6',
                                'descricao': '''
                                Uma Cobertura de Juros entre 4 e 6 reflete capacidade robusta de cobrir despesas com juros, indicando solidez financeira. Empresas como a Ambev (ABEV3), com forte geração de caixa, frequentemente apresentam cobertura nessa faixa. Para investidores, essa faixa é atrativa, pois sugere resiliência a choques financeiros e flexibilidade para investimentos ou dividendos. No entanto, é importante verificar a sustentabilidade do EBIT e os custos de financiamento.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif debt_coverage > 6:
                            return {
                                'classificacao': 'Fora da faixa',
                                'faixa': 'Cobertura de Juros > 6',
                                'descricao': '''
                                Uma Cobertura de Juros acima de 6 é excepcional, indicando que a empresa tem uma margem de segurança extremamente alta para cobrir seus juros. Isso pode ocorrer em empresas com alta geração de caixa, como a Vale (VALE3) em períodos de preços elevados de commodities. Para investidores, essa faixa é altamente atrativa, mas pode indicar subalavancagem, com a empresa não utilizando dívida para alavancar retornos. A análise deve focar na estratégia de alocação de capital e ROIC.
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
                            Ocorreu um erro ao processar a Cobertura de Juros: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se as despesas com juros forem zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o EBIT e as despesas com juros estejam corretos e sejam valores numéricos válidos.
                            ''',
                            'definicao': definicao,
                            'agrupador': agrupador,
                            'formula': formula
                        }

                def evaluate_p_vp(p_vp):
                    '''
                    Avalia o Preço/Valor Patrimonial (P/VP) com base em faixas definidas para o mercado brasileiro:
                    - P/VP < 0.5: Ótimo (subvalorizado, oportunidade de compra)
                    - 0.5 ≤ P/VP ≤ 1: Moderado (valuation justo)
                    - 1 < P/VP ≤ 2: Ruim (sobrevalorizado, cautela necessária)
                    - 2 < P/VP ≤ 3: Péssimo (muito caro, alto risco)
                    - P/VP > 3: Fora da faixa (extremamente sobrevalorizado, risco elevado)
                    '''
                    definicao = '''
                    O Preço/Valor Patrimonial (P/VP) compara o preço da ação ao valor patrimonial por ação, calculado como (Preço da Ação / Patrimônio Líquido por Ação). É um indicador de valuation que avalia se a ação está cara ou barata em relação ao patrimônio líquido da empresa. Um P/VP baixo pode indicar subvalorização, enquanto um valor alto sugere que o mercado está pagando um prêmio elevado. É especialmente útil em setores com ativos tangíveis, como bancos e indústria, mas menos eficaz em empresas com ativos intangíveis elevados, como tecnologia.
                    '''
                    agrupador = 'Valuation'
                    formula = 'P/VP = Preço da Ação / Patrimônio Líquido por Ação'

                    try:
                        if p_vp < 0.5:
                            return {
                                'classificacao': 'Ótimo',
                                'faixa': 'P/VP < 0.5',
                                'descricao': '''
                                Um P/VP abaixo de 0.5 sugere que a ação está subvalorizada em relação ao seu patrimônio líquido, indicando uma potencial oportunidade de compra. Isso é comum em setores cíclicos durante períodos de baixa, como a Vale (VALE3) em momentos de preços deprimidos de commodities. Para investidores, essa faixa é atrativa, especialmente se a empresa tem ativos sólidos. No entanto, é importante verificar se o baixo P/VP não reflete problemas estruturais, como prejuízos recorrentes. Análises complementares de ROE e fluxo de caixa são recomendadas.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 0.5 <= p_vp <= 1:
                            return {
                                'classificacao': 'Moderado',
                                'faixa': '0.5 <= P/VP <= 1',
                                'descricao': '''
                                Um P/VP entre 0.5 e 1 reflete um valuation justo, típico de empresas com patrimônio líquido bem precificado. No Brasil, empresas como a Banco do Brasil (BBAS3) frequentemente operam nessa faixa devido à sua estabilidade no setor financeiro. Para investidores, essa faixa sugere um equilíbrio entre preço e fundamentos, sendo adequada para quem busca retornos consistentes sem grande exposição a riscos de sobrevalorização. É importante avaliar o ROE e a qualidade dos ativos.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 1 < p_vp <= 2:
                            return {
                                'classificacao': 'Ruim',
                                'faixa': '1 < P/VP <= 2',
                                'descricao': '''
                                Um P/VP entre 1 e 2 sugere que a ação está sobrevalorizada em relação ao seu patrimônio líquido, indicando que o mercado espera crescimento ou valor intangível significativo. Empresas como a Raia Drogasil (RADL3) podem atingir essa faixa em períodos de expansão no varejo farmacêutico. Para investidores, essa faixa exige cautela, pois o preço elevado pode não se sustentar sem crescimento robusto. Análise de ROE, crescimento dos lucros e contexto setorial é recomendada.
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
                                Um P/VP entre 2 e 3 indica que a ação é muito cara em relação ao seu patrimônio líquido, sugerindo que o mercado está pagando um prêmio elevado. Empresas como a Localiza (RENT3) podem apresentar P/VP nessa faixa em momentos de otimismo com expansão. Para investidores, essa faixa representa alto risco, pois o preço elevado pode não ser justificado sem crescimento excepcional. É essencial analisar o histórico de crescimento, a escalabilidade do modelo de negócios e o contexto competitivo.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif p_vp > 3:
                            return {
                                'classificacao': 'Fora da faixa',
                                'faixa': 'P/VP > 3',
                                'descricao': '''
                                Um P/VP acima de 3 é extremamente elevado, geralmente associado a empresas com altíssimas expectativas de crescimento ou ativos intangíveis significativos. No Brasil, o Nubank (NUBR33) já apresentou P/VP nessa faixa após sua estreia na bolsa, devido ao entusiasmo com sua disrupção no setor financeiro. Para investidores, essa faixa é de altíssimo risco, pois o preço reflete mais especulação do que fundamentos patrimoniais. A análise deve focar em projeções de longo prazo, execução estratégica e comparação com peers globais.
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
                            Ocorreu um erro ao processar o P/VP: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o patrimônio líquido por ação for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o preço da ação e o patrimônio líquido por ação estejam corretos e sejam valores numéricos válidos.
                            ''',
                            'definicao': definicao,
                            'agrupador': agrupador,
                            'formula': formula
                        }

                def evaluate_capex_receita(capex_receita):
                    '''
                    Avalia o Capex/Receita com base em faixas definidas para o mercado brasileiro:
                    - Capex/Receita < 5%: Fora da faixa (investimento muito baixo, possível subinvestimento)
                    - 5% ≤ Capex/Receita ≤ 10%: Ótimo (investimento equilibrado)
                    - 10% < Capex/Receita ≤ 20%: Moderado (investimento significativo)
                    - 20% < Capex/Receita ≤ 30%: Ruim (investimento elevado, risco de alavancagem)
                    - Capex/Receita > 30%: Crítico (investimento excessivo, risco elevado)
                    '''
                    definicao = '''
                    O Capex/Receita mede a proporção da receita bruta destinada a investimentos em capital (Capex), calculado como (Capex / Receita Bruta). É um indicador que avalia o nível de investimento da empresa em ativos fixos ou expansão, refletindo sua estratégia de crescimento. Um valor baixo pode indicar subinvestimento, enquanto um valor alto sugere expansão agressiva, mas com risco de alavancagem. É especialmente relevante em setores intensivos em capital, como infraestrutura e mineração, mas deve ser analisado em conjunto com ROIC e fluxo de caixa livre.
                    '''
                    agrupador = 'Investimento'
                    formula = 'Capex/Receita = Capex / Receita Bruta'

                    try:
                        if capex_receita < 5:
                            return {
                                'classificacao': 'Fora da faixa',
                                'faixa': 'Capex/Receita < 5%',
                                'descricao': '''
                                Um Capex/Receita abaixo de 5% indica investimento muito baixo em relação à receita, sugerindo possível subinvestimento em ativos ou expansão. Isso pode ocorrer em empresas maduras com baixa necessidade de Capex, como a Engie Brasil (EGIE3). Para investidores, essa faixa pode ser positiva em termos de geração de caixa, mas também pode indicar estagnação no crescimento. A análise deve focar na estratégia de alocação de capital e no potencial de crescimento futuro.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 5 <= capex_receita <= 10:
                            return {
                                'classificacao': 'Ótimo',
                                'faixa': '5% <= Capex/Receita <= 10%',
                                'descricao': '''
                                Um Capex/Receita entre 5% e 10% reflete um nível de investimento equilibrado, indicando que a empresa aloca uma proporção adequada de sua receita para expansão ou manutenção de ativos. Empresas como a Ambev (ABEV3) frequentemente operam nessa faixa devido à sua gestão eficiente de capital. Para investidores, essa faixa é atrativa, pois sugere um equilíbrio entre crescimento e geração de caixa. É importante avaliar o ROIC e a qualidade dos investimentos realizados.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 10 < capex_receita <= 20:
                            return {
                                'classificacao': 'Moderado',
                                'faixa': '10% < Capex/Receita <= 20%',
                                'descricao': '''
                                Um Capex/Receita entre 10% e 20% indica investimento significativo, típico de empresas em fase de expansão ou renovação de ativos. No Brasil, empresas como a Vale (VALE3) podem operar nessa faixa durante períodos de investimentos em mineração. Para investidores, essa faixa sugere um compromisso com crescimento, mas exige atenção ao endividamento e ao retorno dos investimentos. Análise de fluxo de caixa livre e ROIC é recomendada.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 20 < capex_receita <= 30:
                            return {
                                'classificacao': 'Ruim',
                                'faixa': '20% < Capex/Receita <= 30%',
                                'descricao': '''
                                Um Capex/Receita entre 20% e 30% reflete investimento elevado, indicando uma estratégia agressiva de expansão que pode aumentar o endividamento. Empresas como a Petrobras (PETR4) podem apresentar Capex nessa faixa em períodos de grandes projetos. Para investidores, essa faixa exige cautela, pois o alto investimento pode pressionar a geração de caixa. A análise deve focar na viabilidade dos projetos, retorno esperado e estrutura de capital.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif capex_receita > 30:
                            return {
                                'classificacao': 'Crítico',
                                'faixa': 'Capex/Receita > 30%',
                                'descricao': '''
                                Um Capex/Receita acima de 30% indica investimento excessivo, sugerindo que a empresa está alocando uma proporção muito alta de sua receita para expansão ou manutenção de ativos. Isso é comum em empresas em fase inicial ou projetos intensivos, como a CSN (CSNA3) em períodos de expansão siderúrgica. Para investidores, essa faixa é de altíssimo risco, pois pode levar a pressões financeiras significativas. A análise deve focar na viabilidade dos projetos, fluxo de caixa livre e estratégias de financiamento.
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
                            Ocorreu um erro ao processar o Capex/Receita: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o Capex e a receita bruta estejam corretos e sejam valores numéricos válidos.
                            ''',
                            'definicao': definicao,
                            'agrupador': agrupador,
                            'formula': formula
                        }

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
                    A Liquidez Corrente mede a capacidade da empresa de pagar suas obrigações de curto prazo usando seus ativos circulantes, calculada como (Ativo Circulante / Passivo Circulante). É um indicador fundamental de saúde financeira de curto prazo, refletindo a liquidez imediata da empresa. Um valor alto sugere solidez financeira, enquanto um valor baixo indica risco de inadimplência. É especialmente útil em setores com alta rotatividade, como varejo, mas deve ser analisado em conjunto com Liquidez Seca e fluxo de caixa operacional.
                    '''
                    agrupador = 'Liquidez'
                    formula = 'Liquidez Corrente = Ativo Circulante / Passivo Circulante'

                    try:
                        if liquidez_corrente < 0.5:
                            return {
                                'classificacao': 'Crítico',
                                'faixa': 'Liquidez Corrente < 0.5',
                                'descricao': '''
                                Uma Liquidez Corrente abaixo de 0.5 indica dificuldade extrema em pagar obrigações de curto prazo, sugerindo risco elevado de inadimplência. Isso é comum em empresas em crise, como a Oi (OIBR3) durante períodos de reestruturação. Para investidores, essa faixa é um alerta grave, pois reflete problemas graves de liquidez. A análise deve focar na gestão de caixa, qualidade dos ativos circulantes e estratégias de recuperação. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
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
                                Uma Liquidez Corrente entre 0.5 e 1 reflete capacidade limitada de pagar obrigações de curto prazo, indicando que a empresa depende fortemente da conversão de ativos circulantes em caixa. Isso é comum em setores com estoques elevados, como varejo (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode enfrentar dificuldades em cenários de aperto financeiro. É importante analisar a qualidade dos ativos circulantes e a velocidade de conversão em caixa. Análises complementares de Liquidez Seca e fluxo de caixa são recomendadas.
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
                                Uma Liquidez Corrente entre 1 e 1.5 indica capacidade aceitável de pagar obrigações de curto prazo, com ativos circulantes cobrindo as obrigações de forma equilibrada. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua gestão eficiente de caixa. Para investidores, essa faixa sugere um equilíbrio entre liquidez e eficiência, sendo adequada para quem busca segurança financeira de curto prazo. É importante avaliar a composição dos ativos circulantes e a consistência do fluxo de caixa.
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
                                Uma Liquidez Corrente entre 1.5 e 2 reflete boa capacidade de pagar obrigações de curto prazo, com ativos circulantes excedendo confortavelmente o passivo circulante. Empresas como a Ambev (ABEV3), com forte geração de caixa, frequentemente apresentam liquidez nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e resiliência a choques de curto prazo. No entanto, é importante verificar se a liquidez elevada não reflete ineficiência na alocação de recursos. Análises de ciclo operacional e ROIC são recomendadas.
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
                                Uma Liquidez Corrente acima de 2 indica excesso de liquidez, com ativos circulantes muito superiores às obrigações de curto prazo. Isso pode ocorrer em empresas com alta geração de caixa, como a Vale (VALE3) em períodos de preços elevados de commodities. Para investidores, essa faixa pode ser positiva, pois sugere segurança financeira, mas também pode indicar ineficiência na alocação de capital, como excesso de caixa ocioso. A análise deve focar na estratégia de uso dos ativos circulantes (ex.: reinvestimento, dividendos) e no ROIC para avaliar a eficiência.
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
                            Ocorreu um erro ao processar a Liquidez Corrente: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o passivo circulante for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o ativo circulante e o passivo circulante estejam corretos e sejam valores numéricos válidos.
                            ''',
                            'definicao': definicao,
                            'agrupador': agrupador,
                            'formula': formula
                        }

                def evaluate_margem_bruta(margem_bruta):
                    '''
                    Avalia a Margem Bruta com base em faixas definidas para o mercado brasileiro:
                    - Margem Bruta < 10%: Crítico (baixa rentabilidade operacional, risco elevado)
                    - 10% ≤ Margem Bruta ≤ 20%: Ruim (rentabilidade operacional limitada)
                    - 20% < Margem Bruta ≤ 40%: Moderado (rentabilidade operacional aceitável)
                    - 40% < Margem Bruta ≤ 60%: Ótimo (rentabilidade operacional robusta)
                    - Margem Bruta > 60%: Fora da faixa (rentabilidade operacional excepcional, avaliar sustentabilidade)
                    '''
                    definicao = '''
                    A Margem Bruta mede a proporção da receita bruta que permanece após os custos diretos de produção, calculada como ((Receita Bruta - Custo dos Produtos Vendidos) / Receita Bruta). É um indicador de rentabilidade operacional que reflete a eficiência da empresa em gerenciar custos de produção e precificação. Uma margem alta sugere forte poder de precificação ou baixos custos diretos, enquanto uma margem baixa pode indicar pressão competitiva ou ineficiência. É especialmente útil em setores com alta concorrência, como varejo e indústria, mas deve ser analisado em conjunto com margem líquida e crescimento da receita.
                    '''
                    agrupador = 'Rentabilidade'
                    formula = 'Margem Bruta = (Receita Bruta - Custo dos Produtos Vendidos) / Receita Bruta'

                    try:
                        if margem_bruta < 10:
                            return {
                                'classificacao': 'Crítico',
                                'faixa': 'Margem Bruta < 10%',
                                'descricao': '''
                                Uma Margem Bruta abaixo de 10% indica baixa rentabilidade operacional, sugerindo que a empresa enfrenta dificuldades em cobrir os custos diretos de produção. Isso é comum em setores com alta concorrência ou preços deprimidos, como varejo em crise (ex.: Casas Bahia - BHIA3). Para investidores, essa faixa é um alerta de risco elevado, pois reflete ineficiência operacional ou pressão competitiva. A análise deve focar na estrutura de custos, estratégias de precificação e tendências setoriais. Investidores conservadores devem evitar empresas nessa faixa.
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
                                Uma Margem Bruta entre 10% e 20% reflete rentabilidade operacional limitada, indicando que a empresa tem margens apertadas devido a custos elevados ou concorrência. Isso é comum em setores como varejo alimentar (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a aumentos de custos ou oscilações econômicas. É importante analisar estratégias de redução de custos e potencial de melhoria da margem. Análises complementares de margem líquida e giro de ativos são recomendadas.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 20 < margem_bruta <= 40:
                            return {
                                'classificacao': 'Moderado',
                                'faixa': '20% < Margem Bruta <= 40%',
                                'descricao': '''
                                Uma Margem Bruta entre 20% e 40% indica rentabilidade operacional aceitável, típico de empresas com boa gestão de custos e poder de precificação moderado. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua eficiência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência da margem e o impacto de fatores macroeconômicos.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 40 < margem_bruta <= 60:
                            return {
                                'classificacao': 'Ótimo',
                                'faixa': '40% < Margem Bruta <= 60%',
                                'descricao': '''
                                Uma Margem Bruta entre 40% e 60% reflete rentabilidade operacional robusta, indicando que a empresa tem forte controle de custos ou poder de precificação. Empresas como a Ambev (ABEV3), com liderança de mercado no setor de bebidas, frequentemente apresentam margem nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez operacional e potencial para lucros elevados. No entanto, é importante verificar a sustentabilidade da margem, analisando concorrência e custos de produção.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif margem_bruta > 60:
                            return {
                                'classificacao': 'Fora da faixa',
                                'faixa': 'Margem Bruta > 60%',
                                'descricao': '''
                                Uma Margem Bruta acima de 60% é excepcional, indicando que a empresa converte uma proporção extremamente alta de sua receita em lucro bruto. Isso é raro, mas pode ocorrer em empresas com modelos de negócios diferenciados, como a Weg (WEGE3) em períodos de alta eficiência. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois margens tão altas podem não ser sustentáveis a longo prazo. A análise deve focar na escalabilidade do modelo de negócios, barreiras de entrada e consistência da rentabilidade.
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
                            Ocorreu um erro ao processar a Margem Bruta: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que a receita bruta e o custo dos produtos vendidos estejam corretos e sejam valores numéricos válidos.
                            ''',
                            'definicao': definicao,
                            'agrupador': agrupador,
                            'formula': formula
                        }

                def evaluate_roe(roe):
                    '''
                    Avalia o Retorno sobre o Patrimônio Líquido (ROE) com base em faixas definidas para o mercado brasileiro:
                    - ROE < 0%: Crítico (prejuízo, destruição de valor)
                    - 0% ≤ ROE ≤ 5%: Ruim (retorno baixo, ineficiência)
                    - 5% < ROE ≤ 15%: Moderado (retorno aceitável)
                    - 15% < ROE ≤ 25%: Ótimo (retorno robusto)
                    - ROE > 25%: Fora da faixa (retorno excepcional, avaliar sustentabilidade)
                    '''
                    definicao = '''
                    O Retorno sobre o Patrimônio Líquido (ROE) mede a rentabilidade do capital próprio da empresa, calculado como (Lucro Líquido / Patrimônio Líquido). É um indicador chave de eficiência na geração de valor para os acionistas, refletindo quanto lucro a empresa gera com o capital investido pelos acionistas. Um ROE alto sugere eficiência na alocação de capital, enquanto um valor baixo ou negativo indica ineficiência ou prejuízo. É especialmente útil em setores financeiros e industriais, mas deve ser analisado em conjunto com margem líquida e endividamento.
                    '''
                    agrupador = 'Rentabilidade'
                    formula = 'ROE = Lucro Líquido / Patrimônio Líquido'

                    try:
                        if roe < 0:
                            return {
                                'classificacao': 'Crítico',
                                'faixa': 'ROE < 0%',
                                'descricao': '''
                                Um ROE negativo indica que a empresa está gerando prejuízo, destruindo valor para os acionistas. Isso é comum em empresas em crise, como a Gol (GOLL4) durante períodos de baixa demanda no setor aéreo. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades financeiras graves. A análise deve focar na estrutura de custos, endividamento e estratégias de recuperação. Investidores conservadores devem evitar empresas nessa faixa, enquanto investidores especulativos podem considerar apenas com uma tese robusta de turnaround.
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
                                Um ROE entre 0% e 5% reflete retorno baixo, indicando ineficiência na geração de valor com o capital próprio. Isso é comum em setores com margens apertadas ou alta concorrência, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a oscilações econômicas. É importante analisar estratégias de melhoria de rentabilidade e alavancagem financeira. Análises complementares de margem líquida e giro de ativos são recomendadas.
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
                                Um ROE entre 5% e 15% indica retorno aceitável, típico de empresas com eficiência moderada na geração de valor. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua consistência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência do ROE e o impacto de fatores macroeconômicos.
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
                                Um ROE entre 15% e 25% reflete retorno robusto, indicando que a empresa gera valor significativo com o capital próprio. Empresas como a Ambev (ABEV3), com forte eficiência operacional, frequentemente apresentam ROE nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e potencial para dividendos ou reinvestimento. No entanto, é importante verificar se o ROE é impulsionado por alavancagem excessiva, analisando o endividamento.
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
                                Um ROE acima de 25% é excepcional, indicando que a empresa gera retornos extremamente altos com o capital próprio. Isso é raro, mas pode ocorrer em empresas com alta eficiência operacional, como a Weg (WEGE3) em períodos de forte desempenho. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois ROEs tão altos podem ser impulsionados por alavancagem ou não serem sustentáveis. A análise deve focar na estrutura de capital, barreiras de entrada e consistência da rentabilidade.
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
                            Ocorreu um erro ao processar o ROE: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se o patrimônio líquido for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o lucro líquido e o patrimônio líquido estejam corretos e sejam valores numéricos válidos.
                            ''',
                            'definicao': definicao,
                            'agrupador': agrupador,
                            'formula': formula
                        }

                def evaluate_ebit_margin(ebit_margin):
                    '''
                    Avalia a Margem EBIT com base em faixas definidas para o mercado brasileiro:
                    - Margem EBIT < 0%: Crítico (prejuízo operacional, risco elevado)
                    - 0% ≤ Margem EBIT ≤ 5%: Ruim (rentabilidade operacional baixa)
                    - 5% < Margem EBIT ≤ 15%: Moderado (rentabilidade operacional aceitável)
                    - 15% < Margem EBIT ≤ 25%: Ótimo (rentabilidade operacional robusta)
                    - Margem EBIT > 25%: Fora da faixa (rentabilidade operacional excepcional, avaliar sustentabilidade)
                    '''
                    definicao = '''
                    A Margem EBIT mede a proporção da receita bruta que se converte em lucro antes de juros e impostos, calculada como (EBIT / Receita Bruta). É um indicador de rentabilidade operacional que reflete a eficiência da empresa em gerar lucro a partir de suas operações principais, excluindo efeitos de financiamento e impostos. Uma margem alta sugere forte desempenho operacional, enquanto uma margem baixa ou negativa indica ineficiência ou prejuízo. É especialmente útil para comparar empresas dentro do mesmo setor, mas deve ser analisado em conjunto com margem EBITDA e fluxo de caixa.
                    '''
                    agrupador = 'Rentabilidade'
                    formula = 'Margem EBIT = EBIT / Receita Bruta'

                    try:
                        if ebit_margin < 0:
                            return {
                                'classificacao': 'Crítico',
                                'faixa': 'Margem EBIT < 0%',
                                'descricao': '''
                                Uma Margem EBIT negativa indica prejuízo operacional, sugerindo que a empresa não consegue cobrir os custos operacionais com sua receita. Isso é comum em empresas em crise, como a CSN (CSNA3) durante quedas de preços de commodities. Para investidores, essa faixa é um alerta de risco elevado, pois reflete dificuldades operacionais graves. A análise deve focar na estrutura de custos, estratégias de recuperação e tendências setoriais. Investidores conservadores devem evitar empresas nessa faixa.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 0 <= ebit_margin <= 5:
                            return {
                                'classificacao': 'Ruim',
                                'faixa': '0% <= Margem EBIT <= 5%',
                                'descricao': '''
                                Uma Margem EBIT entre 0% e 5% reflete rentabilidade operacional baixa, indicando que a empresa tem dificuldade em gerar lucro significativo a partir de suas operações. Isso é comum em setores com margens apertadas, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode ser vulnerável a aumentos de custos ou oscilações econômicas. É importante analisar estratégias de redução de custos e potencial de melhoria da margem. Análises complementares de margem bruta e fluxo de caixa são recomendadas.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 5 < ebit_margin <= 15:
                            return {
                                'classificacao': 'Moderado',
                                'faixa': '5% < Margem EBIT <= 15%',
                                'descricao': '''
                                Uma Margem EBIT entre 5% e 15% indica rentabilidade operacional aceitável, típico de empresas com eficiência moderada nas operações. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à sua consistência no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre rentabilidade e segurança, sendo adequada para quem busca retornos consistentes. É importante avaliar a consistência da margem e o impacto de fatores macroeconômicos.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 15 < ebit_margin <= 25:
                            return {
                                'classificacao': 'Ótimo',
                                'faixa': '15% < Margem EBIT <= 25%',
                                'descricao': '''
                                Uma Margem EBIT entre 15% e 25% reflete rentabilidade operacional robusta, indicando que a empresa converte uma proporção significativa de sua receita em lucro operacional. Empresas como a Ambev (ABEV3), com forte controle de custos, frequentemente apresentam margem nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez operacional e potencial para lucros elevados. No entanto, é importante verificar a sustentabilidade da margem, analisando concorrência e custos operacionais.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif ebit_margin > 25:
                            return {
                                'classificacao': 'Fora da faixa',
                                'faixa': 'Margem EBIT > 25%',
                                'descricao': '''
                                Uma Margem EBIT acima de 25% é excepcional, indicando que a empresa converte uma proporção extremamente alta de sua receita em lucro operacional. Isso é raro, mas pode ocorrer em empresas com alta eficiência operacional, como a Weg (WEGE3) em períodos de forte desempenho. Para investidores, essa faixa é altamente atrativa, mas exige cautela, pois margens tão altas podem não ser sustentáveis a longo prazo. A análise deve focar na escalabilidade do modelo de negócios, barreiras de entrada e consistência da rentabilidade.
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
                            Ocorreu um erro ao processar a Margem EBIT: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se a receita bruta for zero, o que impede o cálculo. Verifique os dados de entrada, assegurando que o EBIT e a receita bruta estejam corretos e sejam valores numéricos válidos.
                            ''',
                            'definicao': definicao,
                            'agrupador': agrupador,
                            'formula': formula
                        }

                def evaluate_cash_conversion_cycle(cash_conversion_cycle):
                    '''
                    Avalia o Ciclo de Conversão de Caixa (CCC) com base em faixas definidas para o mercado brasileiro:
                    - CCC < 0 dias: Fora da faixa (ciclo negativo, eficiência excepcional)
                    - 0 ≤ CCC ≤ 30 dias: Ótimo (ciclo curto, alta eficiência)
                    - 30 < CCC ≤ 60 dias: Moderado (ciclo aceitável)
                    - 60 < CCC ≤ 90 dias: Ruim (ciclo longo, eficiência limitada)
                    - CCC > 90 dias: Crítico (ciclo muito longo, risco elevado)
                    '''
                    definicao = '''
                    O Ciclo de Conversão de Caixa (CCC) mede o tempo (em dias) que a empresa leva para converter seus investimentos em estoques e contas a receber em caixa, calculado como (Dias de Estoque + Dias de Recebíveis - Dias de Pagáveis). Um CCC curto indica alta eficiência na gestão do capital de giro, enquanto um ciclo longo sugere ineficiência ou necessidade de capital elevado. É especialmente útil em setores com alta rotatividade, como varejo e indústria, mas deve ser analisado em conjunto com liquidez corrente e giro de ativos.
                    '''
                    agrupador = 'Eficiência'
                    formula = 'CCC = Dias de Estoque + Dias de Recebíveis - Dias de Pagáveis'

                    try:
                        if cash_conversion_cycle < 0:
                            return {
                                'classificacao': 'Fora da faixa',
                                'faixa': 'CCC < 0 dias',
                                'descricao': '''
                                Um CCC negativo indica eficiência excepcional, com a empresa recebendo pagamentos de clientes antes de pagar fornecedores, reduzindo a necessidade de capital de giro. Isso é raro, mas pode ocorrer em empresas de varejo com alta rotatividade, como a Magazine Luiza (MGLU3) em períodos de forte desempenho no e-commerce. Para investidores, essa faixa é altamente atrativa, pois sugere gestão eficiente de caixa. A análise deve focar na sustentabilidade do ciclo e na qualidade dos recebíveis.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 0 <= cash_conversion_cycle <= 30:
                            return {
                                'classificacao': 'Ótimo',
                                'faixa': '0 <= CCC <= 30 dias',
                                'descricao': '''
                                Um CCC entre 0 e 30 dias reflete um ciclo curto, indicando alta eficiência na gestão do capital de giro. Empresas como a Ambev (ABEV3), com forte controle de estoques e recebíveis, frequentemente operam nessa faixa. Para investidores, essa faixa é atrativa, pois sugere solidez financeira e baixa necessidade de capital de giro. É importante avaliar a consistência do ciclo e a qualidade dos recebíveis e estoques.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 30 < cash_conversion_cycle <= 60:
                            return {
                                'classificacao': 'Moderado',
                                'faixa': '30 < CCC <= 60 dias',
                                'descricao': '''
                                Um CCC entre 30 e 60 dias indica um ciclo aceitável, típico de empresas com gestão moderada de capital de giro. No Brasil, empresas como a Suzano (SUZB3) frequentemente operam nessa faixa devido à natureza de seus ciclos operacionais no setor de celulose. Para investidores, essa faixa sugere um equilíbrio entre eficiência e risco, sendo adequada para quem busca retornos consistentes. É importante avaliar a composição do ciclo (estoques, recebíveis, pagáveis) e o impacto de fatores setoriais.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif 60 < cash_conversion_cycle <= 90:
                            return {
                                'classificacao': 'Ruim',
                                'faixa': '60 < CCC <= 90 dias',
                                'descricao': '''
                                Um CCC entre 60 e 90 dias reflete um ciclo longo, indicando eficiência limitada na gestão do capital de giro. Isso é comum em setores com estoques elevados ou prazos de recebimento longos, como varejo (ex.: Carrefour Brasil - CRFB3). Para investidores, essa faixa sugere risco moderado, pois a empresa pode precisar de mais capital para financiar operações. Análise da qualidade dos recebíveis e estratégias de redução do ciclo é recomendada.
                                ''',
                                'definicao': definicao,
                                'agrupador': agrupador,
                                'formula': formula
                            }
                        elif cash_conversion_cycle > 90:
                            return {
                                'classificacao': 'Crítico',
                                'faixa': 'CCC > 90 dias',
                                'descricao': '''
                                Um CCC acima de 90 dias indica um ciclo muito longo, sugerindo ineficiência significativa na gestão do capital de giro. Isso é comum em empresas com problemas operacionais, como a Oi (OIBR3) durante períodos de crise. Para investidores, essa faixa é de altíssimo risco, pois reflete alta necessidade de capital de giro e possível pressão financeira. A análise deve focar na gestão de estoques, recebíveis e estratégias de redução do ciclo para avaliar a viabilidade financeira.
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
                            Ocorreu um erro ao processar o Ciclo de Conversão de Caixa: {str(e)}. Isso pode ter acontecido se o valor fornecido não for numérico ou se os dados de estoques, recebíveis ou pagáveis forem inválidos. Verifique os dados de entrada, assegurando que os dias de estoque, recebíveis e pagáveis estejam corretos e sejam valores numéricos válidos.
                            ''',
                            'definicao': definicao,
                            'agrupador': agrupador,
                            'formula': formula



                        }