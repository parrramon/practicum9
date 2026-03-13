with open('input.txt', 'r', encoding='utf-8') as f1:
    lines = f1.readlines()
with open('output.txt', 'w', encoding='utf-8') as f2:
    for line in lines:
        if line.lower().startswith('a'):
            f2.write(line)
