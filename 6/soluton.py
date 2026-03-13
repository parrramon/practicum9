with open('input.txt', 'r', encoding='utf-8') as f1:
    text = f1.read()
    lines = text.split('\n')

with open('output.txt', 'w', encoding='utf-8') as f2:
    try:
        n = int(lines[0])
        count = len(lines[1:])

        if count == n:
            f2.write('TRUE')
        else:
            f2.write('FALSE')

    except ValueError:
        f2.write('ERROR')


