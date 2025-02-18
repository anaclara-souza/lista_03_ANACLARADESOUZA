#Programa 4:No SENAILÂNDIA mulheres e homens podem servir o exército do país.
#O serviço é opcional e é muito comum que as pessoas se apresentem para o serviço em algum momento da vida.
#Existe uma única restrição para o ingresso, que é a idade da pessoa: 
#•	Para mulheres, a idade aceita é entre 21 e 34 anos (>=21 e <=34)•
#Para homens, a idade aceita é entre 18 e 39 anos (>=18 e <=39)
# Escreva um programa que leia 3 dados de entrada: Nome da pessoa, idade e gênero.
#Informe se a pessoa será aceita ou não para o serviço.OBS: Para o gênero deve ser lido somente um caractere, 
#que pode ser: ‘f’ ou ‘F’, ‘m’ ou ‘M’. Qualquer coisa diferente, deve ser informado como inválido.

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
genero = input("Digite o gênero (F ou M): ")

if genero == 'F' or genero == 'f':
    if 21 <= idade <= 34:
        print("Aceita para o serviço militar.")
    else:
        print("Não aceita para o serviço militar.")
elif genero == 'M' or genero == 'm':
    if 18 <= idade <= 39:
        print("Aceito para o serviço militar.")
    else:
        print("Não aceito para o serviço militar.")
else:
    print("Dado inválido! O gênero deve ser 'F' ou 'M'.")
