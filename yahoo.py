import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import yfinance as yf
from datetime import datetime
import time


def fetch_status_invest_fundamentals(ticker):
    """Obtém indicadores fundamentalistas do Status Invest via Selenium."""
    url = f"https://statusinvest.com.br/acoes/{ticker.lower()}"
    fundamentals = {}

    # Configurar Selenium para renderizar JavaScript
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executar sem abrir o navegador
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)
        time.sleep(3)  # Aguardar o carregamento do JavaScript

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Preço atual
        price_element = soup.find("div", {"class": "top-info"})
        if price_element:
            price = price_element.find("strong", {"class": "value"}).text.strip().replace(",", ".")
            fundamentals['Preço Atual (R$)'] = float(price) if price.replace(".", "").isdigit() else 'N/A'

        # Indicadores fundamentalistas
        indicators = soup.find_all("div", {"class": "indicator-item"})
        for indicator in indicators:
            title_elem = indicator.find("h3", {"class": "title"})
            value_elem = indicator.find("strong", {"class": "value"})
            if title_elem and value_elem:
                title = title_elem.text.strip()
                value = value_elem.text.strip().replace(",", ".")
                try:
                    fundamentals[title] = float(value)
                except ValueError:
                    fundamentals[title] = value  # Para valores não numéricos (ex.: "-")

        return fundamentals

    except Exception as e:
        print(f"Erro ao obter dados do Status Invest para {ticker} com Selenium: {e}")
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
        fundamentals['P/L'] = info.get('trailingPE', 'N/A')
        fundamentals['P/VP'] = info.get('priceToBook', 'N/A')
        fundamentals['Dividend Yield (%)'] = info.get('dividendYield', 0) * 100 if info.get('dividendYield') else 'N/A'
        fundamentals['ROE (%)'] = info.get('returnOnEquity', 'N/A') * 100 if info.get('returnOnEquity') else 'N/A'
        fundamentals['Margem Líquida (%)'] = info.get('profitMargins', 'N/A') * 100 if info.get(
            'profitMargins') else 'N/A'
        fundamentals['Dívida Líquida / EBITDA'] = info.get('debtToEquity', 'N/A')
    except Exception as e:
        print(f"Erro ao obter dados do yfinance para {yf_ticker}: {e}")
    return fundamentals


def interpret_fundamentals(fundamentals):
    """Fornece interpretações dos indicadores fundamentalistas."""
    interpretations = []
    if 'Preço / Lucro' in fundamentals and isinstance(fundamentals['Preço / Lucro'], float):
        pl = fundamentals['Preço / Lucro']
        if pl < 10:
            interpretations.append("P/L baixo (<10): A ação pode estar subvalorizada, mas verifique o setor.")
        elif pl > 20:
            interpretations.append(
                "P/L alto (>20): A ação pode estar sobrevalorizada ou com expectativas de crescimento.")
        else:
            interpretations.append("P/L moderado (10-20): Avalie o contexto do setor.")

    if 'Preço / V. Patrimonial' in fundamentals and isinstance(fundamentals['Preço / V. Patrimonial'], float):
        pvp = fundamentals['Preço / V. Patrimonial']
        if pvp < 1:
            interpretations.append("P/VP < 1: A ação pode estar subvalorizada em relação ao patrimônio.")
        elif pvp > 2:
            interpretations.append("P/VP > 2: A ação pode estar cara em relação ao patrimônio.")

    if 'Dividend Yield' in fundamentals and isinstance(fundamentals['Dividend Yield'], float):
        dy = fundamentals['Dividend Yield']
        if dy > 5:
            interpretations.append("Dividend Yield alto (>5%): Atraente para investidores focados em dividendos.")
        elif dy < 2:
            interpretations.append("Dividend Yield baixo (<2%): Menor atratividade para dividendos.")

    if 'ROE' in fundamentals and isinstance(fundamentals['ROE'], float):
        roe = fundamentals['ROE']
        if roe > 15:
            interpretations.append("ROE alto (>15%): Empresa eficiente na geração de lucro com patrimônio.")
        elif roe < 5:
            interpretations.append("ROE baixo (<5%): Eficiência questionável na geração de lucro.")

    if 'Dív. Líquida / EBITDA' in fundamentals and isinstance(fundamentals['Dív. Líquida / EBITDA'], float):
        debt_ebitda = fundamentals['Dív. Líquida / EBITDA']
        if debt_ebitda > 3:
            interpretations.append("Dívida Líquida/EBITDA alto (>3): Risco elevado de endividamento.")
        elif debt_ebitda < 1:
            interpretations.append("Dívida Líquida/EBITDA baixo (<1): Baixo risco de endividamento.")

    return interpretations


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


if __name__ == "__main__":
    main()