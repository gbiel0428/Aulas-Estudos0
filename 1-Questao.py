import os
os.system("cls")

n1_A = float(input("Digite o  numero A: "))
n2_B = float(input("Digite o numero B: "))
n3_C = float(input("Digite o numero C: "))
print("\n")
soma = n1_A + n2_B
print("\n")

if soma < n3_C:
    print("A  + B e menor que C")
elif soma >n3_C:
    print("A + B e maior que c")
print("\n")

print(f"O valor A foi: {n1_A}")
print(F"O valor B foi: {n2_B}")
print(F"O valor c foi: {n3_C}")