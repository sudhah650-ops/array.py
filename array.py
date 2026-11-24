# Array of Scores

scores = []

n = int(input("Enter the number of scores: "))

for i in range(n):
    score = float(input("Enter score: "))
    scores.append(score)

# Calculate sum and average
total = sum(scores)
average = total / n

print("\nScores:", scores)
print("Sum of scores:", total)
print("Average of scores:", average)

# Find maximum and minimum scores
print("Maximum score:", max(scores))
print("Minimum score:", min(scores))