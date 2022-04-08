## 題目說明
請實作一自訂三階方陣的模組`matrix.py`包含以下功能：
* `MatMul(A,B)`
計算並回傳三階方陣`AB`，其中`A`、`B`皆為三階方陣。
* `Transform(x, A)`
計算並回傳三維向量`Ax`，其中`x`為三維向量；`A`為三階方陣。

## 注意事項
* 本題使用二維陣列來表示三階方陣，並保證其row和column的長度皆為3。
假設`mat`為一個二維陣列，`A`為`mat`所代表的矩陣，則：
$$
 A =
 \left[
 \begin{matrix}
   mat[0][0] & mat[0][1] & mat[0][2] \\
   mat[1][0] & mat[1][1] & mat[1][2] \\
   mat[2][0] & mat[2][1] & mat[2][2]
  \end{matrix}
  \right]
$$
* 本題使用一維陣列來表示三維向量，並保證其長度為3。
* 本題將使用如下的`main.py`來測試程式：
```python=
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
```

## Input Format ##
第一行為九個中間以空白隔開的整數，代表初始陣列。
第二行為一正整數`N`，代表對矩陣進行操作的數量，其中`1 ≤ N ≤ 100`。
接著會出現`N`行代表操作的字串，共有兩種可能：
1. `Multiply`：當出現這行字串時，下一行會出現九個中間以空白隔開的整數，代表與之相乘的矩陣。
2. `Transform`：當出現這行字串時，下一行會出現三個中間以空白隔開的整數，代表與之相乘的三維向量。
## Input Format ##
輸出`N`筆資料，每筆資料佔一行。根據輸入的操作共有兩種可能的輸出：
1. `Multiply`：輸出代表相乘後的矩陣的二維陣列。
2. `Transform`：輸出代表經由矩陣變換過的三維向量的一維陣列。
## Sample Input ##
```
1 2 0 1 1 0 2 1 2
2
Multiply
0 2 1 0 0 1 2 1 1
Transform
0 5 4
```
## Sample Output ##
```
[[0, 2, 3], [0, 2, 2], [4, 6, 5]]
[22, 18, 50]
```
## 友善提醒 ##
* 若是上傳的程式中有測試程式或主程式，可以使用`if __name__=='__main__':`來避免被執行的窘境。
* 請確保函式的設計(名稱、傳入參數個數與回傳值)符合題目要求，否則將可能無法通過批改！