#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  O uso do Try...Except serve para 
  lidar com o tratamento de
  exceções. O Try é utilizado quando
  não se quer executar um
  programa, caso haja um erro, ou seja,
  muito usado para verificar
  bugs do sistema. 


  Modificado em 09 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  http://turing.com.br/pydoc/2.7/tutorial/errors.html#excecoes
"""

try:
	with open("teste.txt",'r') as f:
		print (f.readline())
except Exception as e:
	print ("Erro %s"%e)



















