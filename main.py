# Мой первый скрипт для портфолио
name = "Даврон"
goal = "Заработать на i7-3610QM и собрать пушку-ноут"

print(f"Привет! Меня зовут {name}.")
print(f"Моя текущая цель: {goal}")

# Маленький калькулятор для заказов
def estimate_order(hours, rate_per_hour):
    return hours * rate_per_hour

print(f"Если я буду работать 3 часа по 2000 тенге, я заработаю: {estimate_order(3, 2000)} тенге!")
