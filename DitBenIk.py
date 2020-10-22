# variabelen
# input()
# print()

# Doel: Voornaam en achternaam kunnen invoeren. Het programma weergeeft de volledige naam.

Score = 0
import time

print("Hello You!, ik ben Senno Taphoorn")
print("Wie ben jij?")
voornaam = input()

print("")

print("Hello" + " " + voornaam)

print("")

print("Ik ben een nieuwkomer op het Media college in Amsterdam")
print("Ale je een aantal vragen beantwoord, Kan je mij beter leren kennen.")

print("")
print("")
time.sleep(3)

# Vraag 1
antwoord1 = input("Hoe oud ben ik? \na 15 \nb 16 \nc 17 \nd 18 \nAnswer: ")
if antwoord1 == "c" or antwoord1 == "17" or antwoord1 == "C":
    Score +=1
    print("Dat is goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Dat is niet goed! Het antwoord is C (17)")
    print("Score: ", Score)
    print("\n")

time.sleep(1)

# Vraag 2
antwoord2 = input("Wat is mijn favoriete film \na Avengers:Endgame \nb Zootopia \nc Pirates of the Caribbean \nd Guardians of the Galaxy \nAnswer: ")
if antwoord2 == "b" or antwoord2 == "Zootopia" or antwoord2 == "B":
    Score +=1
    print("Dat is goed!")
    print("Score:", Score)
    print("\n")
else:
    Score -=1
    print("Dat is niet goed! Het antwoord is B (Zootopia)")
    print("Score: ", Score)
    print("\n")

time.sleep(1)

# Vraag 3
antwoord2 = input("Wat is mijn favoriete kleur? \na Geel \nb Blauw \nc Groen \nd Zilver \nAnswer: ")
if antwoord2 == "a" or antwoord2 == "Geel" or antwoord2 == "A":
    Score +=1
    print("Goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Dat is niet goed! Het antwoord is A (Geel)")
    print("Score: ", Score)
    print("\n")

time.sleep(1)

# Vraag 4
antwoord2 = input("Wat is mijn favoriete game? \na Fortnite \nb Super Mario Sunshine \nc Minecraft \nd Zelda: Breath of the Wild \nAnswer: ")
if antwoord2 == "b" or antwoord2 == "Super Mario Sunshine" or antwoord2 == "B":
    Score +=1
    print("Goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Dat id niet goed! Het antwoord is B (Super Mario Sunshine)")
    print("Score: ", Score)
    print("\n")

print("")
time.sleep(1)

# Eind score
print("Jouw eind score is: ", Score)
