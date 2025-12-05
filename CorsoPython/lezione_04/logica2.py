import matplotlib.pyplot as plt

"""
dato un numero n positivo, restituire una lista con i primi n numeri di fibonacci
"""

def lista_fibonacci(n: int) -> list[int]:
    # 0 1 1 2 3 5 8 13 21
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci = [0, 1]

    for i in range(2, n):
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])
    return fibonacci

"""
dato un numero n positivo, restituire l'ennesimo numero di fibonacci (partendo da 0, 1)
"""

def calc_fibonacci(n: int) -> int:
    # fib[i] = fib [i-2] + fib [i-1]
    if n ==1:
        return 0
    elif n==2:
        return 1
    finestra = [0, 1, 1]
    for i in range(2, n):
        finestra [2] = finestra[0] + finestra[1]
        finestra[0] = finestra[1]
        finestra[1] = finestra[2]
    return finestra[2]

"""
scriviamo un while per ottenere le sequenze di collatz di n
"""

def sequenza_collatz(n: int) -> list[int]:
    sequenza = []
    while n != 1: # finchè n rimane diverso da 1
        if n % 2 == 0:
            n = n // 2
        else :
            n = 3 * n + 1 # n += 3, n += 1
        sequenza.append(n)
    return sequenza

def plot_sequenza(lista:list) -> None:
    plt.plot(lista)
    plt.show()


if __name__ == "__main__":
    print(lista_fibonacci(30))
    print(calc_fibonacci(30))
    print(sequenza_collatz(250)) # divide per 2 e moltiplica per 3 + 1
    plot_sequenza(sequenza_collatz(1001))