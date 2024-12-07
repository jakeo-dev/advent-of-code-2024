# this code took over 2 minutes to run 🤩🤩🤩 (i am a very efficient programmer!!!!!!!!!!!!)

file1 = open("./advent-of-code-day-7/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()

def getPossibleNumbers(numbersLength, numPossible):
    array = []
    
    # converts each number from 0 to numbersLength to base 3 for the strings of possible combinations
    for i in range(numPossible):
        # https://stackoverflow.com/a/34559825
        nums = []
        while i:
            i, r = divmod(i, 3)
            nums.append(str(r))
        newNum = str("".join(reversed(nums)))
        
        if len(newNum) < numbersLength:
            while len(newNum) < numbersLength:
                newNum = "0" + newNum
        array.append(newNum)

    return array

def areTheNumbersEqual(value, numbers):
    numPossible = 3**(len(numbers)-1)
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
            elif possibleString[n-1] == "2":
                total = int(str(total) + numbers[n])
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