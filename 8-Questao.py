import os
os.system("cls")

print(""" 
   COR \t Preço 
  1 \t Verde \t R$ 10.00
  2 \t Azul \t R$ 20.00
  3 \t Amarelo \t R$ 30.00
  4 \t Vermelho \t R$ 40.00""")


COR = input("Informe a cor: ")

match COR:
    case "verde":
     print("Voce escolheo o cd verde pelo preço de R$ 10.00")
    case "azul":
     print("VOce escolheu o cd azul pelo preço de R$ 20.00")
    case "amarelo":
     print("Voce escolheo o cd amarelo pelo preço de R$ 30.00")
    case "vermelho":
     print("Voce escolheu o cd vermelho pelo preço de R$ 40.00")
    case _:
         print("COR invalida.")
             
     