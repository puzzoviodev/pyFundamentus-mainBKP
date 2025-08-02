import unittest
import math

def evaluate_pl(pl):
    '''Avalia o Preço/Lucro (P/L) com base em faixas:
    - P/L < 0: Crítico
    - 0 ≤ P/L ≤ 10: Ótimo
    - 10 < P/L ≤ 15: Moderado
    - 15 < P/L ≤ 20: Ruim
    - 20 < P/L ≤ 30: Péssimo
    - P/L > 30: Fora da faixa'''
    try:
        if pl < 0:
            return {'classificacao': 'Critico', 'faixa': 'PL < 0', 'descricao': 'P/L negativo indica prejuízo, sugerindo risco elevado (ex.: OI).'}
        elif 0 <= pl <= 10:
            return {'classificacao': 'Otimo', 'faixa': '0 <= PL <= 10', 'descricao': 'P/L baixo sugere subvalorização, comum em bancos (ex.: ITUB4).'}
        elif 10 < pl <= 15:
            return {'classificacao': 'Moderado', 'faixa': '10 < PL <= 15', 'descricao': 'P/L justo, típico de empresas estáveis (ex.: ABEV3).'}
        elif 15 < pl <= 20:
            return {'classificacao': 'Ruim', 'faixa': '15 < PL <= 20', 'descricao': 'P/L elevado, comum em varejo (ex.: MGLU3).'}
        elif 20 < pl <= 30:
            return {'classificacao': 'Pessimo', 'faixa': '20 < PL <= 30', 'descricao': 'P/L muito alto, risco de correção (ex.: TOTS3).'}
        else:
            return {'classificacao': 'Fora da faixa', 'faixa': 'PL > 30', 'descricao': 'P/L extremo, típico de especulação.'}
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar P/L: {str(e)}.'}

def evaluate_pebitda(pebitda):
    '''Avalia o Preço/EBITDA:
    - P/EBITDA < 0: Crítico
    - 0 ≤ P/EBITDA ≤ 4: Ótimo
    - 4 < P/EBITDA ≤ 7: Moderado
    - 7 < P/EBITDA ≤ 10: Ruim
    - 10 < P/EBITDA ≤ 15: Péssimo
    - P/EBITDA > 15: Fora da faixa'''
    try:
        if pebitda < 0:
            return {'classificacao': 'Critico', 'faixa': 'P/EBITDA < 0', 'descricao': 'EBITDA negativo, risco elevado (ex.: GGBR4).'}
        elif 0 <= pebitda <= 4:
            return {'classificacao': 'Otimo', 'faixa': '0 <= P/EBITDA <= 4', 'descricao': 'Subvalorizado, oportunidade (ex.: VALE3).'}
        elif 4 < pebitda <= 7:
            return {'classificacao': 'Moderado', 'faixa': '4 < P/EBITDA <= 7', 'descricao': 'Valuation justo (ex.: ELET3).'}
        elif 7 < pebitda <= 10:
            return {'classificacao': 'Ruim', 'faixa': '7 < P/EBITDA <= 10', 'descricao': 'Sobrevalorizado, cautela (ex.: MGLU3).'}
        elif 10 < pebitda <= 15:
            return {'classificacao': 'Pessimo', 'faixa': '10 < P/EBITDA <= 15', 'descricao': 'Muito caro, alto risco.'}
        else:
            return {'classificacao': 'Fora da faixa', 'faixa': 'P/EBITDA > 15', 'descricao': 'Sobrevalorização severa.'}
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar P/EBITDA: {str(e)}.'}

