file1 = open("./advent-of-code-day-2/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()

def allIncreasing(array):
    for i in range(len(array) - 1):
        diff = int(array[i]) - int(array[i+1])
        if diff > -1 or diff < -3:
            return i
    return -1

def allDecreasing(array):
    for i in range(len(array) - 1):
        diff = int(array[i]) - int(array[i+1])
        if diff < 1 or diff > 3:
            return i
    return -1

safeNum = 0

for line in inpArr:
    levelsArr = line.split(" ")
    
    allInc = allIncreasing(levelsArr)
    allDec = allDecreasing(levelsArr)
        
    if allInc == -1 or allDec == -1:
        safeNum += 1
    else:
        length = len(levelsArr)
        for num in range(length):
            originalArray = list(levelsArr)
            if allInc == 0:
                originalArray.pop(num)
            elif allDec == 0:
                originalArray.pop(num)
        
            allInc = allIncreasing(originalArray)
            allDec = allDecreasing(originalArray)
            if allInc == -1 or allDec == -1:
                safeNum += 1
                break

print(safeNum)