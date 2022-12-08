with open('d4.txt') as f:
    lines = [line.rstrip() for line in f]

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

# Check if one range contains the other
for x in range(len(n1p1)):
    if (n1p1[x] >= n2p1[x] and n2p2[x] >= n1p2[x]):
        score += 1
    elif (n1p1[x] <= n2p1[x] and n2p2[x] <= n1p2[x]):
        score += 1

input(score)