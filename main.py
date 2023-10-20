# Função para gerar uma linha separadora
def ln(x):
    print('-'*x)


def pegaDados():
    nome = input("Digite seu nome: ")
    idade = input("Qual sua idade: ")
    cidade = input("Que cidade nasceu: ")

    resumo = f'Seu nome é {nome}, nasceu em {cidade} e tem {idade} anos de idade.'

    return print(resumo)

pegaDados()
ln(60)
