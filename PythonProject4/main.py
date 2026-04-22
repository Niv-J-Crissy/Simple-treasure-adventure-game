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
print("Hello traveler in this game you will try to find the treasure and overcome problems and dilemmas")
first_answer = input("You have encountered a comically large tree.\n would you climb it? or would you just go past it?\n climb or pass: ")

if first_answer == "climb" or first_answer == "Climb":
        second_answer = int(input("You have successfully climbed to the first branch and encountered three large doors, numbered 1 to 3.\n which one will you choose\n 1, 2 or 3: "))
        if second_answer == 2:
            third_answer = input("After going through the door you have encountered a bird towering a ridicules 3.5m, you notice she is guarding a large gold egg.\n would you:\n a. cast fireball\n b. run towards the egg, snatch it and run for it\n c.leave, fuck that ain't no way\n a, b or c: ")
            if third_answer == "a" or third_answer == "A":
                print("You think for awhile, then and idea surges you...\n what if i try it, you think to yourself.\n You concentrate everything you learned from naruto and some youtube tutorial you watched into one fireball, you scream FIREBALL!!!!!!!\nNothing happened the bird killed you.\n No, seriously what did you think would happen. ")
            elif third_answer == "b" or third_answer == "B":
                print("You try and run for it! the bird attacks you!!!!!!\n YOU DODGED?!?!?!?!?!\n She goes for it AGAIN!\n DID YOU JUST BACKFLIP ABOUT HER HEAD?!?!?!?!\n holy shit you got it you son of a bitch, RUNNNNNNN\n wow you made it out... you actually got the egg well done man\n YOU WON")
            elif third_answer == "c" or third_answer == "C":
                print("Not gonna lie, i would absolutely do the same man...\n You looked at this INSANE 3.5m bird.\n FUCK THAT, I am leavin.\n You didnt get the egg, but you aint stupid i like you.\n You know what you get a cookie")
        elif second_answer == 3:
            print("you open the door to find a hungry dragon that hasn't eaten in decades.\nYour head got chopped of immediately ")
        elif second_answer == 1:
            print("You open the first door really slowly... you can feel there is something there\n you explode")
else:
    print("Like you didn't die or something but you just go on about your day, nothing special happens")
