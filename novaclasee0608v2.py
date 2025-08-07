class PVPEvaluator:
    def __init__(self):
        self._p_vp = None
        self.classificacao = None
        self.faixa = None
        self.descricao = None
        self.riscos = None
        self.referencia_cruzada = None
        self.definicao = '''
        O Preço/Valor Patrimonial (P/VP) compara o preço da ação ao valor patrimonial por ação, calculado
        como (Preço da Ação / Valor Patrimonial por Ação). É um indicador de valuation que avalia se a
        ação está cara ou barata em relação aos ativos líquidos da empresa. Um P/VP baixo sugere
        subvalorização, enquanto um valor alto indica sobrevalorização ou expectativas de crescimento.
        '''
        self.agrupador = 'Valuation'
        self.formula = 'P/VP = Preço da Ação / Valor Patrimonial por Ação'

    @property
    def p_vp(self):
        return self._p_vp

    @p_vp.setter
    def p_vp(self, valor):
        self._p_vp = valor
        self._avaliar(valor)

    def _avaliar(self, p_vp):
        try:
            if p_vp < 0:
                self._set_resultado(
                    'Crítico', 'P/VP < 0',
                    '''
                    Um P/VP negativo indica que o patrimônio líquido da empresa é negativo, sugerindo sérias
                    dificuldades financeiras. Isso é comum em empresas em crise, como a Oi (OIBR3).
                    Recomendações: Indicado apenas para investidores especulativos com alta tolerância a risco.
                    ''',
                    'Alta probabilidade de falência ou diluição acionária em reestruturações.',
                    'Avalie evaluate_debt_to_equity para saúde financeira, evaluate_cash_flow para geração de caixa e evaluate_peg_ratio para perspectivas de crescimento.'
                )
            elif 0 <= p_vp <= 1:
                self._set_resultado(
                    'Ótimo', '0 <= P/VP <= 1',
                    '''
                    Subvalorização significativa. Exemplo: Vale (VALE3) teve P/VP ~0.8 em 2023.
                    Recomendações: Ideal para investidores de longo prazo.
                    ''',
                    'Patrimônio pode incluir ativos obsoletos.',
                    'Analise evaluate_vpa para valor patrimonial e evaluate_roe para rentabilidade.'
                )
            elif 1 < p_vp <= 1.5:
                self._set_resultado(
                    'Moderado', '1 < P/VP <= 1.5',
                    '''
                    Valuation justo, comum em empresas estáveis. Exemplo: Ambev (ABEV3) com P/VP ~1.3.
                    Recomendações: Ideal para portfólios diversificados.
                    ''',
                    'Estagnação em setores maduros.',
                    'Compare com evaluate_p_l para lucros e evaluate_pl_ativos para estrutura.'
                )
            elif 1.5 < p_vp <= 2:
                self._set_resultado(
                    'Ruim', '1.5 < P/VP <= 2',
                    '''
                    Sobrevalorização moderada. Exemplo: Raia Drogasil (RADL3) com P/VP ~1.8.
                    Recomendações: Validar expansão e retorno sobre patrimônio.
                    ''',
                    'Expectativas não realizadas podem levar a correções.',
                    'Verifique evaluate_peg_ratio para crescimento e evaluate_evebitda para valuation.'
                )
            elif 2 < p_vp <= 3:
                self._set_resultado(
                    'Péssimo', '2 < P/VP <= 3',
                    '''
                    Valuation elevado. Exemplo: Localiza (RENT3) com P/VP ~2.5.
                    Recomendações: Conservadores devem evitar.
                    ''',
                    'Sensibilidade a mudanças econômicas.',
                    'Combine com evaluate_psr para receita e evaluate_margem_liquida para eficiência.'
                )
            elif p_vp > 3:
                self._set_resultado(
                    'Fora da faixa', 'P/VP > 3',
                    '''
                    Especulação. Exemplo: Nubank (NUBR33) com P/VP > 3.
                    Recomendações: Alto risco, adequado para especulativos.
                    ''',
                    'Bolhas especulativas.',
                    'Avalie evaluate_p_ativo para ativos e evaluate_crescimento_receita para tendências.'
                )
        except Exception as e:
            self._set_erro(str(e))

    def _set_resultado(self, classificacao, faixa, descricao, riscos, referencia):
        self.classificacao = classificacao
        self.faixa = faixa
        self.descricao = descricao.strip()
        self.riscos = riscos.strip()
        self.referencia_cruzada = referencia.strip()

    def _set_erro(self, mensagem):
        self.classificacao = 'Erro'
        self.faixa = 'N/A'
        self.descricao = f'''
            Ocorreu um erro ao processar o P/VP: {mensagem}.
            Verifique os dados de entrada e assegure que sejam numéricos válidos.
        '''
        self.riscos = ''
        self.referencia_cruzada = ''


# Exemplo de uso
if __name__ == "__main__":
    avaliador = PVPEvaluator()
    avaliador.p_vp = 2.0

    print("📊 Resultado da Avaliação:")
    print(f"Classificação: {avaliador.classificacao}")
    print(f"Faixa: {avaliador.faixa}")
    print(f"Descrição: {avaliador.descricao}")
    print(f"Riscos: {avaliador.riscos}")
    print(f"Referência Cruzada: {avaliador.referencia_cruzada}")
    print(f"Fórmula: {avaliador.formula}")
    print(f"Definição: {avaliador.definicao}")
