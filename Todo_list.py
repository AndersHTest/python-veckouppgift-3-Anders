"""
6 (att göra-lista)
Bygg ett program där användaren kan lägga till saker till en.
Tips: använd en loop, input och en variabel för listan.
Exempel:

1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
Välj ett alternativ: 1
Din lista är tom
.
Välj ett alternativ: 2
Skriv in en ny sak du måste komma ihåg att göra: mata guldfisken
Ok, lade till "mata guldfisken" i listan.
.
Välj ett alternativ: 1
+ Mata guldfisken
.
____________________
Första försöket.. Funkar ej.

todo_list = []

while True:
    user_input = input("Lägg till något i din lista")
    if user_input.lower() == "avsluta":
        print("Avslutar")
        break
    elif user_input.lower() == "innehåll":
        print(todo_list)
        break
    else:
        user_input = input("Lägg till något i din lista")
        todo_list.append(user_input)

____________________

Andra försöket:


def todo_list():
    uppgifter = []
    fardiga_uppgifter = []


    while True:
        print("\n Meny:")
        print("1. Innehåll")
        print("2. Lägg till uppgift")
        print("3. Markera uppgift som klar")
        print("4. Visa alla färdiga uppgifter")
        print("5. Avsluta")

        val = input("Välj ett alternativ: ").strip()

        if val == "1":
            if uppgifter:
                print("Dina uppgifter: ")
                for i, task in enumerate(uppgifter, 1):
                    print(f"{i}. {task}")
            else:
                print("Din lista är tom.")

        elif val == "2":
            task = input("Lägg till en uppgift: ").strip()
            uppgifter.append(task)
            print(f"Lade till \"{task}\" i listan.")

        elif val == "3":
            task_num = int(input("Ange numret på uppgiften du är färdig med: "))
            if 0 < task_num <= len(uppgifter):
                removed_task = uppgifter.pop(task_num - 1)
                print(f"\"{removed_task}\" har markerats som färdig(t).")
                fardiga_uppgifter.append(removed_task)

            else:
                print("Felaktigt nummer. ")

        elif val == "4":
            if fardiga_uppgifter:
                print("Dina färdiga uppgifter: ")
                for i, task in enumerate(fardiga_uppgifter, 1):
                    print(f"{i}. {task}")
                    val_1_0 = input(f"Tryck 1 för att lägga tillbaka något i listan.")
                    if val_1_0 == "1":
                        task_f_num = int(input(f"Ange vilken uppgift som ska läggas tillbaka. "))
                        if 0 < task_f_num <= len(fardiga_uppgifter):
                            borttaget = fardiga_uppgifter.pop(task_f_num - 1)
                            uppgifter.append(borttaget)

            else:
                print("Din lista är tom.")

        elif val == "5":
            print("Hej då!")
            break

        else:
            print("Felaktigt val")

todo_list()

"""