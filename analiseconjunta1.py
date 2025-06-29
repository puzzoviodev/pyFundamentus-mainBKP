
# Código Python para Análise Conjunta de Indicadores Financeiros
# Data: 29/06/2025
# Descrição: Ferramenta interativa para analisar indicadores financeiros em conjunto,
# considerando dependências e o cenário econômico (juros 10-12%, inflação controlada).
# Autor: Grok 3 (xAI)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Definição das faixas de referência para os indicadores
INDICATORS = {
    'Dívida Líquida/EBIT': {'Péssimo': (4, float('inf')), 'Ruim': (3, 4), 'Moderado': (1.5, 3), 'Bom': (0, 1.5),
                            'Ótimo': (-float('inf'), 0)},
    'Dívida Líquida/EBITDA': {'Péssimo': (3.5, float('inf')), 'Ruim': (2.5, 3.5), 'Moderado': (1, 2.5), 'Bom': (0, 1),
                              'Ótimo': (-float('inf'), 0)},
    'Dívida Líquida/Patrimônio Líquido': {'Péssimo': (1, float('inf')), 'Ruim': (0.7, 1), 'Moderado': (0.3, 0.7),
                                          'Bom': (0, 0.3), 'Ótimo': (-float('inf'), 0)},
    'Dividend Yield (DY)': {'Péssimo': (0, 0), 'Ruim': (0.1, 2), 'Moderado': (2, 4), 'Bom': (4, 6),
                            'Ótimo': (6, float('inf'))},
    'EV/EBIT': {'Péssimo': (15, float('inf')), 'Ruim': (12, 15), 'Moderado': (8, 12), 'Bom': (4, 8),
                'Ótimo': (-float('inf'), 4)},
    'EV/EBITDA': {'Péssimo': (12, float('inf')), 'Ruim': (10, 12), 'Moderado': (6, 10), 'Bom': (3, 6),
                  'Ótimo': (-float('inf'), 3)},
    'Giro do Ativo': {'Péssimo': (0, 0.2), 'Ruim': (0.2, 0.4), 'Moderado': (0.4, 0.8), 'Bom': (0.8, 1.2),
                      'Ótimo': (1.2, float('inf'))},
    'Liquidez Corrente': {'Péssimo': (0, 0.8), 'Ruim': (0.8, 1.2), 'Moderado': (1.2, 1.8), 'Bom': (1.8, 2.5),
                          'Ótimo': (2.5, float('inf'))},
    'LPA': {'Péssimo': (-float('inf'), 0), 'Ruim': (0, 0.1), 'Moderado': (0.1, 0.5), 'Bom': (0.5, 1),
            'Ótimo': (1, float('inf'))},
    'Margem Bruta': {'Péssimo': (-float('inf'), 0), 'Ruim': (0, 15), 'Moderado': (15, 30), 'Bom': (30, 50),
                     'Ótimo': (50, float('inf'))},
    'Margem EBIT': {'Péssimo': (-float('inf'), 0), 'Ruim': (0, 5), 'Moderado': (5, 15), 'Bom': (15, 25),
                    'Ótimo': (25, float('inf'))},
    'Margem EBITDA': {'Péssimo': (-float('inf'), 0), 'Ruim': (0, 10), 'Moderado': (10, 20), 'Bom': (20, 30),
                      'Ótimo': (30, float('inf'))},
    'Margem Líquida': {'Péssimo': (-float('inf'), 0), 'Ruim': (0, 5), 'Moderado': (5, 10), 'Bom': (10, 15),
                       'Ótimo': (15, float('inf'))},
    'P/Ativo': {'Péssimo': (1.5, float('inf')), 'Ruim': (1, 1.5), 'Moderado': (0.5, 1), 'Bom': (0.2, 0.5),
                'Ótimo': (0, 0.2)},
    'P/Ativo Circulante Líquido': {'Péssimo': (-float('inf'), 0), 'Ruim': (0, 1), 'Moderado': (1, 2), 'Bom': (2, 3),
                                   'Ótimo': (3, float('inf'))},
    'P/Capital de Giro': {'Péssimo': (-float('inf'), 0), 'Ruim': (0, 2), 'Moderado': (2, 4), 'Bom': (4, 6),
                          'Ótimo': (6, float('inf'))},
    'P/EBIT': {'Péssimo': (20, float('inf')), 'Ruim': (15, 20), 'Moderado': (10, 15), 'Bom': (5, 10), 'Ótimo': (0, 5)},
    'P/EBITDA': {'Péssimo': (15, float('inf')), 'Ruim': (10, 15), 'Moderado': (6, 10), 'Bom': (3, 6), 'Ótimo': (0, 3)},
    'P/L': {'Péssimo': (20, float('inf')), 'Ruim': (15, 20), 'Moderado': (10, 15), 'Bom': (5, 10), 'Ótimo': (0, 5)},
    'P/VPA': {'Péssimo': (2, float('inf')), 'Ruim': (1.5, 2), 'Moderado': (1, 1.5), 'Bom': (0.5, 1), 'Ótimo': (0, 0.5)},
    'Patrimônio/Ativos': {'Péssimo': (0, 0.2), 'Ruim': (0.2, 0.3), 'Moderado': (0.3, 0.5), 'Bom': (0.5, 0.7),
                          'Ótimo': (0.7, float('inf'))},
    'PSR': {'Péssimo': (3, float('inf')), 'Ruim': (2, 3), 'Moderado': (1, 2), 'Bom': (0.5, 1), 'Ótimo': (0, 0.5)},
    'ROA': {'Péssimo': (0, 2), 'Ruim': (2, 5), 'Moderado': (5, 8), 'Bom': (8, 10), 'Ótimo': (10, float('inf'))},
    'ROE': {'Péssimo': (0, 5), 'Ruim': (5, 10), 'Moderado': (10, 15), 'Bom': (15, 20), 'Ótimo': (20, float('inf'))},
    'CAGR Lucros 5 anos': {'Péssimo': (0, 5), 'Ruim': (5, 10), 'Moderado': (10, 15), 'Bom': (15, 20),
                           'Ótimo': (20, float('inf'))},
    'ROIC': {'Péssimo': (0, 5), 'Ruim': (5, 10), 'Moderado': (10, 15), 'Bom': (15, 20), 'Ótimo': (20, float('inf'))},
    'VPA': {'Péssimo': (0, 0.5), 'Ruim': (0.5, 1), 'Moderado': (1, 2), 'Bom': (2, 5), 'Ótimo': (5, float('inf'))},
    'PL/Ativos': {'Péssimo': (0, 0.2), 'Ruim': (0.2, 0.3), 'Moderado': (0.3, 0.5), 'Bom': (0.5, 0.7),
                  'Ótimo': (0.7, float('inf'))}
}

