# Treasure Island
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input('''You're at a crossroad. Where do you want to go?.
        Type "left" or "right"\n''')
if choice == "left":
    ch1 = input("""You've come to a lake. There's an island in the middle of the lake.
        Type "wait" to wait for a boat. Type "swim" to swim across.\n""")
    if ch1 == "wait":
        door = input("""You've arrived at the island unharmed.There is a house with 3 doors.
        One red, one yellow and one blue. Which color do you choose?\n""") 
        if door == "red":
            print("""Burned by fire.
        Game Over.""")
        elif door == "yellow":
            print("You Win!")
        elif door == "blue":
            print("""Eaten by beasts.
        Game Over.""")
        else:
            print("Game Over.")
    else:
        print("""Attacked by Trout.
        Game Over.""")
else:
    print("""You've fallen into a hole.
        Game Over.""") 