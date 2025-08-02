import openpyxl
import re
import time
import numpy as np
import pandas as pd
from unidecode import unidecode
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, FormulaRule
import requests
# teste silvio 3e
import warnings
from openpyxl.styles import numbers
import analisefundamentalista

#from teste01 import metrica

fillvermelho= PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid") # Vermelho

fillverde= PatternFill(start_color="00FF00", end_color="00FF00", fill_type="solid") # Verde

fillamarelo =  PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid") # Amarelo


fillazul = PatternFill(start_color="0000FF", end_color="0000FF", fill_type="solid") # Azul


#filltitulo =   PatternFill(start_color="#002060", end_color="#002060", fill_type="solid")

filltitulo = PatternFill(start_color="002060", end_color="002060", fill_type="solid")  # Azul escuro

font_branca = Font(color="FFFFFF")  # Branco

TITLES = [
    'Identificação', 'Resumo Financeiro', 'Cotações', 'Informações Básicas',
    'Oscilações', 'Indicadores de Valuation', 'Indicadores de Rentabilidade',
    'Indicadores de Endividamento', 'Balanço Patrimonial', 'Demonstrativo de Resultados'
]

linha2 = 1
metricasts= ""
''''categorias = {
    'otimo': {'min': float('-inf'), 'max': -2},  # Valores muito baixos são ótimos
    'bom': {'min': -2, 'max': 0},               # Valores entre -2 e 0
    'moderado': {'min': 0, 'max': 1.5},         # Valores entre 0 e 1.5
    'ruim': {'min': 1.5, 'max': 3},             # Valores entre 1.5 e 3
    'pessimo': {'min': 3, 'max': 4},            # Valores entre 3 e 4
    'critico': {'min': 4, 'max': float('inf')}   # Valores acima de 4
}'''
MetricasStatus = {'Giro ativos', 'Div. liquida/PL','Div. liquida/EBITDA','Div. liquida/EBIT','PL/Ativos',
                           'Passivos/Ativos','Liq. corrente','P/L','PEG Ratio','P/VP','EV/EBITDA','EV/EBIT',
                            'P/EBITDA','P/EBIT','VPA','P/Ativo','LPA',
                            'P/SR','P/Ativo Circ. Liq.','Valor atual','LIQUIDEZ MEDIA DIARIA','Patrimonio liquido',
                             'Ativos','Ativo circulante','Divida bruta','Disponibilidade',
                             'Divida liquida','Valor de mercado','Valor de firma'}

wbsaida = openpyxl.Workbook()


# define selenium webdriver options
options = webdriver.ChromeOptions()

# create selenium webdriver instance
driver = webdriver.Chrome(options=options)

def classificar_divida_ebit(valor):
        indicadortratado = tratamento2(dict_stocks[stock].get('LPA'))
       # print("Pl" , indicadortratado)
        if valor == float('-inf') or valor < 0:
            return {'classificacao': 'pessimo', 'descricao': 'teste'}
        elif 0 <= valor < 1.5:
            return {'classificacao': 'pessimo', 'descricao': 'teste'}
        elif 1.5 <= valor < 3:
            return {'classificacao': 'pessimo', 'descricao': 'teste'}
        elif 3 <= valor < 4:
            return {'classificacao': 'pessimo', 'descricao': 'teste'}
        elif valor >= 4:
            return {'classificacao': 'pessimo', 'descricao': 'teste'}
        else:
            return {'classificacao': 'pessimo', 'descricao': 'teste'}

