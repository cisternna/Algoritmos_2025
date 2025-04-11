# Escriba la siguiente formula: y = 6x^2+3x+2, para x = 2 
x = 2
print(6*x**2+3*x+2)

# solicite al usuario dos valores. El primer valor es el número quedesea redondear 
# (es decir, un número con decimales). El segundo número es el número de decimales 
# (0,1, 2, ...), que es un número entero.
# Ejemplo: primer número = 3.14159, segundo número = 3, salida = 3.142
val_1 = float(input('Ingrese el número que desea redondear: ')) 
val_2 = int(input('Ingrese el número de decimales: ')) 
pre_resultado = val_1*(10**val_2)
resultado = round(pre_resultado)/10**val_2
print(resultado)

# Escriba un programa en python que permita al usuario ingresar dos valores enteros, un numerador y
# un denominador. El programa debería generar estos valores como una fracción impropia y luego
# generar la fracción mixta equivalente.
numerador = int(input('Ingrese el numerador: '))
denominador = int((input('Ingrese el denominador: ')))

entero = numerador//denominador
resto = numerador%denominador

print(str(numerador) + '/'+ str(denominador), 'es equivalente a', entero,'y', str(resto) + '/' + str(denominador))

# Calcular a cuánto dinero han ascendido 1000 euros después de tres años con una tasa de interés del 5 por ciento
# Formula: CANTIDAD_INICIAL(1+INTERES/100)^AÑOS
cantidad_inicial = 1000
interes = 5
años = 3
print(cantidad_inicial*(1+interes/100)**años)

# Verificar ecuaciones: 
# (a+b)^2 = a^2+2ab+b^2
# (a-b)^2 = a^2-2ab+b^2
a = 3.3 
b = 5.3
a2 = a**2
b2 = b**2
eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2
eq1_pow = ( a + b )**2
eq2_pow = ( a - b )**2
print (" Primera ecuacion : ", ( eq1_sum , eq1_pow ) )
print (" Segunda ecuacion : ", ( eq2_sum , eq2_pow ) )