def evaluate_pvp(pvp):
    '''Avalia o Preço/Valor Patrimonial (P/VP):
    - P/VP < 0: Crítico
    - 0 ≤ P/VP ≤ 0.8: Ótimo
    - 0.8 < P/VP ≤ 1.5: Moderado
    - 1.5 < P/VP ≤ 2.5: Ruim
    - 2.5 < P/VP ≤ 4: Péssimo
    - P/VP > 4: Fora da faixa'''
    try:
        if pvp < 0:
            return {'classificacao': 'Critico', 'faixa': 'P/VP < 0', 'descricao': 'Patrimônio negativo, insolvência (ex.: OI).'}
        elif 0 <= pvp <= 0.8:
            return {'classificacao': 'Otimo', 'faixa': '0 <= P/VP <= 0.8', 'descricao': 'Subvalorizado, oportunidade (ex.: BBDC4).'}
        elif 0.8 < pvp <= 1.5:
            return {'classificacao': 'Moderado', 'faixa': '0.8 < P/VP <= 1.5', 'descricao': 'Valuation justo (ex.: SUZB3).'}
        elif 1.5 < pvp <= 2.5:
            return {'classificacao': 'Ruim', 'faixa': '1.5 < P/VP <= 2.5', 'descricao': 'Sobrevalorizado (ex.: LREN3).'}
        elif 2.5 < pvp <= 4:
            return {'classificacao': 'Pessimo', 'faixa': '2.5 < P/VP <= 4', 'descricao': 'Muito caro (ex.: TOTS3).'}
        else:
            return {'classificacao': 'Fora da faixa', 'faixa': 'P/VP > 4', 'descricao': 'Sobrevalorização severa.'}
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar P/VP: {str(e)}.'}

def evaluate_pebit(pebit):
    '''Avalia o Preço/EBIT:
    - P/EBIT < 0: Crítico
    - 0 ≤ P/EBIT ≤ 5: Ótimo
    - 5 < P/EBIT ≤ 10: Moderado
    - 10 < P/EBIT ≤ 15: Ruim
    - 15 < P/EBIT ≤ 20: Péssimo
    - P/EBIT > 20: Fora da faixa'''
    try:
        if pebit < 0:
            return {'classificacao': 'Critico', 'faixa': 'P/EBIT < 0', 'descricao': 'EBIT negativo, risco elevado (ex.: GGBR4).'}
        elif 0 <= pebit <= 5:
            return {'classificacao': 'Otimo', 'faixa': '0 <= P/EBIT <= 5', 'descricao': 'Subvalorizado (ex.: VALE3).'}
        elif 5 < pebit <= 10:
            return {'classificacao': 'Moderado', 'faixa': '5 < P/EBIT <= 10', 'descricao': 'Valuation justo (ex.: ELET3).'}
        elif 10 < pebit <= 15:
            return {'classificacao': 'Ruim', 'faixa': '10 < P/EBIT <= 15', 'descricao': 'Sobrevalorizado (ex.: MGLU3).'}
        elif 15 < pebit <= 20:
            return {'classificacao': 'Pessimo', 'faixa': '15 < P/EBIT <= 20', 'descricao': 'Muito caro.'}
        else:
            return {'classificacao': 'Fora da faixa', 'faixa': 'P/EBIT > 20', 'descricao': 'Sobrevalorização severa.'}
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar P/EBIT: {str(e)}.'}

def evaluate_evebitda(evebitda):
    '''Avalia o EV/EBITDA:
    - EV/EBITDA < 0: Crítico
    - 0 ≤ EV/EBITDA ≤ 4: Ótimo
    - 4 < EV/EBITDA ≤ 7: Moderado
    - 7 < EV/EBITDA ≤ 10: Ruim
    - 10 < EV/EBITDA ≤ 15: Péssimo
    - EV/EBITDA > 15: Fora da faixa'''
    try:
        if evebitda < 0:
            return {'classificacao': 'Critico', 'faixa': 'EV/EBITDA < 0', 'descricao': 'EBITDA negativo, risco elevado (ex.: OI).'}
        elif 0 <= evebitda <= 4:
            return {'classificacao': 'Otimo', 'faixa': '0 <= EV/EBITDA <= 4', 'descricao': 'Subvalorizado (ex.: VALE3).'}
        elif 4 < evebitda <= 7:
            return {'classificacao': 'Moderado', 'faixa': '4 < EV/EBITDA <= 7', 'descricao': 'Valuation justo (ex.: ABEV3).'}
        elif 7 < evebitda <= 10:
            return {'classificacao': 'Ruim', 'faixa': '7 < EV/EBITDA <= 10', 'descricao': 'Sobrevalorizado (ex.: MGLU3).'}
        elif 10 < evebitda <= 15:
            return {'classificacao': 'Pessimo', 'faixa': '10 < EV/EBITDA <= 15', 'descricao': 'Muito caro.'}
        else:
            return {'classificacao': 'Fora da faixa', 'faixa': 'EV/EBITDA > 15', 'descricao': 'Sobrevalorização severa.'}
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar EV/EBITDA: {str(e)}.'}

