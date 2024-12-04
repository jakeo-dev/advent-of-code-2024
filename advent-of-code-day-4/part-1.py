file1 = open("./advent-of-code-day-4/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()

# check if letter exists at certain row and column
def exists(row, col):
    if row >= len(inpArr) or col >= len(inpArr[row]) or row < 0 or col < 0:
        return False
    else:
        return True

# find all letter Ms surrounding a letter X
def findM(row, col):
    allMTypes = []
    
    if exists(row-1, col-1) and inpArr[row-1][col-1] == "M":
        allMTypes.append(1)
        
    if exists(row-1, col) and inpArr[row-1][col] == "M":
        allMTypes.append(2)
        
    if exists(row-1, col+1) and inpArr[row-1][col+1] == "M":
        allMTypes.append(3)
        
    if exists(row, col+1) and inpArr[row][col+1] == "M":
        allMTypes.append(4)
        
    if exists(row+1, col+1) and inpArr[row+1][col+1] == "M":
        allMTypes.append(5)
        
    if exists(row+1, col) and inpArr[row+1][col] == "M":
        allMTypes.append(6)
        
    if exists(row+1, col-1) and inpArr[row+1][col-1] == "M":
        allMTypes.append(7)
        
    if exists(row, col-1) and inpArr[row][col-1] == "M":
        allMTypes.append(8)
    
    return allMTypes

# continue in the direction of the found letter M, checking if there is a letter A, then a letter S
def findTheRest(row, col, mType):
    number = 0
    
    if mType == 1:
        if exists(row-2, col-2) and inpArr[row-2][col-2] == "A" and exists(row-3, col-3) and inpArr[row-3][col-3] == "S":
            number += 1
            
    elif mType == 2:
        if exists(row-2, col) and inpArr[row-2][col] == "A" and exists(row-3, col) and inpArr[row-3][col] == "S":
            number += 1
            
    elif mType == 3:
        if exists(row-2, col+2) and inpArr[row-2][col+2] == "A" and exists(row-3, col+3) and inpArr[row-3][col+3] == "S":
            number += 1
            
    elif mType == 4:
        if exists(row, col+2) and inpArr[row][col+2] == "A" and exists(row, col+3) and inpArr[row][col+3] == "S":
            number += 1
            
    elif mType == 5:
        if exists(row+2, col+2) and inpArr[row+2][col+2] == "A" and exists(row+3, col+3) and inpArr[row+3][col+3] == "S":
            number += 1
            
    elif mType == 6:
        if exists(row+2, col) and inpArr[row+2][col] == "A" and exists(row+3, col) and inpArr[row+3][col] == "S":
            number += 1

    elif mType == 7:
        if exists(row+2, col-2) and inpArr[row+2][col-2] == "A" and exists(row+3, col-3) and inpArr[row+3][col-3] == "S":
            number += 1
            
    elif mType == 8:
        if exists(row, col-2) and inpArr[row][col-2] == "A" and exists(row, col-3) and inpArr[row][col-3] == "S":
            number += 1
    
    return number

superTotal = 0
        
for row in range(len(inpArr)):
    for col in range(len(inpArr[row])):
        if inpArr[row][col] == "X":
            print("\nX:", str(row), str(col))
            allMTypes = findM(row, col)
            print("all M types:", str(allMTypes))
            for mType in allMTypes:
                superTotal += findTheRest(row, col, mType)
                
print("\n\nTOTAL: " + str(superTotal))