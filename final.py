def evaluate_lpa(lpa):
    '''Avalia o Lucro por Ação (LPA) com base em faixas definidas:
    - LPA < 0: Crítico (prejuízo)
    - 0 ≤ LPA ≤ 0.2: Péssimo (lucro muito baixo)
    - 0.2 < LPA ≤ 0.5: Ruim (lucro limitado)
    - 0.5 < LPA ≤ 1: Moderado (lucro adequado)
    - 1 < LPA ≤ 2: Ótimo (lucro alto)
    - LPA > 2: Fora da faixa (lucro excepcional)'''
    definicao = 'indefinido'
    agrupador = 'indefinido'
    formula = 'indefinido'
    try:
        if lpa < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'LPA < 0',
                'descricao': 'LPA negativo indica prejuízo por ação, sugerindo problemas financeiros (ex.: OI).'
            }
        elif 0 <= lpa <= 0.2:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0 <= LPA <= 0.2',
                'descricao': 'LPA muito baixo sugere lucratividade insuficiente, comum em empresas em crise.'
            }
        elif 0.2 < lpa <= 0.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.2 < LPA <= 0.5',
                'descricao': 'LPA limitado indica lucratividade moderada, comum em setores cíclicos (ex.: GGBR4).'
            }
        elif 0.5 < lpa <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < LPA <= 1',
                'descricao': 'LPA adequado sugere lucratividade equilibrada, comum em consumo (ex.: ABEV3).'
            }
        elif 1 < lpa <= 2:
            return {
                'classificacao': 'Otimo',
                'faixa': '1 < LPA <= 2',
                'descricao': 'LPA alto indica forte lucratividade, comum em tecnologia (ex.: TOTS3).'
            }
        else:  # lpa > 2
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'LPA > 2',
                'descricao': 'LPA extremamente alto sugere lucratividade excepcional, comum em empresas líderes (ex.: VALE3).'
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar LPA: {str(e)}. Verifique se o valor fornecido é um número válido.'
        }

def evaluate_psr(psr):
    '''Avalia o Preço/Receita (P/SR) com base em faixas definidas:
    - P/SR < 0: Crítico (receita negativa)
    - 0 ≤ P/SR ≤ 0.3: Ótimo (subvalorizado)
    - 0.3 < P/SR ≤ 0.8: Moderado (valuation justo)
    - 0.8 < P/SR ≤ 1.5: Ruim (sobrevalorizado)
    - 1.5 < P/SR ≤ 2.5: Péssimo (muito caro)
    - P/SR > 2.5: Fora da faixa (extremamente sobrevalorizado)'''
    definicao = 'indefinido'
    agrupador = 'indefinido'
    formula = 'indefinido'
    try:
        if psr < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'P/SR < 0',
                'descricao': 'P/SR negativo indica receita negativa, sugerindo graves problemas operacionais.'
            }
        elif 0 <= psr <= 0.3:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= P/SR <= 0.3',
                'descricao': 'P/SR baixo sugere subvalorização, comum em mineração (ex.: VALE3). Oportunidade de compra.'
            }
        elif 0.3 < psr <= 0.8:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.3 < P/SR <= 0.8',
                'descricao': 'P/SR indica valuation justo, típico de energia (ex.: ELET3). Equilíbrio entre risco e retorno.'
            }
        elif 0.8 < psr <= 1.5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.8 < P/SR <= 1.5',
                'descricao': 'P/SR elevado sugere sobrevalorização, comum em consumo (ex.: ABEV3).'
            }
        elif 1.5 < psr <= 2.5:
            return {
                'classificacao': 'Pessimo',
                'faixa': '1.5 < P/SR <= 2.5',
                'descricao': 'P/SR muito alto indica ação cara, comum em tecnologia.'
            }
        else:  # psr > 2.5
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/SR > 2.5',
                'descricao': 'P/SR extremamente elevado sugere sobrevalorização severa, indicando alto risco.'
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar P/SR: {str(e)}. Verifique se o valor fornecido é um número válido.'
        }

def evaluate_p_ativo_circ_liq(p_acl):
    '''Avalia o Preço/Ativo Circulante Líquido com base em faixas definidas:
    - P/ACL < 0: Crítico (ativo circulante líquido negativo)
    - 0 ≤ P/ACL ≤ 0.2: Ótimo (subvalorizado)
    - 0.2 < P/ACL ≤ 0.5: Moderado (valuation justo)
    - 0.5 < P/ACL ≤ 1: Ruim (sobrevalorizado)
    - 1 < P/ACL ≤ 1.5: Péssimo (muito caro)
    - P/ACL > 1.5: Fora da faixa (extremamente sobrevalorizado)'''
    definicao = 'indefinido'
    agrupador = 'indefinido'
    formula = 'indefinido'
    try:
        if p_acl < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'P/ACL < 0',
                'descricao': 'P/ACL negativo indica ativo circulante líquido negativo, sugerindo problemas de liquidez.'
            }
        elif 0 <= p_acl <= 0.2:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= P/ACL <= 0.2',
                'descricao': 'P/ACL baixo sugere subvalorização em relação à liquidez, comum em mineração (ex.: VALE3).'
            }
        elif 0.2 < p_acl <= 0.5:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.2 < P/ACL <= 0.5',
                'descricao': 'P/ACL indica valuation justo, comum em energia (ex.: ELET3).'
            }
        elif 0.5 < p_acl <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < P/ACL <= 1',
                'descricao': 'P/ACL elevado sugere sobrevalorização, comum em consumo (ex.: ABEV3).'
            }
        elif 1 < p_acl <= 1.5:
            return {
                'classificacao': 'Pessimo',
                'faixa': '1 < P/ACL <= 1.5',
                'descricao': 'P/ACL muito alto indica ação cara, comum em tecnologia.'
            }
        else:  # p_acl > 1.5
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'P/ACL > 1.5',
                'descricao': 'P/ACL extremamente elevado sugere sobrevalorização severa, indicando alto risco.'
            }
    except Exception as e:
        print(f"Erro inesperado tratamento : {e}")
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar P/ACL: {str(e)}. Verifique se o valor fornecido é um número'
        }

