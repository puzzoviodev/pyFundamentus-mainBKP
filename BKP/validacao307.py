
def evaluate_div_liquida_ebit(value, ebit):
    if ebit <= 0:  # EBIT negativo ou zero indica problemas operacionais
        return 'critico'
    if value < 0:  # Dívida líquida negativa (excesso de caixa)
        return 'otimo'
    elif value == 0:
        return 'bom'
    elif value <= 1.5:
        return 'bom'
    elif value <= 3:
        return 'moderado'
    elif value <= 4:
        return 'ruim'
    else:
        return 'pessimo'

def evaluate_div_liquida_ebitda(value, ebitda):
    if ebitda <= 0:  # EBITDA negativo ou zero indica problemas operacionais
        return 'critico'
    if value < 0:  # Dívida líquida negativa (excesso de caixa)
        return 'otimo'
    elif value == 0:
        return 'bom'
    elif value <= 1:
        return 'bom'
    elif value <= 2.5:
        return 'moderado'
    elif value <= 3.5:
        return 'ruim'
    else:
        return 'pessimo'

def evaluate_div_liquida_pl(value, pl):
    if pl <= 0:  # Patrimônio Líquido negativo indica insolvência
        return 'critico'
    if value < 0:  # Dívida líquida negativa é favorável
        return 'otimo'
    elif value <= 0.3:
        return 'bom'
    elif value <= 0.7:
        return 'moderado'
    elif value <= 1:
        return 'ruim'
    else:
        return 'pessimo'

def evaluate_dy(value):
    if value == 0:
        return 'critico'
    elif value <= 0.02:
        return 'ruim'
    elif value <= 0.04:
        return 'moderado'
    elif value <= 0.06:
        return 'bom'
    else:
        return 'otimo'

def evaluate_ev_ebit(value, ebit):
    if ebit <= 0:  # EBIT negativo ou zero indica problemas operacionais
        return 'critico'
    if value < 0:  # EV/EBIT negativo é favorável
        return 'otimo'
    elif value <= 4:
        return 'otimo'
    elif value <= 8:
        return 'bom'
    elif value <= 12:
        return 'moderado'
    elif value <= 15:
        return 'ruim'
    else:
        return 'pessimo'

def evaluate_ev_ebitda(value, ebitda):
    if ebitda <= 0:  # EBITDA negativo ou zero indica problemas operacionais
        return 'critico'
    if value < 0:  # EV/EBITDA negativo é favorável
        return 'otimo'
    elif value <= 3:
        return 'otimo'
    elif value <= 6:
        return 'bom'
    elif value <= 10:
        return 'moderado'
    elif value <= 12:
        return 'ruim'
    else:
        return 'pessimo'

def evaluate_giro_ativo(value):
    if value <= 0:
        return 'critico'
    elif value <= 0.2:
        return 'pessimo'
    elif value <= 0.4:
        return 'ruim'
    elif value <= 0.8:
        return 'moderado'
    elif value <= 1.2:
        return 'bom'
    else:
        return 'otimo'

def evaluate_liq_corrente(value):
    if value <= 0:
        return 'critico'
    elif value <= 0.8:
        return 'pessimo'
    elif value <= 1.2:
        return 'ruim'
    elif value <= 1.8:
        return 'moderado'
    elif value <= 2.5:
        return 'bom'
    else:
        return 'otimo'

def evaluate_lpa(value):
    if value <= 0:
        return 'critico'
    elif value <= 0.1:
        return 'pessimo'
    elif value <= 0.5:
        return 'ruim'
    elif value <= 1:
        return 'moderado'
    elif value <= 2:
        return 'bom'
    else:
        return 'otimo'

def evaluate_m_bruta(value, receita_liquida):
    if receita_liquida <= 0:  # Receita Líquida negativa indica problemas graves
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.15:
        return 'pessimo'
    elif value <= 0.25:
        return 'ruim'
    elif value <= 0.4:
        return 'moderado'
    elif value <= 0.6:
        return 'bom'
    else:
        return 'otimo'

def evaluate_m_ebit(value, receita_liquida):
    if receita_liquida <= 0:  # Receita Líquida negativa indica problemas graves
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.15:
        return 'ruim'
    elif value <= 0.25:
        return 'moderado'
    elif value <= 0.35:
        return 'bom'
    else:
        return 'otimo'

