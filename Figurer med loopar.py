"""
Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

"""

print()
for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1:
            s += "#"
        else:
            s += "."
    print(s)
print()

for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)
print()

for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if 3 <= x <= 5:
            s += "#"
        else:
            s += "."
    print(s)
print()


for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3:
            s += "#"
        elif y == 3:
            s += "#"
        else:
            s += "."
    print(s)
print()


for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 5:
            s += "#"
        elif x + y == 7:
            s += "#"
        else:
            s += "."
    print(s)
print()


for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == y:
            s += "#"
        elif x + y == 7:
            s += "#"
        else:
            s += "."
    print(s)
print()


for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x % 2 != 0:
            s += "#"
        else:
            s += "."
    print(s)
print()


for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if 2 <= x <= 7 and y == 2:
            s += "#"
        elif 2 <= x <= 7 and y == 5:
            s += "#"
        elif 3 <= y <= 4 and x == 2:
            s += "#"
        elif 3 <= y <= 4 and x == 7:
            s += "#"
        else:
            s += "."
    print(s)
print()


for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 1 + y or x == 4 + y or x == 7 + y or y - x == 2 or y - x == 5:
            s += "#"
        elif x == 2 + y or x == 5 + y or y - x == 1 or y - x == 4:
            s += "O"
        else:
            s += "."
    print(s)
print()


for y in range(1, 7):
    s = ""
    for x in range(1, 9):
        if x == 3 and 1 <= y <= 3:
            s += "#"
        elif x == 6 and 1 <= y <= 3:
            s += "#"

        elif x % 2 == 0 and y == 5:
            s += "#"
        elif x % 2 != 0 and y == 6:
            s += "#"
        else:
            s += "."
    print(s)
print()