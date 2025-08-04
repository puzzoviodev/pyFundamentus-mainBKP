import ast
import openpyxl

def extrair_metadados_funcoes(arquivo_origem, nomes_funcoes):
    with open(arquivo_origem, 'r', encoding='utf-8') as f:
        codigo = f.read()

    arvore = ast.parse(codigo)
    funcoes_metadados = []

    for node in arvore.body:
        if isinstance(node, ast.FunctionDef) and node.name in nomes_funcoes:
            nome = node.name
            docstring = ast.get_docstring(node)
            definicao = docstring if docstring else "Sem definição"
            # Os campos abaixo são fictícios e podem ser ajustados conforme necessário
            formula = "N/A"
            classificacao = "N/A"
            faixa = "N/A"
            descricao = definicao
            funcoes_metadados.append([nome, definicao, formula, classificacao, faixa, descricao])

    return funcoes_metadados

def salvar_em_excel(dados, arquivo_excel):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Funções Extraídas"

    # Cabeçalhos
    cabecalhos = ["Nome da função", "Definição", "Fórmula", "Classificação", "Faixa", "Descrição"]
    ws.append(cabecalhos)

    # Dados
    for linha in dados:
        ws.append(linha)

    wb.save(arquivo_excel)
    print(f"Planilha '{arquivo_excel}' criada com {len(dados)} função(ões).")

# Lista de funções desejadas
nomes_funcoes = [
    'evaluate_p_l', 'evaluate_p_ebitda', 'evaluate_p_vp', 'evaluate_pebit',
    'evaluate_evebitda', 'evaluate_ev_ebit', 'evaluate_giro_ativos',
    'evaluate_divida_liquida_patrimonio', 'evaluate_divida_liquida_ebitda',
    'evaluate_pl_ativos', 'evaluate_passivos_ativos', 'evaluate_liquidez_corrente',
    'evaluate_p_ativo', 'evaluate_vpa', 'evaluate_lpa', 'evaluate_psr',
    'evaluate_p_ativo_circ_liq', 'evaluate_disponibilidade',
    'evaluate_patrimonio_liquido', 'evaluate_divida_bruta', 'evaluate_divida_liquida',
    'evaluate_ativos', 'evaluate_ativo_circulante', 'evaluate_liquidez_media_diaria',
    'evaluate_peg_ratio'
]

# Caminhos dos arquivos
arquivo_origem = 'analisefundamentalista.py'
arquivo_excel = 'funcoes.xlsx'

# Executa extração e gravação
metadados = extrair_metadados_funcoes(arquivo_origem, nomes_funcoes)
salvar_em_excel(metadados, arquivo_excel)
