import os
os.system


nome = input("Informe seu nome: ")

masculino = "M"
feminino = "F"

sexo = input("Informe sua sexualidade: ")

print("""    SOLTEIRO(a) \t CASADO(A) \t NAMORANDO""")


estado_civil = input("Informe seu estado civil: ")

if sexo == "F" and estado_civil == "CASADA" :
    tempo_de_casada = float(input("informe o tempo de casada: "))

print(F"Seu nome é: {nome}")
print(F"Sua sexualidade é: {sexo}")
print(F"Seu estado civil é: {estado_civil}")
print(f"Seu tempo de casada é: {tempo_de_casada} anos.")