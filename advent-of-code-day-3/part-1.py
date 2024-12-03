import re

file1 = open("./advent-of-code-day-3/input.txt", "r")

inp = file1.read()
file1.close()

multiplies = re.findall("mul\(\d+,\d+\)", inp)

sum = 0
for i in multiplies:
    j = re.sub("mul|\(|\)", "", i).split(",")
    sum += int(j[0]) * int(j[1])

print(sum)