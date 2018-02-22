#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# INSERT_MY.py

"""
  Nesse arquivo, vamos fazer um teste de
  conexão ao banco de dados 
  do MySQL.
"""

try:
	import MySQLdb
except:
    sys.exitfunc("[!] Por favor, intale a biblioteca mysqldb com o comando: sudo apt-get install python-mysqldb")

try:
	con = MySQLdb.connect(host="10.25.26.245", user="root", db="projeto", passwd="123456") 
	cur = con.cursor()
	cur.execute("insert into cliente(id,nome,cpf) values('1', 'vitor','333.333.222.555')")
	con.commit() # Segue mesma lógica do Postgre, tem que gravar as alteações com o commit
	print ("Registro criado com sucesso")
except Exception as e:
	print ("Erro: %s"%e)
finally:
	print ("Finalizando a conexão com o banco de dados")
	cur.close()
	con.close()


