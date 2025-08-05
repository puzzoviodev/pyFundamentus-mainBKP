# 📦 Definição da classe que avalia o indicador Preço/Valor Patrimonial (P/VP)
class PVPEvaluator:

    # 🔧 Método construtor chamado ao instanciar a classe
    def __init__(self):
        # 📝 Atributo que armazena a definição do indicador P/VP
        self.definicao = '''
        O Preço/Valor Patrimonial (P/VP) compara o preço da ação ao valor patrimonial por ação, calculado
        como (Preço da Ação / Valor Patrimonial por Ação). É um indicador de valuation que avalia se a
        ação está cara ou barata em relação aos ativos líquidos da empresa. Um P/VP baixo sugere
        subvalorização, enquanto um valor alto indica sobrevalorização ou expectativas de crescimento.
        '''

        # 🏷️ Atributo que indica a categoria do indicador
        self.agrupador = 'Valuation'

        # 📐 Atributo que armazena a fórmula do indicador
        self.formula = 'P/VP = Preço da Ação / Valor Patrimonial por Ação'

    # 📊 Método principal que avalia o valor de P/VP e retorna uma análise
    def avaliar(self, p_vp):
        try:
            # 🟥 Faixa crítica: patrimônio líquido negativo
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

            # 🟩 Faixa ótima: ação subvalorizada
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

            # 🟨 Faixa moderada: valuation justo
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

            # 🟧 Faixa ruim: sobrevalorização moderada
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

            # 🟥 Faixa péssima: valuation elevado
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

            # 🚨 Faixa especulativa: risco elevado
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

        # ⚠️ Captura exceções e retorna erro amigável
        except Exception as e:
            return self._erro(mensagem=str(e))

    # 🧾 Método auxiliar que monta o dicionário de resultado
    def _resultado(self, classificacao, faixa, descricao, riscos, referencia):
        return {
            'classificacao': classificacao,  # 🏷️ Nível de avaliação
            'faixa': faixa,  # 📊 Faixa de valor analisada
            'descricao': descricao.strip(),  # 📝 Texto explicativo (sem espaços extras)
            'definicao': self.definicao.strip(),  # 📘 Definição do indicador
            'agrupador': self.agrupador,  # 🏷️ Categoria do indicador
            'formula': self.formula,  # 📐 Fórmula usada
            'riscos': riscos.strip(),  # ⚠️ Riscos associados
            'referencia_cruzada': referencia.strip()  # 🔗 Sugestões de análise complementar
        }

    # ❌ Método auxiliar que retorna estrutura de erro
    def _erro(self, mensagem):
        return {
            'classificacao': 'Erro',  # ❗ Indica falha na avaliação
            'faixa': 'N/A',  # 🚫 Faixa não aplicável
            'descricao': f'''
                Ocorreu um erro ao processar o P/VP: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            'definicao': self.definicao.strip(),  # 📘 Mantém a definição
            'agrupador': self.agrupador,  # 🏷️ Mantém a categoria
            'formula': self.formula  # 📐 Mantém a fórmula
        }


# 🧪 Exemplo de uso da classe
avaliador = PVPEvaluator()  # 🔧 Instancia o avaliador
resultado = avaliador.avaliar(1.2)  # 📊 Avalia o valor 1.2
print(resultado['classificacao'])  # 🖨️ Imprime a classificação: Moderado
print(resultado['formula'])  # 🖨️ Imprime a fórmula usada
