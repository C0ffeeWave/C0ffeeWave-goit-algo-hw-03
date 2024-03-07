# Перша задача
import datetime

def get_days_from_today(date: str) -> int:
    try:
        # Перетворюємо рядок дати на об'єкт datetime
        input_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        # Поточна дата
        current_date = datetime.datetime.today()
        # Різниця між поточною датою та заданою датою
        days_difference = (current_date - input_date).days
        return days_difference
    except ValueError:
        # Обробка винятку неправильного формату
        return "Неправильний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'."