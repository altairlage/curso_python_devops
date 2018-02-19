#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#HERA.py

"""
  Usando o conceito de
  herança com uso de 
  classes

  Modificado em 07 de abril de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Classe "Pai"
class Servidor:
	
	def contratarMemoria(self,memoria):
		self.memoria += memoria

	def contratarCpu(self,cpu):
		self.cpu += cpu

	def contratarDisco(self,disco):
		self.disco += disco

# Classe "Filha"
class Cloud(Servidor):
	def __init__(self):
		self.memoria = 512
		self.cpu = 1
		self.disco = 50

dns = Cloud()

print "Memória Inicial",dns.memoria
print "Disco Inicial",dns.disco
print "CPU Inicial",dns.cpu

dns.contratarDisco(50)

# Classe "Filha"
class Fisico(Servidor):
	def __init__(self):
		self.memoria = 4096
		self.cpu = 4
		self.disco = 1024

dns = Fisico()

print "Memória Inicial",dns.memoria
print "Disco Inicial",dns.disco
print "CPU Inicial",dns.cpu

dns.contratarDisco(1024)

print "Disco total ",dns.disco





