#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: run.py
#  Version: 0.0.1
#
#  Summary: Python Fundamentus
#           Python Fundamentus is a Python API that allows you to quickly
#           access the main fundamental indicators of the main stocks
#           in the Brazilian market.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
# ------------------------------------------------------------------------------

"""
Python Fundamentus API: Instant access to key financial indicators of
Brazilian stocks, empowering investors with comprehensive market analysis.
"""

import fundamentus

# statusinvest

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

TITLES = [
    'Identificação', 'Resumo Financeiro', 'Cotações', 'Informações Básicas',
    'Oscilações', 'Indicadores de Valuation', 'Indicadores de Rentabilidade',
    'Indicadores de Endividamento', 'Balanço Patrimonial', 'Demonstrativo de Resultados'
]

wbsaida = openpyxl.Workbook()

def criaPlanilhaIndiEficiência(IndiEficiência):
    try:
       wbsaida.create_sheet('IndiEficiência')
       IndiEficiência = wbsaida['IndiEficiência']
       IndiEficiência.append(['Fonte','ATIVO','M. Bruta', 'M. EBITDA', 'M. EBIT', 'M. Líquida'])
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        print("criaPlanilhaIndiEficiência")
    return



def teste(dict_stocks,stock):

    print(dict_stocks[stock].get("M. Bruta"))
    print(dict_stocks[stock].get("M. EBITDA"))
    print(dict_stocks[stock].get("M. EBIT"))
    print(dict_stocks[stock].get("M. Liquida"))

#Incio funcionalidades statusinvest

# define selenium webdriver options
options = webdriver.ChromeOptions()

# create selenium webdriver instancee
driver = webdriver.Chrome(options=options)

def get_stock_soup(stock):
    ''' Get raw html from a stock '''

    # access the stock url
    driver.get(f'https://statusinvest.com.br/acoes/{stock}')
    #driver.get(f'https://statusinvest.com.br/acoes/eua/{stock}')

    # get html from stock
    html = driver.find_element(By.ID, 'main-2').get_attribute('innerHTML')

    # remove accents from html and transform html into soup
    soup = BeautifulSoup(unidecode(html), 'html.parser')

    return soup

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

#Fim funcionalidades statusinvest

# pylint: disable=line-too-long
if __name__ == '__main__':
    dict_stocks = {} # dicionario statusinvest

    criaPlanilhaIndiEficiência(wbsaida) # statusinvest + fundamentus
    start = time.time()
    with open('stocks.txt', 'r') as f:
        stocks = f.read().splitlines()
        for stock in stocks:

            main_pipeline = fundamentus.Pipeline(stock.upper())
            response = main_pipeline.get_all_information()

            # Incio statusinvest
            # get data and transform into dictionary
            soup = get_stock_soup(stock)
            dict_stock = soup_to_dict(soup)
            dict_stocks[stock] = dict_stock
            # Fim Statausinvest

            # Extract the information from the response.
            stock_identification = response.transformed_information['stock_identification']
            financial_summary = response.transformed_information['financial_summary']
            price_information = response.transformed_information['price_information']
            detailed_information = response.transformed_information[
                'detailed_information']
            oscillations = response.transformed_information['oscillations']
            valuation_indicators = response.transformed_information[
                'valuation_indicators']
            profitability_indicators = response.transformed_information[
                'profitability_indicators']
            indebtedness_indicators = response.transformed_information[
                'indebtedness_indicators']
            balance_sheet = response.transformed_information['balance_sheet']
            income_statement = response.transformed_information['income_statement']


            print(TITLES[0])
            print('-' * len(TITLES[0]))
            for information in stock_identification:
                print(
                    f'{stock_identification[information].title}: {stock_identification[information].value}'
                )

            print(f'\n{TITLES[1]}')
            print('-' * len(TITLES[1]))
            for information in financial_summary:
                print(
                    f'{financial_summary[information].title}: {financial_summary[information].value}'
                )

            print(f'\n{TITLES[2]}')
            print('-' * len(TITLES[2]))
            for information in price_information:
                print(
                    f'{price_information[information].title}: {price_information[information].value}'
                )

            print(f'\n{TITLES[3]}')
            print('-' * len(TITLES[2]))
            for information in detailed_information:
                if information != 'variation_52_weeks':
                    print(
                        f'{detailed_information[information].title}: {detailed_information[information].value}'
                    )
                else:
                    for sub_information in detailed_information[information]:
                        print(
                            f'{detailed_information[information][sub_information].title}: {detailed_information[information][sub_information].value}'
                        )

            print(f'\n{TITLES[4]}')
            print('-' * len(TITLES[4]))
            for information in oscillations:
                print(
                    f'{oscillations[information].title}: {oscillations[information].value}'
                )

            print(f'\n{TITLES[5]}')
            print('-' * len(TITLES[5]))
            for information in valuation_indicators:
                print(
                    f'{valuation_indicators[information].title}: {valuation_indicators[information].value}'
                )

            print(f'\n{TITLES[6]}')
            print('-' * len(TITLES[6]))
            for information in profitability_indicators:
                print(
                    f'{profitability_indicators[information].title}: {profitability_indicators[information].value}'
                )

            print(f'\n{TITLES[7]}')
            print('-' * len(TITLES[7]))
            for information in indebtedness_indicators:
                print(
                    f'{indebtedness_indicators[information].title}: {indebtedness_indicators[information].value}'
                )

            print(f'\n{TITLES[8]}')
            print('-' * len(TITLES[8]))
            for information in balance_sheet:
                print(
                    f'{balance_sheet[information].title}: {balance_sheet[information].value}'
                )

            print(f'\n{TITLES[9]}')
            print('-' * len(TITLES[9]))
            print('Últimos 03 meses')
            for information in income_statement['three_months']:
                print(
                    f"\t{income_statement['three_months'][information].title}: {income_statement['three_months'][information].value}"
                )
            print('Últimos 12 meses')
            for information in income_statement['twelve_months']:
                print(
                    f"\t{income_statement['twelve_months'][information].title}: {income_statement['twelve_months'][information].value}"
                )


    teste(dict_stocks,stock)
    # exit the driver
    driver.quit()

    # end timer
    end = time.time()
    wbsaida.save("StatusInvest.xlsx") # silvio