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
direction=input("you\'re at the cross road choose your direction 'LEFT' or 'RIGHT'""\n").upper()

if direction=="LEFT":
 choice=input("You reached lake there is a island in the middle of the lake type 'SWIM'to SWIM or type"
              " 'WAIT' to wait for the boat\n").upper()
 if choice=="WAIT":
     door=input("you have reached island there is three doors , RED, BLUE AND YELLOW pick one\n").upper()
     if door=="RED":
         print("Congratulations! you found the treasure!")
     elif door=="BLUE":
         print("you burned by fire! GAME OVER")
     elif door=="YELLOW":
         print("Eaten by a dinosaur,you have reached jurassic park its seems! GAME OVER!")

     else:
         print("invalid input")
 elif choice=="SWIM":
         print("what a treat for sharks! GAME OVER.")
 else:
     print("invalid input")
else:
    if direction=="RIGHT":
        print("you fell in hole! GAME OVER")
    else:
        print("invalid input")







