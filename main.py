def addmultiplenumbers(numeros):
    return sum(numeros)


def multiplymultiplenumbers(numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


# Alias por si tu enunciado usa el nombre en español
def multiplicamultiplenumeros(numeros):
    return multiplymultiplenumbers(numeros)


def multiplicamultiplenúmeros(numeros):
    return multiplymultiplenumbers(numeros)


def isitaninteger(num):
    try:
        return num == int(num)
    except (ValueError, TypeError):
        return False


def isiteven(num):
    return isitaninteger(num) and num % 2 == 0


def main():
    print("Calculadora mejorada")

    while True:
        print("\nElige una opción:")
        print("1. Sumar varios números")
        print("2. Multiplicar varios números")
        print("3. Saber si un número es par")
        print("4. Saber si un número es entero")
        print("5. Salir")

        opcion = input("Opción: ").strip()

        if opcion == "5":
            print("¡Adiós!")
            break

        elif opcion == "1" or opcion == "2":
            entrada = input("Ingresa números separados por espacio: ")
            try:
                numeros = [float(x) for x in entrada.split()]
            except ValueError:
                print("Entrada inválida.")
                continue

            if opcion == "1":
                print("Resultado:", addmultiplenumbers(numeros))
            else:
                print("Resultado:", multiplymultiplenumbers(numeros))

        elif opcion == "3":
            try:
                num = float(input("Ingresa un número: "))
                print(isiteven(num))
            except ValueError:
                print("Entrada inválida.")

        elif opcion == "4":
            try:
                num = float(input("Ingresa un número: "))
                print(isitaninteger(num))
            except ValueError:
                print("Entrada inválida.")

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
    