# Створюю базовий клас Employee з атрибутами ім'я та зарплата
class Employee:
    def __init__(self, name, salary):
        self.name = name  # Зберігаю ім’я працівника
        self.salary = salary  # Зберігаю зарплату працівника

# Створюю клас Manager, який наслідується від Employee
class Manager(Employee):
    def __init__(self, name, salary, department):
        # Явно викликаю конструктор батьківського класу Employee
        Employee.__init__(self, name, salary)
        self.department = department  # Зберігаю відділ, у якому працює менеджер

# Створюю клас Developer, який також наслідується від Employee
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # Явно викликаю конструктор батьківського класу Employee
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language  # Зберігаю мову програмування, яку використовує розробник

# Створюю клас TeamLead, який наслідується і від Manager, і від Developer
class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        # Явно викликаю конструктор класу Employee, щоб уникнути конфлікту з MRO
        Employee.__init__(self, name, salary)
        self.department = department  # Зберігаю відділ як у менеджера
        self.programming_language = programming_language  # Зберігаю мову програмування як у розробника
        self.team_size = team_size  # Зберігаю кількість учасників команди, якою керую
