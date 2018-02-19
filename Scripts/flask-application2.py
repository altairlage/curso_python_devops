#!/usr/bin/python
# -*- coding: UTF-8 -*-
# flask_application2.py

# Importação dos módulos
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello():
	return jsonify({"message":"Aqui serão listados os usuários"})

@app.route("/usuarios/", methods=["POST"]) # create
@app.route("/usuarios/<int:id>/", methods=["GET"]) # retrieve
@app.route("/usuarios/<int:id>/", methods=["PUT"]) # update
@app.route("/usuarios/<int:id>/", methods=["DELETE"]) # delete
def insert_usuario():
	pass

def select_usuario():
	pass

def update_usuario():
	pass

def delete_usuario():
	pass

if __name__=='__main__':
	app.run(debug=True)










