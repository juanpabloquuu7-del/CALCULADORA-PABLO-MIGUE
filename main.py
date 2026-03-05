from usuarioA import serie_fibonacci, es_capicua,es_perfecto

def menu():
    while True:
        print("\n===============================")
        print("    CALCULADORA MATEMÁTICA")
        print("===============================")
        print("1. Serie Fibonacci")
        print("2. Número Capicúa")
        print("3. Número Perfecto")
        print("4. Números Primos en un Rango")
        print("5. Verificar si es Primo")
        print("6. Factorial")
        print("7. Máximo Común Divisor (MCD)")
        print("8. Salir")
        print("===============================")
        
        opcion = input("Seleccione una opción (1-8): ")

        if opcion == "1":
                n = int(input("¿Cuántos términos de Fibonacci desea ver?: "))
                serie_fibonacci(n)
        elif opcion == "2":
                num_input = input("Ingrese el número para verificar si es capicúa: ")
                num_validado = int(num_input)
                es_capicua(num_validado)
        elif opcion == "3":
                num = int(input("Ingrese el número para verificar si es perfecto: "))
                es_perfecto(num)
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        elif opcion == "6":
            pass
        elif opcion == "7":
            pass
        elif opcion == "8":
            pass
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()