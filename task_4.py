from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            # Якщо день припадає на вихідний, переносимо на понеділок
            if congratulation_date.weekday() == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # Неділя
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": name,
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.06.28"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
