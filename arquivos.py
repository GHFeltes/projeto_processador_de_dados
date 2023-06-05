# Essa função recebe um dado e um tipo como parâmetros e converte o dado para o tipo especificado.
def converte_dados(dado, tipo):
    dado_convertido = dado
    if tipo == int:
        dado_convertido = int(dado)
    elif tipo == float:
        dado_convertido = float(dado)
    elif tipo == bool:
        dado_convertido = False
        if dado == 'True':
            dado_convertido = True
    return dado_convertido


# Essa função carrega um arquivo de dados, realiza o processamento necessário e retorna os dados em uma estrutura de lista de dicionários.
def carrega_arquivo(nome_arquivo, separador, tipos):

    f = open(nome_arquivo, 'r')
    linhas = f.readlines()

    cabecalho = linhas[0].replace('\n', '').split(separador)

    alunos = []

    # percorre as linhas do arquivo
    for linha in linhas[1:]:
        dados_linha = linha.replace('\n', '').split(separador)
        
        aluno = {}

        # percorre as colunas de cada linha
        for coluna, tipo in enumerate(tipos):

            campo = cabecalho[coluna]

            aluno[campo] = converte_dados(dados_linha[coluna], tipo)
        
        alunos.append(aluno)
    return alunos, cabecalho



#Essa função recebe o nome de um arquivo, um separador e os dados a serem salvos. A função cria um novo arquivo com o nome especificado e escreve os dados nele.
def salvar_arquivo(nome_arquivo, separador, dados):
    f = open(nome_arquivo, 'w')

    cabecalho_str = ''

    cabecalho = list(dados[0].keys())

    for coluna in cabecalho:
        cabecalho_str += coluna
        if coluna != cabecalho[-1]:
            cabecalho_str += separador
    cabecalho_str += '\n'

    f.write(cabecalho_str)

    for index, linha in enumerate(dados):
        linha_str = ''
        for coluna, valor in linha.items():
            linha_str += str(valor)
            if coluna != cabecalho[-1]:
                linha_str += separador
        if index < len(dados) - 1:
            linha_str += '\n'
        f.write(linha_str)
    
    f.close()