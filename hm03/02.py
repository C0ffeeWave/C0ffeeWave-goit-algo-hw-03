#Друга задача
import random

def get_numbers_ticket(min_value, max_value, quantity):
    # Перевірка  параметрів
    if min_value < 1 or max_value > 1000 or quantity < 1 or quantity > (max_value - min_value + 1):
        return []
    # Генерація унікальних лотерейних чисел
    lottery_numbers = [random.randint(min_value, max_value) for _ in range(quantity)]
    return sorted(set(lottery_numbers))  # Видаляємо повторювані числа множиною і сортуємо

# Тест
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

