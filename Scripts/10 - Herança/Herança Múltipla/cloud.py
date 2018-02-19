#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#cloud.py

from servidor import Servidor
from acesso import Acesso

class Cloud(Servidor,Acesso):
	def __init__(self):
		self.memoria = 512
		self.cpu = 1
		self.disco = 50

dns = Cloud()
dns.acessarConsole()
