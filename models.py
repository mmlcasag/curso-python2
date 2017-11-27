# -*- coding: UTF-8 -*-

class Perfil(object):
	'Classe padrão para perfis de usuários'

	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa

	def imprime(self):
		print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)
	
	@classmethod
	def gerar_perfis(classe, nome_arquivo):
		perfis = []		
		arquivo = open(nome_arquivo)
		for linha in arquivo:
			valores = linha.split(",")
			perfis.append(classe(*valores))
		arquivo.close()
		return perfis

class Data(object):
	'Desafio Alura'

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprime(self):
		print '%s/%s/%s' % (self.dia, self.mes, self.ano)

class Pessoa(object):
	'Desafio 2 Alura'

	def __init__(self, nome, peso, altura):
		self.nome = nome
		self.peso = peso
		self.altura = altura

	def calcula_imc(self):
		return self.peso / (self.altura * self.altura)

	def imprime_imc(self):
		print self.calcula_imc()