def evaluate_m_ebitda(value, receita_liquida):
    if receita_liquida <= 0:  # Receita Líquida negativa indica problemas graves
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.1:
        return 'pessimo'
    elif value <= 0.2:
        return 'ruim'
    elif value <= 0.3:
        return 'moderado'
    elif value <= 0.4:
        return 'bom'
    else:
        return 'otimo'

def evaluate_m_liquida(value, receita_liquida):
    if receita_liquida <= 0:  # Receita Líquida negativa indica problemas graves
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.1:
        return 'ruim'
    elif value <= 0.15:
        return 'moderado'
    elif value <= 0.25:
        return 'bom'
    else:
        return 'otimo'

def evaluate_p_ativo_circulante_liquido(value, ativo_circulante_liquido):
    if ativo_circulante_liquido <= 0:  # Ativo Circulante Líquido negativo indica problemas de liquidez
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 1:
        return 'ruim'
    elif value <= 2:
        return 'moderado'
    elif value <= 3:
        return 'bom'
    else:
        return 'otimo'

def evaluate_p_capital_giro(value, capital_giro):
    if capital_giro <= 0:  # Capital de Giro negativo indica problemas de liquidez
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 2:
        return 'ruim'
    elif value <= 4:
        return 'moderado'
    elif value <= 6:
        return 'bom'
    else:
        return 'otimo'

def evaluate_p_ebit(value, ebit):
    if ebit <= 0:  # EBIT negativo ou zero indica problemas operacionais
        return 'critico'
    if value <= 5:  # Inclui valores negativos e até 5 como ótimo
        return 'otimo'
    elif value <= 10:
        return 'bom'
    elif value <= 15:
        return 'moderado'
    elif value <= 20:
        return 'ruim'
    else:
        return 'pessimo'

def evaluate_p_ebitda(value, ebitda):
    if ebitda <= 0:  # EBITDA negativo ou zero indica problemas operacionais
        return 'critico'
    if value <= 3:  # Inclui valores negativos e até 3 como ótimo
        return 'otimo'
    elif value <= 6:
        return 'bom'
    elif value <= 10:
        return 'moderado'
    elif value <= 15:
        return 'ruim'
    else:
        return 'pessimo'

def evaluate_p_l(value, lucro_liquido):
    if lucro_liquido <= 0:  # Lucro Líquido negativo indica prejuízo
        return 'critico'
    if value <= 5:  # Inclui valores negativos e até 5 como ótimo
        return 'otimo'
    elif value <= 10:
        return 'bom'
    elif value <= 15:
        return 'moderado'
    elif value <= 20:
        return 'ruim'
    else:
        return 'pessimo'

def evaluate_p_vp(value, vp):
    if vp <= 0:  # Valor Patrimonial negativo indica insolvência
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.5:
        return 'otimo'
    elif value <= 1:
        return 'bom'
    elif value <= 1.5:
        return 'moderado'
    elif value <= 2:
        return 'ruim'
    else:
        return 'pessimo'

def evaluate_p_ativo(value):
    if value <= 0:
        return 'critico'
    elif value <= 0.2:
        return 'pessimo'
    elif value <= 0.3:
        return 'ruim'
    elif value <= 0.5:
        return 'moderado'
    elif value <= 0.8:
        return 'bom'
    else:
        return 'otimo'

def evaluate_pl_ativos(value, pl):
    if pl <= 0:  # Patrimônio Líquido negativo indica insolvência
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.2:
        return 'pessimo'
    elif value <= 0.5:
        return 'ruim'
    elif value <= 0.8:
        return 'moderado'
    elif value <= 1:
        return 'bom'
    else:
        return 'otimo'

def evaluate_psr(value, receita_liquida):
    if receita_liquida <= 0:  # Receita Líquida negativa indica problemas graves
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.5:
        return 'otimo'
    elif value <= 1:
        return 'bom'
    elif value <= 2:
        return 'moderado'
    elif value <= 3:
        return 'ruim'
    else:
        return 'pessimo'

