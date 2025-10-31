scores = [73, 84, 92, 68]
sum = 0

for i, score in enumerate(scores):
    print(f"No.{i}: {score}")
    sum += score

average = sum / len(scores)
print(f"平均点: {average:.2f}")