def recursive_nth_fibo(n):

    if n <=0: #podminka ukonceni
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)

def main():
    n = int(input("Zadejte počet prvků Fibonacciho posloupnosti: "))
    seznam = list()
    for i in range(n):
        seznam.append(recursive_nth_fibo(i))
    print(seznam)
    print(seznam[-1])
    # poro in=4 [0, 1, 1, 2] #1,1 pro jeden par kraliku mam 1 moznost


if __name__ == "__main__":
    main()


