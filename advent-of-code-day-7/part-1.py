file1 = open("./advent-of-code-day-7/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()

def getPossibleNumbers(numbersLength, numPossible):
    array = []
    
    for i in range(numPossible):
        newNum = str(bin(i))[2:]
        if len(newNum) < numbersLength:
            while len(newNum) < numbersLength:
                newNum = "0" + newNum
        array.append(newNum)
    
    return array

def areTheNumbersEqual(value, numbers):
    numPossible = 2**(len(numbers)-1)
    # get an array of strings of numbers; each string of nums is a possible combination of + and * that lets the numbers = the value
    possibleArray = getPossibleNumbers(len(numbers)-1, numPossible) # 0 for add, 1 for multiply

    # check every possible combination to see if any make the numbers = the value
    for possibleString in possibleArray:
        total = int(numbers[0])
        for n in range(1, len(numbers)):
            if possibleString[n-1] == "0":
                total += int(numbers[n])
            elif possibleString[n-1] == "1":
                total *= int(numbers[n])
        if total == value:
            return True

finalSum = 0 

for line in inpArr:
    value = int(line.split(": ")[0])
    numbers = line.split(": ")[1].split(" ")
    # if there is a valid solution that makes the numbers = value, add the value to finalSum
    if areTheNumbersEqual(value, numbers):
        finalSum += value

print(finalSum)