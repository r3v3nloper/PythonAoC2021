from AoC import *

lines = read_lines(day=1)
txt = read_string(day=1)

i = 0
for last, next in zip(ints(txt), ints(txt)[1:]):
    if next > last:
        i += 1
print("Part A ", i)


i = 0

#Ich rechne die ersten 3 Zahlen zusammen und danach rechne ich von der zweiten Zahl die 3 Zahlen zusammen und vergleiche diese
for first, second, third, four in zip(ints(txt), ints(txt)[1:], ints(txt)[2:], ints(txt)[3:]):
    if first + second + third < second + third + four:
        i += 1
print("Part B ", i)