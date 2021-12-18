def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x

def fileCreation(fileName):
    try:
        file = open(fileName, 'wt+')
        file.close()
    except:
        print('Erro na criação do arquivo!')
    else:
        print('Arquivo {} foi criado com sucesso!'.format(fileName))

def file_exists(fileName):
    try:
        file = open(fileName, 'rt')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True

def listFile(fileName):
    try:
        file = open(fileName, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(file.read())
    finally:
        file.close()

def registerGame(fileName, gameName, videogameName):
    try:
        file = open(fileName, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        file.write('{}; {}\n'.format(gameName, videogameName))
    finally:
        file.close()

### Programa Principal

arquivo = 'games.txt'

if file_exists(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    fileCreation(arquivo)

while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar itens')
    print('3 - Sair')

    select = valida_int('Escolha a opção desejada: ', 1, 3)

    if select == 1:
        print('Opção de cadastrar novo item selecionada...\n')
        gameName = input('Nome do Jogo: ')
        videogameName = input('Nome do Videogame: ')

        registerGame(arquivo, gameName, videogameName)

    elif select == 2:
        print('Opção de listar selecionada...\n')

        listFile(arquivo)

    elif select == 3:
        print('Encerrando o programa...')
        break