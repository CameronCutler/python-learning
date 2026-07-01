# Vars
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]
a, b, c, d, f = [], [], [], [], []

#  Loop to categorize scores into letter grades
for i, score in enumerate(scores):
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
x = True
while x == True:
    new_score = input("Enter a score (or 'done' to finish): ")
    if new_score != "done":
        scores.append(int(new_score))
        print(f"Updated average: {sum(scores) / len(scores):.1f}")
    elif new_score == "done" or new_score == "Done":
        print(f"\n Final average: {sum(scores) / len(scores):.1f}")
        x = False