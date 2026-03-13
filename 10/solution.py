days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_day_of_year(date_str):
    day, month = map(int, date_str.split('.'))
    days_before = sum(days_in_months[:month-1])
    return days_before + day

with open('input.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

current_date = lines[0]
current_day = get_day_of_year(current_date)
result = []

for line in lines[2:]:
    if not line.strip():
        continue

    line_parts = line.split()
    cell_num = line_parts[0]
    deposite_date = line_parts[1]

    deposite_day = get_day_of_year(deposite_date)

    duration = current_day - deposite_day

    if duration > 3:
        result.append(cell_num)

with open('output.txt', 'w', encoding='utf-8') as f:
    for cell in result:
        f.write(cell + '\n')