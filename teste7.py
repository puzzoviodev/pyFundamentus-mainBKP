import ast
import pandas as pd

def extrair_retornos_recursivamente(nos, variaveis):
    retornos = []
    for no in nos:
        if isinstance(no, ast.If):
            retornos += extrair_retornos_recursivamente(no.body, variaveis)
            if no.orelse:
                retornos += extrair_retornos_recursivamente(no.orelse, variaveis)
        elif isinstance(no, ast.Return) and isinstance(no.value, ast.Dict):
            classificacao = faixa = descricao = "N/A"
            for k, v in zip(no.value.keys, no.value.values):
                try:
                    chave = ast.literal_eval(k)
                    if isinstance(v, ast.Constant):
                        valor = v.value
                    elif isinstance(v, ast.Name):
                        valor = variaveis.get(v.id, "N/A")
                    else:
                        valor = "N/A"
                    if chave == 'classificacao':
                        classificacao = valor.strip()
                    elif chave == 'faixa':
                        faixa = valor.strip()
                    elif chave == 'descricao':
                        descricao = valor.strip()
                except Exception:
                    pass
            retornos.append({
                'classificacao': classificacao,
                'faixa': faixa,
                'descricao': descricao
            })
        elif hasattr(no, 'body'):
            retornos += extrair_retornos_recursivamente(no.body, variaveis)
    return retornos

def extrair_metadados_funcoes(arquivo_origem, nomes_funcoes):
    with open(arquivo_origem, 'r', encoding='utf-8') as f:
        codigo = f.read()

    arvore = ast.parse(codigo)
    todas_linhas = []

    for node in arvore.body:
        if isinstance(node, ast.FunctionDef) and node.name in nomes_funcoes:
            nome = node.name
            docstring = ast.get_docstring(node) or "Sem definição"

            variaveis = {}
            for stmt in node.body:
                if isinstance(stmt, ast.Assign):
                    for target in stmt.targets:
                        if isinstance(target, ast.Name):
                            var_name = target.id
                            try:
                                valor = ast.literal_eval(stmt.value)
                                variaveis[var_name] = valor.strip() if isinstance(valor, str) else str(valor)
                            except Exception:
                                pass

            definicao = variaveis.get('definicao', "N/A")
            agrupador = variaveis.get('agrupador', "N/A")
            formula = variaveis.get('formula', "N/A")

            for stmt in node.body:
                if isinstance(stmt, ast.Try):
                    retornos = extrair_retornos_recursivamente(stmt.body, variaveis)
                    for r in retornos:
                        todas_linhas.append({
                            'nome_funcao': nome,
                            'definicao': definicao,
                            'formula': formula,
                            'classificacao': r['classificacao'],
                            'faixa': r['faixa'],
                            'descricao': r['descricao'],
                            'agrupador': agrupador
                        })

    return todas_linhas

def salvar_em_excel(dados, caminho_saida):
    df = pd.DataFrame(dados)
    df.to_excel(caminho_saida, index=False)
    print(f"✅ Arquivo Excel gerado em: {caminho_saida}")

# 🔧 Configurações
arquivo_origem = 'analisefundamentalista.py'  # Altere para o caminho correto
nomes_funcoes = ['evaluate_divida_liquida_ebitda',
'evaluate_margem_ebitda',
'evaluate_roa',
'evaluate_dividend_payout',
'evaluate_free_cash_flow_yield',
'evaluate_crescimento_lucro',
'evaluate_debt_equity',
'evaluate_margem_liquida_crescimento',
'evaluate_roe',
'evaluate_p_l',
'evaluate_liquidez_corrente',
'evaluate_cobertura_juros',
'evaluate_margem_bruta',
'evaluate_giro_ativos',
'evaluate_divida_ebit',
'evaluate_dividend_yield',
'evaluate_p_vp',
'evaluate_roic',
'evaluate_divida_liquida_patrimonio',
'evaluate_crescimento_ebitda',
'evaluate_margem_ebitda',
'evaluate_p_ebitda',
'evaluate_liquidez_imediata',
'evaluate_crescimento_receita',
'evaluate_margem_operacional',
'evaluate_divida_ativo',
'evaluate_ev_ebit',
'evaluate_payout_ratio',
'evaluate_roa',
'evaluate_capex_receita',
'evaluate_divida_bruta_ebitda',
'evaluate_crescimento_margem_lucro_bruto',
'evaluate_dividend_yield',
'evaluate_free_cash_flow_yield',
'evaluate_giro_ativos',
'evaluate_crescimento_lucro_liquido',
'evaluate_pebit',
'evaluate_evebitda',
'evaluate_pl_ativos',
'evaluate_peg_ratio',
'evaluate_p_ativo',
'evaluate_vpa',
'evaluate_lpa',
'evaluate_passivos_ativos',
'evaluate_psr',
'evaluate_p_ativo_circ_liq',
'evaluate_disponibilidade',
'evaluate_pl',
'evaluate_patrimonio_liquido',
'evaluate_divida_bruta',
'evaluate_divida_liquida',
'evaluate_ativos',
'evaluate_liquidez_media_diaria',
'evaluate_ativo_circulante'
]         # Altere para os nomes reais
caminho_saida = 'metadados_funcoes3.xlsx'

# 🚀 Execução
metadados = extrair_metadados_funcoes(arquivo_origem, nomes_funcoes)
salvar_em_excel(metadados, caminho_saida)
