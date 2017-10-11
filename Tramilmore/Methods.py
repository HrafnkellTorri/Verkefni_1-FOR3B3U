#Imports

import time
import random

#Green = Sullum
#Blue = Tramil
#Yellow = StoryTeller
#Wall = Red
#Exit code 5 is quiting
#Exit code 4 is Trapdoor

def intro():
    Storyteller(),print("*Two figures stand in a shadowy entrence*")
    Sullum(),print("Tramilmore i can't see anything in this darkness.")
    Tramil(),print("Keep moving Sullumbull, i think i see some light up ahead.")
    Storyteller(),print("*On a wall the heroes spot a lone torch on the wall. As they approach they can make out old letters carved on a gigantic gray wall*")
    Sullum(),print("Can you see what is writen on the wall Tramilmore?")
    Tramil(),print("Yes i think it's a riddle.")
    Storyteller(),print("*A loud voice is heard as a face appears on the wall*")
    Wall(),print("'If thou can answer these 5 questions you may pass this door which will lead you to the ancient Drafgnast named Drafgnast and if thee fail you will be slain where you stand!!!'")
def PlayGame():
    decision = False
    while decision == False:
        Wall()
        accept = input("Do thee accept? :").upper()
        if (accept == "NO"):
            Sullum(), print("Tramilmore this is to dangerous ser!")
            Tramil(), print("I agree Sullumbull. Let's head back to the village and we shall return once we have gathered more knowledge")
            exit(5)
        elif (accept == "YES"):
            Storyteller(), print("*The heroes agree that this is a risk worth taking* We accept!")
            print("*The wall clears it's throat*")
            decision = True
        else:
            Tramil(),print("....."),Sullum(),print(".....")
def FirstQuestion():
    Question1()
    answer = Answer("Sullumbullum's answer is :","A")
def SecondQuestion():
    Tramil(),print("Thanks Sullum! I never thought it was the on that melted in 2099")
    Sullum(),print("It melted in 2067.....")
    Question2()
    Tramil(),print("This is a question for I!")
    answer = Answer("Tramilmore's answer is :","A")
def ThirdQuestion():
    Sullum(),print("That one was easy....")
    Tramil(),print("Don't mock me.....")
    Wall(),print("'Now i won't hold back. The easy part is over!")
    Question3()
    answer = Answer("Sullum : ","C")
def FourthQuestion():
    Sullum(),print("That wasn't so hard?")
    Tramil(),print(".....")
    Wall(),print(".....")
    Question4()
    answer = Answer("Sullum : ","A")
def FifthQuestion():
    Tramil(), print(".....")
    Sullum(),print("These questions are getting hard now!")
    Tramil(),print(".....")
    Wall(),print("I Told YEE!")
    Question5()
    answer = Answer("Sullum : ","B")

def Battle():
    Wall()
    print("You may pass....")
    Storyteller()
    print("The Giant wall slides to the side and in the distance the heroes spot the ancient evil Drafgnast")
    Sullum(), print("TRAMIL WATCHOUT!")
    Storyteller(), print("The monster leaps towards tramil but he manages to evade just in time.")
    print("The Battle has begun!")
    tramillife = 4
    sullumlife = 3
    drafgnastlife = 6
    healsleft = 2
    tramildead = False
    sullumdead = False
    while(tramillife > 0 or sullumlife > 0 or drafgnastlife > 0):
        Wall()
        print("----------------------------------------------------------------------------------")
        print("Tramilmore HP left : " + str(tramillife) + "\nSullumBull HP left : " + str(sullumlife) + "\nDrafgnast  HP left : " + str(drafgnastlife))
        Storyteller()
        action = input("What action will you take? (a) Attack (b) Heal (c) Flee : ").upper()
        if(action == "A"):
            if(tramildead == False):
                damage = random.randint(0, 2)
                Tramil()
                print("Tramil stabs the beast and does : " + str(damage) + " Damage!\n")
                drafgnastlife -= int(damage)
            else:
                damage = random.randint(0, 1)
                Sullum()
                print("Tramil attacks the beast and does : " + str(damage) + " Damage!\n")
                drafgnastlife -= int(damage)
        if(action == "B"):
            if(healsleft != 0 and sullumdead == False):
                Sullum()
                choice = input("Who will you heal? (a) Tramilmore (b) Sullumbull : ").upper()
                healsleft -= 1
                if(choice == "A"):
                    tramillife = 4
                    print("Tramilmore has been fully healed")
                elif(choice == "B"):
                    sullumlife = 3
                    print("Sullum has healed him self fully")
            elif(healsleft < 1):
                Wall(),print("You don't cannot heal anymore!")
            elif(sullumdead == True):
                Wall(),print("Sullum is dead! no healing can be done")
        if (action == "C"):
            Flee()


        #Drafgnast attacks
        if(drafgnastlife > 0):
            drafgnastattack = random.randint(1,2)
            choice = random.randint(1,2)
            if(choice > 1 and tramildead == False):
                tramillife -= drafgnastattack
                Wall(),print("The Beast Strikes Tramilmore inflicting " + str(drafgnastattack) + " damage upon him")
            elif(sullumdead == False):
                sullumlife -= drafgnastattack
                Wall(), print("The Beast Attacks Sullumbull inflicting " + str(drafgnastattack) + " damage upon him")


        # If a Hero die
        if (sullumlife < 1 and sullumdead == False):
            sullumdead = True
            Sullum()
            print("ARG!"), Storyteller(),print("Sullum HAS FALLEN!")
        if (tramillife < 1 and tramildead == False):
            tramildead = True
            Tramil()
            print("ARG!"), Storyteller(),print("TRAMIL HAS FALLEN!")

        if(drafgnastlife < 1):
            if(sullumlife < 1):
                Tramillives()
            elif(tramillife < 1):
                SullumLives()
            else:
                Bothlive()

