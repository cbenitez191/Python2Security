import hashlib


hash_file = "459567d3bde4418b7fe302ff9809c4b0befaf7dd"

dic_file = input("Ingrese la direccion del archivo del diccionario: ")

with open(dic_file, 'r') as file:

    diccionary = [line.strip() for line in file]

    for password in diccionary:
    
        hash_calculated = hashlib.sha1(password.encode()).hexdigest()

        if hash_calculated == hash_file:

            print("La contraseña original es: " + password)
            break
        else:
            print:("La contraseña mp se encuentra en el diccionario")

    
    

