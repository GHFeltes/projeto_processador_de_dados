from funcoes import aplicar_funcao

# Essa função é responsável por localizar registros em uma lista de dados com base em um índice ou intervalo de índices.
def localiza(dados, indice):
    if isinstance(indice, int):
        if indice < len(dados):
            return dados[indice]
        else:
            print("Índice superior à quantidade de registros")
            return {}
    elif isinstance(indice, list):
        resultados = []
        for i in indice:
            if i < len(dados):
                resultados.append(dados[i])
            else:
                print("Índice superior à quantidade de registros")
        return resultados
    elif isinstance(indice, tuple) and len(indice) == 2:
        start, end = indice
        if start < len(dados) and end < len(dados) and start <= end:
            return dados[start:end+1]
        else:
            print("Índices inválidos")
            return []
    else:
        print("Tipo de índice inválido")
        return {}


#Essa função recebe dois valores (v1 e v2) e uma operação de comparação (operacao) como parâmetros. 
#A função compara os valores utilizando a operação especificada e retorna um valor booleano indicando se a comparação é verdadeira ou falsa.
def testar(v1, operacao, v2):
    if operacao == '==':
        return v1 == v2
    elif operacao == '>':
        return v1 > v2
    elif operacao == '<':
        return v1 < v2
    elif operacao == '>=':
        return v1 >= v2
    elif operacao == '<=':
        return v1 <= v2
    elif operacao == '!=':
        return v1 != v2
    return False

#Essa função realiza a filtragem dos dados com base em uma coluna, um valor e uma operação de comparação. 
def filtrar(dados, coluna, valor, operacao):
    dados_filtrados = []
    for linha in dados:
        if testar(linha[coluna], operacao, valor):
            dados_filtrados.append(linha)
    return dados_filtrados


#Essa função realiza a projeção dos dados, mantendo apenas as colunas especificadas.
def projetar(dados, colunas):
    dados_projetados = []
    for linha in dados:
        linha_projetada = {}
        for campo, valor in linha.items():
            if campo in colunas:
                linha_projetada[campo] = valor
        dados_projetados.append(linha_projetada)
    return dados_projetados


#Essa função realiza a operação de agrupamento dos dados com base em uma coluna e aplica uma função específica a outra coluna.
def agrupar(dados, coluna, coluna2, funcao):

    dados_agrupados = {}

    for linha in dados:
        valor_celula = linha[coluna]
        if dados_agrupados.get(valor_celula) == None:
            dados_agrupados[valor_celula] = []
        dados_agrupados[valor_celula].append(linha)
    
    for chave, lista in dados_agrupados.items():
        dados_agrupados[chave] = aplicar_funcao(lista, coluna2, funcao)
    
    return dados_agrupados