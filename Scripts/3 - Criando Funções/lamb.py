#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  O uso do lambda é excelente para
  calcular operações matemáticas. 
  Um típico exemplo é o uso na 
  black friday, onde os preços 
  são diminuidos. 


  Modificado em 09 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  melhor exemplo: http://turing.com.br/pydoc/2.7/tutorial/controlflow.html#construcoes-lambda
"""

carrinho = []

produto1 = {"nome":"Tenis","valor":21.32}

black_friday = lambda x: x*2 

print ("Valor do produto:",black_friday(produto1["valor"]))
print ("Com desconto de 50%",produto1["valor"])

















