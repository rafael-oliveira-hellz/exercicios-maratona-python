blocks = int(input("Digite a quantidade de blocos: "))

height = 0

while blocks > height:
    height += 1
    blocks -= height

print(f"A sua pirâmide terá {height} camadas.")