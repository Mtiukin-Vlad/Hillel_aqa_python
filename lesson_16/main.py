from generators import even_numbers_generator, fibonacci_generator
from iterators import ReverseIterator, EvenNumbersIterator
from decorators import log_decorator, exception_handler_decorator


def test_generators():
    print("Генератор парних чисел до 10:")
    for even in even_numbers_generator(10):
        print(even, end=" ")
    print("\n")

    print("Генератор Фібоначчі до 20:")
    for fib in fibonacci_generator(20):
        print(fib, end=" ")
    print("\n")


def test_iterators():
    print("Ітератор для зворотного виведення списку [1, 2, 3, 4, 5]:")
    rev_iter = ReverseIterator([1, 2, 3, 4, 5])
    for item in rev_iter:
        print(item, end=" ")
    print("\n")

    print("Ітератор для парних чисел від 0 до 10:")
    even_iter = EvenNumbersIterator(10)
    for num in even_iter:
        print(num, end=" ")
    print("\n")


def test_decorators():
    @log_decorator
    def multiply(a, b):
        return a * b

    print("Виклик декорованої функції multiply(3, 4):")
    multiply(3, 4)
    print()

    @exception_handler_decorator
    def divide(a, b):
        return a / b

    print("Виклик декорованої функції divide(10, 0) з обробкою винятків:")
    divide(10, 0)


if __name__ == "__main__":
    test_generators()
    test_iterators()
    test_decorators()
