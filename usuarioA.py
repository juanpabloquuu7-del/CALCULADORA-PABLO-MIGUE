def serie_fibonacci(n):
    
    if n <= 0:

        print("Por favor, ingrese un número entero mayor a 0.")

        return


    a, b = 0, 1

    print(f"Los primeros {n} términos son:")


    for _ in range(n):

        print(a, end=" ")

        

        a, b = b, a + b

    print()

    input("presiona enter para continuar...")



def es_capicua(numero):
    
    n_str = str(numero)
    
    if n_str[0] == n_str[-1]:
        print(f"El número {numero} es capicúa")
    else:
        print(f"El número {numero} NO es capicúa")
    input("Presiona enter para continuar...")

def es_perfecto(numero):
    
    pass