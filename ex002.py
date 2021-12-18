# Exercício 2

dias = int(input('Digite o número de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))

dias_result = dias * 86400
horas_result = horas * 3600
minutos_result = minutos * 60
segundos_result = segundos

total = segundos_result + minutos_result + horas_result + dias_result

resultado = 'O número total de segundos calculados é: {}.'.format(total)

print(resultado)

# Exercício 3

preco = float(input('Digite o preço do produto: '))
desconto = int(input('Digite o percentual de desconto a ser aplicado (somente números): '))

v_desc = float(preco * (desconto / 100))
preco_final = preco - v_desc

print('O valor do desconto dado é de: R${:.2f}'.format(v_desc))
print('O valor do produto com desconto é: R${:.2f}'.format(preco_final))

# Exercício 4

c = int(input('Digite a temperatura em graus Celsius: '))
f = ((9 * c) / 5) + 32

print('A temperatura em Fahrenheit é: {}°F'.format(f))