
def recursive_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)





def main():
    print(recursive_nth_fibo(30) / recursive_nth_fibo(29))


if __name__ == "__main__":
    main()
