

# Escrever um algoritmo que leia o nome e peso de um lutador
# em seguida informe a categoria a que pertence o lutador.
# Todos os dados devem ser lidos do teclado.

categoria = ''
peso = ''
nome = ''

#Mostra na tela o meu RU para conferência
print('RU do aluno: 1989043\n')

# Programa principal

# Dados de entrada

while True:
    # Recebe o nome do usuário
    nome = str(input('Digite o seu nome: '))

    # Caso o usuário digite 'sair' o programa se encerra
    if nome.lower() == 'sair':
        break

    # Caso o usuário digite algo diferente de 'sair' o programa pede o peso
    peso = float(input('Digite o seu peso: '))
    print('\n')

    # Bloco que define as categorias baseado no peso que o usuário digitar
    if peso < 65:
        categoria = 'Pena'
    elif (peso >= 65) and (peso < 72):
        categoria = 'Leve'
    elif (peso >= 72) and (peso < 79):
        categoria = 'Ligeiro'
    elif (peso >= 79) and (peso < 86):
        categoria = 'Meio-médio'
    elif (peso >= 86) and (peso < 93):
        categoria = 'Médio'
    elif (peso >= 93) and (peso < 100):
        categoria = 'Meio-pesado'
    else:
        categoria = 'Pesado'
    break

# Mostrando na tela a saída dos dados
print('Nome fornecido: {}'.format(nome))
print('Peso fornecido: {} kg\n'.format(peso))
print('O lutador {} pesa {} kg e se enquadra na categoria {}.'.format(nome, peso, categoria))
