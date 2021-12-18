# Definir o título e verificar a quantidade de caracteres nele
titulo = 'Boletim dos Alunos '
tam_titulo = len(titulo)

# Solicita quantos alunos serão cadastrados
N = int(input('Quantos alunos serão cadastrados? '))

# Dicionário para salvar o cadastro dos boletins
alunos = {}

# Informa à variavel 'nome' quantos alunos serão serão solicitados o nome
for alunoLista in range(1, N + 1):
    # Solicita o nome do aluno e altera o número de acordo com o informado na variável 'N'
    nome = input(f'Nome do aluno {alunoLista}: ')

    # Lista onde é salva as notas informadas
    notas = []

    # Loop que se repete até obter as 4 notas e salva elas na lista
    for alunoNota in range(1, 5):
        # Solicita as 4 notas dos alunos e altera a solicitação conforme a contagem do range na variável 'alunoNota'
        nota = round(float(input(f'Nota {alunoNota} do aluno {alunoLista}: ')), 1)

        # Adiciona as notas informadas à lista de notas
        notas.append(nota)

        # Atribui as notas informadas à lista de nomes de alunos
        alunos[nome] = notas

# Listar o nome dos alunos e as notas que estiverem dentro do dicionário 'alunos'
for nome, notas in alunos.items():
    # Calculará a média das notas
    media = sum(notas) / len(notas)

# Verificará se o aluno passou de ano caso tenha adquirido média maior ou igual a 7
if media >=7:
    status = 'Aprovado'
else:
    status = 'Reprovado'

# Mostrará a saída de informações na tela
print('\n')
print(titulo)
print('-' * tam_titulo)
print(nome, *notas, status)