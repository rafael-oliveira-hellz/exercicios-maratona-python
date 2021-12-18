
titulo = 'Boletim dos Alunos '
tam_titulo = len(titulo)

while True:
    nome = input('Digite o nome do aluno: ')

    # Caso o usuário digite 'sair' o programa se encerra
    if nome.lower() == 'sair':
        break
    nome_nota = dict()
    notas = list()

    for i in range(1,5):
        notas.append(float(input(f'Digite a {i}º nota: ')))

    nome_nota.update({nome: notas})

    for j, k in nome_nota.items():
        media = sum(notas) / len(notas)

        if media >= 7:
            status = 'Aprovado'
        else:
            status = 'Reprovado'
    print('\n')
    print(titulo)
    print('-' * tam_titulo + '\n')
    print(j, *k, status)
