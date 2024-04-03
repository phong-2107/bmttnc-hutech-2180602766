str = input(" nhap X,Y: ")
dimentions = [int(x) for x in str.split(',')]
rowNum = dimentions[0]
colNum = dimentions[1]
multiList = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range (colNum):
        multiList[row][col] =  row * col
        
print(multiList)