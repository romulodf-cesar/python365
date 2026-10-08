# Crie uma algoritmo que leia dois números
# Mostre no final qual o número é o maior

# --ENTRADA---
# leia um número
# leia outro número

# -- PROCESSAMENTO --
# verificar quem é o maior

# -- SAÍDA
# mostrar o maior

print("\nInsira 2 números e eu direi qual deles é maior")

numero_1 = int(input("\ndigite o numero 1: "))
numero_2 = int(input("\ndigite o numero 2: "))

if numero_1 > numero_2:
    print(f"\nO {numero_1} é maior que o {numero_2}")

elif numero_2 > numero_1:
    print(f"\nO {numero_2} é maior que o {numero_1}")

else:
    print("\nOs numeros são iguais")
# Igor, Emanuel e João Miguel