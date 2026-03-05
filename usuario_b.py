#4. NÚMEROS PRIMOS EN UN RANGO

def primos_en_rango(inicio, fin):
    lista_primos = []
    for num in range(inicio, fin + 1):
        if num < 2:
            continue
        
        # Lógica interna para verificar si es primo
        es_primo = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                es_primo = False
                break
        
        if es_primo:
            lista_primos.append(num)
            
    return lista_primos

