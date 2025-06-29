```python
# Código Python para Análise Fundamentalista Completa
# Data: 29/06/2025
# Descrição: Ferramenta interativa e robusta para análise fundamentalista de indicadores financeiros,
# com suporte a entrada flexível, análise conjunta, gráficos interativos, e exportação para CSV/Excel/PDF.
# Autor: Grok 3 (xAI)

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from tabulate import tabulate
import openpyxl
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import json
import os
from datetime import datetime

# Definição das faixas de referência por indicador e setor
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

# Benchmarks setoriais (médias aproximadas para 2025, baseadas em padrões de mercado)
SECTOR_BENCHMARKS = {
    'Bancos': {'P/L': 10, 'ROE': 15, 'DY': 5, 'Margem Líquida': 15, 'Dívida Líquida/EBITDA': 0.8},
    'Varejo': {'P/L': 12, 'ROE': 12, 'DY': 3, 'Margem Líquida': 5, 'Giro do Ativo': 1.2},
    'Mineração': {'P/L': 6, 'ROE': 20, 'DY': 7, 'EV/EBITDA': 4, 'Dívida Líquida/EBITDA': 2},
    'Utilities': {'P/L': 8, 'ROE': 10, 'DY': 6, 'Dívida Líquida/EBITDA': 2.5, 'Margem EBITDA': 30},
    'Tecnologia': {'P/L': 15, 'ROE': 18, 'DY': 1, 'CAGR Lucros 5 anos': 20, 'Margem Bruta': 50}
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


# Função para comparar com benchmarks setoriais
def compare_to_benchmark(indicator, value, sector):
    if sector not in SECTOR_BENCHMARKS or indicator not in SECTOR_BENCHMARKS[sector]:
        return "Sem benchmark setorial disponível."
    benchmark = SECTOR_BENCHMARKS[sector][indicator]
    if value is None:
        return "Valor não informado para comparação."
    if value > benchmark * 1.2:
        return f"Valor {value:.2f} acima do benchmark setorial ({benchmark:.2f})."
    elif value < benchmark * 0.8:
        return f"Valor {value:.2f} abaixo do benchmark setorial ({benchmark:.2f})."
    else:
        return f"Valor {value:.2f} alinhado com o benchmark setorial ({benchmark:.2f})."


# Função para análise conjunta de um grupo de indicadores
def analyze_group(group_name, indicators_data, sector):
    group_indicators = GROUPS[group_name]
    analysis = []

    for indicator in group_indicators:
        value = indicators_data.get(indicator, None)
        rating, comment = classify_indicator(indicator, value)
        benchmark_comment = compare_to_benchmark(indicator, value, sector)
        analysis.append({
            'Indicador': indicator,
            'Valor': value if value is not None else 'N/A',
            'Classificação': rating,
            'Comentário': comment,
            'Benchmark': benchmark_comment
        })

    # Análise conjunta específica por grupo
    joint_analysis = ""
    if group_name == 'Liquidez e Solvência':
        liq_corrente = indicators_data.get('Liquidez Corrente', None)
        p_ativo_circ = indicators_data.get('P/Ativo Circulante Líquido', None)
        if liq_corrente and liq_corrente < 0.8 and (p_ativo_circ is None or p_ativo_circ < 0):
            joint_analysis = "Risco crítico de insolvência: baixa liquidez e capital de giro negativo. Exemplo: OIBR3 em crise. Recomendação: Evitar investimento até reestruturação."
        elif liq_corrente and liq_corrente > 1.8 and p_ativo_circ > 3:
            joint_analysis = "Forte liquidez, mas risco de caixa ocioso (ex.: TOTS3). Verifique alocação de capital e compare com setores defensivos (ex.: ABEV3)."
        else:
            joint_analysis = "Liquidez moderada. Combine com análise de alavancagem para avaliar solvência em 2025 (juros altos). Exemplo: LREN3."

    elif group_name == 'Alavancagem Financeira':
        div_ebitda = indicators_data.get('Dívida Líquida/EBITDA', None)
        div_patrimonio = indicators_data.get('Dívida Líquida/Patrimônio Líquido', None)
        if div_ebitda and div_ebitda > 3.5 and div_patrimonio > 1:
            joint_analysis = "Alta alavancagem, risco elevado em 2025 (juros 10-12%). Exemplo: OIBR3. Recomendação: Analise cobertura de juros (EBITDA/juros > 3) e planos de desalavancagem."
        elif div_ebitda and div_ebitda < 1 and div_patrimonio < 0.3:
            joint_analysis = "Baixa alavancagem, estrutura de capital sólida (ex.: WEGE3). Ideal para setores defensivos ou expansão."
        else:
            joint_analysis = "Alavancagem moderada. Verifique fluxo de caixa livre e tendências setoriais (ex.: VALE3 em ciclos de minério)."

    elif group_name == 'Rentabilidade Operacional':
        margem_bruta = indicators_data.get('Margem Bruta', None)
        margem_liquida = indicators_data.get('Margem Líquida', None)
        if margem_bruta and margem_bruta < 15 and margem_liquida < 5:
            joint_analysis = "Baixa rentabilidade, pressão competitiva ou custos elevados (ex.: MGLU3). Recomendação: Evitar setores com margens comprimidas em 2025."
        elif margem_bruta and margem_bruta > 50 and margem_liquida > 15:
            joint_analysis = "Alta eficiência operacional (ex.: WEGE3). Ideal para tecnologia ou consumo defensivo."
        else:
            joint_analysis = "Rentabilidade moderada. Combine com Giro do Ativo e ROIC para avaliar eficiência. Exemplo: ABEV3."

    elif group_name == 'Eficiência e Retorno':
        roe = indicators_data.get('ROE', None)
        roic = indicators_data.get('ROIC', None)
        if roe and roe > 20 and roic > 15:
            joint_analysis = "Alta eficiência e retorno (ex.: ITUB4). Ideal para bancos ou tecnologia em 2025."
        elif roe and roe < 5 and roic < 5:
            joint_analysis = "Baixa eficiência, risco de estagnação (ex.: OIBR3). Recomendação: Evitar até sinais de recuperação."
        else:
            joint_analysis = "Eficiência moderada. Analise tendências setoriais (ex.: VALE3 em recuperação)."

    elif group_name == 'Valuation e Retorno ao Acionista':
        pl = indicators_data.get('P/L', None)
        pvpa = indicators_data.get('P/VPA', None)
        dy = indicators_data.get('Dividend Yield (DY)', None)
        if pl and pl > 20 and pvpa > 2 and (dy is None or dy < 2):
            joint_analysis = "Sobrevalorizada com baixo retorno (ex.: NUBR33). Exige forte crescimento para justificar em 2025."
        elif pl and pl < 10 and pvpa < 1 and dy > 4:
            joint_analysis = "Subvalorizada com bom retorno (ex.: VALE3). Oportunidade em setores cíclicos."
        else:
            joint_analysis = "Valuation equilibrado. Combine com ROE e CAGR para confirmar potencial (ex.: ITUB4)."

    elif group_name == 'Crescimento e Sustentabilidade':
        cagr = indicators_data.get('CAGR Lucros 5 anos', None)
        roic = indicators_data.get('ROIC', None)
        if cagr and cagr > 15 and roic > 15:
            joint_analysis = "Crescimento sustentável (ex.: WEGE3). Ideal para tecnologia em 2025."
        elif cagr and cagr < 5 and roic < 5:
            joint_analysis = "Estagnação ou ineficiência (ex.: OIBR3). Recomendação: Evitar até recuperação."
        else:
            joint_analysis = "Crescimento moderado. Verifique barreiras de entrada e inovação (ex.: TOTS3)."

    elif group_name == 'Avaliação de Receita':
        psr = indicators_data.get('PSR', None)
        giro_ativo = indicators_data.get('Giro do Ativo', None)
        if psr and psr < 1 and giro_ativo > 1.2:
            joint_analysis = "Subvalorizada com alta eficiência (ex.: VALE3). Oportunidade em setores cíclicos."
        elif psr and psr > 3 and giro_ativo < 0.4:
            joint_analysis = "Sobrevalorizada com baixa eficiência (ex.: startups). Verifique margens."
        else:
            joint_analysis = "Eficiência moderada. Combine com Margem Líquida (ex.: LREN3)."

    return analysis, joint_analysis


# Função para coletar dados do usuário
def collect_data():
    print("=== Ferramenta de Análise Fundamentalista (29/06/2025) ===")
    print("Escolha o método de entrada:")
    print("1. Manual (console)")
    print("2. Arquivo CSV")
    print("3. Arquivo Excel")
    print("4. JSON")
    method = input("Digite o número da opção (1-4): ")

    indicators_data = {}
    sector = input("Digite o setor da empresa (ex.: Bancos, Varejo, Mineração, Utilities, Tecnologia): ").capitalize()

    if method == '1':
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

    elif method in ['2', '3']:
        file_path = input("Digite o caminho do arquivo (CSV ou Excel): ")
        try:
            if method == '2':
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)
            for indicator in INDICATORS.keys():
                indicators_data[indicator] = df.get(indicator, [None])[0]
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            return None, None

    elif method == '4':
        file_path = input("Digite o caminho do arquivo JSON: ")
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            for indicator in INDICATORS.keys():
                indicators_data[indicator] = data.get(indicator, None)
        except Exception as e:
            print(f"Erro ao ler o JSON: {e}")
            return None, None

    else:
        print("Opção inválida. Usando entrada manual.")
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

    return indicators_data, sector


# Função para gerar gráficos interativos
def generate_plots(results, joint_comments):
    # Gráfico de barras para classificações
    df_results = pd.DataFrame(results)
    ratings_count = df_results['Classificação'].value_counts().reindex(['Ótimo', 'Bom', 'Moderado', 'Ruim', 'Péssimo'],
                                                                       fill_value=0)
    fig_bar = px.bar(x=ratings_count.index, y=ratings_count.values,
                     title='Distribuição das Classificações dos Indicadores',
                     labels={'x': 'Classificação', 'y': 'Quantidade'}, color=ratings_count.index,
                     color_discrete_map={'Ótimo': 'green', 'Bom': 'lightgreen', 'Moderado': 'yellow', 'Ruim': 'orange',
                                         'Péssimo': 'red'})
    fig_bar.write_layout(showlegend=False)
    fig_bar.write_yaxes(title='Quantidade')
    fig_bar.write_xaxes(title='Classificação')
    fig_bar.write()

    # Radar chart por grupo
    fig_radar = go.Figure()
    for group_name in GROUPS.keys():
        group_data = [r for r in results if r['Indicador'] in GROUPS[group_name]]
        values = [1 if r['Classificação'] == 'Péssimo' else 2 if r['Classificação'] == 'Ruim' else 3 if r[
                                                                                                            'Classificação'] == 'Moderado' else 4 if
        r['Classificação'] == 'Bom' else 5 if r['Classificação'] == 'Ótimo' else 0 for r in group_data]
        indicators = [r['Indicador'] for r in group_data]
        fig_radar.add_trace(go.Scatterpolar(r=values, theta=indicators, fill='toself', name=group_name))

    fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 5])), showlegend=True,
                            title='Radar Chart por Grupo de Indicadores')
    fig_radar.show()

    return fig_bar


# Função para gerar PDF
def generate_pdf(results, joint_comments, sector, filename='analise_fundamentalista.pdf'):
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica", 12)
    y = 800
    c.drawString(50, y, f"Análise Fundamentalista - {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    c.drawString(50, y - 20, f"Setor: {sector}")
    y -= 40

    for group_name in GROUPS.keys():
        c.drawString(50, y, f"Grupo: {group_name}")
        y -= 20
        group_data = [r for r in results if r['Indicador'] in GROUPS[group_name]]
        for row in group_data:
            text = f"{row['Indicador']}: {row['Valor']} ({row['Classificação']}) - {row['Comentário']} | {row['Benchmark']}"
            if y < 50:
                c.showPage()
                y = 800
            for line in textwrap.wrap(text, 100):
                c.drawString(50, y, line)
                y -= 15
        joint = next((j['Análise Conjunta'] for j in joint_comments if j['Grupo'] == group_name), "")
        for line in textwrap.wrap(f"Análise Conjunta: {joint}", 100):
            c.drawString(50, y, line)
            y -= 15
        y -= 10

    c.save()


# Função principal
def main():
    print("=== Ferramenta de Análise Fundamentalista Avançada (29/06/2025) ===")
    indicators_data, sector = collect_data()
    if indicators_data is None:
        print("Erro na coleta de dados. Encerrando.")
        return

    # Análise por grupo
    results = []
    joint_comments = []
    for group_name in GROUPS.keys():
        group_analysis, joint_analysis = analyze_group(group_name, indicators_data, sector)
        results.extend(group_analysis)
        joint_comments.append({'Grupo': group_name, 'Análise Conjunta': joint_analysis})

    # Criar DataFrames
    df_results = pd.DataFrame(results)
    df_joint = pd.DataFrame(joint_comments)

    # Exibir tabelas
    print("\n=== Resultado da Análise ===")
    print(tabulate(df_results, headers='keys', tablefmt='pretty', showindex=False))
    print("\n=== Análise Conjunta por Grupo ===")
    print(tabulate(df_joint, headers='keys', tablefmt='pretty', showindex=False))

    # Gerar gráficos
    fig_bar = generate_plots(results, joint_comments)

    # Exportar resultados
    df_results.to_csv('analise_indicadores.csv', index=False)
    df_joint.to_csv('analise_conjunta.csv', index=False)
    df_results.to_excel('analise_indicadores.xlsx', index=False)
    df_joint.to_excel('analise_conjunta.xlsx', index=False)
    generate_pdf(results, joint_comments, sector)
    print(
        "\nResultados salvos em 'analise_indicadores.csv', 'analise_indicadores.xlsx', 'analise_conjunta.csv', 'analise_conjunta.xlsx', e 'analise_fundamentalista.pdf'.")


if __name__ == "__main__":
    main()
```

entrada
Indicador,Valor
P/L,8
ROE,20
Dívida Líquida/EBITDA,1.5
...