def evaluate_pl(PL):
    ''''Avalia o Preço/Lucro (P/L) com base em faixas definidas para o mercado brasileiro:
    - P/L < 0: Crítico (prejuízo, risco elevado)
    - 0 ≤ P/L ≤ 10: Ótimo (subvalorizado, oportunidade de compra)
    - 10 < P/L ≤ 15: Moderado (valuation justo, crescimento moderado)
    - 15 < P/L ≤ 20: Ruim (sobrevalorizado, cautela necessária)
    - 20 < P/L ≤ 30: Péssimo (muito caro, alto risco)
    - P/L > 30: Fora da faixa (extremamente sobrevalorizado, risco elevado)'''
    # if lucro_liquido <= 0:  # Lucro Líquido negativo indica prejuízo
    #    return 'critico'   colocar no futuro integração com o fundamentus
    try:
        if PL < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'PL < 0',
                'descricao': 'P/L negativo indica que a empresa está com prejuízo, sugerindo riscos como problemas operacionais, má gestão ou dificuldades de mercado. Pode ser temporário em setores cíclicos (ex.: celulose, mineração), mas exige análise de fundamentos como EBITDA e fluxo de caixa para avaliar recuperação.'
            }
        elif 0 <= PL <= 10:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= PL <= 10',
                'descricao': 'P/L baixo sugere que a ação está subvalorizada ou que o mercado tem perspectiva negativa sobre o futuro da empresa. Comum em setores maduros (ex.: bancos, utilities) ou em empresas com desafios financeiros temporários. Pode representar uma oportunidade de valor se o mercado estiver subestimando o potencial de recuperação.'
            }
        elif 10 < PL <= 15:
            return {
                    'classificacao': 'Moderado',
                'faixa': '10 < PL <= 15',
                'descricao': 'P/L indica valuation justo, típico de empresas com crescimento estável e fundamentos sólidos. Comum em setores consolidados com margens previsíveis (ex.: varejo, energia). Menos potencial de upside que ações subvalorizadas, mas oferece equilíbrio entre risco e retorno.'
            }
        elif 15 < PL <= 20:
            return {
                'classificacao': 'Ruim',
                'faixa': '15 < PL <= 20',
                'descricao': 'P/L elevado sugere sobrevalorização moderada, indicando que o mercado espera crescimento, mas com riscos crescentes. Pode ser justificado em setores dinâmicos (ex.: varejo tech), mas exige análise de perspectivas de lucro e comparação com pares do setor.'
            }
        elif 20 < PL <= 30:
            return {
                'classificacao': 'Pessimo',
                'faixa': '20 < PL <= 30',
                'descricao': 'P/L muito alto indica que a ação está cara, com expectativas de crescimento elevadas que podem não se concretizar. Comum em setores de alto crescimento (ex.: tecnologia), mas há risco significativo de correção se os resultados desapontarem.'
            }
        else:  # PL > 30
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'PL > 30',
                'descricao': 'P/L extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas de mercado. Pode ser aceitável em setores de crescimento excepcional (ex.: tecnologia, biotech), mas o risco de correção é alto. Análise detalhada do crescimento futuro é essencial.'
            }

    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        # print(metrica)  # Certifique-se de que metrica está definida
        # print(indicadortratado)  # Certifique-se de que indicadortratado está definida
        #print('tratamneto - erro', stock, "   ", metrica)

