# Faça um programa que leia a altura e o peso de uma pessoa e calcule seu IMC.
altura = float(input("Digite a altura(M): "))
peso = float(input("Digite o peso(KG): "))
IMC = peso / (altura * altura)
print(f"O seu IMC é {IMC:,.1f}")