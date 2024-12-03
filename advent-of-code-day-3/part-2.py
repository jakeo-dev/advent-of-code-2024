import re

file1 = open("./advent-of-code-day-3/input.txt", "r")

inp = file1.read()
file1.close()

multiplies = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", inp)

sum = 0

enabled = True

for i in multiplies:
    if i == "don't()":
        enabled = False
    elif i == "do()":
        enabled = True
    elif enabled:
        j = re.sub("mul|\(|\)", "", i).split(",")
        sum += int(j[0]) * int(j[1])

print(sum)