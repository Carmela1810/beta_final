import re

# Lista para almacenar los registros
registros = []

# Función para introducir un nuevo registro
def introducir_registro():
    nombre = input("Ingrese el nombre: ")
    while not re.match("^[A-Za-z\s]*$", nombre):
        print("Nombre inválido. Solo se permiten letras y espacios.")
        nombre = input("Ingrese el nombre: ")

    edad = input("Ingrese la edad: ")
    while not edad.isdigit() or int(edad) < 0:
        print("Edad inválida. Debe ser un número positivo.")
        edad = input("Ingrese la edad: ")

    email = input("Ingrese el email: ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Email inválido. Introduzca un email válido.")
        email = input("Ingrese el email: ")

    registro = {
        "nombre": nombre,
        "edad": int(edad),
        "email": email
    }
    registros.append(registro)
    print("Registro introducido con éxito.")

# Función para modificar un registro existente
def modificar_registro():
    listar_registros()
    if not registros:
        return
    
    indice = input("Ingrese el índice del registro a modificar: ")
    while not indice.isdigit() or int(indice) < 0 or int(indice) >= len(registros):
        print("Índice inválido. Introduzca un índice válido.")
        indice = input("Ingrese el índice del registro a modificar: ")

    indice = int(indice)
    print("Deje en blanco cualquier campo que no desee cambiar.")

    nombre = input(f"Ingrese el nuevo nombre (actual: {registros[indice]['nombre']}): ")
    if nombre:
        while not re.match("^[A-Za-z\s]*$", nombre):
            print("Nombre inválido. Solo se permiten letras y espacios.")
            nombre = input("Ingrese el nuevo nombre: ")
        registros[indice]['nombre'] = nombre

    edad = input(f"Ingrese la nueva edad (actual: {registros[indice]['edad']}): ")
    if edad:
        while not edad.isdigit() or int(edad) < 0:
            print("Edad inválida. Debe ser un número positivo.")
            edad = input("Ingrese la nueva edad: ")
        registros[indice]['edad'] = int(edad)

    email = input(f"Ingrese el nuevo email (actual: {registros[indice]['email']}): ")
    if email:
        while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Email inválido. Introduzca un email válido.")
            email = input("Ingrese el nuevo email: ")
        registros[indice]['email'] = email

    print("Registro modificado con éxito.")

# Función para imprimir la lista de registros
def listar_registros():
    if not registros:
        print("No hay registros para mostrar.")
        return
    for i, registro in enumerate(registros):
        print(f"Registro {i}: {registro}")

# Menú principal
def menu():
    while True:
        print("\nMenú:")
        print("1. Introducir Registro")
        print("2. Modificar Registro")
        print("3. Imprimir Lista de Registros")
        print("4. Salir")

        opcion = input("Elija una opción: ")
        if opcion == '1':
            introducir_registro()
        elif opcion == '2':
            modificar_registro()
        elif opcion == '3':
            listar_registros()
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Por favor, elija nuevamente.")

if __name__ == '__main__':
    menu()