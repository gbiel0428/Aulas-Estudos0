import os
os.system("cls")

Produto = input("Informe o nome do produto. ")
Quantidade = float(input("Informe a quantidade de produto. "))

preço_unitario = 5

total = Quantidade  * preço_unitario

if Quantidade <= 5:
    desconto = total * 0.90
elif Quantidade > 5 and Quantidade <= 10:
    desconto = total * 0.15
elif Quantidade > 10:
    desconto = total * 0.5
    
print(F"O produto escolhido foi:  {Produto} , A quantidade: {Quantidade}, O valor total foi: {total_a_pagar}")