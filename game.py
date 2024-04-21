import random

score = 0

while True:
    bot = random.randint(0, 2)

    userinput = input("Choose scissors, paper or stone \n").lower()

    scissors = 0
    paper = 1
    stone = 2

    user = 3

    while user == 3:
        if userinput == "scissors":
            user = 0
        elif userinput == "paper":
            user = 1
        elif userinput == "stone":
            user = 2
        else:
            userinput = input("Please enter again! Choose scissors, paper or stone \n") 
            user = 3

    if bot == 0:
        botinput = "scissors"
    if bot == 1:
        botinput = "paper"
    if bot == 2:
        botinput = "stone"
    print("The bot chose "+botinput)

    if user == bot:
        print("TIE!")

    if bot == 0 and user ==1:
        score -= 1
        print("You Lose!")
    if bot == 0 and user ==2:
        score += 1
        print("You Win!")
    if bot == 1 and user ==0:
        score += 1
        print("You Win!")
    if bot == 1 and user ==2:
        score -= 1
        print("You Lose!")
    if bot == 2 and user ==0:
        score -= 1
        print("You Lose!")
    if bot == 2 and user ==1:
        score += 1
        print("You Win!")
        
    print("===== Your score is: "+str(score)+" =====")