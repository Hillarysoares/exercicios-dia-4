def somar(a,b):
    resultado = a + b
    return resultado

valor_a = float(input('Digite o primeiro valor: '))
valor_b = float(input ('Digite o segundo valor: '))
resultado_soma = somar(a=valor_a , b=valor_b)

if (resultado_soma >40) :
    print('A soma é: ', (resultado_soma))
else:
    print('Ops, só retorno valores acima de 40.')