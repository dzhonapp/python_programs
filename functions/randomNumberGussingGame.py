import random
flag = True


count = 0
play_won = 0
while flag:
    user_guess = []
    numberRandom = random.randint(1, 10)
    for i in range(3):
        user_input = int(input("Guess the number! "))
        user_guess.append(user_input)
    count = count + 1
    if numberRandom in user_guess:
        play_won = play_won +1
        print("Whao, You got it!" , "Random Number was: " , numberRandom)
    else:
        print("Sorry buddy you have to play again, wanna play? " + "Random Number was: " , numberRandom)

    play = input("Y/N")
    if play.upper() == "Y":
        continue
    elif play.upper() =="N":
        flag = False
        print("You played ", " times! and won from them just! ", play_won, "times!")
    else:
        flag = False

print(user_guess)