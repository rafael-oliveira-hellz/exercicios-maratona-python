# Exercício 1 - Calcular a idade de uma pessoa

from datetime import datetime, timedelta
import time

d1 = input('Digite sua data de nascimento: ')
date = time.mktime(datetime.strptime(d1, '%d/%m/%Y').date().timetuple())

# current date and time
now = datetime.now()

timestamp = datetime.timestamp(now)

result = int(timestamp - date)

res = timedelta(seconds=result).days

resultado = res // 365.25

print("Idade: {:.0f} ".format(resultado) + "anos")