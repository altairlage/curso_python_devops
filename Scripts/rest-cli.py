#!/usr/bin/python
# -*- coding: UTF-8 -*-
# rest_cli.py

import requests
import json
import sys

# Definir o caminho URL
def _url(path):
    return 'http://127.0.0.1:3000' + path

# Listar todos os itens no Json
def get_tasks():
    response = json.loads(requests.get("http://127.0.0.1:3000/usuarios/")._content)   
    for r in response:
        print r["id"],r["nome"],r['email']

# Adicionar um item no Json
def add_task(email="",nome=""):
    return requests.post(_url('/usuarios/'), json={
        'email': email,
		'nome': nome,
        })

# Apagar um item no Json
def del_task(task_id):
    return requests.delete(_url('/usuarios/{:d}/'.format(task_id)))

# Atualizar um item no Json
def update_task(task_id, email, nome):
    url = _url('/usuarios/{:d}/'.format(task_id))
    return requests.put(url, json={
        'email': email,
        'nome': nome,
        })

if __name__ == '__main__':
	#get_tasks()
	add_task("Alan Post","email.alan")
	#del_task(5)
	#update_task(5, "@@@@@@@", "vitor9")
	get_tasks()
	





