def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci_sequence(n):
    for i in range(n):
        print(fibonacci(i), end=" ")


if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci terms to print: "))
    print("Fibonacci Sequence:")
    print_fibonacci_sequence(n)