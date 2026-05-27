"""
1. Jag tror att följande skrivs ut:
5
7
9
11
13
15


limit = 15
index = 5

while index <= limit:
    print(index)
    index = index + 2


2. Jag tror att följande skrivs ut:
0
1
2
3
4

6
7
8
9

i = i + 1 är överflödig?


for i in range(10):
    if i == 5:
        print("")
    else:
        print(i)
    i = i + 1


3. Jag tror att summan blir 15.

counter = 0

for i in range(6):
    counter += i
print(counter)


4.
1.	x = 1 (0+1)
2.	x = -1 (1-2)
3.	x = 8 (-1+9)
4.	x = 4 (8-4)
5.	x = 29 (4+25)
6.	x = 23 (29-6)
7.	x = 72 (23+79)
8.	x = 64 (72-8)
9.	x = 145 (64+81)

x = 0
y = 1
while y < 10:
    if y % 2 == 0:
        x -= y
    else:
        x += y * y
    y += 1

5. _tim skrivs ut.
ändra print till print(message[4:8] för att få time.

message = "its_time_to_get_coding"
print(message[4:8])

6.

Genom att ändra värdet på s från "" till "." och ändra stopp-parametern från 9 till 8 för x,
får vi samma struktur men "#" hamnar ett steg åt höger.


for y in range(1,7):
    s = "."
    for x in range(1,8):
        if x == y:
            s += "#"
        else:
            s += "."
    print(s)

"""