import random

# генерируются рандомные числа

with open('input.txt', 'w') as f1:

    for _ in range(365):
        steps = random.randint(2000, 25000)
        f1.write(f"{steps}\n")

months = [
    'Январь', "Февраль", "Март", "Апрель",
    "Май", "Июнь", "Июль", "Август",
    "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
]

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open('input.txt', 'r', encoding='utf-8') as f1:
    steps = [int(line.strip()) for line in f1]

index = 0

with open('output.txt', 'w', encoding='utf-8') as f2:
    for i in range(12):
        days = month_days[i]
        month_steps = steps[index:index + days]
        average = sum(month_steps) / days
        f2.write(f"{months[i]}: {round(average)}\n")
        index += days



