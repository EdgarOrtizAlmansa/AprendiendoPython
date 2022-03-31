entero1 = False
entero2 = False
while entero1 == False or entero2 == False:
    str_numero_1 = input('Introduce un numero: ')
    str_numero_2 = input('Introduce un numero: ')
    entero1 = str_numero_1.isdigit()
    if entero1 == False and str_numero_1[0] == '-':
        numero_1 = int(str_numero_1)
        entero1 = True
    entero2 = str_numero_2.isdigit()
    if entero2 == False and str_numero_2[0] == '-':
        numero_2 = int(str_numero_1)
        entero2 = True

numero_1 = int(str_numero_1)
numero_2 = int(str_numero_2)

numero_1 = numero_1 / 10
numero_2 = numero_2 / 10

print('La suma de los numeros es: ', round(numero_1 + numero_2, 2))
print('La resta de los numeros es: ', round(numero_1 - numero_2, 2))
print('La multiplicacion de los numeros es: ', round(numero_1 * numero_2, 2))
print('La division de los numeros es: ', round(numero_1 / numero_2, 2))
