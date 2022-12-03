with open('day1\d1.txt') as f:
    lines = [line.rstrip() for line in f]

cal = 0
elf = 0
calperelf = []

for x in range(0, len(lines)):
    if lines[x] == '':
        calperelf.append(cal)
        cal = 0
    else:
        cal += int(lines[x])

print(sum(sorted(calperelf, reverse=True)[:3]))