# Define uma classe chamada PVPEvaluator. Em Python, classes são estruturas que agrupam dados (atributos)
# e comportamentos (métodos). Elas são instanciadas para criar objetos.
class PVPEvaluator:

    # Método especial __init__ é o construtor da classe. É chamado automaticamente quando um objeto é criado.
    # Ele inicializa os atributos da instância.
    def __init__(self):
        # Atributo de instância que armazena uma string multilinha com a definição do indicador P/VP.
        # Strings multilinha são delimitadas por três aspas simples ou duplas.
        self.definicao = '''
        O Preço/Valor Patrimonial (P/VP) compara o preço da ação ao valor patrimonial por ação, calculado
        como (Preço da Ação / Valor Patrimonial por Ação). É um indicador de valuation que avalia se a
        ação está cara ou barata em relação aos ativos líquidos da empresa. Um P/VP baixo sugere
        subvalorização, enquanto um valor alto indica sobrevalorização ou expectativas de crescimento.
        '''

        # Atributo que define a categoria do indicador. É uma string simples.
        self.agrupador = 'Valuation'

        # Atributo que armazena a fórmula do indicador como string.
        self.formula = 'P/VP = Preço da Ação / Valor Patrimonial por Ação'

    # Método público chamado avaliar. Recebe um argumento p_vp (esperado como número: float ou int).
    # Avalia o valor de P/VP e retorna um dicionário com a análise correspondente.
    def avaliar(self, p_vp):
        # Bloco try/except usado para capturar exceções que possam ocorrer durante a execução.
        # Protege contra erros como tipos inválidos ou operações ilegais.
        try:
            # Estrutura condicional que verifica se o valor é negativo.
            # Operador relacional < retorna True se p_vp for menor que zero.
            if p_vp < 0:
                # Chama o método auxiliar _resultado e retorna seu resultado.
                # Os argumentos são passados como parâmetros nomeados.
                return self._resultado(
                    classificacao='Crítico',
                    faixa='P/VP < 0',
                    descricao='''...''',
                    riscos='Alta probabilidade de falência ou diluição acionária em reestruturações.',
                    referencia='Avalie evaluate_debt_to_equity para saúde financeira, evaluate_cash_flow para geração de caixa e evaluate_peg_ratio para perspectivas de crescimento.'
                )

            # Verifica se o valor está entre 0 e 1, inclusive.
            # Comparações encadeadas são válidas em Python e retornam True se todas forem verdadeiras.
            elif 0 <= p_vp <= 1:
                return self._resultado(
                    classificacao='Ótimo',
                    faixa='0 <= P/VP <= 1',
                    descricao='''...''',
                    riscos='Patrimônio pode incluir ativos obsoletos.',
                    referencia='Analise evaluate_vpa para valor patrimonial e evaluate_roe para rentabilidade.'
                )

            # Verifica se o valor está entre 1 (exclusivo) e 1.5 (inclusivo).
            elif 1 < p_vp <= 1.5:
                return self._resultado(
                    classificacao='Moderado',
                    faixa='1 < P/VP <= 1.5',
                    descricao='''...''',
                    riscos='Estagnação em setores maduros.',
                    referencia='Compare com evaluate_p_l para lucros e evaluate_pl_ativos para estrutura.'
                )

            # Verifica se o valor está entre 1.5 (exclusivo) e 2 (inclusivo).
            elif 1.5 < p_vp <= 2:
                return self._resultado(
                    classificacao='Ruim',
                    faixa='1.5 < P/VP <= 2',
                    descricao='''...''',
                    riscos='Expectativas não realizadas podem levar a correções.',
                    referencia='Verifique evaluate_peg_ratio para crescimento e evaluate_evebitda para valuation.'
                )

            # Verifica se o valor está entre 2 (exclusivo) e 3 (inclusivo).
            elif 2 < p_vp <= 3:
                return self._resultado(
                    classificacao='Péssimo',
                    faixa='2 < P/VP <= 3',
                    descricao='''...''',
                    riscos='Sensibilidade a mudanças econômicas.',
                    referencia='Combine com evaluate_psr para receita e evaluate_margem_liquida para eficiência.'
                )

            # Verifica se o valor é maior que 3.
            elif p_vp > 3:
                return self._resultado(
                    classificacao='Fora da faixa',
                    faixa='P/VP > 3',
                    descricao='''...''',
                    riscos='Bolhas especulativas.',
                    referencia='Avalie evaluate_p_ativo para ativos e evaluate_crescimento_receita para tendências.'
                )

        # Bloco de tratamento de exceção. Captura qualquer erro que ocorra no try.
        # A variável e contém o objeto da exceção, e str(e) converte a mensagem para string.
        except Exception as e:
            return self._erro(mensagem=str(e))

    # Método auxiliar privado (por convenção, prefixado com _) que monta e retorna um dicionário.
    # Os dados são organizados em pares chave-valor.
    def _resultado(self, classificacao, faixa, descricao, riscos, referencia):
        return {
            'classificacao': classificacao,  # String com a classificação do indicador
            'faixa': faixa,  # Faixa de valor analisada
            'descricao': descricao.strip(),  # Remove espaços extras da descrição
            'definicao': self.definicao.strip(),  # Remove espaços extras da definição
            'agrupador': self.agrupador,  # Categoria do indicador
            'formula': self.formula,  # Fórmula usada para cálculo
            'riscos': riscos.strip(),  # Riscos associados à faixa
            'referencia_cruzada': referencia.strip()  # Sugestões de análise complementar
        }

    # Método auxiliar que retorna um dicionário de erro.
    # Usado quando ocorre uma exceção durante a avaliação.
    def _erro(self, mensagem):
        return {
            'classificacao': 'Erro',  # Indica que houve falha
            'faixa': 'N/A',  # Faixa não aplicável
            'descricao': f'''
                Ocorreu um erro ao processar o P/VP: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',  # Mensagem interpolada com f-string
            'definicao': self.definicao.strip(),  # Mantém a definição original
            'agrupador': self.agrupador,  # Mantém a categoria
            'formula': self.formula  # Mantém a fórmula
        }


# 🧪 Exemplo de uso da classe
avaliador = PVPEvaluator()  # Cria uma instância da classe, chamando __init__
resultado = avaliador.avaliar(1.2)  # Chama o método avaliar com o valor 1.2
print(resultado['classificacao'])  # Imprime a classificação retornada: 'Moderado'
print(resultado['formula'])  # Imprime a fórmula usada: 'P/VP = Preço da Ação / Valor Patrimonial por Ação'
