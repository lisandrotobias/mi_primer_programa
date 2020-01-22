import os

numero_a_adivinar = int(input("Dime el número a adivinar: "))

os.system ("cls")


numero = int(input("Adivina el número: "))

while numero != numero_a_adivinar:
    print("Intenta otra vez")
    numero = int(input("Adivina el número: "))

print("Has adivinado")