def evaluate_p_sales_ratio(value, receita_liquida):
    if receita_liquida <= 0:  # Receita Líquida negativa indica problemas graves
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.5:
        return 'otimo'
    elif value <= 1:
        return 'bom'
    elif value <= 2:
        return 'moderado'
    elif value <= 3:
        return 'ruim'
    else:
        return 'pessimo'

def evaluate_roa(value):
    if value <= 0:
        return 'critico'
    elif value <= 0.03:
        return 'pessimo'
    elif value <= 0.08:
        return 'ruim'
    elif value <= 0.15:
        return 'moderado'
    elif value <= 0.25:
        return 'bom'
    else:
        return 'otimo'

def evaluate_roe(value, pl):
    if pl <= 0:  # Patrimônio Líquido negativo indica insolvência
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.1:
        return 'ruim'
    elif value <= 0.15:
        return 'moderado'
    elif value <= 0.25:
        return 'bom'
    else:
        return 'otimo'

def evaluate_roic(value):
    if value <= 0:
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.1:
        return 'ruim'
    elif value <= 0.15:
        return 'moderado'
    elif value <= 0.2:
        return 'bom'
    else:
        return 'otimo'

def evaluate_vpa(value, pl):
    if pl <= 0:  # Patrimônio Líquido negativo indica insolvência
        return 'critico'
    if value <= 0:
        return 'critico'
    elif value <= 0.5:
        return 'pessimo'
    elif value <= 1:
        return 'ruim'
    elif value <= 2:
        return 'moderado'
    elif value <= 5:
        return 'bom'
    else:
        return 'otimo'

def evaluate_cagr_lucros_5_anos(value):
    if value <= 0:
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.1:
        return 'ruim'
    elif value <= 0.15:
        return 'moderado'
    elif value <= 0.2:
        return 'bom'
amtrix_value, receita_liquida)
    print(f"M. Liquida = {matrix_value:.3f}, Receita Líquida = {receita_liquida} → {result}")

    # P/Ativo Circulante Líquido
    matrix_value = 301000 / 25000
    ativo_circulante_liquido = 25000
    result = evaluate_p_ativo_circulante_liquido(matrix_value, ativo_circulante_liquido)
    print(f"P/Ativo Circulante Líquido = {matrix_value:.3f}, Ativo Circulante Líquido = {ativo_circulante_liquido} → {result}")

    # P/Capital de Giro
    matrix_value = 301000 / 25000
    capital_giro = 25000
    result = evaluate_p_capital_giro(matrix_value, capital_giro)
    print(f"P/Capital de Giro = {matrix_value:.3f}, Capital de Giro = {capital_giro} → {result}")

    # P/L
    matrix_value = 301000 / 65000
    lucro_liquido = 65000
    result = evaluate_p_l(matrix_value, lucro_liquido)
    print(f"P/L = {matrix_value:.3f}, Lucro Líquido = {lucro_liquido} → {result}")

    # P/VP
    matrix_value = 70 / 32.56
    vp = 32.56
    result = evaluate_p_vp(matrix_value, vp)
    print(f"P/VP = {matrix_value:.3f}, Valor Patrimonial = {vp} → {result}")

    # PL/Ativos
    matrix_value = 140000 / 450000
    pl = 140000
    result = evaluate_pl_ativos(matrix_value, pl)
    print(f"PL/Ativos = {matrix_value:.3f}, Patrimônio Líquido = {pl} → {result}")

    # PSR
    matrix_value = 301000 / 210000
    receita_liquida = 210000
    result = evaluate_psr(matrix_value, receita_liquida)
    print(f"PSR = {matrix_value:.3f}, Receita Líquida = {receita_liquida} → {result}")

    # P/Sales Ratio
    matrix_value = 301000 / 210000
    receita_liquida = 210000
    result = evaluate_p_sales_ratio(matrix_value, receita_liquida)
    print(f"P/Sales Ratio = {matrix_value:.3f}, Receita Líquida = {receita_liquida} → {result}")

    # ROE
    matrix_value = 65000 / 140000
    pl = 140000
    result = evaluate_roe(matrix_value, pl)
    print(f"ROE = {matrix_value:.3f}, Patrimônio Líquido = {pl} → {result}")

    # VPA
    matrix_value = 140000 / 4300
    pl = 140000
    result = evaluate_vpa(matrix_value, pl)
    print(f"VPA = {matrix_value:.3f}, Patrimônio Líquido = {pl} → {result}")

