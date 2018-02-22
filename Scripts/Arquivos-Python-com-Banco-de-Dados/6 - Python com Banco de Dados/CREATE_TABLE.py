#!/usr/bin/python

import MySQLdb

try:
    # Open database connection
    con = MySQLdb.connect(host="10.25.26.245", user="root", db="projeto", passwd="123456")

    # prepare a cursor object using cursor() method
    cur = con.cursor()

    # Drop table if it already exist using execute() method.
    cur.execute("DROP TABLE IF EXISTS cliente;")

    # Create table as per requirement
    sql = """CREATE TABLE cliente (
            id  INTEGER NOT NULL,
            nome VARCHAR(255),
            cpf VARCHAR(255),  
            PRIMARY KEY(id));"""

    cur.execute(sql)
except Exception as e:
	print ("Erro: %s"%e)
finally:
	print ("Finalizando a conexão com o banco de dados")
	cur.close()
	con.close()

