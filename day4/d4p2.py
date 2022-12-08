with open('d4.txt') as f:
    lines = [line.rstrip() for line in f]

# Black magic to check if two lists overlap
# This method uses sets to create the ranges from the given lower and upper bounds, and then uses the & (intersection) operator to find the overlap, if any, between the two sets. The bool function is then used to convert the resulting set to a boolean value, which will be True if the sets have any elements in common, and False otherwise.
def is_overlapping(range1, range2):
    lower1, upper1 = range1
    lower2, upper2 = range2
    return bool(set(range(lower1, upper1+1)) & set(range(lower2, upper2+1)))

n1p1 = []
n1p2 = []
n2p1 = []
n2p2 = []
buffer = ""
seperator = "-"
score = 0

# Prepare the list
buffer=seperator.join(lines)
lines=buffer.split(',')
buffer = ""
seperator = "-"
buffer=seperator.join(lines)
lines=buffer.split('-')

# Split the list into 4
index = 0
while index < len(lines):
    n1p1.append(int(lines[index]))
    index +=4

index = 1
while index < len(lines):
    n1p2.append(int(lines[index]))
    index +=4

index = 2
while index < len(lines):
    n2p1.append(int(lines[index]))
    index +=4

index = 3
while index < len(lines):
    n2p2.append(int(lines[index]))
    index +=4

# Check if one range overlaps the other
for x in range(len(n1p1)):
    if is_overlapping((n1p1[x], n1p2[x]), (n2p1[x], n2p2[x])):
        score += 1

input(score)