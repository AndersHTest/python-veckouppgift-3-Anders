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
Ingenting, då det saknas en print ;) men vid jämna siffror på y går vi den första vägen, ojämna siffror på y går via else.
Första rundan x = 1 (y=1)
Andra rundan x = -1 (y=2)
Tredje rundan = 8 (y=3)
Resultatet tar jag mig inte till i huvudet gärna :).
Sista rundan kan jag räkna ut när jag vet svaret:
y = 9
x + 9 * 9 = 145.
x måste alltså ha varit 145 - 81 = 64 på näst sista steget.

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