import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр і плюса
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    # Якщо номер починається з '+', перевіряємо, чи це +380
    if cleaned.startswith("+"):
        if not cleaned.startswith("+380"):
            # Якщо не +380, можемо залишити як є або адаптувати під інші умови
            return cleaned
        return cleaned  # вже правильний формат

    # Якщо починається з '380' без '+'
    if cleaned.startswith("380"):
        return f"+{cleaned}"

    # Якщо це просто локальний номер — додаємо код країни
    return f"+38{cleaned}"

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери:", sanitized_numbers)