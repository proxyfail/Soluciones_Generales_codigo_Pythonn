# Este programa permite crear usuarios y generar un código cifrado único para cada uno de ellos.
# Utiliza el algoritmo SHA-256 para cifrar el nombre del usuario.

import hashlib

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.codigo_cifrado = self.generar_codigo_cifrado(nombre)

    def generar_codigo_cifrado(self, texto):
        sha256 = hashlib.sha256()
        sha256.update(texto.encode('utf-8'))
        return sha256.hexdigest()

def main():
    usuarios = []

    print("=== Sistema de Creación de Usuarios ===")

    while True:
        entrada = input("Ingrese el nombre del usuario (o 'salir' para terminar): ")
        if entrada.lower() == 'salir':
            break

        nuevo_usuario = Usuario(entrada)
        usuarios.append(nuevo_usuario)
        print(f"Usuario creado: {nuevo_usuario.nombre}")
        print(f"Código cifrado: {nuevo_usuario.codigo_cifrado}\n")

    print("\nUsuarios registrados:")
    for usuario in usuarios:
        print(f"- {usuario.nombre}: {usuario.codigo_cifrado}")

if __name__ == "__main__":
    main()