def evaluate_pvp(PVP):
    '''
    Avalia o Preço/Valor Patrimonial (P/VP) com base em faixas definidas para o mercado brasileiro:
    - P/VP < 0: Crítico (patrimônio líquido negativo, risco elevado)
    - 0 ≤ P/VP ≤ 1: Subvalorizado (ótimo, ação abaixo do patrimônio)
    - 1 < P/VP ≤ 2: Justo (moderado, valuation alinhado)
    - 2 < P/VP ≤ 3: Caro (ruim, sobrevalorizado)
    - 3 < P/VP ≤ 5: Muito Caro (péssimo, alto risco)
    - P/VP > 5: Extremamente Caro (fora da faixa, risco elevado)

    Args:
        PVP (float or int): Valor do índice Preço/Valor Patrimonial.

    Returns:
        dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do P/VP.

    Raises:
        TypeError: Se PVP não for um número (int ou float).
    '''
    try:
        if PVP < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'P/VP < 0',
                'descricao': 'P/VP negativo indica patrimônio líquido negativo, sugerindo graves problemas financeiros, como dívidas elevadas ou prejuízos recorrentes. Extremamente raro, exige análise cuidadosa de ativos e passivos para avaliar viabilidade.'
            }
        elif 0 <= PVP <= 1:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= P/VP <= 1',
                'descricao': 'P/VP baixo sugere que a ação está subvalorizada, negociada abaixo de seu valor patrimonial. Comum em setores maduros (ex.: bancos, siderurgia) ou empresas com desafios temporários. Representa uma oportunidade de compra se os fundamentos forem sólidos.'
            }
        elif 1 < PVP <= 2:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < P/VP <= 2',
                'descricao': 'P/VP indica valuation justo, típico de empresas com estabilidade financeira e crescimento moderado. Comum em setores consolidados (ex.: energia, celulose). Oferece equilíbrio entre risco e retorno, com potencial de valorização moderado.'
            }
        elif 2 < PVP <= 3:
            return {
                'classificacao': 'Ruim',
                'faixa': '2 < P/VP <= 3',
                'descricao': 'P/VP elevado sugere sobrevalorização moderada, com o mercado precificando crescimento ou ativos intangíveis (ex.: marca, tecnologia). Pode ser justificado em setores dinâmicos, mas exige análise de perspectivas de lucro e comparação com pares do setor.'
            }
        elif 3 < PVP <= 5:
            return {
                'classificacao': 'Pessimo',
                'faixa': '3 < P/VP <= 5',
                'descricao': 'P/VP muito alto indica que a ação está cara, com expectativas de crescimento elevadas que podem não se concretizar. Comum em setores de alto crescimento (ex.: tecnologia, varejo online), mas há risco significativo de correção se os resultados desapontarem.'
            }
        else:  # pvp > 5
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/VP > 5',
                'descricao': 'P/VP extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas de mercado. Pode ser aceitável em setores de crescimento excepcional (ex.: tecnologia, biotech), mas o risco de correção é alto. Análise detalhada do crescimento futuro é essencial.'
            }

    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        # print(metrica)  # Certifique-se de que metrica está definida
        # print(indicadortratado)  # Certifique-se de que indicadortratado está definida


