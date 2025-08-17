"""
indicadores_scraper.py

Este módulo é compatível com os sites:
- StatusInvest
- Investidor10
- Fundamentus

Ele utiliza Selenium e BeautifulSoup para extrair indicadores financeiros de páginas web,
tratando diferentes estruturas HTML como:
- Blocos estruturados (ex: <div class="indicator">)
- Elementos irmãos (ex: <span> seguido de <div class="value">)
- Tabelas (ex: <td> com nome seguido de <td> com valor)

Funções principais:
- buscar_indicador(driver, nome_indicador): busca um indicador específico.
- extrair_todos_indicadores(driver): extrai todos os indicadores da página.
"""

import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configurações por site
SITE_CONFIG = {
    'statusinvest': {
        'item_class': 'indicator',  # Ajustado baseado na estrutura inferida; mude para 'item' se necessário
        'title_tags': ['h3', 'span'],
        'title_class': 'label',  # Pode ser None se não houver classe específica
        'value_tags': ['strong', 'span'],
        'value_class_pattern': r'value',
        'sibling_value_class_pattern': r'value',
        'table_class': None  # Se houver tabela específica
    },
    'investidor10': {
        'item_class': 'data',
        'title_tags': ['span'],
        'title_class': None,
        'value_tags': ['span', 'strong'],
        'value_class_pattern': r'value',
        'sibling_value_class_pattern': r'value',
        'table_class': None
    },
    'fundamentus': {
        'item_class': None,
        'title_tags': ['td'],
        'title_class': None,
        'value_tags': ['td'],
        'value_class_pattern': None,
        'sibling_value_class_pattern': None,
        'table_class': 'w728'  # Exemplo para tabelas
    }
}

# Aliases para indicadores comuns
INDICADOR_ALIASES = {
    'ROE': ['ROE', 'Retorno sobre o Patrimônio', 'Return on Equity'],
    'P/L': ['P/L', 'Preço/Lucro', 'P/E'],
    # Adicione mais aliases conforme necessário
}

# Função para limpar e validar valores
def limpar_valor(valor_str):
    if not valor_str or valor_str in ['N/A', '-', '']:
        return None
    # Remove % e troca , por . para números
    valor_str = valor_str.replace('%', '').replace(',', '.').strip()
    try:
        return float(valor_str)
    except ValueError:
        return valor_str  # Retorna string se não for número

# Função para buscar um indicador específico pelo nome
def buscar_indicador(driver, nome_indicador, site='statusinvest', id_container='main-2', verbose=True):
    config = SITE_CONFIG.get(site, SITE_CONFIG['statusinvest'])
    aliases = INDICADOR_ALIASES.get(nome_indicador, [nome_indicador])

    try:
        # Espera pelo container principal
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_container)))

        # Extrai HTML com fallbacks
        try:
            html = driver.find_element(By.ID, id_container).get_attribute('innerHTML')
            if verbose: print(f"[INFO] HTML extraído de #{id_container}")
        except:
            try:
                html = driver.find_element(By.CLASS_NAME, 'container').get_attribute('innerHTML')
                if verbose: print(f"[INFO] HTML extraído de .container")
            except:
                html = driver.page_source
                if verbose: print(f"[WARN] Usando page_source como última opção.")

        soup = BeautifulSoup(html, 'html.parser')

        for alias in aliases:
            pattern = re.compile(rf'\b{re.escape(alias)}\b', re.IGNORECASE)

            # 1. Busca em blocos estruturados
            if config['item_class']:
                items = soup.find_all('div', class_=config['item_class'])
                for item in items:
                    title_tag = item.find(config['title_tags'], string=pattern, class_=config['title_class'] if config['title_class'] else None)
                    if title_tag:
                        value_tag = item.find(config['value_tags'], class_=re.compile(config['value_class_pattern']))
                        if value_tag:
                            valor_str = value_tag.get_text().strip()
                            valor = limpar_valor(valor_str)
                            if verbose: print(f"[OK] '{alias}' encontrado em bloco estruturado: {valor}")
                            return valor

            # 2. Busca por elementos irmãos
            labels = soup.find_all('span', string=pattern)
            for label in labels:
                parent = label.find_parent('div')
                if parent:
                    value_div = parent.find_next_sibling('div', class_=re.compile(config['sibling_value_class_pattern']))
                    if value_div:
                        value_span = value_div.find(['span', 'strong'])
                        if value_span:
                            valor_str = value_span.get_text().strip()
                            valor = limpar_valor(valor_str)
                            if verbose: print(f"[OK] '{alias}' encontrado como irmão: {valor}")
                            return valor

            # 3. Busca em tabelas
            if config['table_class']:
                tables = soup.find_all('table', class_=config['table_class'])
                for table in tables:
                    tds = table.find_all('td', string=pattern)
                    for td in tds:
                        next_td = td.find_next_sibling('td')
                        if next_td:
                            valor_str = next_td.get_text().strip()
                            valor = limpar_valor(valor_str)
                            if verbose: print(f"[OK] '{alias}' encontrado em tabela: {valor}")
                            return valor
            else:
                tds = soup.find_all('td', string=pattern)
                for td in tds:
                    next_td = td.find_next_sibling('td')
                    if next_td:
                        valor_str = next_td.get_text().strip()
                        valor = limpar_valor(valor_str)
                        if verbose: print(f"[OK] '{alias}' encontrado em tabela: {valor}")
                        return valor

        if verbose: print(f"[NOT FOUND] Indicador '{nome_indicador}' não encontrado.")
        return None

    except Exception as e:
        if verbose: print(f"[ERROR] Erro ao buscar '{nome_indicador}': {e}")
        return None

