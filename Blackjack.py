#Leikur Eftir Hrafnkel Þorra Og Erlu Óskarsdóttir

roundover = False
gameover = False
mymoney = 5000

while gameover == False:
    mybet = 0
    gameover = False
    roundover = False
    sumofcards = 0
    drawanothercard = 0
    cpucard = 0
    pot = 0
    card1 = 0
    card2 = 0
    if (int(mymoney) > 14999):
        print("YOU HAVE OVER 14999$ YOU WIN!")
        exit()
    elif (int(mymoney) == 0):
        print("You Have no money. You lose.....")
        exit()
    else:
        print("")
        print("i have", mymoney, "$")
        mybet = input('i bet: ')
        if int(mybet) < 500:
                print("you have to bet 500 or more")
        elif int(mybet) > mymoney:
                print("Bet is to high you dont have that much to give!")
        elif int(mymoney) < 1:
                print("You are out of money")
                exit()

        elif int(mybet) >= 500:

            print('i bet', mybet, "$")
            mymoney = int(mymoney) - int(mybet)
            print('then i have', mymoney, '$ left and i have', mybet, '$ on the table')
            from random import randint
            card1 = (randint(1, 13))
            cpucard = (randint(7,23))
            print("Your first drawn card has the value of ", card1)
            sumofcards = sumofcards + card1
            pot = 2 * int(mybet)
            while roundover == False:
                drawanothercard = input("Enter 'Yes' if you want to draw another card: ").upper()
                if drawanothercard == "YES":
                    from random import randint
                    card2 = (randint(1,13))
                    sumofcards = sumofcards + card2
                    print("the next card had the value of ", card2, " the sum of your cards is: ", sumofcards)
                    if cpucard > 21:
                        roundover = True
                        print("Your opponent went over 21 and lost! YOU WIN!")
                        mymoney = mybet * 2
                    elif sumofcards > 21 and cpucard < 22:
                        roundover = True
                        print("You Went over 21 and lost! YOU LOST")
                    elif sumofcards > 21 and cpucard > 21:
                        roundover = True
                        print("You and your opponent both went over 21! DRAW!")
                        mymoney = mymoney + mybet
                elif drawanothercard == "NO":
                    if sumofcards > cpucard and sumofcards < 22: #if you win
                        roundover = True
                        print("You have the sum of ", sumofcards, " and the opponent has", cpucard)
                        print("You win! You earned ", int(mybet), "$")
                        mymoney = int(mymoney) + int(pot)
                    elif sumofcards < cpucard and sumofcards < 22: #if you win
                        roundover = True
                        print("You have the sum of ", sumofcards, " and the opponent has", cpucard)
                        print("You Lost! You have lost", mybet, "$")
                    elif sumofcards == cpucard: #if there is a draw
                        roundover = True
                        print("You have the sum of ", sumofcards, " and the opponent has", cpucard)
                        print("You and your opponent have the same sum of cards! you get your bet back! DRAW!")
                        mymoney = mymoney + int(mybet)