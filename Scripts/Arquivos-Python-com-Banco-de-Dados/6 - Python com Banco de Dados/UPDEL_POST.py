#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Nesse arquivo, forçamos o uso do
  rollback quando digitamos o update 
  de forma errada. 


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
	cur.execute("update cliente set nome='vitor' where id=1")
	print "Atualização feita com sucesso"
	cur.execute("delete from cliente where id=2")
	print "Remoção feita com sucesso"
	con.commit()
except Exception as e:
	print "Erro: %s"%e
	print "Fazendo o rollback"
	con.rollback()
finally:
	print "Finalizando a conexão com o banco de dados"
	cur.close
	con.close



















