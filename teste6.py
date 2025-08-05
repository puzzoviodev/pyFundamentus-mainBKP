import ast
import os
import pandas as pd

def extrair_metadados_funcoes(arquivo_origem, nomes_funcoes):
    with open(arquivo_origem, 'r', encoding='utf-8') as f:
        codigo = f.read()

    arvore = ast.parse(codigo)
    funcoes_metadados = []

    for node in arvore.body:
        if isinstance(node, ast.FunctionDef) and node.name in nomes_funcoes:
            nome = node.name
            docstring = ast.get_docstring(node) or "Sem definição"

            # Inicializa valores
            definicao = agrupador = formula = classificacao = faixa = descricao = "N/A"

            # Mapeia variáveis atribuídas no início da função
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
                                pass  # ignora valores não literais

            definicao = variaveis.get('definicao', definicao)
            agrupador = variaveis.get('agrupador', agrupador)
            formula = variaveis.get('formula', formula)

            # Procura retornos com dicionário
            for stmt in node.body:
                if isinstance(stmt, ast.Try):
                    for substmt in stmt.body:
                        if isinstance(substmt, ast.If):
                            for retorno in substmt.body:
                                if isinstance(retorno, ast.Return) and isinstance(retorno.value, ast.Dict):
                                    for k, v in zip(retorno.value.keys, retorno.value.values):
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

            funcoes_metadados.append({
                'nome_funcao': nome,
                'definicao': definicao,
                'formula': formula,
                'classificacao': classificacao,
                'faixa': faixa,
                'descricao': descricao,
                'agrupador': agrupador
            })

    return funcoes_metadados

def salvar_em_excel(dados, caminho_saida):
    df = pd.DataFrame(dados)
    df.to_excel(caminho_saida, index=False)
    print(f"✅ Arquivo Excel gerado em: {caminho_saida}")

# 🔧 Configurações
#arquivo_origem = 'D:/Financeiro/GIT2/Robov1/funcoes.py'  # Altere para o caminho correto
#nomes_funcoes = ['funcao1', 'funcao2', 'funcao3']         # Altere para os nomes reais
#caminho_saida = 'D:/Financeiro/GIT2/Robov1/metadados_funcoes.xlsx'


arquivo_origem = 'analisefundamentalista.py'  # Altere para o caminho correto
nomes_funcoes = ['evaluate_p_l', 'evaluate_p_ebitda', 'evaluate_p_vp', 'evaluate_pebit',
    'evaluate_evebitda', 'evaluate_ev_ebit', 'evaluate_giro_ativos',
    'evaluate_divida_liquida_patrimonio', 'evaluate_divida_liquida_ebitda',
    'evaluate_pl_ativos', 'evaluate_passivos_ativos', 'evaluate_liquidez_corrente',
    'evaluate_p_ativo', 'evaluate_vpa', 'evaluate_lpa', 'evaluate_psr',
    'evaluate_p_ativo_circ_liq', 'evaluate_disponibilidade',
    'evaluate_patrimonio_liquido', 'evaluate_divida_bruta', 'evaluate_divida_liquida',
    'evaluate_ativos', 'evaluate_ativo_circulante', 'evaluate_liquidez_media_diaria',
    'evaluate_peg_ratio']         # Altere para os nomes reais
caminho_saida = 'metadados_funcoes.xlsx'

# 🚀 Execução
metadados = extrair_metadados_funcoes(arquivo_origem, nomes_funcoes)
salvar_em_excel(metadados, caminho_saida)
