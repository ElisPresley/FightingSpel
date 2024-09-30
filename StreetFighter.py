import random
import time

PlayerWins = 0
FighterBWins = 0
Equal = 0

name = input("Ange ditt namn: ")

print("Klara")
time.sleep(0.5)
print("Färdiga")
time.sleep(0.5)
print("KÖR!")
time.sleep(0.5)

def StreetFighter():
    global PlayerWins, FighterBWins, Equal, name
    PlayerHP = 100
    FighterBHP = 100

    while PlayerHP > 0 and FighterBHP > 0:
        FighterBHP -= random.randint(5,15)
        PlayerHP -= random.randint(5,15)
        print(str(name) + " HP:" + str(PlayerHP) + ", Fighter B HP: " + str(FighterBHP))
        time.sleep(1)

    if PlayerHP > 0 and FighterBHP <= 0:
        print(str(name) + " vinner!")
        PlayerWins += 1
        print(str(name) + " vinster: " + str(PlayerWins) + "! Fighter B vinster: " + str(FighterBWins) + "! Oavgjort: " + str(Equal))
    elif FighterBHP > 0 and PlayerHP <= 0:
        print("Fighter B vinner!")
        FighterBWins += 1
        print(str(name) + " vinster: " + str(PlayerWins) + "! Fighter B vinster: " + str(FighterBWins) + "! Oavgjort: " + str(Equal))
    else:
        print("Oavgjort!")
        Equal += 1
        print(str(name) + " vinster: " + str(PlayerWins) + "! Fighter B vinster: " + str(FighterBWins) + "! Oavgjort: " + str(Equal))


while True:
    StreetFighter()

    play_again = input("Vill du köra igen? yes/no: ").lower()
    if play_again != "yes":
        print("Tack för att du spelade!")
        break