import string
import random

length = int(input("Ingrese la contrasela: "))

char = string.ascii_letters + string.digits + string.punctuation

pass = "".join(rando.choice(char) for i in range(length) )
print("La contraseña segura es: " + pass)

#Generar una contrasela apartir de un texto
