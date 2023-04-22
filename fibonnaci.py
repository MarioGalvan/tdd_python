def make_fibonnaci(n):
    # Inicializar la secuencia de Fibonacci
    fib = [0, 1]

    # Generar los valores subsiguientes de Fibonacci
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    return fib[:n]