def evaluate_evebit(evebit):
    '''Avalia o EV/EBIT:
    - EV/EBIT < 0: Crítico
    - 0 ≤ EV/EBIT ≤ 5: Ótimo
    - 5 < EV/EBIT ≤ 10: Moderado
    - 10 < EV/EBIT ≤ 15: Ruim
    - 15 < EV/EBIT ≤ 20: Péssimo
    - EV/EBIT > 20: Fora da faixa'''
    try:
        if evebit < 0:
            return {'classificacao': 'Critico', 'faixa': 'EV/EBIT < 0', 'descricao': 'EBIT negativo, risco elevado (ex.: GGBR4).'}
        elif 0 <= evebit <= 5:
            return {'classificacao': 'Otimo', 'faixa': '0 <= EV/EBIT <= 5', 'descricao': 'Subvalorizado (ex.: VALE3).'}
        elif 5 < evebit <= 10:
            return {'classificacao': 'Moderado', 'faixa': '5 < EV/EBIT <= 10', 'descricao': 'Valuation justo (ex.: ELET3).'}
        elif 10 < evebit <= 15:
            return {'classificacao': 'Ruim', 'faixa': '10 < EV/EBIT <= 15', 'descricao': 'Sobrevalorizado (ex.: MGLU3).'}
        elif 15 < evebit <= 20:
            return {'classificacao': 'Pessimo', 'faixa': '15 < EV/EBIT <= 20', 'descricao': 'Muito caro.'}
        else:
            return {'classificacao': 'Fora da faixa', 'faixa': 'EV/EBIT > 20', 'descricao': 'Sobrevalorização severa.'}
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar EV/EBIT: {str(e)}.'}

def evaluate_giro_ativos(giro):
    '''Avalia o Giro de Ativos:
    - Giro < 0: Crítico
    - 0 ≤ Giro ≤ 0.2: Péssimo
    - 0.2 < Giro ≤ 0.5: Ruim
    - 0.5 < Giro ≤ 1.0: Moderado
    - 1.0 < Giro ≤ 2.0: Ótimo
    - Giro > 2.0: Fora da faixa'''
    try:
        if giro < 0:
            return {'classificacao': 'Critico', 'faixa': 'Giro < 0', 'descricao': 'Receita negativa, risco elevado.'}
        elif 0 <= giro <= 0.2:
            return {'classificacao': 'Pessimo', 'faixa': '0 <= Giro <= 0.2', 'descricao': 'Baixa eficiência, comum em infraestrutura (ex.: CCRD3).'}
        elif 0.2 < giro <= 0.5:
            return {'classificacao': 'Ruim', 'faixa': '0.2 < Giro <= 0.5', 'descricao': 'Eficiência limitada (ex.: CPLE6).'}
        elif 0.5 < giro <= 1.0:
            return {'classificacao': 'Moderado', 'faixa': '0.5 < Giro <= 1.0', 'descricao': 'Eficiência adequada (ex.: WEGE3).'}
        elif 1.0 < giro <= 2.0:
            return {'classificacao': 'Otimo', 'faixa': '1.0 < Giro <= 2.0', 'descricao': 'Alta eficiência (ex.: MGLU3).'}
        else:
            return {'classificacao': 'Fora da faixa', 'faixa': 'Giro > 2.0', 'descricao': 'Eficiência excepcional (ex.: TOTS3).'}
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar Giro de Ativos: {str(e)}.'}