def evaluate_cobertura_juros(cobertura):
            '''Avalia a Cobertura de Juros (EBIT/Juros) com base em faixas definidas:
            - Cobertura < 1: Crítico (incapacidade de cobrir juros)
            - 1 ≤ Cobertura ≤ 1.5: Péssimo (cobertura muito baixa)
            - 1.5 < Cobertura ≤ 3: Ruim (cobertura limitada)
            - 3 < Cobertura ≤ 5: Moderado (cobertura adequada)
            - 5 < Cobertura ≤ 10: Ótimo (cobertura alta)
            - Cobertura > 10: Fora da faixa (cobertura excepcional)'''
            definicao = 'indefinido'
            agrupador = 'indefinido'
            formula = 'indefinido'
            try:
                if cobertura < 1:
                    return {
                        'classificacao': 'Critico',
                        'faixa': 'Cobertura < 1',
                        'descricao': 'Cobertura de juros abaixo de 1 indica incapacidade de cobrir despesas com juros, sugerindo alto risco financeiro (ex.: OI). Exige análise de fluxo de caixa e endividamento.'
                    }
                elif 1 <= cobertura <= 1.5:
                    return {
                        'classificacao': 'Pessimo',
                        'faixa': '1 <= Cobertura <= 1.5',
                        'descricao': 'Cobertura muito baixa sugere dificuldades em cumprir obrigações financeiras, comum em empresas alavancadas (ex.: CYRE3). Monitoramento necessário.'
                    }
                elif 1.5 < cobertura <= 3:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '1.5 < Cobertura <= 3',
                        'descricao': 'Cobertura limitada indica capacidade moderada de cobrir juros, comum em indústrias (ex.: SUZB3). Análise de margens operacionais recomendada.'
                    }
                elif 3 < cobertura <= 5:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '3 < Cobertura <= 5',
                        'descricao': 'Cobertura adequada sugere equilíbrio financeiro, comum em consumo (ex.: ABEV3). Boa capacidade de gerenciar dívidas.'
                    }
                elif 5 < cobertura <= 10:
                    return {
                        'classificacao': 'Otimo',
                        'faixa': '5 < Cobertura <= 10',
                        'descricao': 'Cobertura alta indica forte capacidade de cobrir juros, comum em tecnologia (ex.: TOTS3). Sinal de saúde financeira.'
                    }
                else:  # cobertura > 10
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'Cobertura > 10',
                        'descricao': 'Cobertura excepcional sugere eficiência financeira superior, comum em empresas líderes (ex.: WEGE3). Pode indicar subutilização de alavancagem.'
                    }
            except Exception as e:
                print(f"Erro inesperado tratamento : {e}")
                return {
                    'classificacao': 'Erro',
                    'faixa': 'N/A',
                    'descricao': f'Erro ao processar Cobertura de Juros: {str(e)}. Verifique se o valor fornecido é um número válido.'
                }

def evaluate_receita_ativo_circulante(rac):
            '''Avalia a Receita/Ativo Circulante com base em faixas definidas:
            - RAC < 0: Crítico (receita negativa, risco elevado)
            - 0 ≤ RAC ≤ 0.5: Péssimo (baixa eficiência)
            - 0.5 < RAC ≤ 1: Ruim (eficiência limitada)
            - 1 < RAC ≤ 2: Moderado (eficiência adequada)
            - 2 < RAC ≤ 4: Ótimo (alta eficiência)
            - RAC > 4: Fora da faixa (eficiência excepcional)'''
            definicao = 'indefinido'
            agrupador = 'indefinido'
            formula = 'indefinido'
            try:
                if rac < 0:
                    return {
                        'classificacao': 'Critico',
                        'faixa': 'RAC < 0',
                        'descricao': 'Receita/Ativo Circulante negativa indica receita negativa, sugerindo problemas operacionais graves (ex.: OI). Exige análise detalhada.'
                    }
                elif 0 <= rac <= 0.5:
                    return {
                        'classificacao': 'Pessimo',
                        'faixa': '0 <= RAC <= 0.5',
                        'descricao': 'RAC muito baixo sugere baixa eficiência no uso de ativos circulantes, comum em setores intensivos em capital (ex.: ENGI11).'
                    }
                elif 0.5 < rac <= 1:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '0.5 < RAC <= 1',
                        'descricao': 'RAC limitado indica eficiência moderada, comum em indústrias (ex.: GGBR4). Análise de ciclo operacional recomendada.'
                    }
                elif 1 < rac <= 2:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '1 < RAC <= 2',
                        'descricao': 'RAC adequado sugere equilíbrio na utilização de ativos circulantes, comum em consumo (ex.: ABEV3).'
                    }
                elif 2 < rac <= 4:
                    return {
                        'classificacao': 'Otimo',
                        'faixa': '2 < RAC <= 4',
                        'descricao': 'RAC alto indica alta eficiência, comum em varejo (ex.: MGLU3). Sinal de boa gestão de ativos.'
                    }
                else:  # rac > 4
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'RAC > 4',
                        'descricao': 'RAC excepcional sugere eficiência superior no uso de ativos circulantes, comum em tecnologia (ex.: TOTS3).'
                    }
            except Exception as e:
                print(f"Erro inesperado tratamento : {e}")
                return {
                    'classificacao': 'Erro',
                    'faixa': 'N/A',
                    'descricao': f'Erro ao processar Receita/Ativo Circulante: {str(e)}. Verifique se o valor fornecido é um número válido.'
                }

