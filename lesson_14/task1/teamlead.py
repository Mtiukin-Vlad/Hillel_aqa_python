# Базовий клас Employee
class Employee:
    def __init__(self, name, salary, **kwargs):
        super().__init__(**kwargs)  # Викликаю наступний конструктор в MRO
        self.name = name  # Ім’я працівника
        self.salary = salary  # Зарплата працівника

# Клас Manager наслідується від Employee
class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)  # Викликаю конструктор Employee
        self.department = department  # Відділ менеджера

# Клас Developer наслідується від Employee
class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)  # Викликаю конструктор Employee
        self.programming_language = programming_language  # Мова програмування

# Клас TeamLead наслідує і від Manager, і від Developer
class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        # Викликаю super(), який проходить по MRO
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language,
        )
        self.team_size = team_size  # Розмір команди
