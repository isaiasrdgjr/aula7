def multiplos(x):
    dobro = x * 2
    triplo = x * 3
    quadrado = x ** 2

    return dobro, triplo, quadrado    


num = int(input('Informe um número: '))
d, t, q = multiplos(num)

print(f'O dobro do número é: {d}')
print(f'O triplo do número é: {t}')
print(f'O quadrado do número é: {q}')
