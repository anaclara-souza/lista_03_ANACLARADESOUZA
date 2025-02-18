#Programa 2:Escreva um programa para exibir na tela o nome e a categoria de um lutador, 
#o programa deve ler uma string para o nome e um número real para o peso.Conforme o peso, ocorrerá o enquadramento na categoria:
# Entrada de dados
nome = input("Nome do lutador: ")
peso = input("Peso do lutador (kg): ")
try:
    peso = float(peso)
    if peso < 52:
        categoria = "Inválido"
    elif peso < 65:
        categoria = "Peso Pena"
    elif peso < 72:
        categoria = "Peso Leve"
    elif peso < 79:
        categoria = "Peso Ligeiro"
    elif peso < 86:
        categoria = "Peso Meio-Médio"
    elif peso < 90:
        categoria = "Peso Médio"
    elif peso < 100:
        categoria = "Peso Meio-Pesado"
    else:
        categoria = "Peso Pesado"

    print("Lutador: {}\nCategoria: {}".format(nome, categoria))
except:
    print("Dado inválido! O peso deve ser um número real.")
print("Ana Clara De Souza")