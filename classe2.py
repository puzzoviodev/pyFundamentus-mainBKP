class PVPEvaluator:
    def __init__(self):
        self.definicao = '''
        O Preço/Valor Patrimonial (P/VP) compara o preço da ação ao valor patrimonial por ação, calculado
        como (Preço da Ação / Valor Patrimonial por Ação). É um indicador de valuation que avalia se a
        ação está cara ou barata em relação aos ativos líquidos da empresa. Um P/VP baixo sugere
        subvalorização, enquanto um valor alto indica sobrevalorização ou expectativas de crescimento.
        '''
        self.agrupador = 'Valuation'
        self.formula = 'P/VP = Preço da Ação / Valor Patrimonial por Ação'

    def avaliar(self, p_vp):
        try:
            if p_vp < 0:
                return self._resultado(
                    classificacao='Crítico',
                    faixa='P/VP < 0',
                    descricao='''
                        Um P/VP negativo indica que o patrimônio líquido da empresa é negativo, sugerindo sérias
                        dificuldades financeiras. Isso é comum em empresas em crise, como a Oi (OIBR3).
                        Recomendações: Indicado apenas para investidores especulativos com alta tolerância a risco.
                    ''',
                    riscos='Alta probabilidade de falência ou diluição acionária em reestruturações.',
                    referencia='Avalie evaluate_debt_to_equity para saúde financeira, evaluate_cash_flow para geração de caixa e evaluate_peg_ratio para perspectivas de crescimento.'
                )
            elif 0 <= p_vp <= 1:
                return self._resultado(
                    classificacao='Ótimo',
                    faixa='0 <= P/VP <= 1',
                    descricao='''
                        Subvalorização significativa. Exemplo: Vale (VALE3) teve P/VP ~0.8 em 2023.
                        Recomendações: Ideal para investidores de longo prazo.
                    ''',
                    riscos='Patrimônio pode incluir ativos obsoletos.',
                    referencia='Analise evaluate_vpa para valor patrimonial e evaluate_roe para rentabilidade.'
                )
            elif 1 < p_vp <= 1.5:
                return self._resultado(
                    classificacao='Moderado',
                    faixa='1 < P/VP <= 1.5',
                    descricao='''
                        Valuation justo, comum em empresas estáveis. Exemplo: Ambev (ABEV3) com P/VP ~1.3.
                        Recomendações: Ideal para portfólios diversificados.
                    ''',
                    riscos='Estagnação em setores maduros.',
                    referencia='Compare com evaluate_p_l para lucros e evaluate_pl_ativos para estrutura.'
                )
            elif 1.5 < p_vp <= 2:
                return self._resultado(
                    classificacao='Ruim',
                    faixa='1.5 < P/VP <= 2',
                    descricao='''
                        Sobrevalorização moderada. Exemplo: Raia Drogasil (RADL3) com P/VP ~1.8.
                        Recomendações: Validar expansão e retorno sobre patrimônio.
                    ''',
                    riscos='Expectativas não realizadas podem levar a correções.',
                    referencia='Verifique evaluate_peg_ratio para crescimento e evaluate_evebitda para valuation.'
                )
            elif 2 < p_vp <= 3:
                return self._resultado(
                    classificacao='Péssimo',
                    faixa='2 < P/VP <= 3',
                    descricao='''
                        Valuation elevado. Exemplo: Localiza (RENT3) com P/VP ~2.5.
                        Recomendações: Conservadores devem evitar.
                    ''',
                    riscos='Sensibilidade a mudanças econômicas.',
                    referencia='Combine com evaluate_psr para receita e evaluate_margem_liquida para eficiência.'
                )
            elif p_vp > 3:
                return self._resultado(
                    classificacao='Fora da faixa',
                    faixa='P/VP > 3',
                    descricao='''
                        Especulação. Exemplo: Nubank (NUBR33) com P/VP > 3.
                        Recomendações: Alto risco, adequado para especulativos.
                    ''',
                    riscos='Bolhas especulativas.',
                    referencia='Avalie evaluate_p_ativo para ativos e evaluate_crescimento_receita para tendências.'
                )
        except Exception as e:
            return self._erro(mensagem=str(e))

    def _resultado(self, classificacao, faixa, descricao, riscos, referencia):
        return {
            'classificacao': classificacao,
            'faixa': faixa,
            'descricao': descricao.strip(),
            'definicao': self.definicao.strip(),
            'agrupador': self.agrupador,
            'formula': self.formula,
            'riscos': riscos.strip(),
            'referencia_cruzada': referencia.strip()
        }

    def _erro(self, mensagem):
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'''
                Ocorreu um erro ao processar o P/VP: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            'definicao': self.definicao.strip(),
            'agrupador': self.agrupador,
            'formula': self.formula
        }

# 🔍 Exemplo de uso
avaliador = PVPEvaluator()
resultado = avaliador.avaliar(1.2)
print(resultado['classificacao'])  # Moderado
print(resultado['formula'])        # P/VP = Preço da Ação / Valor Patrimonial por Ação
