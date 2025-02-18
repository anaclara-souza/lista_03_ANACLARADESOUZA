#Programa 1:Escreva um programa que forneça um tipo de aplicação financeira adequado a um investidor a partir de 2 dados fornecidos:
#O grau de aceitação de risco e o valor a ser investido.Deve ser lido no teclado na
#forma BX ou AL risco. Se for fornecido algo diferente disso, o programa deve mostrar uma mensagem indicando que foi 
#fornecido um dado inválido.Para o valor, deve ser um número real.
risco = input("Risco (BX ou AL): ")  
valor = input("Valor a investir: ")  

try:  
    valor = float(valor)  
    if risco == "BX":  
        if valor < 1000:  
            print("Poupança")  
        else:  
            print("Renda Fixa")  
    elif risco == "AL":  
        if valor < 1000:  
            print("Bitcoins")  
        else:  
            print("Ações")  
    else:  
        print("Dado inválido!")  
except:  
    print("Dado inválido!")  