# Grupos de indicadores com dependências
GROUPS = {
    'Liquidez e Solvência': ['Liquidez Corrente', 'P/Ativo Circulante Líquido', 'P/Capital de Giro'],
    'Alavancagem Financeira': ['Dívida Líquida/EBIT', 'Dívida Líquida/EBITDA', 'Dívida Líquida/Patrimônio Líquido',
                               'Patrimônio/Ativos'],
    'Rentabilidade Operacional': ['Margem Bruta', 'Margem EBIT', 'Margem EBITDA', 'Margem Líquida'],
    'Eficiência e Retorno': ['ROA', 'ROE', 'ROIC', 'Giro do Ativo'],
    'Valuation e Retorno ao Acionista': ['P/L', 'P/VPA', 'EV/EBIT', 'EV/EBITDA', 'LPA', 'VPA', 'Dividend Yield (DY)'],
    'Crescimento e Sustentabilidade': ['CAGR Lucros 5 anos', 'ROIC'],
    'Avaliação de Receita': ['PSR', 'Giro do Ativo']
}


# Função para classificar um indicador com base na faixa
def classify_indicator(indicator, value):
    if value is None or pd.isna(value):
        return 'Não informado', 'Dados ausentes para análise.'

    for rating, (low, high) in INDICATORS[indicator].items():
        if low <= value < high:
            return rating, f"Valor {value:.2f} está na faixa {rating} ({low} a {high})."
    return 'Fora de faixa', f"Valor {value:.2f} fora das faixas definidas."