def evaluate_divida_liquida_pl(dl_pl):
    '''Avalia a Dívida Líquida/Patrimônio Líquido:
    - DL/PL < -1: Crítico
    - -1 ≤ DL/PL < 0: Ótimo
    - 0 ≤ DL/PL ≤ 0.5: Moderado
    - 0.5 < DL/PL ≤ 1: Ruim
    - 1 < DL/PL ≤ 2: Péssimo
    - DL/PL > 2: Fora da faixa'''
    try:
        if dl_pl < -1:
            return {'classificacao': 'Critico', 'faixa': 'DL/PL < -1', 'descricao': 'Caixa excessivo, ineficiência (ex.: WIZS3).'}
        elif -1 <= dl_pl < 0:
            return {'classificacao': 'Otimo', 'faixa': '-1 <= DL/PL < 0', 'descricao': 'Caixa supera dívida (ex.: VALE3).'}
        elif 0 <= dl_pl <= 0.5:
            return {'classificacao': 'Moderado', 'faixa': '0 <= DL/PL <= 0.5', 'descricao': 'Endividamento baixo (ex.: ABEV3).'}
        elif 0.5 < dl_pl <= 1:
            return {'classificacao': 'Ruim', 'faixa': '0.5 < DL/PL <= 1', 'descricao': 'Endividamento moderado (ex.: SUZB3).'}
        elif 1 < dl_pl <= 2:
            return {'classificacao': 'Pessimo', 'faixa': '1 < DL/PL <= 2', 'descricao': 'Endividamento alto (ex.: ENGI11).'}
        else:
            return {'classificacao': 'Fora da faixa', 'faixa': 'DL/PL > 2', 'descricao': 'Endividamento excessivo (ex.: CYRE3).'}
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar DL/PL: {str(e)}.'}

def evaluate_divida_liquida_ebitda(dl_ebitda):
    '''Avalia a Dívida Líquida/EBITDA:
    - DL/EBITDA < -2: Crítico
    - -2 ≤ DL/EBITDA < 0: Ótimo
    - 0 ≤ DL/EBITDA ≤ 1.5: Moderado
    - 1.5 < DL/EBITDA ≤ 3: Ruim
    - 3 < DL/EBITDA ≤ 4.5: Péssimo
    - DL/EBITDA > 4.5: Fora da faixa'''
    try:
        if dl_ebitda < -2:
            return {'classificacao': 'Critico', 'faixa': 'DL/EBITDA < -2', 'descricao': 'Caixa excessivo (ex.: VALE3).'}
        elif -2 <= dl_ebitda < 0:
            return {'classificacao': 'Otimo', 'faixa': '-2 <= DL/EBITDA < 0', 'descricao': 'Caixa supera dívida (ex.: WEGE3).'}
        elif 0 <= dl_ebitda <= 1.5:
            return {'classificacao': 'Moderado', 'faixa': '0 <= DL/EBITDA <= 1.5', 'descricao': 'Endividamento baixo (ex.: ABEV3).'}
        elif 1.5 < dl_ebitda <= 3:
            return {'classificacao': 'Ruim', 'faixa': '1.5 < DL/EBITDA <= 3', 'descricao': 'Endividamento moderado (ex.: SUZB3).'}
        elif 3 < dl_ebitda <= 4.5:
            return {'classificacao': 'Pessimo', 'faixa': '3 < DL/EBITDA <= 4.5', 'descricao': 'Endividamento alto (ex.: ENGI11).'}
        else:
            return {'classificacao': 'Fora da faixa', 'faixa': 'DL/EBITDA > 4.5', 'descricao': 'Endividamento excessivo (ex.: OI).'}
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar DL/EBITDA: {str(e)}.'}

