from arquivos import carrega_arquivo, salvar_arquivo
from processamento import localiza, filtrar, projetar

alunos, cabecalho = carrega_arquivo('dados/alunos.csv', ',', [str, int, str, float, float, int, float, bool])

# linha = localiza(alunos, 4999)

#alunos_pedro_ii = filtrar(alunos, 'escola', 'Pedro II', '==')

#print(len(alunos_pedro_ii))

#alunos_pedro_ii_monitoria = filtrar(alunos_pedro_ii, 'monitoria', True, '==')

#print(len(alunos_pedro_ii_monitoria))

#alunos_pedro_ii_monitoria_sem1_7 = filtrar(alunos_pedro_ii_monitoria, 'nota_semestre_1', 7, '>')

#print(len(alunos_pedro_ii_monitoria_sem1_7))

# alunos_pedro_ii_monitoria_sem1_7_projetado = projetar(alunos_pedro_ii_monitoria_sem1_7, ['nome', 'nota_semestre_1', 'monitoria'])

# aluno = localiza(alunos_pedro_ii_monitoria_sem1_7_projetado, 0)

# print(aluno)

#salvar_arquivo('dados/alunos_filtrados.csv', ',', alunos_pedro_ii_monitoria_sem1_7)

# Exemplo de acesso por um único índice
aluno_1 = localiza(alunos, 0)
print(aluno_1)
input()
# Exemplo de acesso por uma lista de índices
indices = [2, 4, 6]
alunos_indices = localiza(alunos, indices)
print(alunos_indices)
input()
# Exemplo de acesso por intervalo de índices
intervalo = (1, 3)
alunos_intervalo = localiza(alunos, intervalo)
print(alunos_intervalo)
