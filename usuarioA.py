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
    
    
    texto = str(numero)
    # El [::-1] da vuelta todo el texto de forma exacta
    if texto == texto[::-1]:
        print(f"¡Si! El número {numero} es capicúa de principio a fin.")
    else:
        print(f"No, el número {numero} no es capicúa.")
    
    print()
    input("presiona enter para continuar...")

def es_perfecto(numero):
    
    for i in numero: 
        print(i)
    if numero == i:
        print("Es perfecto")
    