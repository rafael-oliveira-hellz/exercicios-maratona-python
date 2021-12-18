# Mostra na tela o meu RU para conferência
print('RU do aluno: 1989043\n')

# Função que verifica se o número digitado é inteiro e se está dentro do intervalo de 10000 e 30000

def valida_codigo(min, max):
    # laço de repetição para verificar o número informado.
    while True:
        try:
            # Recebe o número digitado pelo usuário
            codigo = int(input(f'Digite um número entre {min} e {max}: '))

            # Verifica se o valor digitado está entre o que foi especificado
            if ((codigo >= min) and (codigo <= max)):
                # Se a condição não for atendida voltará para a solicitação do número e apresentará a mensagem de erro
                return codigo
            else:
                print((f'O número digitado deve estar entre {min} e {max}'))
        # Se caso for digitado um caractere inválido, será solicitado que o usuário digite novamente
        except ValueError:
            print('Você não digitou um número')

# Calcula o dígito verificador baseado no número recebido pela função valida_codigo armazenado na variável
def multiply(digitos):
    digitos = str(digitos)
    peso = [2, 3, 4, 5, 6]

    mult1 = int(digitos[0]) * int(peso[0])
    mult2 = int(digitos[1]) * int(peso[1])
    mult3 = int(digitos[2]) * int(peso[2])
    mult4 = int(digitos[3]) * int(peso[3])
    mult5 = int(digitos[4]) * int(peso[4])

    # Soma os valores armazenados nas variáveis mult1, 2, 3, 4 e 5
    soma = mult1 + mult2 + mult3 + mult4 + mult5
    mult = soma % 7

    return mult

# Variável que recebe o parâmetro solicitado
digitos = valida_codigo(10000, 30000)

# Váriavel que recebe o cálculo do dígito verificador na função 'multiply'
digito = multiply(digitos)

# Imprime o resultado
print(f'{digitos}-{digito}')


