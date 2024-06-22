print("Enter 10 test scores:")
scores = [int(input(">> ")) for _ in range(10)]

# (a)
print("Highest and lowest scores:", max(scores), min(scores))

# (b)
print("Average score:", sum(scores) / 10)

# (c)
print("Second highest score:", sorted(scores, reverse=True)[1])

# (d)
if any(score > 100 for score in scores):
    print("Warning: A score over 100 has been entered.")

# (e)
sorted_scores = sorted(scores)
print("Average after dropping the two lowest scores:", sum(sorted_scores[2:]) / 8)
