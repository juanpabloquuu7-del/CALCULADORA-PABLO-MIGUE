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
