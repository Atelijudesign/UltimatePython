edad = int(input("¿Cuál es tu edad? "))

if 18 <= edad < 65:
#if edad >= 18 and edad < 65:
    print("Eres mayor de edad, puedes ver la pelicula")
elif edad >= 65:
    print("Eres mayor de edad, Tines un super descuento!!")
else:
    print("Eres menor de edad, no puedo ver la pelicula")
