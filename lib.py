def gera_nome_convite(convite):
	posicao_final = len(convite)
	posicao_inicial = posicao_final - 4
	parte1 = convite[0:4]
	parte2 = convite[posicao_inicial : posicao_final]
	return parte1 + ' ' + parte2

def envia_convite(convite):
	print 'Enviando convite para %s' % (convite)

def processa_convite(convite):
	codigo_convite = gera_nome_convite(convite)
	envia_convite(codigo_convite)

from datetime import date
def calcula_idade():
	print 'Informe seu ano de nascimento: '
	v_ano = raw_input()
	n_ano = int(v_ano)
	n_idade = date.today().year - n_ano
	print 'Entao sua idade é %s' % (n_idade)

def cadastra_nomes(nomes):
	print 'Informe o nome que você deseja cadastrar:'
	nome = raw_input()
	nomes.append(nome)

def remove_nomes(nomes):
	print 'Informe o nome que você deseja remover:'
	nome = raw_input()
	nomes.remove(nome)