def evaluate_lucro_bruto_receita(lbr):
            '''Avalia o Lucro Bruto/Receita com base em faixas definidas:
            - LBR < 0: Crítico (lucro bruto negativo, risco elevado)
            - 0 ≤ LBR ≤ 0.1: Péssimo (margem muito baixa)
            - 0.1 < LBR ≤ 0.3: Ruim (margem limitada)
            - 0.3 < LBR ≤ 0.5: Moderado (margem adequada)
            - 0.5 < LBR ≤ 0.7: Ótimo (margem alta)
            - LBR > 0.7: Fora da faixa (margem excepcional)'''
            definicao = 'indefinido'
            agrupador = 'indefinido'
            formula = 'indefinido'
            try:
                if lbr < 0:
                    return {
                        'classificacao': 'Critico',
                        'faixa': 'LBR < 0',
                        'descricao': 'Lucro Bruto/Receita negativo indica prejuízo operacional, sugerindo ineficiência ou altos custos (ex.: OI).'
                    }
                elif 0 <= lbr <= 0.1:
                    return {
                        'classificacao': 'Pessimo',
                        'faixa': '0 <= LBR <= 0.1',
                        'descricao': 'LBR muito baixo sugere baixa lucratividade, comum em varejo de baixa margem (ex.: PCAR3).'
                    }
                elif 0.1 < lbr <= 0.3:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '0.1 < LBR <= 0.3',
                        'descricao': 'LBR limitado indica eficiência moderada, comum em indústrias (ex.: GGBR4).'
                    }
                elif 0.3 < lbr <= 0.5:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '0.3 < LBR <= 0.5',
                        'descricao': 'LBR adequado sugere equilíbrio operacional, comum em consumo (ex.: ABEV3).'
                    }
                elif 0.5 < lbr <= 0.7:
                    return {
                        'classificacao': 'Otimo',
                        'faixa': '0.5 < LBR <= 0.7',
                        'descricao': 'LBR alto indica forte lucratividade, comum em tecnologia (ex.: TOTS3).'
                    }
                else:  # lbr > 0.7
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'LBR > 0.7',
                        'descricao': 'LBR excepcional sugere eficiência superior, comum em empresas premium (ex.: WEGE3).'
                    }
            except Exception as e:
                print(f"Erro inesperado tratamento : {e}")
                return {
                    'classificacao': 'Erro',
                    'faixa': 'N/A',
                    'descricao': f'Erro ao processar Lucro Bruto/Receita: {str(e)}. Verifique se o valor fornecido é um número válido.'
                }

def evaluate_lucro_operacional_receita(lor):
            '''Avalia o Lucro Operacional/Receita com base em faixas definidas:
            - LOR < 0: Crítico (prejuízo operacional, risco elevado)
            - 0 ≤ LOR ≤ 0.05: Péssimo (margem muito baixa)
            - 0.05 < LOR ≤ 0.1: Ruim (margem limitada)
            - 0.1 < LOR ≤ 0.2: Moderado (margem adequada)
            - 0.2 < LOR ≤ 0.3: Ótimo (margem alta)
            - LOR > 0.3: Fora da faixa (margem excepcional)'''
            definicao = 'indefinido'
            agrupador = 'indefinido'
            formula = 'indefinido'

            try:
                if lor < 0:
                    return {
                        'classificacao': 'Critico',
                        'faixa': 'LOR < 0',
                        'descricao': 'Lucro Operacional/Receita negativo indica prejuízo operacional, sugerindo ineficiência grave (ex.: OI).'
                    }
                elif 0 <= lor <= 0.05:
                    return {
                        'classificacao': 'Pessimo',
                        'faixa': '0 <= LOR <= 0.05',
                        'descricao': 'LOR muito baixo sugere baixa lucratividade operacional, comum em varejo de baixa margem (ex.: PCAR3).'
                    }
                elif 0.05 < lor <= 0.1:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '0.05 < LOR <= 0.1',
                        'descricao': 'LOR limitado indica eficiência moderada, comum em indústrias (ex.: GGBR4).'
                    }
                elif 0.1 < lor <= 0.2:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '0.1 < LOR <= 0.2',
                        'descricao': 'LOR adequado sugere equilíbrio operacional, comum em consumo (ex.: ABEV3).'
                    }
                elif 0.2 < lor <= 0.3:
                    return {
                        'classificacao': 'Otimo',
                        'faixa': '0.2 < LOR <= 0.3',
                        'descricao': 'LOR alto indica forte lucratividade operacional, comum em tecnologia (ex.: TOTS3).'
                    }
                else:  # lor > 0.3
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'LOR > 0.3',
                        'descricao': 'LOR excepcional sugere eficiência superior, comum em empresas líderes (ex.: WEGE3).'
                    }
            except Exception as e:
                print(f"Erro inesperado tratamento : {e}")
                return {
                    'classificacao': 'Erro',
                    'faixa': 'N/A',
                    'descricao': f'Erro ao processar Lucro Operacional/Receita: {str(e)}. Verifique se o valor fornecido é um número válido.'
                }

