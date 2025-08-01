def evaluate_pl(PL):
    if PL <= 0:
        return 'critico'
    elif 20 <= PL <= 30:
        return 'pessimo'
    elif 15 <= PL <= 20:
        return 'ruim'
    elif 10 <= PL <= 15:
        return 'moderado'
    elif 0 <= PL <= 10:
        return 'Otimo'
    else:  # value > 25
        return 'fora da faixa'

# 🔍 Testando a função com vários valores
valores_de_teste = [-5, 0, 5, 7.79
, 14.9, 15, 19.9, 20, 25, 30, 31]

for valor in valores_de_teste:
    resultado = evaluate_pl(valor)
    print(f"PL = {valor:>5} → {resultado}")
