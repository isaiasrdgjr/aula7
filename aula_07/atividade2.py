pesopeixes = float(input('Informe o peso total de peixes pescados: '))

PESO_LIMITE = 100.0
MULTA_KG = 4.0

if pesopeixes > PESO_LIMITE:
    def multaexcesso(p):
        e = p - PESO_LIMITE
        m = e * MULTA_KG
        return m
    multa = multaexcesso(pesopeixes)
    print(f'O peso de peixes excedeu o limite, você recebeu uma multa de: R${multa:.2f}')
else:
    print('Pesca liberada.')
