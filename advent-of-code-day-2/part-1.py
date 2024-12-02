file1 = open("./advent-of-code-day-2/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()

def difference(a, b):
    return a - b

def allIncreasing(array):
    for i in range(len(array) - 1):
        diff = difference(int(array[i]), int(array[i+1]))
        if diff > -1 or diff < -3:
            return False
    return True

def allDecreasing(array):
    for i in range(len(array) - 1):
        diff = difference(int(array[i]), int(array[i+1]))
        if diff < 1 or diff > 3:
            return False
    return True

safeNum = 0

for line in inpArr:
    levelsArr = line.split(" ")
    if allIncreasing(levelsArr) or allDecreasing(levelsArr):
        safeNum += 1

print(safeNum)