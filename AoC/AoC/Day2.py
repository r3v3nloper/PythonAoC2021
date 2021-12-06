from AoC import *

lines = read_lines(day=2)
txt = read_string(day=2)

x = 0
y = 0

for line in lines:
    command, step = line.split()
    step = int(step)
    if command == "forward":
        x += step
    if command == "down":
        y += step
    if command == "up":
        y -= step
print("Part A", x*y)

x = 0
y = 0
aim = 0

from math import *

for line in lines:
    command, step = line.split()
    step = int(step)
    if command == "forward":
        x += step
        y += step*aim
    if command == "down":
        aim += step
    if command == "up":
        aim -= step

print("Part B", y*x)