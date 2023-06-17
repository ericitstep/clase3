#Ejercicio: Implemente una de las siguientes tres estructuras de datos en Python (Pilas,Colas,Arboles)con 
#las siguientes funciones basicas: agregar, eliminar, buscar.

#Definimos la clase Pila con los metodos necesarios para realizar las operaciones: agregar,eliminar,buscar
class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return len(self.items) == 0

    def apilar(self, dato):
        self.items.append(dato)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

    def buscar(self, dato):
        if dato in self.items:
            return True
        return False

#Definimos el menu a mostrar al usuario para ejecuar la accion de su eleccion a la pila.
def mostrarMenu():
    print("1. Agregar elemento a la pila")
    print("2. Eliminar elemento de la pila")
    print("3. Buscar elemento en la pila")
    print("4. Salir")

#Creamos un objeto de la clase pila
pila = Pila()

# Creamos el bucle while que permite que el programa se ejecute continuamente hasta que se elija la 
# opcion de salir. 
while True:
    mostrarMenu()
    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        elemento = input("Ingrese el elemento a agregar: ")
        pila.apilar(elemento)
        print("Elemento agregado a la pila.")

    elif opcion == "2":
        if pila.esta_vacia():
            print("La pila esta vacia.")
        else:
            elemento = pila.desapilar()
            print(f"Elemento eliminado de la pila: {elemento}")

    elif opcion == "3":
        elemento = input("Ingrese el elemento a buscar: ")
        if pila.buscar(elemento):
            print("El elemento se encuentra en la pila.")
        else:
            print("El elemento no se encuentra en la pila.")

    elif opcion == "4":
        print("Fin del programa")
        break

    else:
        print("Opcion invalida. Por favor, ingrese una opcion valida.")
