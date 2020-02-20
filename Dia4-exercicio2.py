def retornar_meu_nome(nome, sobrenome) :
    resultado = 'Olá, seu nome é: ' + nome + ' ' + sobrenome
    return resultado

nome_input = input('Digite seu nome: ')
sobrenome_input = input ('Digite seu sobrenome: ')

meu_nome = retornar_meu_nome(sobrenome=sobrenome_input , nome=nome_input)
print(meu_nome)

resultado_soma = somar(a=valor_a , b=valor_b)
print (resultado_soma)