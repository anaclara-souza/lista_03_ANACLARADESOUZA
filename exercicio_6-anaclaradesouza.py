#Programa 6:Nas eleições municipais, os munícipios com 200.000 eleitores ou mais,
#tem segundo turno caso o 1º colocado não tenha mais que 50% dos votos.Escreva um programa que leia: O nome do munícipio,
#a quantidade de eleitores e a quantidade de votos do candidato mais votado. Informe se haverá segundo turno ou não.

municipio = input("Digite o nome do município: ")
qatd_elei = int(input("Digite a quantidade de eleitores: "))
votos_candidatos = int(input("Digite a quantidade de votos do candidato mais votado: "))

if qatd_elei >= 200000:
    if votos_candidatos <= 0.50 * qatd_elei:
        print("Haverá segundo turno.")
    else:
        print("Não haverá segundo turno.")
else:
    print("O município não tem segundo turno.")
