sum = 0
grade_score = 0
for i in range(20):
    a, b, c = input().split()
    if c == 'P':
        continue
    elif c == 'A+':
        grade = 4.5
    elif c == 'A0':
        grade = 4.0
    elif c == 'B+':
        grade = 3.5
    elif c == 'B0':
        grade = 3.0
    elif c == 'C+':
        grade = 2.5
    elif c == 'C0':
        grade = 2.0
    elif c == 'D+':
        grade = 1.5
    elif c == 'D0':
        grade = 1.0
    else:
        grade = 0.0
    sum += float(b)
    grade_score += float(b)*grade
print(grade_score/sum)
    
