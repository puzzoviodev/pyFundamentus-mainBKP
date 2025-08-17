# resultado_pvp_evaluator.py

class ResultadoPVP:
    def __init__(self, classificacao, faixa, descricao, definicao, agrupador, formula, riscos, referencia_cruzada):
        self.classificacao = classificacao
        self.faixa = faixa
        self.descricao = descricao.strip()
        self.definicao = definicao.strip()
        self.agrupador = agrupador
        self.formula = formula
        self.riscos = riscos.strip()
        self.referencia_cruzada = referencia_cruzada.strip()

    def __repr__(self):
        return f"<ResultadoPVP: {self.classificacao} | Faixa: {self.faixa}>"

    def to_dict(self):
        return {
            'classificacao': self.classificacao,
            'faixa': self.faixa,
            'descricao': self.descricao,
            'definicao': self.definicao,
            'agrupador': self.agrupador,
            'formula': self.formula,
            'riscos': self.riscos,
            'referencia_cruzada': self.referencia_cruzada
        }


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
            p_vp = float(p_vp)  # Garante que o valor seja numérico
            if p_vp < 0:
                return self.gerar_resultado(
                    classificacao='Crítico',
                    faixa='P/VP < 0',
                    descricao='Valor negativo pode indicar distorções contábeis ou prejuízos acumulados.',
                    riscos='Alta probabilidade de falência ou diluição acionária em reestruturações.',
                    referencia='Avalie evaluate_debt_to_equity para saúde financeira, evaluate_cash_flow para geração de caixa e evaluate_peg_ratio para perspectivas de crescimento.'
                )
            elif 0 <= p_vp <= 1:
                return self.gerar_resultado(
                    classificacao='Ótimo',
                    faixa='0 <= P/VP <= 1',
                    descricao='A ação está sendo negociada abaixo do valor patrimonial.',
                    riscos='Patrimônio pode incluir ativos obsoletos.',
                    referencia='Analise evaluate_vpa para valor patrimonial e evaluate_roe para rentabilidade.'
                )
            elif 1 < p_vp <= 1.5:
                return self.gerar_resultado(
                    classificacao='Moderado',
                    faixa='1 < P/VP <= 1.5',
                    descricao='Preço próximo ao valor patrimonial, com leve prêmio.',
                    riscos='Estagnação em setores maduros.',
                    referencia='Compare com evaluate_p_l para lucros e evaluate_pl_ativos para estrutura.'
                )
            elif 1.5 < p_vp <= 2:
                return self.gerar_resultado(
                    classificacao='Ruim',
                    faixa='1.5 < P/VP <= 2',
                    descricao='Preço elevado em relação ao patrimônio.',
                    riscos='Expectativas não realizadas podem levar a correções.',
                    referencia='Verifique evaluate_peg_ratio para crescimento e evaluate_evebitda para valuation.'
                )
            elif 2 < p_vp <= 3:
                return self.gerar_resultado(
                    classificacao='Péssimo',
                    faixa='2 < P/VP <= 3',
                    descricao='Preço muito acima do valor patrimonial.',
                    riscos='Sensibilidade a mudanças econômicas.',
                    referencia='Combine com evaluate_psr para receita e evaluate_margem_liquida para eficiência.'
                )
            elif p_vp > 3:
                return self.gerar_resultado(
                    classificacao='Fora da faixa',
                    faixa='P/VP > 3',
                    descricao='Preço extremamente elevado em relação ao patrimônio.',
                    riscos='Bolhas especulativas.',
                    referencia='Avalie evaluate_p_ativo para ativos e evaluate_crescimento_receita para tendências.'
                )
        except Exception as e:
            return self._erro(mensagem=str(e))

    def gerar_resultado(self, classificacao, faixa, descricao, riscos, referencia):
        return ResultadoPVP(
            classificacao=classificacao,
            faixa=faixa,
            descricao=descricao,
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos=riscos,
            referencia_cruzada=referencia
        )

    def _erro(self, mensagem):
        return ResultadoPVP(
            classificacao='Erro',
            faixa='N/A',
            descricao=f'''
                Ocorreu um erro ao processar o P/VP: {mensagem}.
                Verifique os dados de entrada e assegure que sejam numéricos válidos.
            ''',
            definicao=self.definicao,
            agrupador=self.agrupador,
            formula=self.formula,
            riscos='N/A',
            referencia_cruzada='N/A'
        )


# 🧪 Testes
if __name__ == "__main__":
    avaliador = PVPEvaluator()

    # Teste 1: Avaliação automática com valor P/VP
    resultado_avaliacao = avaliador.avaliar(1.2)
    print("🔍 Teste de avaliação automática:")
    print(resultado_avaliacao)
    print(resultado_avaliacao.to_dict())
    print()

    # Teste 2: Geração manual de resultado público
    resultado_manual = avaliador.gerar_resultado(
        classificacao='Teste',
        faixa='1.0 - 2.0',
        descricao='Exemplo de uso externo',
        riscos='Risco moderado',
        referencia='Referência fictícia'
    )
    print("🧪 Teste de geração manual de resultado:")
    print(resultado_manual)
    print(resultado_manual.to_dict())
    print()

    # Teste 3: Simulação de erro
    resultado_erro = avaliador.avaliar("valor_invalido")
    print("⚠️ Teste de erro:")
    print(resultado_erro)
    print(resultado_erro.to_dict())


# executar_avaliacao.py

from classefinal import PVPEvaluator  # Importa a classe avaliadora

def exibir_resultado(resultado):
    print("📊 Resultado da Avaliação P/VP")
    print(f"Classificação: {resultado.classificacao}")
    print(f"Faixa: {resultado.faixa}")
    print(f"Descrição: {resultado.descricao}")
    print(f"Definição: {resultado.definicao}")
    print(f"Agrupador: {resultado.agrupador}")
    print(f"Fórmula: {resultado.formula}")
    print(f"Riscos: {resultado.riscos}")
    print(f"Referência Cruzada: {resultado.referencia_cruzada}")
    print("-" * 60)

if __name__ == "__main__":
    avaliador = PVPEvaluator()

    # 🔍 Avaliação com valor real
    valor_pvp = 1.2
    resultado = avaliador.avaliar(valor_pvp)

    # 🖨️ Exibe os dados formatados
    exibir_resultado(resultado)

    # ✅ Também pode acessar como dicionário
    resultado_dict = resultado.to_dict()
    print("📦 Resultado como dicionário:")
    print(resultado_dict)
