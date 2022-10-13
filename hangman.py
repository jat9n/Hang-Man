import random

def hangman():
    word = random.choice(['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks'])
    valid = 'qwertyuioplkjhgfdsazxcvbnm'
    turns = 10
    guessmade = ''

    while len(word)>0:
        main=""
        for letter in word:
            if letter in guessmade:
                main = main+letter
            else:
                main = main+"_" +" "

        if main==word:
            print(main)
            print("you win!")
            break

        print("guess the word: " , main)

        guess = input()

        if guess in valid:
            guessmade = guessmade+guess
        else:
            print("invalid input")
            turns=turns+1

        if guess not in word:
            turns = turns-1
            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns==6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns==5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns==4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns==3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns==3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns==2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O|/    ")
                print("     |      ")
                print("    / \     ")
            if turns==1:
                print("1 turns left")
                print("last breath counting")
                print("  --------  ")
                print("   \|O|/    ")
                print("     |      ")
                print("    / \     ")
            if turns==0:
                print("you loose")
                print("u let a kind men die")
                print("  --------  ")
                print("    |x|     ")
                print("   / | \    ")
                print("    | |     ")
                print("the word was "+word)
                break



name = input("enter your name ")
print("welcome %s to the hangman game " %name)
print("-------------------------")
print("try to guess the word in less than 10 attempts")
hangman()
print()