def evaluate_divida_liquida_ebit(dl_ebit):
    '''Avalia a Dívida Líquida/EBIT:
    - DL/EBIT < -3: Crítico
    - -3 ≤ DL/EBIT < 0: Ótimo
    - 0 ≤ DL/EBIT ≤ 2: Moderado
    - 2 < DL/EBIT ≤ 4: Ruim
    - 4 < DL/EBIT ≤ 6: Péssimo
    - DL/EBIT > 6: Fora da faixa'''
    try:
        if dl_ebit < -3:
            return {'classificacao': 'Critico', 'faixa': 'DL/EBIT < -3', 'descricao': 'Caixa excessivo, ineficiência.'}
        elif -3 <= dl_ebit < 0:
            return {'classificacao': 'Otimo', 'faixa': '-3 <= DL/EBIT < 0', 'descricao': 'Caixa supera dívida (ex.: ABEV3).'}
        elif 0 <= dl_ebit <= 2:
            return {'classificacao': 'Moderado', 'faixa': '0 <= DL/EBIT <= 2', 'descricao': 'Endividamento baixo (ex.: SUZB3).'}
        elif 2 < dl_ebit <= 4:
            return {'classificacao': 'Ruim', 'faixa': '2 < DL/EBIT <= 4', 'descricao': 'Endividamento moderado.'}
        elif 4 < dl_ebit <= 6:
            return {'classificacao': 'Pessimo', 'faixa': '4 < DL/EBIT <= 6', 'descricao': 'Endividamento alto.'}
        else:
            return {'classificacao': 'Fora da faixa', 'faixa': 'DL/EBIT > 6', 'descricao': 'Endividamento excessivo.'}
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar DL/EBIT: {str(e)}.'}

