from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        # Перетворюємо рядок дати у об'єкт datetime (лише дата без часу)
        input_date = datetime.strptime(date, '%Y-%m-%d').date()

        # Поточна дата
        today = datetime.today().date()

        # Різниця в днях: сьогодні мінус задана дата
        delta = today - input_date

        return delta.days
    except ValueError:
        raise ValueError("Невірний формат дати. Очікується 'РРРР-ММ-ДД'.")
    
print(get_days_from_today('2025-06-27'))  