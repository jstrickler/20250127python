from pprint import pprint

scores = {}
total_of_scores = 0

DATA_FILE = "../DATA/test_scores.txt"

with open(DATA_FILE) as f:
    for line in f:
        (name, score) = line.split(":")
        score = int(score)
        scores[name] = score
        total_of_scores += score

pprint(scores)
print('-' * 60)
pprint(scores.items())
print('-' * 60)

def by_score(element):
    return element[1]

for student, score in sorted(scores.items(), key=by_score, reverse=True):
    grade = None
    if score > 94:
        grade = 'A'
    elif score > 88:
        grade = 'B'
    elif score > 82:
        grade = 'C'
    elif score > 74:
        grade = 'D'
    else:
        grade = 'F'
    print(f"{student:20s} {score} {grade}")

average = total_of_scores / len(scores)
print(f"\naverage score is  {average:.2f}\n")
