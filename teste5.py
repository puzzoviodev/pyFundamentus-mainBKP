import ast

def listar_funcoes(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        codigo = f.read()

    arvore = ast.parse(codigo)
    funcoes = [node.name for node in arvore.body if isinstance(node, ast.FunctionDef)]

    return funcoes

# Exemplo de uso
arquivo_python = 'analisefundamentalista.py'  # substitua pelo nome do seu arquivo
funcoes_encontradas = listar_funcoes(arquivo_python)

print("Funções encontradas:")
for func in funcoes_encontradas:
    print("-", func)
