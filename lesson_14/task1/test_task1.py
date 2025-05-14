from task1 import TeamLead

# Перевіряю, чи TeamLead має всі необхідні атрибути
def test_teamlead_attributes():
    # Створюю об'єкт TeamLead
    lead = TeamLead("Vladyslav", 4000, "QA", "Python", 5)

    # Перевіряю, чи коректно зберігаються всі атрибути
    assert lead.name == "Vladyslav"  # Ім’я
    assert lead.salary == 4000  # Зарплата
    assert lead.department == "QA"  # Відділ
    assert lead.programming_language == "Python"  # Мова програмування
    assert lead.team_size == 5  # Розмір команди