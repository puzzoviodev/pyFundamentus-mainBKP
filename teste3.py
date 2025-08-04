import ast

def extrair_funcoes(arquivo_origem, nomes_funcoes, arquivo_destino):
    with open(arquivo_origem, 'r', encoding='utf-8') as f:
        codigo = f.read()

    arvore = ast.parse(codigo)
    funcoes_extraidas = []

    for node in arvore.body:
        if isinstance(node, ast.FunctionDef) and node.name in nomes_funcoes:
            inicio = node.lineno - 1
            fim = max(getattr(node, 'end_lineno', inicio + 1), inicio + 1)
            linhas = codigo.splitlines()[inicio:fim]
            funcoes_extraidas.append('\n'.join(linhas))

    if funcoes_extraidas:
        with open(arquivo_destino, 'w', encoding='utf-8') as f_out:
            f_out.write("# Funções extraídas\n\n")
            f_out.write('\n\n'.join(funcoes_extraidas))
        print(f"Arquivo '{arquivo_destino}' criado com {len(funcoes_extraidas)} função(ões).")
    else:
        print("Nenhuma função encontrada com os nomes fornecidos.")

# Lista de funções desejadas
nomes = [
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

# Executa a extração
extrair_funcoes('analisefundamentalista.py', nomes, 'indicadores_selecionados.py')
