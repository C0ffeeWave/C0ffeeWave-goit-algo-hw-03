#Друга задача
import random

def get_numbers_ticket(min_value, max_value, quantity):
    lottery_numbers = [random.randint(min_value, max_value) for _ in range(quantity)]
    return lottery_numbers

# Тест
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
