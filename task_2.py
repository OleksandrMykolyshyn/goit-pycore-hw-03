import random

def get_numbers_ticket(min_value, max_value, quantity):
    # Перевірка валідності параметрів
    if (
        not isinstance(min_value, int) or not isinstance(max_value, int) or not isinstance(quantity, int)
        or min_value < 1
        or max_value > 1000
        or quantity < 1
        or quantity > (max_value - min_value + 1)
    ):
        return []

    # Генерація унікальних чисел
    numbers = random.sample(range(min_value, max_value + 1), quantity)

    # Повертаємо відсортований список
    return sorted(numbers)

# Приклад використання

min_value = int(input("Від якого числа: "))
max_value = int(input("До якого числа: "))
quantity = int(input("Скільки чисел вибрати: "))

lottery_numbers = get_numbers_ticket(min_value, max_value, quantity)
print("Ваші лотерейні числа:", lottery_numbers)