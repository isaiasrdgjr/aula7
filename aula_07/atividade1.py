def multiplos(x):
    d = x * 2
    t = x * 3
    q = x ** 2
    print(f'O dobro do número é: {d}')
    print(f'O triplo do número é: {t}')
    print(f'O quadrado do número é: {q}')


num = int(input('Informe um número: '))
multiplos_num = multiplos(num)
