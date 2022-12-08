import string

with open('d3.txt') as f:
    lines = [line.rstrip() for line in f]

comp1 = []
comp2 = []
comp3 = []
intersect = []
letters = list(string.ascii_letters) 
numbers = list(range(1, len(letters)+1))

def weird_range_thing(start, end, step):
    while start <= end:
        yield start
        start += step

for x in weird_range_thing(2, len(lines)-1, 3): # Get the three sections
    print(lines[x])
    comp1.append(lines[x])
    comp2.append(lines[x-1])
    comp3.append(lines[x-2])

for x in range(len(comp1)): # Find the char in all three lists
    intersect.append(''.join(set(comp1[x]).intersection(comp2[x]).intersection(comp3[x])))

for x in range(len(intersect)): # Translate each char to an int
    intersect[x] = numbers[letters.index(intersect[x])]

result = sum(intersect) # Add all the numbers together

input(result)