import matrix

def CreateMat():
    matraw = list(map(int, input().split()))
    return [[matraw[0],matraw[1],matraw[2]],[matraw[3],matraw[4],matraw[5]],[matraw[6],matraw[7],matraw[8]]]

def PrintMat(mat):
    print(mat[0])
    print(mat[1])
    print(mat[2])

mat = CreateMat()
num = int(input())

for i in range(num):
    instr = input()
    if(instr == 'Multiply'):
        mat = matrix.MatMul(mat, CreateMat())
        PrintMat(mat)
    elif(instr == 'Transpose'):
        mat = matrix.Transpose(mat)
        PrintMat(mat)
    elif(instr == 'Determinant'):
        print(matrix.Determinant(mat))
    elif(instr == 'Transform'):
        vec = list(map(int, input().split()))
        print(matrix.Transform(vec, mat))
    else:
        print("WTF")