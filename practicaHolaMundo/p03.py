nombre = input("Como te llamas ")
strEdad = input("Que edad tienes? ")
strAnno = input("Que año es? ")
strCumplidos = input("Cumpliste ya? ")
edad = int(strEdad)
anno = int(strAnno)
if strCumplidos == "Si":
    print("Hola", nombre, "Naciste en el año",anno-edad)
else:
    print("Hola", nombre, "Naciste en el año",anno-edad-1)