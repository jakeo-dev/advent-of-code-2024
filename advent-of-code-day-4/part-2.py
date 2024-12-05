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

def findMAS1(row, col):
    if exists(row-1, col-1) and inpArr[row-1][col-1] == "M" and exists(row+1, col+1) and inpArr[row+1][col+1] == "S":
        return True

def findMAS2(row, col):
    if exists(row-1, col+1) and inpArr[row-1][col+1] == "M" and exists(row+1, col-1) and inpArr[row+1][col-1] == "S":
        return True

def findMAS3(row, col):
    if exists(row+1, col+1) and inpArr[row+1][col+1] == "M" and exists(row-1, col-1) and inpArr[row-1][col-1] == "S":
        return True

def findMAS4(row, col):
    if exists(row+1, col-1) and inpArr[row+1][col-1] == "M" and exists(row-1, col+1) and inpArr[row-1][col+1] == "S":
        return True

total = 0
        
for row in range(len(inpArr)):
    for col in range(len(inpArr[row])):
        if inpArr[row][col] == "A":
            # check for the different possible configurations of "MAS"
            if (findMAS1(row, col) or findMAS3(row, col)) and (findMAS2(row, col) or findMAS4(row, col)):
                total += 1
                
print(total)