# Função para análise conjunta de um grupo de indicadores
def analyze_group(group_name, indicators_data):
    group_indicators = GROUPS[group_name]
    analysis = []

    for indicator in group_indicators:
        value = indicators_data.get(indicator, None)
        rating, comment = classify_indicator(indicator, value)
        analysis.append({
            'Indicador': indicator,
            'Valor': value if value is not None else 'N/A',
            'Classificação': rating,
            'Comentário': comment
        })

    # Análise conjunta específica por grupo
    joint_analysis = ""
    if group_name == 'Liquidez e Solvência':
        liq_corrente = indicators_data.get('Liquidez Corrente', None)
        p_ativo_circ = indicators_data.get('P/Ativo Circulante Líquido', None)
        p_cap_giro = indicators_data.get('P/Capital de Giro', None)
        if liq_corrente and liq_corrente < 0.8 and (p_ativo_circ is None or p_ativo_circ < 0):
            joint_analysis = "Risco crítico de insolvência: baixa liquidez corrente e capital de giro negativo. Exemplo: OIBR3 em crise. Verifique fluxo de caixa operacional."
        elif liq_corrente and liq_corrente > 1.8 and p_ativo_circ > 3:
            joint_analysis = "Forte posição de liquidez, mas cuidado com caixa ocioso (ex.: TOTS3). Analise alocação de capital."
        else:
            joint_analysis = "Liquidez moderada. Combine com análise de alavancagem para avaliar solvência. Exemplo: ABEV3 com liquidez equilibrada."

    elif group_name == 'Alavancagem Financeira':
        div_ebitda = indicators_data.get('Dívida Líquida/EBITDA', None)
        div_patrimonio = indicators_data.get('Dívida Líquida/Patrimônio Líquido', None)
        pat_ativo = indicators_data.get('Patrimônio/Ativos', None)
        if div_ebitda and div_ebitda > 3.5 and div_patrimonio > 1:
            joint_analysis = "Alta alavancagem, risco elevado de default em 2025 (juros 10-12%). Exemplo: OIBR3. Verifique cobertura de juros."
        elif div_ebitda and div_ebitda < 1 and pat_ativo > 0.7:
            joint_analysis = "Baixa alavancagem e estrutura de capital sólida (ex.: WEGE3). Ideal para dividendos ou expansão."
        else:
            joint_analysis = "Alavancagem moderada. Analise fluxo de caixa livre e ROIC para sustentabilidade. Exemplo: PETR4."

    elif group_name == 'Rentabilidade Operacional':
        margem_bruta = indicators_data.get('Margem Bruta', None)
        margem_liquida = indicators_data.get('Margem Líquida', None)
        if margem_bruta and margem_bruta < 15 and margem_liquida < 5:
            joint_analysis = "Baixa rentabilidade, pressão competitiva ou custos elevados (ex.: MGLU3). Verifique custos operacionais."
        elif margem_bruta and margem_bruta > 50 and margem_liquida > 15:
            joint_analysis = "Alta eficiência operacional e rentabilidade (ex.: WEGE3). Confirme consistência com fluxo de caixa."
        else:
            joint_analysis = "Rentabilidade moderada. Combine com Giro do Ativo para avaliar eficiência. Exemplo: ABEV3."

    elif group_name == 'Eficiência e Retorno':
        roe = indicators_data.get('ROE', None)
        roic = indicators_data.get('ROIC', None)
        if roe and roe > 20 and roic > 15:
            joint_analysis = "Alta eficiência e retorno sobre capital (ex.: ITUB4). Ideal para setores maduros."
        elif roe and roe < 5 and roic < 5:
            joint_analysis = "Baixa eficiência, risco de estagnação (ex.: OIBR3). Verifique alavancagem."
        else:
            joint_analysis = "Eficiência moderada. Analise tendências setoriais e fluxo de caixa. Exemplo: VALE3 em recuperação."

    elif group_name == 'Valuation e Retorno ao Acionista':
        pl = indicators_data.get('P/L', None)
        pvpa = indicators_data.get('P/VPA', None)
        dy = indicators_data.get('Dividend Yield (DY)', None)
        if pl and pl > 20 and pvpa > 2 and (dy is None or dy < 2):
            joint_analysis = "Sobrevalorizada com baixo retorno (ex.: NUBR33). Exige forte crescimento para justificar."
        elif pl and pl < 10 and pvpa < 1 and dy > 4:
            joint_analysis = "Subvalorizada com bom retorno (ex.: VALE3 em baixa). Oportunidade em setores cíclicos."
        else:
            joint_analysis = "Valuation equilibrado. Combine com ROE e CAGR para confirmar potencial. Exemplo: ITUB4."

    elif group_name == 'Crescimento e Sustentabilidade':
        cagr = indicators_data.get('CAGR Lucros 5 anos', None)
        roic = indicators_data.get('ROIC', None)
        if cagr and cagr > 15 and roic > 15:
            joint_analysis = "Crescimento sustentável e eficiente (ex.: WEGE3). Ideal para tecnologia."
        elif cagr and cagr < 5 and roic < 5:
            joint_analysis = "Estagnação ou ineficiência (ex.: OIBR3). Verifique planos de recuperação."
        else:
            joint_analysis = "Crescimento moderado. Analise tendências setoriais e barreiras de entrada. Exemplo: TOTS3."

    elif group_name == 'Avaliação de Receita':
        psr = indicators_data.get('PSR', None)
        giro_ativo = indicators_data.get('Giro do Ativo', None)
        if psr and psr < 1 and giro_ativo > 1.2:
            joint_analysis = "Subvalorizada com alta eficiência de receita (ex.: VALE3). Oportunidade em setores cíclicos."
        elif psr and psr > 3 and giro_ativo < 0.4:
            joint_analysis = "Sobrevalorizada com baixa eficiência (ex.: startups). Verifique margens."
        else:
            joint_analysis = "Eficiência moderada. Combine com Margem Líquida para confirmar rentabilidade. Exemplo: LREN3."

    return analysis, joint_analysis


