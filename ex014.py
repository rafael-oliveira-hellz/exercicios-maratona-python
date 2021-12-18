#Mostra na tela o meu RU para conferência
print('RU do aluno: 1989043\n')

# Programa principal
# Dicionário onde será armazenado as informações dos aluno

while True:
    terminar = input('Deseja cadastrar uma pessoa? [S/N]: ')

    if terminar.upper() in 'N':
        print('Encerrando o programa...')
        break

    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÃO')
        continue

    titulo = 'Boletim dos Alunos '
    tam_titulo = len(titulo)

    alunos = {}

    nome = input('Nome do aluno: ')

    notas = []

    for j in range(1, 5):
        nota = round(float(input(f'Nota {j} do aluno: ')), 1)

        notas.append(nota)

    alunos[nome] = notas

for nome, notas in alunos.items():
    media = sum(notas) / len(notas)

    resultado = 'aprovado' if media >= 7.0 else 'reprovado'

print('\n')
print(titulo)
print('-' * tam_titulo)

print(nome, *notas, resultado)
