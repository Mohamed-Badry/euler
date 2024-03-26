def krange(i, p, mat):
    if i-p < 0:
        return range(i+p+1)
    if i+p+1 > len(mat):
        return range(i-p, len(mat))
    return range(i-p,i+p+1)
    

matrix = [[(i,j) for i in range(5)] for j in range(5)]        

for row in matrix:
    print(row)

mat_dict = {}

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        mat_dict[matrix[i][j]] = []
        for k in krange(i, 1, matrix):
            for l in krange(j, 1, matrix):
                 if (i, j) == (k, l):
                     continue
                 mat_dict[matrix[i][j]].append(matrix[k][l])
                
for key in mat_dict:
    print(f'{key}: {mat_dict[key]}')