MetricasStatus = {
    'Margem Líquida': {
        'critico': {'min': float('-inf'), 'max': 0},
        'pessimo': {'min': 0, 'max': 0.05},
        'ruim': {'min': 0.05, 'max': 0.1},
        'moderado': {'min': 0.1, 'max': 0.15},
        'bom': {'min': 0.15, 'max': 0.25},
        'otimo': {'min': 0.25, 'max': float('inf')},
        'descricao': 'Lucro líquido dividido pela receita líquida. Mede rentabilidade final após todas as despesas.',
        'agrupador': 'Eficiência',
        'descrcritico': 'Prejuízo líquido, indicando ineficiência operacional ou financeira grave. Comum em empresas em crise (ex.: OIBR3) ou setores com alta concorrência (ex.: varejo, CRFB3). Investidores devem evitar, salvo plano robusto de recuperação.',
        'descrpessimo': 'Baixa rentabilidade, indicando desafios operacionais ou financeiros. Comum em setores competitivos (ex.: varejo, MGLU3). Investidores devem analisar potencial de melhoria e redução de custos.',
        'descrruim': 'Rentabilidade limitada, comum em setores cíclicos (ex.: siderurgia, GGBR4). Investidores devem verificar tendência do lucro líquido e riscos setoriais.',
        'descrmoderado': 'Rentabilidade moderada, aceitável em setores maduros (ex.: indústria, CSNA3). Investidores devem analisar sustentabilidade do lucro e concorrência.',
        'descrbom': 'Boa rentabilidade, desempenho sólido, comum em setores com barreiras de entrada (ex.: ABEV3). Investidores devem confirmar consistência do lucro líquido.',
        'descrotimo': 'Alta rentabilidade, desempenho excepcional, comum em setores de alta margem (ex.: tecnologia, TOTS3). Investidores devem verificar sustentabilidade frente a riscos setoriais.'
    },