def evaluate_pebitda(pebitda):
            """
            Avalia o Preço/EBITDA (P/EBITDA) com base em faixas definidas para o mercado brasileiro:
            - P/EBITDA < 0: Crítico (EBITDA negativo, risco extremo)
            - 0 ≤ P/EBITDA ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
            - 5 < P/EBITDA ≤ 8: Moderado (valuation justo, crescimento moderado)
            - 8 < P/EBITDA ≤ 12: Ruim (sobrevalorizado, cautela necessária)
            - 12 < P/EBITDA ≤ 16: Péssimo (muito caro, alto risco)
            - P/EBITDA > 16: Fora da faixa (extremamente sobrevalorizado, risco elevado)

            Args:
                pebitda (float or int): Valor do índice Preço/EBITDA.

            Returns:
                dict: Dicionário com 'classificacao', 'faixa' e 'descricao' do P/EBITDA.

            Raises:
                TypeError: Se P/EBITDA não for um número (int ou float).
            """
            # TODO: Futura integração com Fundamentus para obter P/EBITDA automaticamente
            # Exemplo: Usar web scraping ou API para extrair dados de https://www.fundamentus.com.br/

            try:
                if pebitda < 0:
                    return {
                        'classificacao': 'Critico',
                        'faixa': 'P/EBITDA < 0',
                        'descricao': 'P/EBITDA negativo indica EBITDA negativo, sugerindo graves problemas operacionais ou crise financeira. Extremamente raro, exige análise detalhada de fluxo de caixa e perspectivas de recuperação.'
                    }
                elif 0 <= pebitda <= 5:
                    return {
                        'classificacao': 'Otimo',
                        'faixa': '0 <= P/EBITDA <= 5',
                        'descricao': 'P/EBITDA baixo sugere que a ação está subvalorizada em relação à sua geração de caixa operacional. Comum em setores maduros (ex.: bancos, utilities) ou empresas em recuperação. Representa uma oportunidade de compra se os fundamentos forem sólidos.'
                    }
                elif 5 < pebitda <= 8:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '5 < P/EBITDA <= 8',
                        'descricao': 'P/EBITDA indica valuation justo, típico de empresas com geração de caixa estável e crescimento moderado. Comum em setores consolidados (ex.: indústria, energia). Oferece equilíbrio entre risco e retorno.'
                    }
                elif 8 < pebitda <= 12:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '8 < P/EBITDA <= 12',
                        'descricao': 'P/EBITDA elevado sugere sobrevalorização, com o mercado esperando crescimento significativo. Aceitável em setores dinâmicos (ex.: varejo tech), mas exige cautela e comparação com a média do setor.'
                    }
                elif 12 < pebitda <= 16:
                    return {
                        'classificacao': 'Pessimo',
                        'faixa': '12 < P/EBITDA <= 16',
                        'descricao': 'P/EBITDA muito alto indica que a ação está cara, com expectativas de crescimento elevadas que podem não se concretizar. Comum em setores de alto crescimento, mas o risco de correção é significativo.'
                    }
                else:  # pebitda > 16
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'P/EBITDA > 16',
                        'descricao': 'P/EBITDA extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas de mercado. Pode ser justificado em setores de crescimento excepcional (ex.: tecnologia, biotech), mas o risco de correção é alto.'
                    }

            except Exception as e:
                print(f"Erro inesperado tratamento : {e}")
                # print(metrica)  # Certifique-se de que metrica está definida
                # print(indicadortratado)  # Certifique-se de que indicadortratado está definida
                # print('tratamneto - erro', stock, "   ", metrica)


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
    # TODO: Futura integração com Fundamentus para obter P/EBIT automaticamente
    # Exemplo: Usar web scraping ou API para extrair dados de https://www.fundamentus.com.br/

    try:
        if pebit < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'P/EBIT < 0',
                'descricao': 'P/EBIT negativo indica prejuízo operacional, sugerindo sérios problemas na geração de lucro antes de juros e impostos. Exige análise detalhada da operação e perspectivas de recuperação.'
            }
        elif 0 <= pebit <= 6:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= P/EBIT <= 6',
                'descricao': 'P/EBIT baixo sugere que a ação está subvalorizada em relação ao lucro operacional. Pode representar uma oportunidade de compra, especialmente em setores maduros ou empresas em recuperação.'
            }
        elif 6 < pebit <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '6 < P/EBIT <= 10',
                'descricao': 'P/EBIT indica valuation justo, típico de empresas com operação estável e crescimento moderado. Comum em setores consolidados como energia e indústria.'
            }
        elif 10 < pebit <= 15:
            return {
                'classificacao': 'Ruim',
                'faixa': '10 < P/EBIT <= 15',
                'descricao': 'P/EBIT elevado sugere sobrevalorização, com o mercado esperando crescimento significativo. Aceitável em setores dinâmicos, mas exige cautela e análise comparativa.'
            }
        elif 15 < pebit <= 20:
            return {
                'classificacao': 'Pessimo',
                'faixa': '15 < P/EBIT <= 20',
                'descricao': 'P/EBIT muito alto indica que a ação está cara, com expectativas elevadas que podem não se concretizar. Comum em empresas de crescimento acelerado, mas com risco elevado.'
            }
        else:  # pebit > 20
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/EBIT > 20',
                'descricao': 'P/EBIT extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas ou em bolhas. Pode ser aceitável em setores de inovação, mas o risco de correção é alto.'
            }

    except Exception as e:
        print(f"Erro inesperado no tratamento: {e}")


