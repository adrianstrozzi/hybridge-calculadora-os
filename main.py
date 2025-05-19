import dividir
import multiplicacion
import resta
import sumar
import suma_avanzada

def mostrar_menu():
    print("\nCalculadora:\n")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Suma avanzada (multiples números)")
    print("6 - Salir\n")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción:")

        if opcion == "1":
            a = float(input("\nIngresa el primer número:"))
            b = float(input("Ingresa el segundo número:"))
            print("\nResultado de SUMA:", sumar.sumar(a, b))

        elif opcion == "2":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("\nResultado de RESTA:", resta.restar(a, b))

        elif opcion == "3":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("\nResultado de MUTIPLICACIÓN:", multiplicacion.multiplicar(a, b))

        elif opcion == "4":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("\nResultado de DIVISIÓN:", dividir.dividir(a, b))

        elif opcion == "5":
            numeros = input("Ingresa los números separados por espacio: ").split()
            numeros = [float(num) for num in numeros]
            print("\nResultado de SUMA AVANZADA:", suma_avanzada.suma_avanzada(*numeros))

        elif opcion == "6":
            print("\nSaliendo.\n")
            break

        else:
            print("\nOpción no válida.")