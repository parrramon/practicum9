with open('input.txt', 'r', encoding='utf-8') as f1:
    text = f1.read()

result = text.upper()

with open('output.txt', 'w', encoding='utf-8') as f2:
    f2.write(result)