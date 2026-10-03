# Vars
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]
a, b, c, d, f = [], [], [], [], []

#  Loop to categorize scores into letter grades
for score in scores:
    if score >= 90:
        a.append(score)
    elif score >= 80:
        b.append(score)
    elif score >= 70:
        c.append(score)
    elif score >= 60:
        d.append(score)
    else:
        f.append(score)
        
passing_scores_length = len(a) + len(b) + len(c) + len(d)       
# Output
print("\n--- Grade Analyzer ---")
print(f"Total Scores: {len(scores)}")
print(f"Average Score: {sum(scores) / len(scores):.1f}")
print(f"Highest Score: {max(scores)}")
print(f"Lowest Score: {min(scores)}")
print(f"Passing Scores: {passing_scores_length} ({(passing_scores_length / len(scores)) * 100:.2f}%)")
print(f"Failing Scores: {len(f)} ({(len(f) / len(scores)) * 100:.2f}%)")

print("\n--- Grade Distribution ---")
print(f"A Grades: {len(a)} students")
print(f"B Grades: {len(b)} students")
print(f"C Grades: {len(c)} students")
print(f"D Grades: {len(d)} students")
print(f"F Grades: {len(f)} students")


print("\n--- Add More Scores ---")
while True:
    new_score = input("Enter a score (or 'done' to finish): ").strip()
    if new_score.lower() == "done":
        print(f"\n Final average: {sum(scores) / len(scores):.1f}")
        break

    try:
        score = int(new_score)
    except ValueError:
        print("Please enter a whole-number score or 'done'.")
        continue

    if 0 <= score <= 100:
        scores.append(score)
        print(f"Updated average: {sum(scores) / len(scores):.1f}")
    else:
        print("Score must be between 0 and 100.")