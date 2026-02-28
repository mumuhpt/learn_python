#Vamos criar um programa que exibe o calendario no terminal 

import calendar

year = int(input('Digite o ano: '))
month = int(input('Digite o mes: '))

cal = calendar.month(year, month)

print(cal)
