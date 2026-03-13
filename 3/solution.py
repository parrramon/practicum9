word = ''
with open('input.txt', 'r', encoding='utf-8') as f1:
    for line in f1:
        if line.strip():
            word += line[0]

with open('output.txt', 'w', encoding='utf-8') as f2:
    f2.write(word)