class TestEvaluateIndicatorsPart1(unittest.TestCase):
    def test_evaluate_pl(self):
        self.assertEqual(evaluate_pl(-1)['classificacao'], 'Critico')
        self.assertEqual(evaluate_pl(5)['classificacao'], 'Otimo')
        self.assertEqual(evaluate_pl(12)['classificacao'], 'Moderado')
        self.assertEqual(evaluate_pl(18)['classificacao'], 'Ruim')
        self.assertEqual(evaluate_pl(25)['classificacao'], 'Pessimo')
        self.assertEqual(evaluate_pl(35)['classificacao'], 'Fora da faixa')
        self.assertEqual(evaluate_pl(None)['classificacao'], 'Erro')
        self.assertEqual(evaluate_pl("invalid")['classificacao'], 'Erro')
        self.assertEqual(evaluate_pl([1, 2])['classificacao'], 'Erro')
        self.assertEqual(evaluate_pl(math.nan)['classificacao'], 'Erro')
        self.assertEqual(evaluate_pl(math.inf)['classificacao'], 'Erro')

    def test_evaluate_pebitda(self):
        self.assertEqual(evaluate_pebitda(-1)['classificacao'], 'Critico')
        self.assertEqual(evaluate_pebitda(3)['classificacao'], 'Otimo')
        self.assertEqual(evaluate_pebitda(6)['classificacao'], 'Moderado')
        self.assertEqual(evaluate_pebitda(9)['classificacao'], 'Ruim')
        self.assertEqual(evaluate_pebitda(12)['classificacao'], 'Pessimo')
        self.assertEqual(evaluate_pebitda(20)['classificacao'], 'Fora da faixa')
        self.assertEqual(evaluate_pebitda(None)['classificacao'], 'Erro')

    def test_evaluate_pvp(self):
        self.assertEqual(evaluate_pvp(-0.5)['classificacao'], 'Critico')
        self.assertEqual(evaluate_pvp(0.5)['classificacao'], 'Otimo')
        self.assertEqual(evaluate_pvp(1.2)['classificacao'], 'Moderado')
        self.assertEqual(evaluate_pvp(2)['classificacao'], 'Ruim')
        self.assertEqual(evaluate_pvp(3)['classificacao'], 'Pessimo')
        self.assertEqual(evaluate_pvp(5)['classificacao'], 'Fora da faixa')
        self.assertEqual(evaluate_pvp(None)['classificacao'], 'Erro')

    def test_evaluate_pebit(self):
        self.assertEqual(evaluate_pebit(-1)['classificacao'], 'Critico')
        self.assertEqual(evaluate_pebit(3)['classificacao'], 'Otimo')
        self.assertEqual(evaluate_pebit(8)['classificacao'], 'Moderado')
        self.assertEqual(evaluate_pebit(12)['classificacao'], 'Ruim')
        self.assertEqual(evaluate_pebit(18)['classificacao'], 'Pessimo')
        self.assertEqual(evaluate_pebit(25)['classificacao'], 'Fora da faixa')
        self.assertEqual(evaluate_pebit(None)['classificacao'], 'Erro')

    def test_evaluate_evebitda(self):
        self.assertEqual(evaluate_evebitda(-1)['classificacao'], 'Critico')
        self.assertEqual(evaluate_evebitda(3)['classificacao'], 'Otimo')
        self.assertEqual(evaluate_evebitda(6)['classificacao'], 'Moderado')
        self.assertEqual(evaluate_evebitda(9)['classificacao'], 'Ruim')
        self.assertEqual(evaluate_evebitda(12)['classificacao'], 'Pessimo')
        self.assertEqual(evaluate_evebitda(20)['classificacao'], 'Fora da faixa')
        self.assertEqual(evaluate_evebitda(None)['classificacao'], 'Erro')

    def test_evaluate_evebit(self):
        self.assertEqual(evaluate_evebit(-1)['classificacao'], 'Critico')
        self.assertEqual(evaluate_evebit(3)['classificacao'], 'Otimo')
        self.assertEqual(evaluate_evebit(8)['classificacao'], 'Moderado')
        self.assertEqual(evaluate_evebit(12)['classificacao'], 'Ruim')
        self.assertEqual(evaluate_evebit(18)['classificacao'], 'Pessimo')
        self.assertEqual(evaluate_evebit(25)['classificacao'], 'Fora da faixa')
        self.assertEqual(evaluate_evebit(None)['classificacao'], 'Erro')

    def test_evaluate_giro_ativos(self):
        self.assertEqual(evaluate_giro_ativos(-0.1)['classificacao'], 'Critico')
        self.assertEqual(evaluate_giro_ativos(0.1)['classificacao'], 'Pessimo')
        self.assertEqual(evaluate_giro_ativos(0.3)['classificacao'], 'Ruim')
        self.assertEqual(evaluate_giro_ativos(0.7)['classificacao'], 'Moderado')
        self.assertEqual(evaluate_giro_ativos(1.5)['classificacao'], 'Otimo')
        self.assertEqual(evaluate_giro_ativos(3)['classificacao'], 'Fora da faixa')
        self.assertEqual(evaluate_giro_ativos(None)['classificacao'], 'Erro')

    def test_evaluate_divida_liquida_pl(self):
        self.assertEqual(evaluate_divida_liquida_pl(-2)['classificacao'], 'Critico')
        self.assertEqual(evaluate_divida_liquida_pl(-0.5)['classificacao'], 'Otimo')
        self.assertEqual(evaluate_divida_liquida_pl(0.3)['classificacao'], 'Moderado')
        self.assertEqual(evaluate_divida_liquida_pl(0.7)['classificacao'], 'Ruim')
        self.assertEqual(evaluate_divida_liquida_pl(1.5)['classificacao'], 'Pessimo')
        self.assertEqual(evaluate_divida_liquida_pl(3)['classificacao'], 'Fora da faixa')
        self.assertEqual(evaluate_divida_liquida_pl(None)['classificacao'], 'Erro')

    def test_evaluate_divida_liquida_ebitda(self):
        self.assertEqual(evaluate_divida_liquida_ebitda(-3)['classificacao'], 'Critico')
        self.assertEqual(evaluate_divida_liquida_ebitda(-1)['classificacao'], 'Otimo')
        self.assertEqual(evaluate_divida_liquida_ebitda(1)['classificacao'], 'Moderado')
        self.assertEqual(evaluate_divida_liquida_ebitda(2)['classificacao'], 'Ruim')
        self.assertEqual(evaluate_divida_liquida_ebitda(4)['classificacao'], 'Pessimo')
        self.assertEqual(evaluate_divida_liquida_ebitda(6)['classificacao'], 'Fora da faixa')
        self.assertEqual(evaluate_divida_liquida_ebitda(None)['classificacao'], 'Erro')

    def test_evaluate_divida_liquida_ebit(self):
        self.assertEqual(evaluate_divida_liquida_ebit(-4)['classificacao'], 'Critico')
        self.assertEqual(evaluate_divida_liquida_ebit(-1)['classificacao'], 'Otimo')
        self.assertEqual(evaluate_divida_liquida_ebit(1)['classificacao'], 'Moderado')
        self.assertEqual(evaluate_divida_liquida_ebit(3)['classificacao'], 'Ruim')
        self.assertEqual(evaluate_divida_liquida_ebit(5)['classificacao'], 'Pessimo')
        self.assertEqual(evaluate_divida_liquida_ebit(7)['classificacao'], 'Fora da faixa')
        self.assertEqual(evaluate_divida_liquida_ebit(None)['classificacao'], 'Erro')