def evaluate_ebitda_receita(ebitda_r):
            '''Avalia o EBITDA/Receita com base em faixas definidas:
            - EBITDA/R < 0: Crítico (EBITDA negativo, risco elevado)
            - 0 ≤ EBITDA/R ≤ 0.1: Péssimo (margem muito baixa)
            - 0.1 < EBITDA/R ≤ 0.2: Ruim (margem limitada)
            - 0.2 < EBITDA/R ≤ 0.4: Moderado (margem adequada)
            - 0.4 < EBITDA/R ≤ 0.6: Ótimo (margem alta)
            - EBITDA/R > 0.6: Fora da faixa (margem excepcional)'''
            definicao = 'indefinido'
            agrupador = 'indefinido'
            formula = 'indefinido'
            try:
                if ebitda_r < 0:
                    return {
                        'classificacao': 'Critico',
                        'faixa': 'EBITDA/R < 0',
                        'descricao': 'EBITDA/Receita negativo indica ineficiência operacional, comum em empresas em crise (ex.: OI).'
                    }
                elif 0 <= ebitda_r <= 0.1:
                    return {
                        'classificacao': 'Pessimo',
                        'faixa': '0 <= EBITDA/R <= 0.1',
                        'descricao': 'EBITDA/Receita muito baixo sugere baixa geração de caixa, comum em varejo de baixa margem (ex.: PCAR3).'
                    }
                elif 0.1 < ebitda_r <= 0.2:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '0.1 < EBITDA/R <= 0.2',
                        'descricao': 'EBITDA/Receita limitado indica eficiência moderada, comum em indústrias (ex.: GGBR4).'
                    }
                elif 0.2 < ebitda_r <= 0.4:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '0.2 < EBITDA/R <= 0.4',
                        'descricao': 'EBITDA/Receita adequado sugere equilíbrio operacional, comum em consumo (ex.: ABEV3).'
                    }
                elif 0.4 < ebitda_r <= 0.6:
                    return {
                        'classificacao': 'Otimo',
                        'faixa': '0.4 < EBITDA/R <= 0.6',
                        'descricao': 'EBITDA/Receita alto indica forte geração de caixa, comum em tecnologia (ex.: TOTS3).'
                    }
                else:  # ebitda_r > 0.6
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'EBITDA/R > 0.6',
                        'descricao': 'EBITDA/Receita excepcional sugere eficiência superior, comum em empresas líderes (ex.: WEGE3).'
                    }
            except Exception as e:
                print(f"Erro inesperado tratamento : {e}")
                return {
                    'classificacao': 'Erro',
                    'faixa': 'N/A',
                    'descricao': f'Erro ao processar EBITDA/Receita: {str(e)}. Verifique se o valor fornecido é um número válido.'
                }

def evaluate_preco_fcl(pfcl):
            '''Avalia o Preço/Fluxo de Caixa Livre com base em faixas definidas:
            - P/FCL < 0: Crítico (fluxo de caixa livre negativo, risco elevado)
            - 0 ≤ P/FCL ≤ 5: Ótimo (subvalorizado, oportunidade de compra)
            - 5 < P/FCL ≤ 10: Moderado (valuation justo)
            - 10 < P/FCL ≤ 15: Ruim (sobrevalorizado, cautela necessária)
            - 15 < P/FCL ≤ 20: Péssimo (muito caro, alto risco)
            - P/FCL > 20: Fora da faixa (extremamente sobrevalorizado)'''
            definicao = 'indefinido'
            agrupador = 'indefinido'
            formula = 'indefinido'
            try:
                if pfcl < 0:
                    return {
                        'classificacao': 'Critico',
                        'faixa': 'P/FCL < 0',
                        'descricao': 'P/FCL negativo indica fluxo de caixa livre negativo, sugerindo problemas financeiros graves (ex.: OI). Exige análise de fluxo de caixa.'
                    }
                elif 0 <= pfcl <= 5:
                    return {
                        'classificacao': 'Otimo',
                        'faixa': '0 <= P/FCL <= 5',
                        'descricao': 'P/FCL baixo sugere subvalorização, indicando oportunidade de compra, comum em setores cíclicos (ex.: VALE3).'
                    }
                elif 5 < pfcl <= 10:
                    return {
                        'classificacao': 'Moderado',
                        'faixa': '5 < P/FCL <= 10',
                        'descricao': 'P/FCL indica valuation justo, típico de empresas com geração de caixa estável (ex.: ABEV3).'
                    }
                elif 10 < pfcl <= 15:
                    return {
                        'classificacao': 'Ruim',
                        'faixa': '10 < P/FCL <= 15',
                        'descricao': 'P/FCL elevado sugere sobrevalorização moderada, comum em setores de crescimento (ex.: MGLU3).'
                    }
                elif 15 < pfcl <= 20:
                    return {
                        'classificacao': 'Pessimo',
                        'faixa': '15 < P/FCL <= 20',
                        'descricao': 'P/FCL muito alto indica ação cara, comum em tecnologia (ex.: TOTS3). Risco de correção.'
                    }
                else:  # pfcl > 20
                    return {
                        'classificacao': 'Fora da faixa',
                        'faixa': 'P/FCL > 20',
                        'descricao': 'P/FCL extremamente elevado sugere sobrevalorização severa, típica de empresas especulativas. Análise detalhada é essencial.'
                    }
            except Exception as e:
                print(f"Erro inesperado tratamento : {e}")
                return {
                    'classificacao': 'Erro',
                    'faixa': 'N/A',
                    'descricao': f'Erro ao processar Preço/Fluxo de Caixa Livre: {str(e)}. Verifique se o valor fornecido é um número válido.'
                }