# Função para extrair todos os indicadores da página como um dicionário
def extrair_todos_indicadores(driver, site='statusinvest', id_container='main-2', verbose=True):
    indicadores = {}
    config = SITE_CONFIG.get(site, SITE_CONFIG['statusinvest'])

    try:
        # Espera pelo container
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, id_container)))

        # Extrai HTML com fallbacks
        try:
            html = driver.find_element(By.ID, id_container).get_attribute('innerHTML')
            if verbose: print(f"[INFO] HTML extraído de #{id_container}")
        except:
            try:
                html = driver.find_element(By.CLASS_NAME, 'container').get_attribute('innerHTML')
                if verbose: print(f"[INFO] HTML extraído de .container")
            except:
                html = driver.page_source
                if verbose: print(f"[WARN] Usando page_source como última opção.")

        soup = BeautifulSoup(html, 'html.parser')

        # 1. Blocos estruturados
        if config['item_class']:
            items = soup.find_all('div', class_=config['item_class'])
            for item in items:
                title_tag = item.find(config['title_tags'], class_=config['title_class'] if config['title_class'] else None)
                value_tag = item.find(config['value_tags'], class_=re.compile(config['value_class_pattern']))
                if title_tag and value_tag:
                    nome = title_tag.get_text().strip()
                    valor_str = value_tag.get_text().strip()
                    valor = limpar_valor(valor_str)
                    if nome not in indicadores:
                        indicadores[nome] = valor
                        if verbose: print(f"[OK] Indicador encontrado: {nome} = {valor}")

        # 2. Elementos irmãos
        labels = soup.find_all('span', string=True)
        for label in labels:
            texto = label.get_text().strip()
            if texto and texto not in indicadores:
                parent = label.find_parent('div')
                if parent:
                    value_div = parent.find_next_sibling('div', class_=re.compile(config['sibling_value_class_pattern']))
                    if value_div:
                        value_span = value_div.find(['span', 'strong'])
                        if value_span:
                            valor_str = value_span.get_text().strip()
                            valor = limpar_valor(valor_str)
                            indicadores[texto] = valor
                            if verbose: print(f"[OK] Indicador irmão: {texto} = {valor}")

        # 3. Tabelas
        if config['table_class']:
            tables = soup.find_all('table', class_=config['table_class'])
            for table in tables:
                tds = table.find_all('td', string=True)
                for td in tds:
                    texto = td.get_text().strip()
                    next_td = td.find_next_sibling('td')
                    if texto and next_td and texto not in indicadores:
                        valor_str = next_td.get_text().strip()
                        valor = limpar_valor(valor_str)
                        indicadores[texto] = valor
                        if verbose: print(f"[OK] Indicador em tabela: {texto} = {valor}")
        else:
            tds = soup.find_all('td', string=True)
            for td in tds:
                texto = td.get_text().strip()
                next_td = td.find_next_sibling('td')
                if texto and next_td and texto not in indicadores:
                    valor_str = next_td.get_text().strip()
                    valor = limpar_valor(valor_str)
                    indicadores[texto] = valor
                    if verbose: print(f"[OK] Indicador em tabela: {texto} = {valor}")

        return indicadores

    except Exception as e:
        if verbose: print(f"[ERROR] Erro ao extrair indicadores: {e}")
        return indicadores

# =========================
# EXEMPLO DE USO
# =========================
if __name__ == "__main__":
    options = Options()
    options.add_argument('--headless')
    with webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) as driver:
        # Acessa a página desejada
        driver.get("https://statusinvest.com.br/acoes/ITSA4")

        # Busca um indicador específico
        roe = buscar_indicador(driver, 'ROE', site='statusinvest')
        print("ROE:", roe)

        # Extrai todos os indicadores da página
        todos = extrair_todos_indicadores(driver, site='statusinvest')
        for nome, valor in todos.items():
            print(f"{nome}: {valor}")