"""
Gör ett program som upprepade gånger ber användaren skriva in ett tal. När man skriver in strängen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen. Exempel:
Välkommen till Kvittokompis! Avsluta genom att skriva: quit
Skriv in ett belopp: 25
Skriv in ett belopp: 50
Skriv in ett belopp: quit
Det blir 75 kr totalt. Välkommen åter!

Det går nog att göra detta på ett smidigare sätt...

print(f"Välkommen Kvittokompis! Avsluta genom att skriva: quit")

kvittolista = []
summa = 0

while True:
    inkommande = input(f"Skriv in ett belopp: ")
    kvittolista.append(inkommande)

    if inkommande == "quit" or inkommande == "avsluta":
        kvittolista.pop(-1)
        break

for i in kvittolista:
    summa += int(i)

print(f"Det blir {summa} kr totalt. Välkommen åter!")


____________________

Version 2: programmet ska fråga hur många man är, och tala om hur mycket varje person i sällskapet ska betala.
Hur många är ni? 3
Det blir 75 kr totalt, alltså 25.0 kr per person. Välkommen åter!



print(f"Välkommen Kvittokompis! Avsluta genom att skriva: quit")

kvittolista = []
summa = 0

while True:
    inkommande = input(f"Skriv in ett belopp: ")
    kvittolista.append(inkommande)

    if inkommande == "quit" or inkommande == "avsluta":
        kvittolista.pop(-1)
        break

for i in kvittolista:
    summa += int(i)

antal_personer = int(input(f"Hur många är ni? "))

antal_personer_split = summa / antal_personer

print(f"Det blir {summa} kr totalt, alltså {antal_personer_split} kr per person. Välkommen åter!")

____________________

Version 3: programmet ska fråga hur många procent dricks man vill lägga på.
Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.


print(f"Välkommen Kvittokompis! Avsluta genom att skriva: quit")

kvittolista = []
summa = 0

while True:
    inkommande = input(f"Skriv in ett belopp: ")
    kvittolista.append(inkommande)

    if inkommande == "quit" or inkommande == "avsluta":
        kvittolista.pop(-1)
        break

for i in kvittolista:
    summa += int(i)

antal_personer_input = int(input(f"Hur många är ni? "))
dricks_input = input(f"Hur många % dricks vill ni lägga på? ")

if dricks_input.isdigit():
    dricks_input = int(dricks_input)
    if dricks_input >= 0:
        summa_dricks = summa + summa * (int(dricks_input) / 100)
else:
    dricks_input = str(dricks_input)
    summa_dricks = summa + summa * (10 / 100)

antal_personer_split = summa_dricks / antal_personer_input

print(f"Det blir {summa_dricks} kr totalt, alltså {antal_personer_split} kr per person. Välkommen åter!")

"""