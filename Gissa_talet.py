"""
Gör ett spel som slumpar ett hemligt tal mellan 1 och 100. Sedan ska man försöka gissa det.
Om man gissar för lågt eller för högt ska spelet tala om det.
Efter att man har gissat rätt ska spelet skriva ut antalet gissningar.

# Slumpa ett hemligt tal
secret = random.randint(1, 100)

Exempel:
Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?
Gissa: 40
Nej, det är för lågt!
Gissa: 55
Nej, det är för högt!
Gissa: 51
Det är rätt!! Du gjorde det på 3 gissningar.


import random

secret = random.randint(1, 100)
count = 0

try:
    guess = int(input(f"Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är? "))
    while True:
        if guess < secret:
            count += 1
            print(f"Nej, det är för lågt!")
            guess = int(input(f"Gissa: "))

        elif guess > secret:
            count += 1
            print(f"Nej, det är för högt!")
            guess = int(input(f"Gissa: "))

        elif guess == secret:
            count += 1
            print(f"Det är rätt! Du gjorde det på {count} gissningar.")
            break

except ValueError:
    print(f"Du måste skriva ett heltal. Avslutar.")
    pass

____________________

Version 2: Version 2: skriv ut om man är nära ifall man gissar högst 5 ifrån det rätta svaret.
"Nu börjar det brännas!"

import random

secret = random.randint(1, 100)
count = 0

try:
    guess = int(input(f"Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är? "))
    while True:
        if guess < secret:
            count += 1
            if secret - guess <= 5:
                print(f"Nej, det är för lågt, men nu börjar det brännas.")
                guess = int(input(f"Gissa: "))
            else:
                print(f"Nej, det är för lågt!")
                guess = int(input(f"Gissa: "))

        elif guess > secret:
            count += 1
            if guess - secret <= 5:
                print(f"Nej, det är för högt, men nu börjar det brännas.")
                guess = int(input(f"Gissa: "))
            else:
                print(f"Nej, det är för högt!")
                guess = int(input(f"Gissa: "))

        elif guess == secret:
            count += 1
            print(f"Det är rätt! Du gjorde det på {count} gissningar.")
            break

except ValueError:
    print(f"Du måste skriva ett heltal. Avslutar.")
    pass

"""

