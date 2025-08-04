import re

def extrair_funcoes(caminho_entrada, caminho_saida, nomes_funcoes):
    # Abre o arquivo de entrada
    with open(caminho_entrada, "r") as arquivo_entrada:
        conteudo = arquivo_entrada.read()

    # Expressão regular para encontrar definições de funções
    padrao_funcao = r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*$.*?$\s*:(?:\s*#.*)?\s*(?:(?:\"\"\".*?\"\"\"|'''.*?''')\s*)?(?:\s*#[^\n]*)*\s*(?:.*?\s*)*?(?=\n(?:[^\s#]|$))"

    # Encontra todas as funções no arquivo
    funcoes = re.finditer(padrao_funcao, conteudo, re.DOTALL)

    # Filtra as funções desejadas
    funcoes_desejadas = [match.group(0) for match in funcoes if match.group(1) in nomes_funcoes]

    # Escreve as funções no arquivo de saída
    with open(caminho_saida, "w") as arquivo_saida:
        for funcao in funcoes_desejadas:
            arquivo_saida.write(funcao + "\n\n")

# Uso do código
# Exemplo: deseja extrair as funções "funcao1" e "funcao2" do arquivo "entrada.py" e salvar no arquivo "saida.py"
caminho_entrada = "analisefundamentalista.py"
caminho_saida = "saida.py"
nomes_funcoes = ["evaluate_divida_liquida_patrimonio", "evaluate_vpa"]

extrair_funcoes(caminho_entrada, caminho_saida, nomes_funcoes)