# Função principal para coletar dados e gerar análise
def main():
    print("=== Ferramenta de Análise Fundamentalista (29/06/2025) ===")
    print("Insira os valores dos indicadores financeiros (deixe em branco para N/A):")

    # Coleta de dados do usuário
    indicators_data = {}
    for indicator in INDICATORS.keys():
        while True:
            try:
                value = input(f"{indicator} (ex.: 1.5, pressione Enter para N/A): ")
                if value.strip() == "":
                    indicators_data[indicator] = None
                    break
                indicators_data[indicator] = float(value)
                break
            except ValueError:
                print("Entrada inválida. Insira um número ou deixe em branco.")

    # Análise por grupo
    results = []
    joint_comments = []

    for group_name in GROUPS.keys():
        group_analysis, joint_analysis = analyze_group(group_name, indicators_data)
        results.extend(group_analysis)
        joint_comments.append({'Grupo': group_name, 'Análise Conjunta': joint_analysis})

    # Criar DataFrame com os resultados
    df_results = pd.DataFrame(results)
    df_joint = pd.DataFrame(joint_comments)

    # Exibir tabelas
    print("\n=== Resultado da Análise ===")
    print(tabulate(df_results, headers='keys', tablefmt='pretty', showindex=False))
    print("\n=== Análise Conjunta por Grupo ===")
    print(tabulate(df_joint, headers='keys', tablefmt='pretty', showindex=False))

    # Gerar gráfico de barras para classificações
    ratings_count = df_results['Classificação'].value_counts()
    plt.figure(figsize=(10, 6))
    ratings_count.plot(kind='bar', color=['red', 'orange', 'yellow', 'lightgreen', 'green'])
    plt.title('Distribuição das Classificações dos Indicadores')
    plt.xlabel('Classificação')
    plt.ylabel('Quantidade')
    plt.tight_layout()
    plt.show()

    # Salvar resultados em CSV
    df_results.to_csv('analise_indicadores.csv', index=False)
    df_joint.to_csv('analise_conjunta.csv', index=False)
    print("\nResultados salvos em 'analise_indicadores.csv' e 'analise_conjunta.csv'.")


if __name__ == "__main__":
    main()
