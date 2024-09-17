# Faça um programa que leia o preço de um produto e aplique um desconto de 10%.
produto = float(input("Digite o valor do produto: "))
desconto = produto - ((10 / 100) * produto)
print(f"O produto foi de {produto} para {desconto} com seus 10% de desconto")