import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import yfinance as yf
from datetime import datetime
import time
import csv
import os


def fetch_status_invest_fundamentals(ticker):
    """Obtém indicadores fundamentalistas do Status Invest via Selenium."""
    url = f"https://statusinvest.com.br/acoes/{ticker.lower()}"
    fundamentals = {}

    # Configurar Selenium para renderizar JavaScript
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executar sem abrir o navegador
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"Erro ao iniciar o ChromeDriver: {e}. Certifique-se de que o ChromeDriver está instalado e no PATH.")
        return None

    try:
        driver.get(url)
        time.sleep(5)  # Aguardar o carregamento completo do JavaScript

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Preço atual
        price_element = soup.find("div", {"class": "top-info"})
        if price_element:
            price = price_element.find("strong", {"class": "value"}).text.strip().replace(",", ".")
            fundamentals['Preço Atual (R$)'] = float(price) if price.replace(".", "").replace("-",
                                                                                              "").isdigit() else 'N/A'

        # Indicadores fundamentalistas (seção de valuation)
        indicator_sections = soup.find_all("div", {"class": "card bg-main-gd-h white-text rounded ov-hidden mb-2"})
        for section in indicator_sections:
            indicators = section.find_all("div", {"class": "indicator-item"})
            for indicator in indicators:
                title_elem = indicator.find("h3", {"class": "title"})
                value_elem = indicator.find("strong", {"class": "value"})
                if title_elem and value_elem:
                    title = title_elem.text.strip()
                    value = value_elem.text.strip().replace(",", ".").replace("%", "")
                    try:
                        fundamentals[title] = float(value)
                    except ValueError:
                        fundamentals[title] = value  # Para valores não numéricos (ex.: "-")

        return fundamentals

    except Exception as e:
        print(f"Erro ao obter dados do Status Invest para {ticker}: {e}")
        return None
    finally:
        driver.quit()


def fetch_yfinance_fundamentals(ticker):
    """Obtém indicadores fundamentalistas limitados do yfinance como fallback."""
    yf_ticker = ticker + ".SA" if not ticker.endswith(".SA") else ticker
    stock = yf.Ticker(yf_ticker)
    info = stock.info
    fundamentals = {}
    try:
        fundamentals['Preço Atual (R$)'] = info.get('currentPrice', 'N/A')
        fundamentals['Preço / Lucro'] = info.get('trailingPE', 'N/A')
        fundamentals['Preço / V. Patrimonial'] = info.get('priceToBook', 'N/A')
        fundamentals['Dividend Yield'] = info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 'N/A'
        fundamentals['ROE'] = info.get('returnOnEquity', 'N/A') * 100 if info.get('returnOnEquity') else 'N/A'
        fundamentals['Margem Líquida'] = info.get('profitMargins', 'N/A') * 100 if info.get('profitMargins') else 'N/A'
        fundamentals['Dív. Líquida / EBITDA'] = info.get('debtToEquity', 'N/A')
    except Exception as e:
        print(f"Erro ao obter dados do yfinance para {yf_ticker}: {e}")
    return fundamentals
def interpretar_roe(x):
    if x > 15:
        return "ROE alto (>15%): Empresa eficiente na geração de lucros com patrimônio."
    elif x < 5:
        return "ROE baixo (<5%): Baixa eficiência, avalie as causas."
    else:
        return "ROE moderado (5-15%): Performance típica, compare com o setor."


def interpret_fundamentals(fundamentals):
    """Fornece interpretações dos indicadores fundamentalistas."""
    interpretations = []
    key_indicators = {
        'Preço / Lucro': lambda x: (
            "P/L baixo (<10): Ação pode estar subvalorizada, mas verifique o setor." if x < 10 else
            "P/L alto (>20): Ação pode estar sobrevalorizada ou com expectativas de crescimento." if x > 20 else
            "P/L moderado (10-20): Avalie o contexto do setor."
        ),
        'Preço / V. Patrimonial': lambda x: (
            "P/VP < 1: Ação pode estar subvalorizada em relação ao patrimônio." if x < 1 else
            "P/VP > 2: Ação pode estar cara em relação ao patrimônio." if x > 2 else
            "P/VP moderado (1-2): Avalie o contexto do setor."
        ),
        'Dividend Yield': lambda x: (
            "Dividend Yield alto (>5%): Atraente para investidores focados em dividendos." if x > 5 else
            "Dividend Yield baixo (<2%): Menor atratividade para dividendos." if x < 2 else
            "Dividend Yield moderado (2-5%): Razoável, dependendo do objetivo."
        ),
        'ROE': lambda x: (
            "ROE alto (>15%): Empresa eficiente na geração de lucro com patrimônio." if x > 15 else
            "ROE baixo (<5%): Eficiência questionável na geração de lucro." if x < 5 else
            "ROE moderado (5-15%): Avalie o setor."
        ),
        'Dív. Líquida / EBITDA': lambda x: (
            "Dívida Líquida/EBITDA alto (>3): Risco elevado de endividamento." if x > 3 else
            "Dívida Líquida/EBITDA baixo (<1): Baixo risco de endividamento." if x < 1 else
            "Dívida Líquida/EBITDA moderado (1-3): Risco aceitável, avalie o setor."
        )
    }

    for key, interpreter in key_indicators.items():
        if key in fundamentals and isinstance(fundamentals[key], float):
            interpretations.append(interpreter(fundamentals[key]))

    return interpretations


def save_to_csv(ticker, fundamentals):
    """Salva os indicadores em um arquivo CSV."""
    filename = f"{ticker}_fundamentalist_analysis_{datetime.now().strftime('%Y%m%d')}.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Indicador', 'Valor'])
        for key, value in fundamentals.items():
            writer.writerow([key, value])
    print(f"\nDados salvos em {filename}")


def main():
    ticker = input("Digite o símbolo da ação (exemplo: PETR4 para Petrobras): ").upper()

    # Tentar obter dados do Status Invest
    print(f"\nTentando coletar dados do Status Invest para {ticker}...")
    fundamentals = fetch_status_invest_fundamentals(ticker)

    # Fallback para yfinance se o Status Invest falhar
    if not fundamentals:
        print("Falha ao obter dados do Status Invest. Tentando yfinance...")
        fundamentals = fetch_yfinance_fundamentals(ticker)
        if not fundamentals:
            print("Não foi possível obter dados fundamentalistas. Verifique o símbolo ou a conexão.")
            return

    # Exibir resumo
    print(f"\nResumo Fundamentalista para {ticker} ({datetime.now().strftime('%Y-%m-%d')}):")
    for key, value in fundamentals.items():
        if isinstance(value, float):
            print(f"{key}: {value:.2f}")
        else:
            print(f"{key}: {value}")

    # Interpretações
    interpretations = interpret_fundamentals(fundamentals)
    if interpretations:
        print("\nInterpretações:")
        for interp in interpretations:
            print(f"- {interp}")
    else:
        print("\nNão foi possível gerar interpretações devido a dados insuficientes.")

    # Salvar em CSV
    save_to_csv(ticker, fundamentals)


if __name__ == "__main__":
    main()