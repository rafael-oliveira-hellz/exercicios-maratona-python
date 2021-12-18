nasc = int(input('Digite o ano do seu nascimento: '))
now = int(input('Digite o ano atual: '))

idade = int(now - nasc)

if (idade >= 18):
    print('Vocé já é maior de idade e pode tirar sua carta de motorista')

else:
    print('Vocé é menor de idade e não pode tirar sua carta de motorista ainda!')