
operation = input("¿Que operación quieres realizar (multiplicar / dividir / sumar / restar)? ").upper()
numero1 = int(input("Primer número: "))
numero2 = int(input("Segundo número: "))

if operation == "MULTIPLICAR":
    result = numero1 * numero2

elif operation == "DIVIDIR":
    result = numero1 / numero2

elif operation == "SUMAR":
    result = numero1 + numero2

elif operation == "RESTAR":
    result = numero1 - numero2





print("Resultado: {} ".format(result))