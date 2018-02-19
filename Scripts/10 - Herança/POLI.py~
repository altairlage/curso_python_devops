#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#POLI.py

"""
  Usando o conceito de
  polimosrfismo 


  Modificado em 07 de abril de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importamos a outra classe do arquivo HERA.py
from HERA import Servidor

class Fisico(Servidor):
	def __init__(self):
		self.memoria = 4096
		self.cpu = 4
		self.disco = 1024
		self.total_slots = 4
		self.slots_ocupados = 1

	def contratatDisco(self,disco):
		if disco == 500 or disco == 1024:
			if self.total_slots > self.slots_ocupados:
				self.slots_ocupados += 1
				self.disco += disco
			else:
				print "Você não possui mais slots disponíveis"
				print "Total de Slots ",self.total_slots
				print "Total Ocupados",self.slots_ocupados
		else:
			print "Tamanho de disco não é válido"

dns = Fisico()

print "Memória Inicial",dns.memoria
print "Disco Inicial",dns.disco
print "CPU Inicial",dns.cpu 

dns.contratarDisco(1024) # 1 
dns.contratarDisco(1024) # 2
dns.contratarDisco(1024) # 3
dns.contratarDisco(1024) # 4

print "Disco total ",dns.disco



























