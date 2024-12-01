file1 = open("./advent-of-code-day-1/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()
finalArr = []


def smallestNumber(array):
    smallest = 999999

    for i in range(len(array)):
        if array[i] < smallest:
            smallest = array[i]
    return smallest


firstArr = []
secondArr = []


for line in inpArr:
    first = int(line.split("   ")[0])
    second = int(line.split("   ")[-1])
    firstArr.append(first)
    secondArr.append(second)


length = len(firstArr)
totalDistance = 0

for i in range(length):
    firstSmallest = smallestNumber(firstArr)
    secondSmallest = smallestNumber(secondArr)
    totalDistance += abs(secondSmallest - firstSmallest)

    firstArr.remove(firstSmallest)
    secondArr.remove(secondSmallest)

print(totalDistance)