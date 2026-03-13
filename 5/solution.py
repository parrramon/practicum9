try:
    with open('input.txt', 'r', encoding='utf-8') as f1:
        numbers = [int(line.strip()) for line in f1 if line.strip()]
        a, b, c = numbers

        operation = a / b + c
        with open('output.txt', 'w', encoding='utf-8') as f2:
            f2.write(str(operation))
except (ValueError, IndexError):
    with open('output.txt', 'w', encoding='utf-8') as f2:
        f2.write('Обнаружена ошибка записи чисел')
except ZeroDivisionError:
    with open('output.txt', 'w', encoding='utf-8') as f2:
        f2.write('На ноль делить нельзя')

