# Crie um programa que converta uma quantidade de segundos para horas, minutos e segundos.
segundos = int(input("Digite uma quantidade de segundos: "))
minuto = segundos / 60
hora = minuto / 60
print(f"{segundos} segundos corrempondem a {hora:,.0f} horas e {minuto:,.0f} minutos")