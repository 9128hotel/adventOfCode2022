with open('d2.txt') as f:
    lines = [line.rstrip() for line in f]

opch = []
frch = []
score = 0

# Load op- and friendly- choice
for word in lines:
    opch.append(word[0])
    frch.append(word[2])

# Calculate the scores based on wins/losses and choices
for x in range(0, len(opch)):
    if (frch[x] == 'X' and opch[x] == 'C') or (frch[x] == 'Y' and opch[x] == 'A') or (frch[x] == 'Z' and opch[x] == 'B'): # Figures out if you won
        score += 6
        if frch[x] == 'X':
            score += 1
        elif frch[x] == 'Y':
            score += 2
        elif frch[x] == 'Z':
            score += 3
    elif (opch[x] == 'A' and frch[x] == 'X') or (opch[x] == 'B' and frch[x] == 'Y') or (opch[x] == 'C' and frch[x] == 'Z'): # Figures out if you drew
        score += 3
        if frch[x] == 'X':
            score += 1
        elif frch[x] == 'Y':
            score += 2
        elif frch[x] == 'Z':
            score += 3
    else: # Assumes you lost
        if frch[x] == 'X':
            score += 1
        elif frch[x] == 'Y':
            score += 2
        elif frch[x] == 'Z':
            score += 3

print(score)