def evaluate_valor_atual(valor_atual, vpa=None):
    '''Avalia o Valor Atual (preço da ação) em relação ao Valor Patrimonial por Ação (VPA):
    - Valor Atual < 0: Crítico
    - 0 ≤ Valor Atual/VPA ≤ 0.5: Ótimo
    - 0.5 < Valor Atual/VPA ≤ 1.0: Moderado
    - 1.0 < Valor Atual/VPA ≤ 1.5: Ruim
    - 1.5 < Valor Atual/VPA ≤ 2.0: Péssimo
    - Valor Atual/VPA > 2.0: Fora da faixa
    - Se VPA não fornecido, considera apenas Valor Atual absoluto'''
    try:
        if valor_atual < 0:
            return {'classificacao': 'Critico',
                    'faixa': 'Valor Atual < 0',
                    'descricao': 'Preço da ação negativo, erro nos dados.'}
        if vpa is None or vpa <= 0:
            # Avaliação apenas pelo preço absoluto (faixas em R$)
            if 0 <= valor_atual <= 5:
                return {'classificacao': 'Baixo',
                        'faixa': '0 <= Valor Atual <= 5',
                        'descricao': 'Preço muito baixo, típico de small caps ou empresas em dificuldade (ex.: OI).'}
            elif 5 < valor_atual <= 20:
                return {'classificacao': 'Moderado',
                        'faixa': '5 < Valor Atual <= 20',
                        'descricao': 'Preço comum em mid caps (ex.: ENGI11).'}
            elif 20 < valor_atual <= 50:
                return {'classificacao': 'Alto',
                        'faixa': '20 < Valor Atual <= 50',
                        'descricao': 'Preço típico de large caps (ex.: ITUB4).'}
            else:
                return {'classificacao': 'Muito Alto',
                        'faixa': 'Valor Atual > 50',
                        'descricao': 'Preço elevado, comum em blue chips ou empresas de alto crescimento (ex.: WEGE3).'}
        else:
            # Avaliação em relação ao VPA
            valor_vpa = valor_atual / vpa
            if 0 <= valor_vpa <= 0.5:
                return {'classificacao': 'Otimo',
                        'faixa': '0 <= Valor Atual/VPA <= 0.5',
                        'descricao': 'Ação muito subvalorizada em relação ao patrimônio (ex.: SANB11).'}
            elif 0.5 < valor_vpa <= 1.0:
                return {'classificacao': 'Moderado',
                        'faixa': '0.5 < Valor Atual/VPA <= 1.0',
                        'descricao': 'Valuation justo em relação ao VPA (ex.: ABEV3).'}
            elif 1.0 < valor_vpa <= 1.5:
                return {'classificacao': 'Ruim',
                        'faixa': '1.0 < Valor Atual/VPA <= 1.5',
                        'descricao': 'Ação ligeiramente sobrevalorizada (ex.: MGLU3).'}
            elif 1.5 < valor_vpa <= 2.0:
                return {'classificacao': 'Pessimo',
                        'faixa': '1.5 < Valor Atual/VPA <= 2.0',
                        'descricao': 'Ação significativamente cara (ex.: TOTS3).'}
            else:
                return {'classificacao': 'Fora da faixa',
                        'faixa': 'Valor Atual/VPA > 2.0', 'descricao': 'Sobrevalorização severa em relação ao VPA (ex.: WEGE3).'}
    except Exception as e:
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar Valor Atual: {str(e)}.'}

def evaluate_liquidez_media_diaria(liquidez):
    '''Avalia a Liquidez Média Diária (em R$ milhões):
    - Liquidez < 0: Crítico
    - 0 ≤ Liquidez ≤ 0.5: Péssimo
    - 0.5 < Liquidez ≤ 5: Ruim
    - 5 < Liquidez ≤ 20: Moderado
    - 20 < Liquidez ≤ 100: Ótimo
    - Liquidez > 100: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para milhões).'''
    definicao = 'indefinido'
    agrupador = 'indefinido'
    formula = 'indefinido'
    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(liquidez, str):
            # Remove "R$" e espaços
            liquidez = liquidez.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            liquidez = liquidez.replace('.', '').replace(',', '.')
            liquidez = float(liquidez) / 1_000_000  # Converte para milhões
        else:
            # Garante que é float
            liquidez = float(liquidez) / 1_000_000 if liquidez >= 1_000_000 else float(liquidez)

        if liquidez < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'Liquidez < 0',
                'descricao': 'Liquidez média diária negativa, erro nos dados.'
            }
        elif 0 <= liquidez <= 0.5:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0 <= Liquidez <= 0.5',
                'descricao': 'Liquidez muito baixa, ação ilíquida, risco elevado (ex.: small caps pouco negociadas).'
            }
        elif 0.5 < liquidez <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < Liquidez <= 5',
                'descricao': 'Liquidez limitada, comum em small caps (ex.: ENAT3).'
            }
        elif 5 < liquidez <= 20:
            return {
                'classificacao': 'Moderado',
                'faixa': '5 < Liquidez <= 20',
                'descricao': 'Liquidez adequada, típica de mid caps (ex.: ABEV3).'
            }
        elif 20 < liquidez <= 100:
            return {
                'classificacao': 'Otimo',
                'faixa': '20 < Liquidez <= 100',
                'descricao': 'Liquidez robusta, comum em large caps (ex.: ITUB4).'
            }
        else:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Liquidez > 100',
                'descricao': 'Liquidez excepcional, típica de blue chips (ex.: VALE3).'
            }
    except Exception as e:
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Liquidez Média Diária: {str(e)}. Verifique se o valor é um número válido ou no formato R$ XXX.XXX.XXX.'
        }

