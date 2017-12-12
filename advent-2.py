text = open('/Users/woo/CS497J/project/.idea/advent-2.txt', 'r')
all_rows = []

for line in text:
    row = line.split('\t')
    row = [int(x) for x in row]
    all_rows.append(sorted(row))

sum = 0


def find_even_division(row):
    """Row in ascending sorting order"""
    for i in reversed(range(len(row))):
        for j in reversed(range(i)):
            if row[i] % row[j] == 0:
                return row[i] / row[j]
    return 0


for row in all_rows:
    sum += find_even_division(row)

print(sum)