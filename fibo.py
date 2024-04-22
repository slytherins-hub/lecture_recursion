def recursive_nth_fibo(n):
    """
    Returns n-th value of Fibonaci sequence
    :param n: (int) position of value
    :return: (int) value at n-th position
    """
    if n <= 1:
        return n
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)


def main():
    print(recursive_nth_fibo(6))


if __name__ == "__main__":
    main()
