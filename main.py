# Função para calcular a idade da criatura
def calculaIdade(anoNas, anoAtual):
    return anoAtual-anoNas

# Função para gerar uma linha separadora
def ln(x):
    print('-'*x)

# Função de calculadora
def operar(num1,num2):

    menu = 'O que deseja fazer com os dois números digitados?\n    [ 1 ] - Potencia\n    [ 2 ] - Divisão\n    [ 3 ] - Multiplicação\n    [ 4 ] - Soma\n    [ 5 ] - Subtração\n    [ 6 ] - Divisão inteira\n    [ 7 ] - Resto da divisão\n'
    menu_opt = int(input(menu))
    if menu_opt == 1:
        resultado = num1**num2;
    elif menu_opt == 2:
        resultado = num1/num2;
    elif menu_opt == 3:
        resultado = num1*num2;
    elif menu_opt == 4:
        resultado = num1+num2;
    elif menu_opt == 5:
        resultado = num1-num2;
    elif menu_opt == 6:
        resultado = num1//num2;
    elif menu_opt == 7:
        resultado = num1%num2;
    else:
        resultado = print("Você digitou uma opção inválida")
    return int(resultado)

# Chamando a função
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print(f'Resultado: {operar(num1,num2)}')































# anoNas = int(input("Digite o ano de seu nascimento: "))
# anoAtual = int(input("Digite o ano atual: "))
# print(calculaIdade(anoAtual, anoNas))
# ln(30)
# print(f"Você tem {anoAtual - anoNas} anos de idade")
# ln(30)




# invertexto.com/609aula1logica