# Cenário 2: Hipotético com Denominadores Negativos
print("\nCenário 2: Vale com Denominadores Negativos (Hipotético)")
# Suponha: PL = -10000, Receita Líquida = -5000, Ativo Circulante Líquido = -5000, Capital de Giro = -5000, Lucro Líquido = -15000
# Recalculando apenas os indicadores ajustados
# Div. liquida/PL
matrix_value = 57000 / -10000  # -5.7
pl = -10000
result = evaluate_div_liquida_pl(matrix_value, pl)
print(f"Div. Líquida/PL = {matrix_value:.3f}, Patrimônio Líquido = {pl} → {result}")

# M. Bruta
matrix_value = 95000 / -5000  # -19.0
receita_liquida = -5000
result = evaluate_m_bruta(matrix_value, receita_liquida)
print(f"M. Bruta = {matrix_value:.3f}, Receita Líquida = {receita_liquida} → {result}")

# M. EBIT
matrix_value = 90000 / -5000  # -18.0
receita_liquida = -5000
result = evaluate_m_ebit(matrix_value, receita_liquida)
print(f"M. EBIT = {matrix_value:.3f}, Receita Líquida = {receita_liquida} → {result}")

# M. EBITDA
matrix_value = 110000 / -5000  # -22.0
receita_liquida = -5000
result = evaluate_m_ebitda(matrix_value, receita_liquida)
print(f"M. EBITDA = {matrix_value:.3f}, Receita Líquida = {receita_liquida} → {result}")

# M. Liquida
matrix_value = 65000 / -5000  # -13.0
receita_liquida = -5000
result = evaluate_m_liquida(matrix_value, receita_liquida)
print(f"M. Liquida = {matrix_value:.3f}, Receita Líquida = {receita_liquida} → {result}")

# P/Ativo Circulante Líquido
matrix_value = 301000 / -5000  # -60.2
ativo_circulante_liquido = -5000
result = evaluate_p_ativo_circulante_liquido(matrix_value, ativo_circulante_liquido)
print(f"P/Ativo Circulante Líquido = {matrix_value:.3f}, Ativo Circulante Líquido = {ativo_circulante_liquido} → {result}")

# P/Capital de Giro
matrix_value = 301000 / -5000  # -60.2
capital_giro = -5000
result = evaluate_p_capital_giro(matrix_value, capital_giro)
print(f"P/Capital de Giro = {matrix_value:.3f}, Capital de Giro = {capital_giro} → {result}")

# P/L
matrix_value = 301000 / -15000  # -20.067
lucro_liquido = -15000
result = evaluate_p_l(matrix_value, lucro_liquido)
print(f"P/L = {matrix_value:.3f}, Lucro Líquido = {lucro_liquido} → {result}")

# P/VP
matrix_value = 70 / (-10000 / 4300)  # -30.1
vp = -10000 / 4300
result = evaluate_p_vp(matrix_value, vp)
print(f"P/VP = {matrix_value:.3f}, Valor Patrimonial = {vp:.2f} → {result}")

# PL/Ativos
matrix_value = -10000 / 450000  # -0.022
pl = -10000
result = evaluate_pl_ativos(matrix_value, pl)
print(f"PL/Ativos = {matrix_value:.3f}, Patrimônio Líquido = {pl} → {result}")

# PSR
matrix_value = 301000 / -5000  # -60.2
receita_liquida = -5000
result = evaluate_psr(matrix_value, receita_liquida)
print(f"PSR = {matrix_value:.3f}, Receita Líquida = {receita_liquida} → {result}")

# P/Sales Ratio
matrix_value = 301000 / -5000  # -60.2
receita_liquida = -5000
result = evaluate_p_sales_ratio(matrix_value, receita_liquida)
print(f"P/Sales Ratio = {matrix_value:.3f}, Rece             return 'otimo'

def evaluate_divida_bruta(value):
    if value <= 0:
        return 'critico'
    elif value <= 0.05:
        return 'pessimo'
    elif value <= 0.1:
        return 'ruim'
    elif value <= 0.15:
        return 'moderado'
    elif value <= 0.2:
        return 'bom'
    else:
        return 'otimo'