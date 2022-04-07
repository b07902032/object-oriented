def Transform(vector, matrix):
    x = matrix[0][0] * vector[0] + matrix[0][1] * vector[1] + matrix[0][2] * vector[2]
    y = matrix[1][0] * vector[0] + matrix[1][1] * vector[1] + matrix[1][2] * vector[2]
    z = matrix[2][0] * vector[0] + matrix[2][1] * vector[1] + matrix[2][2] * vector[2]
    return [x,y,z]

def MatMul(matA, matB):
    m00 = matA[0][0] * matB[0][0] + matA[0][1] * matB[1][0] + matA[0][2] * matB[2][0]
    m01 = matA[0][0] * matB[0][1] + matA[0][1] * matB[1][1] + matA[0][2] * matB[2][1]
    m02 = matA[0][0] * matB[0][2] + matA[0][1] * matB[1][2] + matA[0][2] * matB[2][2]
    m10 = matA[1][0] * matB[0][0] + matA[1][1] * matB[1][0] + matA[1][2] * matB[2][0]
    m11 = matA[1][0] * matB[0][1] + matA[1][1] * matB[1][1] + matA[1][2] * matB[2][1]
    m12 = matA[1][0] * matB[0][2] + matA[1][1] * matB[1][2] + matA[1][2] * matB[2][2]
    m20 = matA[2][0] * matB[0][0] + matA[2][1] * matB[1][0] + matA[2][2] * matB[2][0]
    m21 = matA[2][0] * matB[0][1] + matA[2][1] * matB[1][1] + matA[2][2] * matB[2][1]
    m22 = matA[2][0] * matB[0][2] + matA[2][1] * matB[1][2] + matA[2][2] * matB[2][2]
    return [[m00,m01,m02],[m10,m11,m12],[m20,m21,m22]]

def Transpose(matrix):
	matrix[0][1],matrix[1][0] = matrix[1][0],matrix[0][1]
	matrix[0][2],matrix[2][0] = matrix[2][0],matrix[0][2]
	matrix[1][2],matrix[2][1] = matrix[2][1],matrix[1][2]
	return matrix

def Determinant(matrix):
	a = matrix[0][0]*matrix[1][1]*matrix[2][2]
	b = matrix[0][1]*matrix[1][2]*matrix[2][0]
	c = matrix[0][2]*matrix[1][0]*matrix[2][1]
	d = matrix[2][0]*matrix[1][1]*matrix[0][2]
	e = matrix[0][1]*matrix[1][0]*matrix[2][2]
	f = matrix[0][0]*matrix[1][2]*matrix[2][1]
	return a+b+c-d-e-f