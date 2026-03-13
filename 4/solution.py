with open('input.txt', 'r', encoding='utf-8') as f1:
    lines = f1.readlines()
with open('output.txt', 'w', encoding='utf-8') as f2:
    for line in lines:
        if len(line.rstrip('\n')) > 20:
            f2.write(line)