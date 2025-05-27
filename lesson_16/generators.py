# generators.py

# Генератор парних чисел від 0 до N
def even_numbers_generator(N):
    for num in range(0, N + 1):
        if num % 2 == 0:
            yield num

# Генератор чисел Фібоначчі до N
def fibonacci_generator(N):
    a, b = 0, 1
    while a <= N:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("Генератор парних чисел до 10:")
    for even in even_numbers_generator(10):
        print(even, end=" ")
    print("\n")

    print("Генератор Фібоначчі до 20:")
    for fib in fibonacci_generator(20):
        print(fib, end=" ")
    print("\n")
