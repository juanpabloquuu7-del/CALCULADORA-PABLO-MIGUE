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
    
    for i in numero:
    print(i)

def es_perfecto(numero):
    
    pass