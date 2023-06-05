#Essa função recebe uma lista de dados, o nome de uma coluna e o nome de uma função como parâmetros. 
#A função aplicar_funcao verifica qual função foi especificada e, com base nisso, chama a função correspondente para processar os dados.

def aplicar_funcao(dados, coluna, funcao):
    if funcao == 'media':
        return media(dados, coluna)
    if funcao == 'somatorio':
        return somatorio(dados, coluna)

#Essa função calcula o somatório dos valores em uma determinada coluna dos dados fornecidos.
def somatorio(dados, coluna):
    soma = 0
    for registro in dados:
        soma += registro[coluna]
    return soma

#Essa função calcula a média dos valores em uma determinada coluna dos dados fornecidos. 
def media(dados, coluna):
    soma = 0
    for registro in dados:
        soma += registro[coluna]
    return soma / len(dados)