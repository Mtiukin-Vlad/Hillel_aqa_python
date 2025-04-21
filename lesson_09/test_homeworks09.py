import pytest
from homeworks import total_area, count_products, laptop_cost

# Тести для total_area
class TestTotalArea:

    def test_total_area_normal(self):
        result = total_area(436402, 37800)
        expected = 474202  # Загальна площа Чорного та Азовського морів
        assert result == expected, f"Очікувалось {expected}, отримано {result}"

    def test_total_area_zero(self):
        result = total_area(0, 0)
        expected = 0  # Якщо обидві площі 0, то результат теж 0
        assert result == expected, f"Очікувалось {expected}, отримано {result}"

    def test_total_area_large_values(self):
        result = total_area(1_000_000, 2_000_000)
        expected = 3_000_000  # Загальна площа двох великих морів
        assert result == expected, f"Очікувалось {expected}, отримано {result}"

    def test_total_area_one_zero(self):
        result = total_area(100, 0)
        expected = 100  # Якщо площа одного моря 0, то результат дорівнює площі іншого
        assert result == expected, f"Очікувалось {expected}, отримано {result}"

# Негативні перевирки
    def test_total_area_with_string(self):
        with pytest.raises(TypeError):
            total_area("100", 200)


# Тести для count_products
class TestCountProducts:

    def test_count_products_standard_case(self):
        result = count_products(375291, 250449, 222950)
        expected = (152341, 98108, 124842)  # Кількість товарів на кожному зі складів
        assert result == expected, f"Очікувалось {expected}, отримано {result}"

    def test_count_products_all_zero(self):
        result = count_products(0, 0, 0)
        expected = (0, 0, 0)  # Якщо всі складські запаси 0, то на кожному складі 0 товарів
        assert result == expected, f"Очікувалось {expected}, отримано {result}"

    def test_count_products_balanced_values(self):
        result = count_products(300, 200, 200)
        expected = (100, 100, 100)  # Якщо товар розподілений рівномірно, кожен склад має однакову кількість товарів
        assert result == expected, f"Очікувалось {expected}, отримано {result}"

    def test_count_products_negative_check(self):
        result = count_products(500, 350, 300)
        # Перевіряємо, що всі значення є невід'ємними цілими числами
        assert all(isinstance(x, int) and x >= 0 for x in result), f"Очікувалось, що всі значення позитивні, отримано {result}"

# Негативні перевирки
    def test_count_products_with_string_input(self):
        with pytest.raises(TypeError):
            count_products("1000", 500, 400)


# Тести для laptop_cost
class TestLaptopCost:

    def test_laptop_cost_standard_case(self):
        result = laptop_cost(1179, 18)
        expected = 21222  # Загальна вартість комп'ютера при таких умовах
        assert result == expected, f"Очікувалось {expected}, отримано {result}"

    def test_laptop_cost_zero_payment(self):
        result = laptop_cost(0, 18)
        expected = 0  # Якщо місячний платіж 0, то вартість комп'ютера буде 0
        assert result == expected, f"Очікувалось {expected}, отримано {result}"

    def test_laptop_cost_zero_months(self):
        result = laptop_cost(1000, 0)
        expected = 0  # Якщо кількість місяців 0, то загальна вартість буде 0
        assert result == expected, f"Очікувалось {expected}, отримано {result}"

    def test_laptop_cost_large_values(self):
        result = laptop_cost(10_000, 12)
        expected = 120_000  # Якщо вартість комп'ютера 10 000 грн на місяць, а термін кредиту 12 місяців
        assert result == expected, f"Очікувалось {expected}, отримано {result}"

# Негативні перевирки
    def test_laptop_cost_with_none_input(self):
        with pytest.raises(TypeError):
            laptop_cost(None, 12)

