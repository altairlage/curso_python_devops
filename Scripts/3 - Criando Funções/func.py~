#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Abaixo segue um exemplo do uso de 
  funções. A primeira dela possui 
  uma parâmetro obrigatório e outra 
  não. O parâmetro é o valor esperado 
  entre parênteses nas funções.


  Modificado em 09 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

produtos = [] # Uma lista vazia a ser preenchida com todos os itens que serão salvos aqui!

# Função que faz o cadastramento de produtos e armazena na lista 'produtos'
def cadastrarProduto(produto):
	global produtos
	produtos.append(produto)

# Função que mostra os produtos na lista 'produtos'
def listarProdutos():
	global produtos
	for p in produtos: # Usa a interação for...in para percorrer toda a lista e mostrar quais itens estão presentes
		print p # printa os itens

produto = "" # variavel do 'raw_input' ** não confunda com a lista acima! **
while produto <> "sair": # Ao escrever sair, ele para o script
	produto = raw_input("Digite o produto que queira cadastrar: ")
	cadastrarProduto(produto) # Chama a função 'cadastrarProduto'
	print "produtos cadastrados com sucesso" # Printa na tela se foi cadastrado ou não
	listarProdutos() # mostra os produtos cadastrados na lista
	
