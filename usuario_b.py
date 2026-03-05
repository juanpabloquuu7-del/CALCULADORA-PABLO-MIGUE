#4. NÚMEROS PRIMOS EN UN RANGO

def primos_en_rango():
    while True:
        try:
            inicio = int(input("Desde qué número: "))
            fin = int(input("Hasta qué número: "))
            break
        except:
            print("Escribe un número entero, porfa.")

    if inicio > fin:
        inicio, fin = fin, inicio
    lista_primos = []
    for num in range(inicio, fin + 1):
        if num < 2:
            continue

        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        
        if es_primo:
            lista_primos.append(num)
            
    print(lista_primos)
    input ("Presione cualquier tecla para continuar -->")


#5. Es primo?

def verificar_si_es_primo():

    while True:
        try:
            n = int(input("Introduce el número que quieres verificar: "))
            break
        except:
            print("Escribe un número entero, porfa.")

    es_primo = True
    if n < 2:
        es_primo = False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                es_primo = False
                break
    
    if es_primo:
        print(f"El número {n} sí es primo.")
    else:
        print(f"El número {n} no es primo.")
    input ("Presione cualquier tecla para continuar -->")