def evaluate_patrimonio_liquido(pl):
    '''Avalia o Patrimônio Líquido (em R$ bilhões):
    - PL < 0: Crítico
    - 0 ≤ PL ≤ 0.5: Péssimo
    - 0.5 < PL ≤ 2: Ruim
    - 2 < PL ≤ 10: Moderado
    - 10 < PL ≤ 50: Ótimo
    - PL > 50: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).'''
    definicao = 'indefinido'
    agrupador = 'indefinido'
    formula = 'indefinido'
    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(pl, str):
            # Remove "R$" e espaços
            pl = pl.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            pl = pl.replace('.', '').replace(',', '.')
            pl = float(pl) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            pl = float(pl) / 1_000_000_000 if pl >= 1_000_000 else float(pl)

        if pl < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'PL < 0',
                'descricao': 'Patrimônio líquido negativo, alto risco financeiro (ex.: OI).'
            }
        elif 0 <= pl <= 0.5:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0 <= PL <= 0.5',
                'descricao': 'Patrimônio muito baixo, típico de small caps (ex.: ENAT3).'
            }
        elif 0.5 < pl <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.5 < PL <= 2',
                'descricao': 'Patrimônio limitado, comum em empresas menores (ex.: CYRE3).'
            }
        elif 2 < pl <= 10:
            return {
                'classificacao': 'Moderado',
                'faixa': '2 < PL <= 10',
                'descricao': 'Patrimônio sólido, típico de mid caps (ex.: ABEV3).'
            }
        elif 10 < pl <= 50:
            return {
                'classificacao': 'Otimo',
                'faixa': '10 < PL <= 50',
                'descricao': 'Patrimônio robusto, comum em large caps (ex.: ITUB4).'
            }
        else:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'PL > 50',
                'descricao': 'Patrimônio excepcional, típico de blue chips (ex.: VALE3).'
            }
    except Exception as e:
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Patrimônio Líquido: {str(e)}. Verifique se o valor é um número válido ou no formato R$ XXX.XXX.XXX.'
        }

def evaluate_ativos(ativos):
    '''Avalia os Ativos Totais (em R$ bilhões):
    - Ativos < 0: Crítico
    - 0 ≤ Ativos ≤ 1: Péssimo
    - 1 < Ativos ≤ 5: Ruim
    - 5 < Ativos ≤ 20: Moderado
    - 20 < Ativos ≤ 100: Ótimo
    - Ativos > 100: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).'''
    definicao = 'indefinido'
    agrupador = 'indefinido'
    formula = 'indefinido'
    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(ativos, str):
            # Remove "R$" e espaços
            ativos = ativos.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            ativos = ativos.replace('.', '').replace(',', '.')
            ativos = float(ativos) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            ativos = float(ativos) / 1_000_000_000 if ativos >= 1_000_000 else float(ativos)

        if ativos < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'Ativos < 0',
                'descricao': 'Ativos negativos, erro nos dados.'
            }
        elif 0 <= ativos <= 1:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0 <= Ativos <= 1',
                'descricao': 'Ativos muito baixos, típico de small caps (ex.: ENAT3).'
            }
        elif 1 < ativos <= 5:
            return {
                'classificacao': 'Ruim',
                'faixa': '1 < Ativos <= 5',
                'descricao': 'Ativos limitados, comum em empresas menores (ex.: CYRE3).'
            }
        elif 5 < ativos <= 20:
            return {
                'classificacao': 'Moderado',
                'faixa': '5 < Ativos <= 20',
                'descricao': 'Ativos sólidos, típico de mid caps (ex.: ABEV3).'
            }
        elif 20 < ativos <= 100:
            return {
                'classificacao': 'Otimo',
                'faixa': '20 < Ativos <= 100',
                'descricao': 'Ativos robustos, comum em large caps (ex.: ITUB4).'
            }
        else:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Ativos > 100',
                'descricao': 'Ativos excepcionais, típico de blue chips (ex.: VALE3).'
            }
    except Exception as e:
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Ativos: {str(e)}. Verifique se o valor é um número válido ou no formato R$ XXX.XXX.XXX.'
        }

def evaluate_ativo_circulante(ativo_circulante):
    '''Avalia o Ativo Circulante (em R$ bilhões):
    - Ativo Circulante < 0: Crítico
    - 0 ≤ Ativo Circulante ≤ 0.2: Péssimo
    - 0.2 < Ativo Circulante ≤ 1: Ruim
    - 1 < Ativo Circulante ≤ 5: Moderado
    - 5 < Ativo Circulante ≤ 20: Ótimo
    - Ativo Circulante > 20: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).'''
    definicao = 'indefinido'
    agrupador = 'indefinido'
    formula = 'indefinido'
    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(ativo_circulante, str):
            # Remove "R$" e espaços
            ativo_circulante = ativo_circulante.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            ativo_circulante = ativo_circulante.replace('.', '').replace(',', '.')
            ativo_circulante = float(ativo_circulante) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            ativo_circulante = float(ativo_circulante) / 1_000_000_000 if ativo_circulante >= 1_000_000 else float(ativo_circulante)

        if ativo_circulante < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'Ativo Circulante < 0',
                'descricao': 'Ativo circulante negativo, erro nos dados.'
            }
        elif 0 <= ativo_circulante <= 0.2:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0 <= Ativo Circulante <= 0.2',
                'descricao': 'Ativo circulante muito baixo, risco de liquidez (ex.: OI).'
            }
        elif 0.2 < ativo_circulante <= 1:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.2 < Ativo Circulante <= 1',
                'descricao': 'Ativo circulante limitado, comum em small caps (ex.: ENAT3).'
            }
        elif 1 < ativo_circulante <= 5:
            return {
                'classificacao': 'Moderado',
                'faixa': '1 < Ativo Circulante <= 5',
                'descricao': 'Ativo circulante adequado, típico de mid caps (ex.: ABEV3).'
            }
        elif 5 < ativo_circulante <= 20:
            return {
                'classificacao': 'Otimo',
                'faixa': '5 < Ativo Circulante <= 20',
                'descricao': 'Ativo circulante robusto, comum em large caps (ex.: ITUB4).'
            }
        else:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Ativo Circulante > 20',
                'descricao': 'Ativo circulante excepcional, típico de blue chips (ex.: VALE3).'
            }
    except Exception as e:
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Ativo Circulante: {str(e)}. Verifique se o valor é um número válido ou no formato R$ XXX.XXX.XXX.'
        }

