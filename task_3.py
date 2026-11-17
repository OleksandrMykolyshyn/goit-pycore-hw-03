import re


def normalize_phone(phone_number):
    # Видаляємо все, крім цифр і плюса
    cleaned = re.sub(r"[^\d+]", "", phone_number)

    # Якщо міжнародний код уже з плюсом
    if cleaned.startswith("+"):
        return cleaned

    # Якщо є 380, додаємо лише плюс
    if cleaned.startswith("380"):
        return f"+{cleaned}"

    # Для місцевого номера додаємо +38
    return f"+38{cleaned}"

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)