from sys import argv

def findNeigh(x, y, z, matrix, control: int, row, column):
    x = int(x)
    y = int(y)
    #z = int(z)


    matrix[x][y] = chr(32)

    if matrix[x+1][y] == z:
        control = 1
        findNeigh(x+1, y, z, matrix, control, row, column)
    if matrix[x][y+1] == z:
        control = 1
        findNeigh(x, y+1, z, matrix, control, row, column)
    if matrix[x-1][y] == z:
        control = 1
        findNeigh(x-1, y, z, matrix, control, row, column)
    if matrix[x][y-1] == z:
        control = 1
        findNeigh(x, y-1, z, matrix, control, row, column)
    if control == 0:
        print("Game over")
        exit(0)
    else:
        return




def findDestroy(matrix, r, c):
    destroy = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == chr(32):
                destroy += 1
    return destroy


def delMatrix(matrix, r, c):
    i = 0
    j= 0
    while i < c:
        j = 0
        while j < r:
            if matrix[j][i] == chr(32) and j - 1 >= 0 and matrix[j - 1][i] != chr(32):
                matrix[j][i] = matrix[j - 1][i]
                matrix[j - 1][i] = chr(32)
                j -= 1

            else:
                j += 1
        i += 1

def checkMatrix(matrix, r, c):
    i = 0
    j = 0
    count = 0
    control = 0
    while i < c:
        j = 0
        control = 0
        while j < r:
            if matrix[j][i] == chr(32) and control == 0:
                count += 1
                if count == r:
                    control = 1
            if count == r and control == 1 and i + 1 <= r:
                z = 0
                #assert isinstance(c, object)
                while z < r:
                    matrix[z][i] = matrix[z][i + 1]
                    matrix[z][i+1] = chr(32)
                    z += 1
                control = 0
            j += 1
        count = 0
        i += 1

def printMatrix(matrix, r, c):
    for i in range(row):
        for j in range(column):
            print(matrix[i][j], end='')
        print()

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

file = open(argv[1], "r")
lines = file.readlines()
rCount = 0
cCount = 0
#print(lines)
for i in lines:
    cCount = 0
    for a in i:
        if a == chr(32) or a == chr(10):
            continue
        else:
            cCount += 1
    rCount += 1


matrix = [[0 for x in range(cCount+1)] for y in range(rCount+1)]
row = 0
column = 0
for i in lines:
    column = 0
    for a in i:
        if a == chr(32) or a == chr(10):
            continue
        else:
            #print(row, column)
            matrix[row][column] = a
            column += 1
    row += 1

#print(row, column)

check = 0
score = 0
destroy = 0
destroyOld = 0

printMatrix(matrix, row, column)
while check == 0:

    print("Your score is:", score)
    a = input("Please enter a row and column number: ")
    rC = []
    rC = a.split(" ")
    #try:
    yedek = int(matrix[int(rC[0]) - 1][int(rC[1]) - 1])
    findNeigh(int(rC[0]) - 1, int(rC[1]) - 1, matrix[int(rC[0]) - 1][int(rC[1]) - 1], matrix, 0, row, column)
    destroy = findDestroy(matrix, row, column) - destroyOld
    destroyOld = destroy
    score = score + yedek * fib(destroy)

    delMatrix(matrix, row, column)
    checkMatrix(matrix, row, column)
    printMatrix(matrix, row, column)
    destroy = 0
    #except:
        #print("Please enter a correct size!")



