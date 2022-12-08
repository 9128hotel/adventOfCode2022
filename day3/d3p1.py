import string

with open('d3.txt') as f:
    lines = [line.rstrip() for line in f]

comp1 = []
comp2 = []
intersect = []
letters = list(string.ascii_letters) # Create a list of ascii letters
numbers = list(range(1, len(letters)+1)) # Create a list of all numbers from 1 to the length of letters

for x in range(len(lines)): # Get the two halves of backpack contents
    comp1.append(lines[x][0:len(lines[x])//2])
    comp2.append(lines[x][len(lines[x])//2 if len(lines[x])%2 == 0 else ((len(lines[x])//2)+1):])

for x in range(len(comp1)): # Find the char in both lists
    intersect.append(''.join(set(comp1[x]).intersection(comp2[x])))

for x in range(len(intersect)): # Translate each char to an int
    intersect[x] = numbers[letters.index(intersect[x])]

result = sum(intersect) # Add all the numbers together

input(result)