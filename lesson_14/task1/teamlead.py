class Employee:
    def __init__(self, name, salary):
        # Ініціалізую ім’я та зарплату співробітника.
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        # Викликаю конструктор базового класу Employee
        super().__init__(name, salary)
        # Ініціалізую відділ менеджера.
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # Викликаю конструктор базового класу Employee
        super().__init__(name, salary)
        # Ініціалізую мову програмування розробника
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        # Явно викликаю конструктор базового класу Employee,
        # щоб уникнути проблем з множинним наслідуванням
        Employee.__init__(self, name, salary)
        # Ініціалізую відділ
        self.department = department
        # Ініціалізую мову програмування
        self.programming_language = programming_language
        # Ініціалізую розмір команди
        self.team_size = team_size