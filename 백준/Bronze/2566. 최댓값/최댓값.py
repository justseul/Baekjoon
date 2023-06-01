matrix = []
max = 0 
for _ in range(9):
    rows = list(map(int, input().split()))
    matrix.append(rows)
for i in range(9):
    for j in range(9):
        if matrix[i][j] >= max:
            max = matrix[i][j]
            row = i+1
            col = j+1
print(max)
print(row, col)
        