def evaluate_divida_bruta(divida_bruta):
    '''Avalia a Dívida Bruta (em R$ bilhões):
    - Dívida Bruta < 0: Crítico
    - 0 ≤ Dívida Bruta ≤ 0.5: Ótimo
    - 0.5 < Dívida Bruta ≤ 2: Moderado
    - 2 < Dívida Bruta ≤ 10: Ruim
    - 10 < Dívida Bruta ≤ 20: Péssimo
    - Dívida Bruta > 20: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).'''
    definicao = 'indefinido'
    agrupador = 'indefinido'
    formula = 'indefinido'
    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(divida_bruta, str):
            # Remove "R$" e espaços
            divida_bruta = divida_bruta.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            divida_bruta = divida_bruta.replace('.', '').replace(',', '.')
            divida_bruta = float(divida_bruta) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            divida_bruta = float(divida_bruta) / 1_000_000_000 if divida_bruta >= 1_000_000 else float(divida_bruta)

        if divida_bruta < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'Dívida Bruta < 0',
                'descricao': 'Dívida bruta negativa, erro nos dados.'
            }
        elif 0 <= divida_bruta <= 0.5:
            return {
                'classificacao': 'Otimo',
                'faixa': '0 <= Dívida Bruta <= 0.5',
                'descricao': 'Dívida bruta muito baixa, baixo risco financeiro (ex.: TOTS3).'
            }
        elif 0.5 < divida_bruta <= 2:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.5 < Dívida Bruta <= 2',
                'descricao': 'Dívida bruta controlada, típica de mid caps (ex.: ABEV3).'
            }
        elif 2 < divida_bruta <= 10:
            return {
                'classificacao': 'Ruim',
                'faixa': '2 < Dívida Bruta <= 10',
                'descricao': 'Dívida bruta moderada, exige atenção (ex.: SUZB3).'
            }
        elif 10 < divida_bruta <= 20:
            return {
                'classificacao': 'Pessimo',
                'faixa': '10 < Dívida Bruta <= 20',
                'descricao': 'Dívida bruta alta, risco elevado (ex.: ENGI11).'
            }
        else:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Bruta > 20',
                'descricao': 'Dívida bruta excessiva, típico de empresas alavancadas (ex.: VALE3).'
            }
    except Exception as e:
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Dívida Bruta: {str(e)}. Verifique se o valor é um número válido ou no formato R$ XXX.XXX.XXX.'
        }

def evaluate_disponibilidade(disponibilidade):
    '''Avalia a Disponibilidade (caixa e equivalentes, em R$ bilhões):
    - Disponibilidade < 0: Crítico
    - 0 ≤ Disponibilidade ≤ 0.05: Péssimo
    - 0.05 < Disponibilidade ≤ 0.2: Ruim
    - 0.2 < Disponibilidade ≤ 1: Moderado
    - 1 < Disponibilidade ≤ 10: Ótimo
    - Disponibilidade > 10: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).'''
    definicao = 'indefinido'
    agrupador = 'indefinido'
    formula = 'indefinido'
    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(disponibilidade, str):
            # Remove "R$" e espaços
            disponibilidade = disponibilidade.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            disponibilidade = disponibilidade.replace('.', '').replace(',', '.')
            disponibilidade = float(disponibilidade) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            disponibilidade = float(disponibilidade) / 1_000_000_000 if disponibilidade >= 1_000_000 else float(disponibilidade)

        if disponibilidade < 0:
            return {
                'classificacao': 'Critico',
                'faixa': 'Disponibilidade < 0',
                'descricao': 'Disponibilidade negativa, erro nos dados.'
            }
        elif 0 <= disponibilidade <= 0.05:
            return {
                'classificacao': 'Pessimo',
                'faixa': '0 <= Disponibilidade <= 0.05',
                'descricao': 'Caixa muito baixo, alto risco de liquidez (ex.: empresas em crise como OI).'
            }
        elif 0.05 < disponibilidade <= 0.2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0.05 < Disponibilidade <= 0.2',
                'descricao': 'Caixa limitado, comum em small caps (ex.: ENAT3).'
            }
        elif 0.2 < disponibilidade <= 1:
            return {
                'classificacao': 'Moderado',
                'faixa': '0.2 < Disponibilidade <= 1',
                'descricao': 'Caixa adequado, típico de mid caps (ex.: ABEV3).'
            }
        elif 1 < disponibilidade <= 10:
            return {
                'classificacao': 'Otimo',
                'faixa': '1 < Disponibilidade <= 10',
                'descricao': 'Caixa robusto, comum em large caps (ex.: ITUB4).'
            }
        else:
            return {
                'classificacao': 'Otimo',
                'faixa': 'Disponibilidade > 10',
                'descricao': 'Caixa excepcional, típico de blue chips (ex.: VALE3).'
            }
    except Exception as e:
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Disponibilidade: {str(e)}. Verifique se o valor é um número válido ou no formato R$ XXX.XXX.XXX.'
        }


