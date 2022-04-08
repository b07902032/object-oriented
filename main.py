import matrix

def CreateMat():
    matRaw = list(map(int, input().split()))
    return [[matRaw[0],matRaw[1],matRaw[2]],[matRaw[3],matRaw[4],matRaw[5]],[matRaw[6],matRaw[7],matRaw[8]]]

mat = CreateMat()
num = int(input())

for i in range(num):
    instr = input()
    if(instr == 'Multiply'):
        mat = matrix.MatMul(mat, CreateMat())
        print(mat)
    elif(instr == 'Transform'):
        vec = list(map(int, input().split()))
        print(matrix.Transform(vec, mat))
    elif(instr == 'Transpose'):
        mat = matrix.Transpose(mat)
        print(mat)
    elif(instr == 'Determinant'):
        print(matrix.Determinant(mat))