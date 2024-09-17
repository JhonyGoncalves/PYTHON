# Crie um programa que leia o salário de um funcionário e exiba o novo salário com um aumento de 15%.
salario = float(input("Digite o salário: "))
aumento = ((15 / 100) * salario)
print(f"O salário foi de R${salario} para R${aumento + salario}")