if __name__ == '__main__':

    from evaluate_indicators_part3 import (
        evaluate_divida_bruta_pl,
        evaluate_divida_bruta_ebitda,
        evaluate_cobertura_juros,
        evaluate_receita_ativo_circulante,
        evaluate_lucro_bruto_receita,
        evaluate_lucro_operacional_receita,
        evaluate_ebitda_receita,
        evaluate_preco_fcl,
        evaluate_ebit_ativo,
        evaluate_dividend_yield
    )


    def analyze_company(indicators, company_name="Empresa Exemplo"):
        """
        Analisa os indicadores financeiros da Parte 3 para uma empresa.

        Args:
            indicators (dict): Dicionário com os valores dos indicadores (ex.: {'db_pl': 0.5, 'dy': 0.05}).
            company_name (str): Nome da empresa para exibição (default: 'Empresa Exemplo').

        Returns:
            dict: Resultados da análise para cada indicador.
        """
        results = {}

        # Lista de indicadores e suas respectivas funções
        indicator_functions = [
            ('Dívida Bruta/PL', 'db_pl', evaluate_divida_bruta_pl),
            ('Dívida Bruta/EBITDA', 'db_ebitda', evaluate_divida_bruta_ebitda),
            ('Cobertura de Juros', 'cobertura', evaluate_cobertura_juros),
            ('Receita/Ativo Circulante', 'rac', evaluate_receita_ativo_circulante),
            ('Lucro Bruto/Receita', 'lbr', evaluate_lucro_bruto_receita),
            ('Lucro Operacional/Receita', 'lor', evaluate_lucro_operacional_receita),
            ('EBITDA/Receita', 'ebitda_r', evaluate_ebitda_receita),
            ('Preço/Fluxo de Caixa Livre', 'pfcl', evaluate_preco_fcl),
            ('EBIT/Ativo', 'ebit_ativo', evaluate_ebit_ativo),
            ('Dividend Yield', 'dy', evaluate_dividend_yield)
        ]

        print(f"\nAnálise Financeira da {company_name}:\n{'-' * 50}")

        for indicator_name, key, func in indicator_functions:
            try:
                result = func(indicators.get(key))
                results[indicator_name] = result
                classificacao = result['classificacao']
                faixa = result['faixa']
                descricao = result['descricao']
                print(f"{indicator_name}: {classificacao} ({faixa}) - {descricao}")
            except Exception as e:
                print(f"{indicator_name}: Erro inesperado - {str(e)}")

        print('-' * 50)
        return results


    if __name__ == '__main__':
        # Exemplo 1: Análise de uma empresa com valores válidos (ex.: ABEV3)
        indicators_valid = {
            'db_pl': 0.5,
            'db_ebitda': 1.5,
            'cobertura': 4.0,
            'rac': 1.5,
            'lbr': 0.4,
            'lor': 0.15,
            'ebitda_r': 0.3,
            'pfcl': 7.0,
            'ebit_ativo': 0.08,
            'dy': 0.05
        }
        analyze_company(indicators_valid, company_name="ABEV3")

        # Exemplo 2: Análise com valores inválidos para testar tratamento de erros
        indicators_invalid = {
            'db_pl': 0.5,
            'db_ebitda': "invalid",
            'cobertura': None,
            'rac': [1, 2],
            'lbr': float('nan'),
            'lor': float('inf'),
            'ebitda_r': 0.3,
            'pfcl': 7.0,
            'ebit_ativo': -0.1,
            'dy': 0.12
        }
        analyze_company(indicators_invalid, company_name="Empresa com Erros")



        ============================

        from evaluate_indicators_part3 import (
            evaluate_divida_bruta_pl,
            evaluate_divida_bruta_ebitda,
            evaluate_cobertura_juros,
            evaluate_receita_ativo_circulante,
            evaluate_lucro_bruto_receita,
            evaluate_lucro_operacional_receita,
            evaluate_ebitda_receita,
            evaluate_preco_fcl,
            evaluate_ebit_ativo,
            evaluate_dividend_yield
        )


        def print_indicator_result(indicator_name, result):
            """
            Exibe o resultado de um indicador de forma formatada.

            Args:
                indicator_name (str): Nome do indicador.
                result (dict): Dicionário com 'classificacao', 'faixa' e 'descricao'.
            """
            print(f"{indicator_name}: {result['classificacao']} ({result['faixa']}) - {result['descricao']}")


        def analyze_company_individual(company_name, db_pl, db_ebitda, cobertura, rac, lbr, lor, ebitda_r, pfcl,
                                       ebit_ativo, dy):
            """
            Analisa os indicadores financeiros chamando cada função individualmente.

            Args:
                company_name (str): Nome da empresa.
                db_pl, db_ebitda, cobertura, rac, lbr, lor, ebitda_r, pfcl, ebit_ativo, dy: Valores dos indicadores.
            """
            print(f"\nAnálise Financeira da {company_name}:\n{'-' * 50}")

            # Chamada individual de cada função
            result_db_pl = evaluate_divida_bruta_pl(db_pl)
            print_indicator_result("Dívida Bruta/PL", result_db_pl)

            result_db_ebitda = evaluate_divida_bruta_ebitda(db_ebitda)
            print_indicator_result("Dívida Bruta/EBITDA", result_db_ebitda)

            result_cobertura = evaluate_cobertura_juros(cobertura)
            print_indicator_result("Cobertura de Juros", result_cobertura)

            result_rac = evaluate_receita_ativo_circulante(rac)
            print_indicator_result("Receita/Ativo Circulante", result_rac)

            result_lbr = evaluate_lucro_bruto_receita(lbr)
            print_indicator_result("Lucro Bruto/Receita", result_lbr)

            result_lor = evaluate_lucro_operacional_receita(lor)
            print_indicator_result("Lucro Operacional/Receita", result_lor)

            result_ebitda_r = evaluate_ebitda_receita(ebitda_r)
            print_indicator_result("EBITDA/Receita", result_ebitda_r)

            result_pfcl = evaluate_preco_fcl(pfcl)
            print_indicator_result("Preço/Fluxo de Caixa Livre", result_pfcl)

            result_ebit_ativo = evaluate_ebit_ativo(ebit_ativo)
            print_indicator_result("EBIT/Ativo", result_ebit_ativo)

            result_dy = evaluate_dividend_yield(dy)
            print_indicator_result("Dividend Yield", result_dy)

            print('-' * 50)


        if __name__ == '__main__':
            # Exemplo 1: Análise com valores válidos (ex.: ABEV3)
            print("Exemplo 1: Valores Válidos (ABEV3)")
            analyze_company_individual(
                company_name="ABEV3",
                db_pl=0.5,
                db_ebitda=1.5,
                cobertura=4.0,
                rac=1.5,
                lbr=0.4,
                lor=0.15,
                ebitda_r=0.3,
                pfcl=7.0,
                ebit_ativo=0.08,
                dy=0.05
            )

            # Exemplo 2: Análise com valores inválidos para testar tratamento de erros
            print("\nExemplo 2: Valores Inválidos (Empresa com Erros)")
            analyze_company_individual(
                company_name="Empresa com Erros",
                db_pl=0.5,
                db_ebitda="invalid",
                cobertura=None,
                rac=[1, 2],
                lbr=float('nan'),
                lor=float('inf'),
                ebitda_r=0.3,
                pfcl=7.0,
                ebit_ativo=-0.1,
                dy=0.12
            )

            from evaluate_indicators_part1 import evaluate_pl

            # Valor de exemplo para P/L (ex.: ITUB4)
            pl_value = 8
            result = evaluate_pl(pl_value)

            # Exibir resultado
            print(f"P/L: {result['classificacao']} ({result['faixa']})")
            print(f"Descrição: {result['descricao']}")