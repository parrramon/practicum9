with open('input.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
filtered = [line for line in lines if line.strip() != '100']

with open('input.txt', 'w', encoding='utf-8') as f:
    f.writelines(filtered)

