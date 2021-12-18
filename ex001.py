# Montar um algoritmo para calcular a equação do delta na fórmula de Bhaskara

# Δ = b² – 4ac
# Bhaskara
## x = -b +- raiz de delta / 2.a

a = int(input('Digite um valor para "a": '))
b = int(input('Digite um valor para "b": '))
c = int(input('Digite um valor para "c": '))

delta = (b * b) - ((4 * a) * c)

x_um = (-(b) + (pow(delta)) / 2 * a)
x_dois = (-(b) - (pow(delta)) / 2 * a)

print('x¹ = {}'.format(x_um))
print('x² = {}'.format(x_dois))