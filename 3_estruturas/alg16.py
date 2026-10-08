# desafio- 
'''
  Elabore um programa que leia um número
  Verifique se o número é par ou ímpar
  E mostre a mensagem na tela
      "É par"  ou "É impar"

'''
# Entender o problema
numero = int(input("Digite um número"))
# Se o resto da divisão por 2 = 0
if numero % 2 == 0:
    print("o número é par")
else:
    print("o número é impar")