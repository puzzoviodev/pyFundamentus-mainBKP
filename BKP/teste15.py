evaluate_pl(PL) # P/L
evaluate_pebitda(pebitda) #P/EBITDA
evaluate_pvp(pvp) #P/VP
evaluate_pebit(pebit) #P/EBIT
evaluate_evebitda(evebitda) #  EV/EBITDA
evaluate_evebit(evebit) # EV/EBIT
evaluate_giro_ativos(giro) # 'Giro ativos'
evaluate_divida_liquida_pl(dl_pl) #Div. liquida/PL
evaluate_divida_liquida_ebitda(dl_ebitda) #Div. liquida/EBITDA
evaluate_divida_liquida_ebit(dl_ebit) # Div. liquida/EBIT
evaluate_pl_ativos(pl_ativos) #PL/Ativos
evaluate_passivos_ativos(passivos_ativos) # Passivos/Ativos
evaluate_liquidez_corrente(lc) # Liq. corrente
evaluate_peg_ratio(peg) # PEG Ratio
evaluate_p_ativo(p_ativo) # P/Ativo
evaluate_vpa(vpa_preco) #VPA
evaluate_lpa(lpa) # LPA
evaluate_psr(psr) #P/SR
evaluate_p_ativo_circ_liq(p_acl) # P/Ativo Circ. Liq
evaluate_cobertura_juros(cobertura)
evaluate_receita_ativo_circulante(rac)
evaluate_lucro_bruto_receita(lbr)
evaluate_lucro_operacional_receita(lor)
evaluate_ebitda_receita(ebitda_r)
evaluate_preco_fcl(pfcl)


MetricasStatus = {, '','','','',
                           '','','','','','','',
                            '','','','','',
                            '','.','Valor atual','LIQUIDEZ MEDIA DIARIA','Patrimonio liquido',
                             'Ativos','Ativo circulante','Divida bruta','Disponibilidade',
                             'Divida liquida','Valor de mercado','Valor de firma'}


resultado = analisefundamentalista.evaluate_pl(valor_pl)

resultado = analisefundamentalista.evaluate_pl(valor_pl)
                faixa1 = resultado['faixa']
                descricao1 = resultado['descricao']
                print("func1" + faixa1)
                print("func2" + descricao1)

               # categoria_pl = categorizar_valor(metrica, (valor_pl))
                if metrica == 'P/L':
                   categoria_pl = evaluate_pl(valor_pl)
                if metrica == 'P/VP':
if metrica == 'P/L':
   analisefundamentalista.evaluate_pl(PL) # P/L
if metriaca ==  'P/EBITDA':
   analisefundamentalista.evaluate_pebitda(pebitda) #P/EBITDA
if metriaca == 'P/VP':
    evaluate_pvp(pvp) #P/VP
if metriaca == 'P/EBIT':
    analisefundamentalista.evaluate_pebit(pebit) #P/EBIT
if metriaca == 'P/EBIT':
    analisefundamentalista.evaluate_evebitda(evebitda) #  EV/EBITDA
if metriaca == 'EV/EBIT':
    analisefundamentalista.evaluate_evebit(evebit) # EV/EBIT
if metriaca == 'Giro ativos':
    analisefundamentalista.evaluate_giro_ativos(giro) # 'Giro ativos'
if metriaca == 'Div. liquida/PL':
    analisefundamentalista.evaluate_divida_liquida_pl(dl_pl) #Div. liquida/PL
if metriaca == 'Div. liquida/EBITDA':
    analisefundamentalista.evaluate_divida_liquida_ebitda(dl_ebitda) #Div. liquida/EBITDA
if metriaca == 'Div. liquida/EBIT':
    analisefundamentalista.evaluate_divida_liquida_ebit(dl_ebit) # Div. liquida/EBIT
if metriaca == 'PL/Ativos':
    analisefundamentalista.evaluate_pl_ativos(pl_ativos) #PL/Ativos
if metriaca == 'PL/Ativos':
    analisefundamentalista.analisefundamentalista.evaluate_passivos_ativos(passivos_ativos) # Passivos/Ativos
if metriaca == 'Liq. corrente':
    analisefundamentalista.evaluate_liquidez_corrente(lc) # Liq. corrente
if metriaca == 'PEG Ratio':
    analisefundamentalista.evaluate_peg_ratio(peg) # PEG Ratio
if metriaca == 'P/Ativo':
    analisefundamentalista.evaluate_p_ativo(p_ativo) # P/Ativo
if metriaca == 'VPA':
    analisefundamentalista.evaluate_vpa(vpa_preco) #VPA
if metriaca == 'LPA':
    analisefundamentalista.evaluate_lpa(lpa) # LPA
if metriaca == 'P/SR':
    analisefundamentalista.evaluate_psr(psr) #P/SR
if metriaca == 'P/Ativo Circ. Liq':
    analisefundamentalista.evaluate_p_ativo_circ_liq(p_acl) # P/Ativo Circ. Liq

    resultado = analisefundamentalista.evaluate_disponibilidade(valor_pl)
    print("faixa " + faixa)
    print("descricao " + descricao)
    print("classificacao " + classificacao)