def categorizar_valor(metrica, valor):
    try:
        if metrica not in MetricasStatus:
            return 'Métrica não reconhecida'
        valor2 = float(valor)
        #print("categoriza_valor", valor2)
        for categoria, limites in MetricasStatus[metrica].items():

            if categoria in ['descricao', 'agrupador','descrcritico','descrpessimo','descrruim','descrmoderado','descrbom','descrotimo']:
                continue
            if limites['min'] <= valor2 < limites['max']:
                return categoria
        return 'Valor fora do alcance definido'
    except Exception as e:
        print("Debug - limites:", limites)
        print(f"Erro inesperado categorizar: {e}")
        print(f"Erro metrica: {e}")
        print("categorizar_valor - Erro" , metrica)
        print("categoriza_valor", valor2)
        print('categoriza_valor' ,stock)
    finally:
       # print("categorizar_valor - OK2")
       pass

def criaPlanilhaIndRentabilidade(wbsaida):
    wbsaida.create_sheet('IndiRentabilidade')
    IndiRentabilidade = wbsaida['IndiRentabilidade']
    IndiRentabilidade.append(
        ['Agrupador', 'Fonte', 'ATIVO', 'Indicador', 'Valor', 'Referencia','Critico', 'Pessimo','Ruim', 'Moderado', 'Bom', 'Otimo', 'Descrição'])

    for cell in IndiRentabilidade[1]:  # Apenas o cabeçalho
        cell.fill = filltitulo
        cell.font = font_branca

def tratamento(indicador):
    indicador2 = indicador

    try:
        if indicador2 in ["-", "--","--%"]:
            indicador2 = 0
        elif indicador2 is None or is_null_zero_or_spaces(indicador2):
            indicador2 = 0
        else:
            if indicador2 == "":  # Verificação adicionada para string vazia
                indicador2 = 0
            else:
                indicador2 = float(indicador2.strip('%')) / 100
        return indicador2

    except Exception as e:
        print(f"Erro inesperado tratamento : {e}", "metrica  ", metricasts, " indicador  ", indicador, " stock  ",stock)
        # print(metrica)  # Certifique-se de que metrica está definida
        # print(indicadortratado)  # Certifique-se de que indicadortratado está definida
        #print('tratamneto - erro', stock, "   ", metrica)


    finally:
       # print('tratamneto OK')
       pass
def tratamento3(indicador):
    indicador2 = indicador

    try:
        if indicador2 in ["-", "--","--%"]:
            indicador2 = 0
        elif indicador2 is None or is_null_zero_or_spaces(indicador2):
            indicador2 = 0
        else:
            if indicador2 == "":  # Verificação adicionada para string vazia
                indicador2 = 0
            else:
                indicador2 = float(indicador2)
        return indicador2

    except Exception as e:
        print(f"Erro inesperado tratamento 3 : {e}", " metrica  ", metricasts, " indicador  ", indicador, " stock  ",stock)
        # print(metrica)  # Certifique-se de que metrica está definida
        # print(indicadortratado)  # Certifique-se de que indicadortratado está definida
        #print('tratamneto3 - erro', stock, "   ", metrica)


    finally:
        #print('tratamneto3 OK')
        pass
# Certifique-se de que as variáveis `metrica` e `indicadortratado` estão definidas corretamente no contexto onde a função é chamada.

def tratamento2(indicador):
    indicador2 = indicador

    try:
        if indicador2 in ["-", "--","--%"]:
            indicador2 = 0
        elif indicador2 is None or is_null_zero_or_spaces(indicador2):
            indicador2 = 0
        elif indicador2 == "":  # Verificação adicionada para string vazia
            indicador2 = 0
        else:
            indicador2 = float(indicador2)
        return indicador2


        return indicador2
    except Exception as e:
      # print(f"Erro inesperado tratamento2: {e}", " metrica  ", metrica, " indicador  ", indicador ," stock ", stock)
        # print(metrica) g # Certifique-se de que metrica está definida
        # print(indicadortratado)  # Certifique-se de que indicadortratado está definida
        print('tratamneto2 - erro', stock)


    finally:
        #print('tratamneto2 OK', indicador)
        pass
