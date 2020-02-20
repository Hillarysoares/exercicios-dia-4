import datetime as date

def calcular_dias_de_vida (hoje , nasc):
    resultado =  (hoje - nasc)
    return resultado

day_input = int(input('Digite o dia vc em que nasceu: '))
month_input = int(input('Digite o mes em que vc nasceu: '))
year_input = int(input('Digite o ano em que vc nasceu: '))

dia_nasc = date.date (year=year_input, month=month_input, day=day_input)
dia_hoje = date.date (year=2020 , month=2, day=20)

dias_de_vida = dia_hoje - dia_nasc
print ('Você está vivendo: ', (dias_de_vida))