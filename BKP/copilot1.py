from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Inicializa o navegador
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # modo invisível
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL alvo
url = "https://statusinvest.com.br/acoes/petr4"
driver.get(url)
time.sleep(5)  # Espera o carregamento da página

# Dicionário para armazenar os dados
dados = {}

# Lista de indicadores alvo (texto das seções)
indicadores = ['P/L', 'ROE', 'Div. Yield', 'Margem Líquida']

# Busca os valores dos indicadores
for indicador in indicadores:
    try:
        elemento = driver.find_element(By.XPATH, f"//h3[text()='{indicador}']/following-sibling::strong")
        valor = elemento.text.strip()
        dados[indicador] = valor
    except:
        dados[indicador] = 'Não encontrado'

driver.quit()

# Exibe os dados
df = pd.DataFrame([dados])
print(df)
