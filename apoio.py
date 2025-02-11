ROE = f"{float(Dicprofitability_indicators.get('ROE')) * 100}%"
ROA = ''
ROIC = f"{float(Dicprofitability_indicators.get('ROIC')) * 100}%"
Giroativos = f"{float(Dicprofitability_indicators.get('Giro ativos')) * 100}%"

MBruta = f"{float(Dicprofitability_indicators.get("Margem bruta")) * 100}%"
MEBITDA = ''
MEBIT = f"{float(Dicprofitability_indicators.get("Margem EBIT")) * 100}%"
MLiquida = f"{float(Dicprofitability_indicators.get("Margem líquida")) * 100}%"

DivliquidaPL = f"{float(Dicindebtedness_indicators.get("Dívida líquida/Patrim")) * 100}%"
DivliquidaEBITDA = f"{float(Dicindebtedness_indicators.get("Dívida líquida/EBITDA")) * 100}%"
DivliquidaEBIT = ""
PLAtivos = f"{float(Dicindebtedness_indicators.get("PL/Ativos")) * 100}%"
PassivosAtivos = ""
Liqcorrente = f"{float(Dicindebtedness_indicators.get("Liquidez corrente")) * 100}%"

PL = f"{float(Dicvaluation_indicators.get("P/L")) * 100}%"
PEGRatio = ""
PVP = f"{float(Dicvaluation_indicators.get("P/VP")) * 100}%"
EVEBITDA = f"{float(Dicvaluation_indicators.get("EV/EBITDA")) * 100}%"
EVEBIT = f"{float(Dicvaluation_indicators.get("EV/EBIT")) * 100}%"
PEBITDA = ""
PEBIT = f"{float(Dicvaluation_indicators.get("P/EBIT")) * 100}%"
VPA = f"{float(Dicdetailed_information.get("VPA")) * 100}%"
PAtivo = f"{float(Dicvaluation_indicators.get("Preço/Ativos")) * 100}%"
LPA = f"{float(Dicdetailed_information.get("LPA")) * 100}%"
PSR = f"{float(Dicvaluation_indicators.get("PSR")) * 100}%"
PCapGiro = f"{float(Dicvaluation_indicators.get("Preço/Capital de giro")) * 100}%"
PAtivoCircLiq = f"{float(Dicvaluation_indicators.get("Preço/Ativ circ liq")) * 100}%"


MetricasFund = {
    'M. Liquida': {
        'baixo': {'min': 0, 'max': 3},
        'regular': {'min': 3, 'max': 6},
        'bom': {'min': 6, 'max': 10},
        'otimo': {'min': 10, 'max': float('inf')},
        'descricao': 'Rendimento de dividendos. Acima de 6% é considerado bom.',
        'agrupador': 'Eficiência'
    }