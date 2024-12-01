file1 = open("./advent-of-code-day-1/input.txt", "r")

inp = file1.read()
inpArr = inp.split("\n")
file1.close()
finalArr = []


firstArr = []
secondArr = []


for line in inpArr:
    first = int(line.split("   ")[0])
    second = int(line.split("   ")[-1])
    firstArr.append(first)
    secondArr.append(second)


total = 0

for number in firstArr:
    count = 0
    for i in secondArr:
        if number == i:
            count += 1
    total += (number * count)

print(total)