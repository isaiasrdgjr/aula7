# Funçõe em python a
# palavra reservada def.
# Funções são rotinas emm seu conceito.

# def saudacao():
#     print('Olá, mundo!')


# saudacao()

# def mostrar_linha():
#     print(30*'=')


# mostrar_linha()
# print('MÓDULO 01')
# mostrar_linha()
# print('ALGORITIMOS')
# mostrar_linha()
# print('ANÁLISE DE DADOS')
# mostrar_linha()


# def saudacao(texto):
#     print(f'Olá, {texto}!')


# nome = input('Informe o nome: ')
# saudacao(nome)

# def somar(a, b):
#     s = a + b
#     return s


# soma = somar(4, 5)
# print(f'O valor da variável soma é {soma}')

def somar_numeros(x, y):
    s = x + y
    return s


for i in range(3):
    n1 = int(input('Informe o número: '))
    n2 = int(input('Informe o número: '))

    soma = somar_numeros(n1, n2)
    print(soma)
