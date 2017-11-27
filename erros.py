from models import *
arquivo = None
try:
	perfis = []	
	arquivo = open('perfis.csv','r')
	valores = arquivo.readline().split(',')
	perfis.append(Perfil(*valores))
	print 'arquivo aberto com sucesso'
	arquivo.close()
except IOError as erro:
	print '--> IOError: %s ' % (erro)
except TypeError as erro:
	print '--> TypeError: %s ' % (erro)
finally:
	if arquivo is not None:
		print('fechando arquivo')
		arquivo.close()
