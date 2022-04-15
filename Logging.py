from logging import debug, info, warning, error, critical
from logging import basicConfig
from logging import WARNING

basicConfig(
    level=WARNING,
    filename='/home/guilherme/Documentos/meuslogs.txt',
    filemode='a',
    format='%(asctime)s %(levelname)s %(message)s'
    )

debug('Inicio do código')
 
def funcao():
    warning('Executaram a função')
    
error('Erro')
funcao()


debug('Fim do código')