def Answer(name,answer):
    Answer = input(name).upper()
    finalanswer = input("'Is that your final answer?'").upper()
    while finalanswer == "NO":
        Answer = input(name).upper()
        finalanswer = input("*Is that your final answer?'*").upper()
    if Answer != answer:
        Trapdoor()
    else:
        print("That is correct hero.\n*The heroes sigh in relief*")

#List of Questions
def Question1():
    Wall(), print("'#1 What is the name of the biggest glacier in pre-war Iceland?' (a) Vatnajökull. (b) Langjökull (c) There are no galciers in Iceland?.'")
def Question2():
    Wall(),print("'#2 Where is the strongest muscle in the body located?' *(a) In the Jaw. (b) In the Thigh. (c) in the Tounge.'")
def Question3():
    Wall(),print("'#3 Mr. Smith has 4 daughters. Each of his daughters has a brother. How many children does Mr. Smith have?' (a) 8. (b) There is not brother. (c) 5'")
def Question4():
    Wall(),print("'#4 During what month do people sleep the least?' *(a) February. (b) January. (c) July.'")
def Question5():
    Wall(),print("'#5 What is the center of gravity? *(a) Center of Earth. (b) V. (c) There is no thing as the center of gravity the earth is flat!'")

#Types of failures
def Trapdoor():
    print("A Trapdoor bellow Tramilmore and Sullumbull opens up and they both fell to their death! The end........")
    exit(4)
def Flee():
    Sullum(), print("Tramilmore this is to dangerous ser!")
    Tramil(), print("I agree Sullumbull. Let's head back to the village and we shall return once we have gathered more knowledge")
    exit(4)

#Types of Successes
def Tramillives():
    Storyteller()
    print("Drafgnast has been slain. But Sullum has fallen... The End.")
    exit(10)
def SullumLives():
    Storyteller()
    print("Drafgnast has been slain. But Tramil has fallen... The End.")
    exit(10)
def Bothlive():
    Sullum(), print("Wow....This has to be the best ending...")
    Tramil(), print("I agree Sullumbull. Dragnast has been slayed and we are both still standing.")
    Storyteller(),print("Drafgnast has been slain. This is the best possible outcome congrats :) The End.")
    exit(10)

#Report
def HeroStatusReport():
    ("Tramilmore HP left : " + str(tramillife) + "\nSullumBull HP left : " + str(sullumlife) + "\nSullum can heal " + str(healsleft) + " more times\n")

#Colors, delays and character Traits
def Wall(): #RED
        time.sleep(2)
        print("\033[1;31;0m")
def Sullum(): #GREEN
        time.sleep(1)
        print("\033[1;32;20m")
def Storyteller(): #STORYTELLER
        time.sleep(1)
        print("\033[1;33;0m")
def Tramil(): #BLUE

        time.sleep(2)
        print("\033[1;34;0m")
def Purple():
        print("\033[1;35;0m")
def Cyan():
        print("\033[1;36;0m")
def White():
        print("\033[1;37;0m")
