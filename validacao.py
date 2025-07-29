def classificar_divida_ebit(valor):
    if valor == float('-inf') or valor < 0:
        return 'otimo'  # Caixa líquido supera dívida
    elif 0 <= valor < 1.5:
        return 'bom'  # Dívida quitável em menos de 1,5 anos de EBIT
    elif 1.5 <= valor < 3:
        return 'moderado'  # Endividamento moderado, pagável em 1,5-3 anos
    elif 3 <= valor < 4:
        return 'ruim'  # Endividamento elevado, 3-4 anos para pagar dívida
    elif valor >= 4:
        return 'pessimo'  # Endividamento crítico, mais de 4 anos para quitar
    else:
        # cobre o caso de EBIT negativo ou valor impossível se for float('-inf')
        return 'critico'

    def classificar_divida_ebitda(valor):
        """
        Classifica a métrica Dívida Líquida/EBITDA com base no valor fornecido.

        Args:
            valor (float): Valor da métrica Dívida Líquida/EBITDA

        Returns:
            str: Classificação ('otimo', 'bom', 'moderado', 'ruim', 'pessimo', 'critico')
        """
        if valor == float('-inf') or valor < 0:
            return 'otimo'  # Caixa líquido excede dívida
        elif 0 <= valor < 1:
            return 'bom'  # Dívida quitável rapidamente
        elif 1 <= valor < 2.5:
            return 'moderado'  # Endividamento moderado, pagável em 1-2,5 anos
        elif 2.5 <= valor < 3.5:
            return 'ruim'  # Endividamento elevado, 2,5-3,5 anos para pagar dívida
        elif valor >= 3.5:
            return 'pessimo'  # Endividamento crítico, mais de 3,5 anos para quitar
        else:
            return 'critico'  # EBITDA negativo ou valor impossível

    def classificar_dy(valor):
        """
        Classifica a métrica Dividend Yield (D.Y) com base no valor fornecido.

        Args:
            valor (float): Valor da métrica D.Y

        Returns:
            str: Classificação ('otimo', 'bom', 'moderado', 'ruim', 'pessimo', 'critico')
        """
        if valor >= 0.06:
            return 'otimo'  # Alto retorno, muito atrativo
        elif 0.04 <= valor < 0.06:
            return 'bom'  # Retorno atrativo para investidores de renda
        elif 0.02 <= valor < 0.04:
            return 'moderado'  # Retorno moderado, equilíbrio entre dividendos e reinvestimento
        elif 0.001 <= valor < 0.02:
            return 'ruim'  # Retorno baixo, pouco atrativo
        elif valor == 0:
            return 'critico'  # Sem pagamento de dividendos
        else:
            return 'pessimo'  # Sem dividendos ou valor inválido

    def classificar_pl(valor):
        """
        Classifica a métrica Preço/Lucro (P/L) com base no valor fornecido.

        Args:
            valor (float): Valor da métrica P/L

        Returns:
            str: Classificação ('otimo', 'bom', 'moderado', 'ruim', 'pessimo', 'critico')
        """
        if valor == float('-inf') or (0 <= valor < 5):
            return 'otimo'  # Extremamente subvalorizada, sugere oportunidade
        elif 5 <= valor < 10:
            return 'bom'  # Subvalorizada, oportunidade em setores cíclicos
        elif 10 <= valor < 15:
            return 'moderado'  # Avaliação razoável, comum em setores maduros
        elif 15 <= valor < 20:
            return 'ruim'  # Empresa cara, comum em setores de crescimento
        elif valor >= 20:
            return 'pessimo'  # Empresa extremamente cara, sugere sobrevalorização
        else:
            return 'critico'  # Prejuízo por ação ou valor inválido

    def classificar_margem_ebitda(valor):
        """
        Classifica a métrica Margem EBITDA com base no valor fornecido.

        Args:
            valor (float): Valor da métrica Margem EBITDA

        Returns:
            str: Classificação ('otimo', 'bom', 'moderado', 'ruim', 'pessimo', 'critico')
        """
        if valor >= 0.4:
            return 'otimo'  # Geração de caixa excepcional
        elif 0.3 <= valor < 0.4:
            return 'bom'  # Alta geração de caixa, desempenho sólido
        elif 0.2 <= valor < 0.3:
            return 'moderado'  # Geração de caixa moderada, desempenho razoável
        elif 0.1 <= valor < 0.2:
            return 'ruim'  # Geração de caixa limitada
        elif 0 <= valor < 0.1:
            return 'pessimo'  # Baixa geração de caixa, eficiência limitada
        else:
            return 'critico'  # Prejuízo operacional, problemas estruturais graves

    # Exemplo de uso com função para exibir resultados
    def display_classification(metric_name, valor, classifier_func):
        """
        Exibe a classificação de uma métrica financeira.

        Args:
            metric_name (str): Nome da métrica
            valor (float): Valor da métrica
            classifier_func (function): Função de classificação específica
        """
        classificacao = classifier_func(valor)
        print(f"Métrica: {metric_name}")
        print(f"Valor: {valor}")
        print(f"Classificação: {classificacao}")
        print("-" * 50)

    # Testando as funções
    if __name__ == "__main__":
        test_cases = [
            ('Div. liquida/EBITDA', -1.0, classificar_divida_ebitda),
            ('Div. liquida/EBITDA', 2.0, classificar_divida_ebitda),
            ('D.Y', 0.05, classificar_dy),
            ('P/L', 12.0, classificar_pl),
            ('M. EBITDA', 0.25, classificar_margem_ebitda),
            ('M. EBITDA', -0.1, classificar_margem_ebitda),
        ]

        for metric, valor, func in test_cases:
            display_classification(metric, valor, func)
