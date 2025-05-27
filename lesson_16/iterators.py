# iterators.py

# Ітератор для зворотного виведення елементів списку
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

# Ітератор, який повертає всі парні числа в діапазоні від 0 до N
class EvenNumbersIterator:
    def __init__(self, N):
        self.current = 0
        self.N = N

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.N:
            num = self.current
            self.current += 1
            if num % 2 == 0:
                return num
        raise StopIteration


if __name__ == "__main__":
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
