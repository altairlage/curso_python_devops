#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# servidor.py

class Servidor:
	
	def contratarMemoria(self,memoria):
		self.memoria += memoria

	def contratarCpu(self,cpu):
		self.cpu += cpu

	def contratarDisco(self,disco):
		self.disco += disco
