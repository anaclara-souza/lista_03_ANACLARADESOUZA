#Programa 3:Uma empresa financeira consegue empréstimo a pessoas físicas,
#quando o valor da parcela é menor que 8% do salário da pessoa. Escreva um programa que leia 2 números reais:
#O valor do salário e o valor da parcela.E informe se o empréstimo será concedido ou não.
# Entrada de dados
salario = float(input("Digite o valor do salário: "))
parcela = float(input("Digite o valor da parcela: "))
if parcela < 0.08 * salario:
    print("Empréstimo concedido")
else:
    print("Empréstimo negado")


