#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  O registro usando o DML, ficará ravado na 
  memória ate que seja executado o comando
  commit, caso contrário não será gravado. 


  Modificado em 22 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

try:
	import psycopg2
except:
    sys.exit("[!] Por favor, intale a biblioteca psycopg2 com o comando: sudo apt-get install python-psycopg2")

try:
	con = psycopg2.connect("host=127.0.0.1 dbname=projeto user=admin password=123456") 
	cur = con.cursor()
	cur.execute("insert into cliente(id,nome,cpf) values(1, 'vitor','333.333.222.555')")
	con.commit()
	print "Registro criado com sucesso"
except Exception as e:
	print "Erro: %s"%e
	print "Fazendo o rollback"
	con.rollback()
finally:
	print "Finalizando a conexão com o banco de dados"
	cur.close
	con.close



