def gravaIndiEficiênciaoStaus(wsIndiRentabilidade, dict_stocks, stock):
    # fontes ['StatusInvest', 'Fundamentus']



    global linha2
    global metricasts
    #linha2 = 1
    try:
        #print(dict_stocks)
        for metrica in MetricasStatus:
    #        print(f'Métrica: {metrica}')
            linha2 += 1
            metricasts = metrica
            if metrica in ['Giro ativos', 'Div. liquida/PL','Div. liquida/EBITDA','Div. liquida/EBIT','PL/Ativos',
                           'Passivos/Ativos','Liq. corrente','P/L','PEG Ratio','P/VP','EV/EBITDA','EV/EBIT',
                            'P/EBITDA','P/EBIT','VPA','P/Ativo','LPA',
                            'P/SR','P/Ativo Circ. Liq.']:
             #   print('IF tratamneto2 ',metrica )

                indicadortratado = tratamento2(dict_stocks[stock].get(metrica))
                valor_pl = indicadortratado
                resultado = analisefundamentalista.evaluate_pl(valor_pl)
                faixa1 = resultado['faixa']
                descricao1 = resultado['descricao']
                print("func1" + faixa1)
                print("func2" + descricao1)

               # categoria_pl = categorizar_valor(metrica, (valor_pl))
                if metrica == 'P/L':
                   categoria_pl = evaluate_pl(valor_pl)
                if metrica == 'P/VP':
                   categoria_pl = evaluate_pvp(valor_pl)
                if metrica == 'P/EBITDA':
                   categoria_pl = evaluate_pebitda(valor_pl)
                if metrica == 'P/EBIT':
                    categoria_pl = evaluate_pebit(valor_pl)

                classificacao = categoria_pl['classificacao']
                faixa = categoria_pl['faixa']
                descricao = categoria_pl['descricao']

                print(f"Classificação:" + classificacao)
                print(f"Faixa:" +  faixa)
                #print(retorno)
                #teste = classificar_divida_ebit(valor_pl)
                 #print("descricao:", teste['descricao'])
                 #print("Classificação:", teste['classificacao'])
                #print(teste)
                #print(teste['classificacao'])  # saída: 'pessimo'
                #print(teste['descricao'])  # saída: 'teste'
              #  print("categoria " + categoria_pl)
               # print("categoria tratamento2 " + categoria_pl)
            elif metrica in ['Valor atual','LIQUIDEZ MEDIA DIARIA','Patrimonio liquido',
                             'Ativos','Ativo circulante','Divida bruta','Disponibilidade',
                             'Divida liquida','Valor de mercado','Valor de firma']:
               # print('IF tratamneto3 ', metrica)
               # print("categoria " + categoria_pl)
               # print('Patrimonio liquido ' + dict_stocks[stock].get('Patrimonio liquido'))
                indicadortratado = tratamento3(dict_stocks[stock].get(metrica))
                valor_pl = indicadortratado
                categoria_pl = categorizar_valor(metrica, (valor_pl))
               # print("categoria tratamento3" + categoria_pl)
            else:
               # print('IF tratamneto ', metrica)
                indicadortratado = tratamento(dict_stocks[stock].get(metrica))
                valor_pl = indicadortratado
                categoria_pl = categorizar_valor(metrica,(valor_pl * 100))
                #print("categoria tratamento" + categoria_pl)
                # Certifique-se de que 'ROE' é o valor correto para a métrica
   #         print(f'O índice P/L {valor_pl} é categorizado como: {categoria_pl}')
   #         print(f"  Agrupador: {detalhes['agrupador']}")


           # wsIndiRentabilidade.cell(row=linha2, column=1, value=detalhes['agrupador'])
            wsIndiRentabilidade.cell(row=linha2, column=2, value='StausInvest')
            wsIndiRentabilidade.cell(row=linha2, column=3, value=stock)
          #  print('celula - Indicador', metrica)
            wsIndiRentabilidade.cell(row=linha2, column=4, value=metrica)
            if metrica in ['Giro ativos', 'Div. liquida/PL','Div. liquida/EBITDA','Div. liquida/EBITDA',
                           'Div. liquida/EBIT','PL/Ativos','Passivos/Ativos','Liq. corrente',
                           'P/L','PEG Ratio','P/VP','EV/EBITDA','EV/EBIT',
                            'P/EBITDA','P/EBIT','VPA','P/Ativo','LPA',
                            'P/SR','P/Ativo Circ. Liq.']:
               # print('IF da celula - Indicador', metrica )
               # print('IF da celula - valor', valor_pl)
                wsIndiRentabilidade.cell(row=linha2, column=5, value=valor_pl).number_format = numbers.FORMAT_NUMBER_00
            elif  metrica in ['Valor atual','LIQUIDEZ MEDIA DIARIA','Patrimonio liquido',
                             'Ativos','Ativo circulante','Divida bruta','Disponibilidade',
                             'Divida liquida','Valor de mercado','Valor de firma']:
                  #print('IF da celula - valor', valor_pl)
                  #print('IF da celula - Indicador', metrica)
                  wsIndiRentabilidade.cell(row=linha2, column=5, value=valor_pl).number_format = 'R$ #,##0.00'
            else:
                wsIndiRentabilidade.cell(row=linha2, column=5, value=valor_pl).number_format = numbers.FORMAT_PERCENTAGE_00


            #print(detalhes)'''
            desc1 =  ("Lucro Líquido ≤ 0: Prejuízo (crítico)- 0 < P/L ≤ 8: Subvalorizado (ótimo) - 8 < P/L ≤ 12:"
                       " Atraente (bom) - 12 < P/L ≤ 18: Neutro (moderado)    - 18 < P/L ≤ 25: Caro (ruim)  - "
                       "P/L > 25: Sobrevalorizado (péssimo) ")




            #if metrica == 'Div. liquida/EBITDA':
            if classificacao == 'Critico':
                wsIndiRentabilidade.cell(row=linha2, column=6, value=classificacao).fill = fillvermelho
                wsIndiRentabilidade.cell(row=linha2, column=7, value=faixa)
                wsIndiRentabilidade.cell(row=linha2, column=13, value=descricao)
            if classificacao == 'Pessimo':
                wsIndiRentabilidade.cell(row=linha2, column=6, value=classificacao).fill = fillvermelho
                wsIndiRentabilidade.cell(row=linha2, column=8, value=faixa)
                wsIndiRentabilidade.cell(row=linha2, column=13, value=descricao)
            if classificacao == 'Ruim':
                wsIndiRentabilidade.cell(row=linha2, column=6, value=classificacao).fill = fillvermelho
                wsIndiRentabilidade.cell(row=linha2, column=9, value=faixa)
                wsIndiRentabilidade.cell(row=linha2, column=13, value=descricao)
            if  classificacao == 'Moderado':
                wsIndiRentabilidade.cell(row=linha2, column=6, value=classificacao).fill =fillamarelo
                wsIndiRentabilidade.cell(row=linha2, column=10, value=faixa)
                wsIndiRentabilidade.cell(row=linha2, column=13, value=descricao)
            if  classificacao == 'Bom':
                wsIndiRentabilidade.cell(row=linha2, column=6, value=classificacao).fill = fillverde
                wsIndiRentabilidade.cell(row=linha2, column=11, value=faixa)
                wsIndiRentabilidade.cell(row=linha2, column=13, value=descricao)
            if classificacao == 'Otimo':
                wsIndiRentabilidade.cell(row=linha2, column=6, value=classificacao).fill =fillazul
                wsIndiRentabilidade.cell(row=linha2, column=12, value=faixa)
                wsIndiRentabilidade.cell(row=linha2, column=13, value=descricao)
            if classificacao == 'Fora da faixa':
                wsIndiRentabilidade.cell(row=linha2, column=6, value=classificacao).fill = fillazul
                wsIndiRentabilidade.cell(row=linha2, column=12, value=faixa)
                wsIndiRentabilidade.cell(row=linha2, column=13, value=descricao)


    except Exception as e:
        print(f"Erro inesperado grava planilha2: {e}")
        print(metrica)
        print(indicadortratado)

        print('gravaIndiEficiênciaoStaus - erro' ,  stock,"    ", metrica)
    finally:
        print('gravaIndiEficiênciaoStaus  OK''', stock)

