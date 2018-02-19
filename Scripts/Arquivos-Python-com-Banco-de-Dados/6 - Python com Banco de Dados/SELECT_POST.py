#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Nesse arquivo, usamos os comandos
  fetchone e fatchall 


  Modificado em 27 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

try:
	import psycopg2
except:
    sys.exit("[!] Por favor, intale a biblioteca psycopg2 com o comando: sudo apt-get install python-psycopg2")

try:
	con = psycopg2.connect("host=127.0.0.1 dbname=projeto user=admin password=123456") 
	cur = con.cursor()
	cur.execute("select * from cliente")
	print "Primeiro registro ",cur.fetchone()
	print "Todos os registros ",cur.fetchall()
except Exception as e:
	print "Erro: %s"%e
finally:
	print "Finalizando a conexão com o banco de dados"
	cur.close
	con.close



















