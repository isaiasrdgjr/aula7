pesopeixes = float(input('Informe o peso total de peixes pescados: '))

PESO_LIMITE = 100.0

if pesopeixes > PESO_LIMITE:
    def multaexcesso(x):
        e = x - PESO_LIMITE
        m = e * 4.0
        return m


multa = multaexcesso(pesopeixes)
print(f'O peso de peixes excedeu o limite, você recebeu uma multa de: R${multa:.2f}')