def is_null_zero_or_spaces(variable):
    # Verifica se a variável é None
    if variable is None:
        return True
    # Verifica se a variável é zero (0)
    elif variable == 0:
        return True
    # Verifica se a variável é uma string e contém apenas espaços
    elif isinstance(variable, str) and variable.strip() == '':
        return True
    elif variable == '-%':
        return True
    else:
        return False


def get_stock_soup(stock):
    ''' Get raw html from a stock '''

    # access the stock urlww
    driver.get(f'https://statusinvest.com.br/acoes/{stock}')

    # get html from stock
    html = driver.find_element(By.ID, 'main-2').get_attribute('innerHTML')

    # remove accents from html and transform html into soup
    soup = BeautifulSoup(unidecode(html), 'html.parser')

    return soup


def soup_to_dict(soup):
    '''Get all data from stock soup and return as a dictionary '''
    keys, values = [], []

    # get divs from stock
    soup1 = soup.find('div', class_='pb-3 pb-md-5')
    soup2 = soup.find('div', class_='card rounded text-main-green-dark')
    soup3 = soup.find('div', class_='indicator-today-container')
    soup4 = soup.find(
        'div', class_='top-info info-3 sm d-flex justify-between mb-3')
    soups = [soup1, soup2, soup3, soup4]

    for s in soups:
        # get only titles from a div and append to keys
        titles = s.find_all('h3', re.compile('title m-0[^"]*'))
        titles = [t.get_text() for t in titles]
        keys += titles

        # get only numbers from a div and append to values
        numbers = s.find_all('strong', re.compile('value[^"]*'))
        numbers = [n.get_text()for n in numbers]
        values += numbers

    # remove unused key and insert needed keys
    keys.remove('PART. IBOV')
    keys.insert(6, 'TAG ALONG')
    keys.insert(7, 'LIQUIDEZ MEDIA DIARIA')

    # clean keys list
    keys = [k.replace('\nhelp_outline', '').strip() for k in keys]
    keys = [k for k in keys if k != '']

    # clean values list
    values = [v.replace('\nhelp_outline', '').strip() for v in values]
    values = [v.replace('.', '').replace(',', '.') for v in values]

    # create a dictionary using keys and values from indicators
    d = {k: v for k, v in zip(keys, values)}

    return d


