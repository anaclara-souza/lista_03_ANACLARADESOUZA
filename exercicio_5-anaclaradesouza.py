#Programa 5:No comércio o conceito de margem bruta é uma porcentagem que é aplicada ao preço de custo para se obter o preço de venda.
#Uma loja tem como política comercial, aplicar uma margem bruta de 45%, quando o peço de custo é <= R$100,00. 
#Se o produto custa mais que isso, a margem de lucro é 35%.Escreva um programa que leia o preço do produto e mostre seu preço de venda. 

preco_custo = float(input("Digite o preço de custo do produto: R$"))

if preco_custo <= 100:
    preco_venda = preco_custo * 1.45  
else:
    preco_venda = preco_custo * 1.35 

print("Preço de venda do produto: R${:.2f}".format(preco_venda))

print("Ana Clara De Souza")