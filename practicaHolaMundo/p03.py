nombre = input("Como te llamas ")
strEdad = input("Que edad tienes? ")
strDia = input("Que dia es? ")
strMes = input("Que mes es? ")
strAnno = input("Que anno es? ") 
# # strCumplidos = input("Cumpliste ya? ")
edad = int(strEdad)
dia = int(strDia)
mes = int(strMes)
anno = int(strAnno)
prob = int
trans = int
if mes == 1:
    prob = (dia / 365) * 100
    print("Hola", nombre, "la probabilidad de que hayas cumplido annos en ",anno, "es de: ", prob)
elif mes == 2:
    trans = 31 + dia
    prob = (trans / 365) * 100
    print("Hola", nombre, "la probabilidad de que hayas cumplido annos en ",anno, "es de: ", prob)
elif mes == 3:
    trans = 31 + 28 + dia
    prob = (trans / 365) * 100
    print("Hola", nombre, "la probabilidad de que hayas cumplido annos en ",anno, "es de: ", prob)
elif mes == 4:
    trans = 31 + 28 + 31 + dia
    prob = (trans / 365) * 100
    print("Hola", nombre, "la probabilidad de que hayas cumplido annos en ",anno, "es de: ", prob)
elif mes == 5:
    trans = 31 + 28 + 31 + 30 + dia
    prob = (trans / 365) * 100
    print("Hola", nombre, "la probabilidad de que hayas cumplido annos en ",anno, "es de: ", prob)
elif mes == 6:
    trans = 31 + 28 + 31 + 30 + 31 + dia
    prob = (trans / 365) * 100
    print("Hola", nombre, "la probabilidad de que hayas cumplido annos en ",anno, "es de: ", prob)
elif mes == 7:
    trans = 31 + 28 + 31 + 30 + 31 + 30 + dia
    prob = (trans / 365) * 100
    print("Hola", nombre, "la probabilidad de que hayas cumplido annos en ",anno, "es de: ", prob)
elif mes == 8:
    trans = 31 + 28 + 31 + 30 + 31 + 30 + 31 + dia
    prob = (trans / 365) * 100
    print("Hola", nombre, "la probabilidad de que hayas cumplido annos en ",anno, "es de: ", prob)
elif mes == 9:
    trans = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + dia
    prob = (trans / 365) * 100
    print("Hola", nombre, "la probabilidad de que hayas cumplido annos en ",anno, "es de: ", prob)
elif mes == 10:
    trans = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dia
    prob = (trans / 365) * 100
    print("Hola", nombre, "la probabilidad de que hayas cumplido annos en ",anno, "es de: ", prob)
elif mes == 11:
    trans = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dia 
    prob = (trans / 365) * 100
    print("Hola", nombre, "la probabilidad de que hayas cumplido annos en ",anno, "es de: ", prob)
elif mes == 12:
    trans = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dia 
    prob = (trans / 365) * 100
    print("Hola", nombre, "la probabilidad de que hayas cumplido annos en ",anno, "es de: ", prob)    
else:
    print("Hola", nombre, "has introducido un dato incorrecto")

# # if strCumplidos == "Si":
# #     print("Hola", nombre, "Naciste en el año",anno-edad)
# # else:
# #     print("Hola", nombre, "Naciste en el año",anno-edad-1)
