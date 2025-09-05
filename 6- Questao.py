import os
os.system("cls")

nota_1 = float(input("Informe a primeira nota: "))
nota_2 = float(input("Informe a segunda nota: "))

soma = nota_1 + nota_2
media = (nota_1 + nota_2) / 2

print("\n")
 
print(f"A media foi: {media}")

print("\n")

if media > 6:
    print("O aluno esta aprovado. ")
elif media > 4.1 and 5.9:
    print("O aluno esta em recuperaçao. ")
else:
    print("O aluno esta reprovado.")