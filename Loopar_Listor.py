"""

1a Skriv färdigt kodexemplet.
answer = 0
for i in ????????????:
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55


answer = 0
for i in range(11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55

____________________

1b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)


answer = 0
for i in range(101):
    answer += i
print("Summan av talen 1 till 100 är: " + str(answer))

____________________

1c Skriv om 1b så att den använder en while-loop.


answer = 0
x = 0

while x < 101:
    answer += x
    x += 1

print("Summan av talen 1 till 100 är: " + str(answer))

____________________

2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3]


---for loop:

nummerserie = [1, -2, 3, -2, 4, -3]
answer = 0

for i in nummerserie:
    answer += i

print(answer)

---while loop:

nummerserie = [1, -2, 3, -2, 4, -3]
x = 0
answer = 0

while x < len(nummerserie):
    answer += nummerserie[x]
    x += 1

print(answer)

____________________

3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar.
Skriv ut hela listan med funktionen print.


filmer = ["Titanic", "Titanic 2", "The Ring", "Saw"]
n = len(filmer)

for i in range(n):
    print(f"Film {i+1}: {filmer[i]}.")

____________________

3b Lägg till "Fellowship of the ring" sist i listan.


filmer = ["Titanic", "Titanic 2", "The Ring", "Saw"]

filmer.append("Fellowship of the ring")

print(filmer)

____________________

3c Lägg till "The two towers" på första platsen i listan. (index noll)


filmer = ['Titanic', 'Titanic 2', 'The Ring', 'Saw', 'Fellowship of the ring']

filmer.insert(0, "The two towers")

print(filmer)

____________________

3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
--Filmen ligger på position 5.


filmer = ['The two towers', 'Titanic', 'Titanic 2', 'The Ring', 'Saw', 'Fellowship of the ring']

print(filmer.index("Fellowship of the ring"))

____________________

3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
-- Ja, positionen har ändrats till 4.


filmer = ['The two towers', 'Titanic', 'Titanic 2', 'The Ring', 'Saw', 'Fellowship of the ring']

filmer.remove("Titanic 2")

print(filmer.index("Fellowship of the ring"))

____________________

3f Ta reda på hur lång listan är. (len)
--Listan innehåller 5 element.


filmer = ['The two towers', 'Titanic', 'The Ring', 'Saw', 'Fellowship of the ring']

print(len(filmer))

____________________

3g Vänd listan baklänges.


filmer = ['The two towers', 'Titanic', 'The Ring', 'Saw', 'Fellowship of the ring']

filmer.reverse()

print(filmer)

____________________

3h Sortera listan stigande i bokstavsordning.


filmer = ['Fellowship of the ring', 'Saw', 'The Ring', 'Titanic', 'The two towers']

filmer.sort()

print(filmer)

"""