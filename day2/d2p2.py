with open('d2.txt') as f:
    lines = [line.rstrip() for line in f]

opch = []
result = []
score = 0

# Load opchoice and results
for word in lines:
    opch.append(word[0])
    result.append(word[2])

# Checks results and op plays and calculates scores by figuring out what friendly would need to play to win
for x in range(0, len(opch)):
    if result[x] == 'Z':
        score += 6
        if opch[x] == 'A':
            score += 2 # Op chooses rock, I must choose paper to win
        elif opch[x] == 'B':
            score += 3 # Op chooses paper, I must choose scissors to win
        elif opch[x] == 'C':
            score += 1 # Op chooses scissors, I must choose rock to win
    elif result[x] == 'Y':
        score += 3
        if opch[x] == 'A': # All of these are draws
            score += 1
        elif opch[x] == 'B':
            score += 2
        elif opch[x] == 'C':
            score += 3
    else:
        if opch[x] == 'A':
            score += 3 # Op chooses rock, I must choose scissors to loose
        elif opch[x] == 'B':
            score += 1 # Op chooses paper, I must choose rock to loose
        elif opch[x] == 'C':
            score += 2 # Op chooses scissors, I must choose paper to loose

print(score)