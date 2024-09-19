# Crie um programa que converta uma quantidade de segundos para horas, minutos e segundos.
tempo_em_segundos = int(input("Digite a quantidade de segundos: "))
horas = tempo_em_segundos // 3600
minutos = (tempo_em_segundos % 3600) // 60
segundos = tempo_em_segundos % 60
print(f"{tempo_em_segundos} segundos equivalem a {horas} horas, {minutos} minutos e {segundos}segundos")