def evaluate_divida_liquida(divida_liquida):
    '''Avalia a Dívida Líquida (em R$ bilhões):
    - Dívida Líquida ≤ -0.5: Ótimo
    - -0.5 < Dívida Líquida ≤ 0: Moderado
    - 0 < Dívida Líquida ≤ 2: Ruim
    - 2 < Dívida Líquida ≤ 10: Péssimo
    - Dívida Líquida > 10: Fora da faixa
    Aceita valores no formato R$ 112.714.000 (converte para bilhões).'''
    definicao = 'indefinido'
    agrupador = 'indefinido'
    formula = 'indefinido'
    try:
        # Se for string, processar formato monetário brasileiro
        if isinstance(divida_liquida, str):
            # Remove "R$" e espaços
            divida_liquida = divida_liquida.replace('R$', '').replace(' ', '')
            # Substitui ponto (milhares) e vírgula (decimal)
            divida_liquida = divida_liquida.replace('.', '').replace(',', '.')
            divida_liquida = float(divida_liquida) / 1_000_000_000  # Converte para bilhões
        else:
            # Garante que é float
            divida_liquida = float(divida_liquida) / 1_000_000_000 if abs(divida_liquida) >= 1_000_000 else float(divida_liquida)

        if divida_liquida <= -0.5:
            return {
                'classificacao': 'Otimo',
                'faixa': 'Dívida Líquida <= -0.5',
                'descricao': 'Dívida líquida negativa (caixa líquido), excelente saúde financeira (ex.: TOTS3).'
            }
        elif -0.5 < divida_liquida <= 0:
            return {
                'classificacao': 'Moderado',
                'faixa': '-0.5 < Dívida Líquida <= 0',
                'descricao': 'Dívida líquida próxima de zero, situação equilibrada (ex.: ABEV3).'
            }
        elif 0 < divida_liquida <= 2:
            return {
                'classificacao': 'Ruim',
                'faixa': '0 < Dívida Líquida <= 2',
                'descricao': 'Dívida líquida moderada, exige atenção (ex.: CYRE3).'
            }
        elif 2 < divida_liquida <= 10:
            return {
                'classificacao': 'Pessimo',
                'faixa': '2 < Dívida Líquida <= 10',
                'descricao': 'Dívida líquida alta, risco elevado (ex.: SUZB3).'
            }
        else:
            return {
                'classificacao': 'Fora da faixa',
                'faixa': 'Dívida Líquida > 10',
                'descricao': 'Dívida líquida excessiva, alto risco financeiro (ex.: VALE3).'
            }
    except Exception as e:
        return {
            'classificacao': 'Erro',
            'faixa': 'N/A',
            'descricao': f'Erro ao processar Dívida Líquida: {str(e)}. Verifique se o valor é um número válido ou no formato R$ XXX.XXX.XXX.'
        }


def evaluate_valor_mercado(valor_mercado):
    '''Avalia o Valor de Mercado (em R$ bilhões):
    - Valor Mercado < 0: Crítico
    - 0 ≤ Valor Mercado ≤ 1: Péssimo
    - 1 < Valor Mercado ≤ 5: Ruim
    - 5 < Valor Mercado ≤ 20: Moderado
    - 20 < Valor Mercado ≤ 100: Ótimo
    - Valor Mercado > 100: Fora da faixa'''
    definicao = 'indefinido'
    agrupador = 'indefinido'
    formula = 'indefinido'
    try:
        if valor_mercado < 0:
            return {'classificacao': 'Critico', 'faixa': 'Valor Mercado < 0', 'descricao': 'Valor de mercado negativo, erro nos dados.'}
        elif 0 <= valor_mercado <= 1:
            return {'classificacao': 'Pessimo', 'faixa': '0 <= Valor Mercado <= 1', 'descricao': 'Valor de mercado muito baixo, típico de small caps (ex.: ENAT3).'}
        elif 1 < valor_mercado <= 5:
            return {'classificacao': 'Ruim', 'faixa': '1 < Valor Mercado <= 5', 'descricao': 'Valor de mercado limitado, comum em small caps (ex.: CYRE3).'}
        elif 5 < valor_mercado <= 20:
            return {'classificacao': 'Moderado', 'faixa': '5 < Valor Mercado <= 20', 'descricao': 'Valor de mercado sólido, típico de mid caps (ex.: ABEV3).'}
        elif 20 < valor_mercado <= 100:
            return {'classificacao': 'Otimo', 'faixa': '20 < Valor Mercado <= 100', 'descricao': 'Valor de mercado robusto, comum em large caps (ex.: ITUB4).'}
        else:
            return {'classificacao': 'Fora da faixa', 'faixa': 'Valor Mercado > 100', 'descricao': 'Valor de mercado excepcional, típico de blue chips (ex.: VALE3).'}
    except Exception as e:
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar Valor de Mercado: {str(e)}.'}

def evaluate_valor_firma(valor_firma):
    '''Avalia o Valor de Firma (em R$ bilhões):
    - Valor Firma < 0: Crítico
    - 0 ≤ Valor Firma ≤ 2: Péssimo
    - 2 < Valor Firma ≤ 10: Ruim
    - 10 < Valor Firma ≤ 50: Moderado
    - 50 < Valor Firma ≤ 150: Ótimo
    - Valor Firma > 150: Fora da faixa'''
    try:
        if valor_firma < 0:
            return {'classificacao': 'Critico', 'faixa': 'Valor Firma < 0', 'descricao': 'Valor de firma negativo, erro nos dados.'}
        elif 0 <= valor_firma <= 2:
            return {'classificacao': 'Pessimo', 'faixa': '0 <= Valor Firma <= 2', 'descricao': 'Valor de firma muito baixo, típico de small caps (ex.: ENAT3).'}
        elif 2 < valor_firma <= 10:
            return {'classificacao': 'Ruim', 'faixa': '2 < Valor Firma <= 10', 'descricao': 'Valor de firma limitado, comum em small caps (ex.: CYRE3).'}
        elif 10 < valor_firma <= 50:
            return {'classificacao': 'Moderado', 'faixa': '10 < Valor Firma <= 50', 'descricao': 'Valor de firma sólido, típico de mid caps (ex.: ABEV3).'}
        elif 50 < valor_firma <= 150:
            return {'classificacao': 'Otimo', 'faixa': '50 < Valor Firma <= 150', 'descricao': 'Valor de firma robusto, comum em large caps (ex.: ITUB4).'}
        else:
            return {'classificacao': 'Fora da faixa', 'faixa': 'Valor Firma > 150', 'descricao': 'Valor de firma excepcional, típico de blue chips (ex.: VALE3).'}
    except Exception as e:
        return {'classificacao': 'Erro', 'faixa': 'N/A', 'descricao': f'Erro ao processar Valor de Firma: {str(e)}.'}

