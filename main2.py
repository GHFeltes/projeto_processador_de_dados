from arquivos import carrega_arquivo, salvar_arquivo
from processamento import localiza, filtrar, projetar, agrupar

alunos, cabecalho = carrega_arquivo('dados/alunos.csv', ',', [str, int, str, float, float, int, float, bool])

agrupamento = agrupar(alunos, 'escola', 'faltas', 'media')

print(agrupamento)