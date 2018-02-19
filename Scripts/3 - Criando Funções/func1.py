#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Um função com um parâmetro
  opcional, seria o cálculo de
  uma compra com o uso de 
  um cupom de desconto


  Modificado em 09 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

carrinho = []

produto1 = {"nome":"tenis","valor":21.32}
produto2 = {"nome":"meia","valor":31.32}
produto3 = {"nome":"camiseta","valor":31.32}
produto4 = {"nome":"shorts","valor":41.32}


carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)
carrinho.append(produto4)

def totalCarrinho(carrinho):
	return sum(produto["valor"] for produto in carrinho)

def cupomDesconto(cupom=""):
	if cupom == "gratis":
		return 0.70 # Desconto de 30% é calculado
	else:
		return 1

print "o total de sua compra é de: ", (totalCarrinho(carrinho)
	  *cupomDesconto())
print "usando o cupom gratis seu valor será de: ",(totalCarrinho(carrinho)*cupomDesconto("gratis")),"30% menos!"



















