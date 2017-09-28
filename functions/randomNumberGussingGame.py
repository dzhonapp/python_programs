import random
flag = True

user_guess = []

while flag:
    numberRandom = random.randint(1, 10)
    for i in range(3):
        user_input = int(input("Guess the number! "))
        user_guess.append(user_input)

    if numberRandom in user_guess:
        print("You got it!" , "Random Number was: " , numberRandom)
    else:
        print("Sorry buddy you have to play again, wanna play? " + "Random Number was: " , numberRandom)

    play = input("Y/N")
    if play.upper() == "Y":
        continue
    else:
        flag = False
print(user_guess)