#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  O registro usando o DML, ficará ravado na 
  memória ate que seja executado o comando
  commit, caso contrário não será gravado. 
"""
import sys

try:
	import psycopg2
except:
    sys.exitfunc("[!] Por favor, intale a biblioteca psycopg2 com o comando: sudo apt-get install python-psycopg2")

try:
	con = psycopg2.connect("host=10.25.26.245 dbname=projeto user=admin password=123456") 
	cur = con.cursor()
	cur.execute("insert into cliente(id,nome,cpf) values(1, 'vitor','333.333.222.555')")
	con.commit()
	print ("Registro criado com sucesso")
except Exception as e:
	print ("Erro: %s"%e)
	print ("Fazendo o rollback")
	con.rollback()
finally:
	print ("Finalizando a conexão com o banco de dados")
	cur.close
	con.close
















