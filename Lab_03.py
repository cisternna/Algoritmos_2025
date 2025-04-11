# Elija una canción de su gusto personal y escriba un programa en Python utilizando funciones, 
# que permita separarla en estrofas, coros y puentes.

def estrofa_1():
    print("So close no matter how far\n" 
    "Coulnt be much more from the heart\n" 
    "Forever trust in who we are\n" 
    "And nothing else matters\n")
def estrofa_2():
    print("Never opened myself this way\n" 
    "Life is our we live it our way\n" 
    "Aall these words I dont just say\n" 
    "And nothing else matters \n" 
    "Trust I seek and I find in you\n " 
    "Everyday for Us something new\n" 
    "Open mind for a different view\n" 
    "And nothing else matters\n")
def coro():
    print("Never cared for what they do\n" 
    "Never cared for what they know\n" 
    "But I know\n")
def puente():
    print("*Solo de guitarra*\n")

# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 y no por 400.
# Escriba un programa que reciba un año como entrada e indique True si un año es bisiesto o False si no lo es.

year = int(input('Ingrese el año: '))
if year%4 == 0:                             # Si el año es divisible por 4
    if year%100 == 0:                       # Si el año es divisible por 100
        if year%400 != 0:                   # Si el año NO es divisible por 400
            print('False')                  # Si cumple todo lo anterior NO es bisiesto
        else: print('True')                 # Si es divisible por 100 y 400 Entonces SI es bisiesto
    else: print("True")                     # Si NO son divisibles por 100 pero Si por 4 son bisiestos
else:
    print("False")                          # Si no es divisible por 4 entonces NO es bisiesto

# Crea una función que tome dos números como entrada y un operador matemático (+, −, ∗,/) como otro argumento. 
# La función debe realizar la operación matemática correspondiente y devolver el resultado.

def ejercicio_02():
    numero_1 = int(input("Ingrese el primer numero: "))
    operador = input("Ingrese el operador: ")
    numero_2 = int(input("Ingrese el segundo numero: "))
    if operador == "+":
        print(numero_1+numero_2)
    elif operador == "-":
        print(numero_1-numero_2)
    elif operador == "/":
        print(numero_1/numero_2)
    elif operador == "*":
        print(numero_1*numero_2)
    
# Considerar la siguiente tabla que muestra la tasa de impuesto a pagar por una persona según su sueldo.
sueldo = int(input("Ingrese su sueldo: "))
if sueldo < 1000:
    print("la tasa de interes es: 0%")
elif 1000 <= sueldo <= 2000:
        print("la tasa de interes es: 5%")
elif 2000 <= sueldo < 4000:
        print("la tasa de interes es: 10%")
elif sueldo >= 4000:
         print("la tasa de interes es: 12%")

# 4
val = int(input("Ingrese un valor: "))
if val > 120:
  print (" Green !")
elif val > 80:
    print (" Blue !")
elif val < 32:
 print ("Red !")
else :
 print (" Orange !")

#5
x = int(input("Ingrese un valor: "))
if x < 30:
    print (" linea 1")
elif x < 60:
    print ( " linea 2")
else :
    print ( " linea 3")
# x = 15: linea 1    x = 45: linea 2    x = 60: linea 3

# Escriba un programa que pregunte a un usuario por la temperatura Actual y luego imprima una mensaje según 
# la temperatura
temperatura = int(input("¿Cual es la temperatura?: "))
if temperatura > 30: 
    print("El dia esta muy caluroso")
elif temperatura < 10:
    print("Un dia de otoño, pero esta templado")
elif 10 <= temperatura <= 30:
    print("Un dia normal")


def main():
    estrofa_1()
    estrofa_2()
    coro()
    estrofa_1()
    coro()
    estrofa_2()
    coro()
    puente()
    estrofa_1()
    ejercicio_02()

main()