if __name__ == "__main__":
    dict_stocks = {}
    criaPlanilhaIndRentabilidade(wbsaida)
    wsIndiRentabilidade = wbsaida['IndiRentabilidade']

    # start timer
    start = time.time()

    # read file with stocks codes to get stock information
    with open('stocks.txt', 'r') as f:
        stocks = f.read().splitlines()

        # get stock information and create excel sheet
        for stock in stocks:
            #print("stock :"  ,stock)
            try:
                # get data and transform into dictionary
                soup = get_stock_soup(stock)
                dict_stock = soup_to_dict(soup)
                dict_stocks[stock] = dict_stock
                gravaIndiEficiênciaoStaus(wsIndiRentabilidade, dict_stocks, stock)
            except:
                # if we not get the information... just skip it
                print(f'Could not get {stock} information', "    ", metricasts)

    # create dataframe using dictionary of stocks informations
    df = pd.DataFrame(dict_stocks)

    # replace missing values with NaN to facilitate processing
    df = df.replace(['', '-', '--', '-%', '--%'], np.nan)

    # write dataframe into csv file
    df.to_excel('stocks_data.xlsx', index_label='indicadores')

    # exit the driver
    driver.quit()

    # end timer
    end = time.time()
    wbsaida.save("StatusInvest.xlsx")
    #print("teste")
    print(f'Brasilian stocks information got in {int(end-start)} s')
# silvio teste