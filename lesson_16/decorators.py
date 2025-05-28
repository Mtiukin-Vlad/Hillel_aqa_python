# Декоратор для логування аргументів та результатів функції
def log_decorator(func):
    def wrapper(*args, **kwargs):
        # Логую аргументи функції
        print(f"Виклик функції {func.__name__} з аргументами {args} {kwargs}")
        result = func(*args, **kwargs)
        # Логую результат функції
        print(f"Функція {func.__name__} повернула {result}")
        return result
    return wrapper

# Декоратор для обробки винятків у функції
def exception_handler_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            # Працюю з функцією в блоці try
            return func(*args, **kwargs)
        except Exception as e:
            # Якщо сталася помилка, виводжу її і не даю програмі впасти
            print(f"Виняток у функції {func.__name__}: {e}")
    return wrapper
