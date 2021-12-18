# tomar qualquer número inteiro não-negativo e não-nulo e nomeá-lo c0;
# se for par, avalie um novo c0 como c0 ÷ 2;
# caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
# Se c0 ≠ 1, saltar para o ponto 2.
# A hipótese diz que, independentemente do valor inicial de c0, irá sempre para 1.
# Escreva um programa que leia um número natural e execute os passos acima indicados, desde que c0 permaneça diferente de 1. 
# Também queremos que conte os passos necessários para alcançar o objetivo. 
# O seu código deve fazer output de todos os valores intermédios de c0, também.
# Dica: a parte mais importante do problema é como transformar a ideia de Collatz num loop while - esta é a chave para o sucesso.

num = int(input("Digite um número inteiro diferente de zero: "))

counter = 0

if num > 0 and num != None:
    c0 = num
else:
    exit()

while c0 != 1:
    if c0 % 2 == 0:
        c0 = int(c0 / 2)
    elif c0 % 2 == 1:
        c0 = int(3 * c0 + 1)
    counter += 1
        
    print(c0)

print(f"\nSteps: {counter}")