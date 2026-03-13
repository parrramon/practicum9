import os

os.makedirs('simple', exist_ok=True)

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

even_lines = lines[1::2]

with open(os.path.join('simple', 'output.txt'), 'w', encoding='utf-8') as f:
    f.writelines(even_lines)
