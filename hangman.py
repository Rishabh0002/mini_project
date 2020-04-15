#Hangman Game
import random 
words = ['apple','banana','orange','coconut','strawberry','lime','grapefruit','lemon','kumquat','blueberry','melon']

while True:
    print("Guess the name of the fruit:-")
    user_input=input("\nPress enter/return to play and press Q to exit:")
    user=user_input.lower()
    if(user == 'q'):
        break
    elif(user == ""):
        word=random.choice(words)
        good=[]
        bad=[]
        list1=[]
        glist=[]
                
        while len(bad) < 6 and len(good) != len(list(word)):
            for letter in word:
                if letter in good:
                    print ( letter , end='')
                else:
                    print('_', end=' ')
               
                    
            print("\n\tStrike {}/6".format(len(list(bad))))

            guess=input("\n\nGuess a letter:")
            if(guess in word):
                glist.append(guess)
                good.append(guess)
                if(len(set(glist)) == len(set(word))):
                    print("\n\n**You won**\nThe word was:",word)
                    break
                    
            elif len(guess) != 1:
                print ("\nYou can only guess a single letter !")
                continue
            elif not guess.isalpha():
                print ("\nYou can only guess letters !")
                continue
                    
            else:
                bad.append(guess)
                
        else:
            print("\n\nYou didn't guess it my word was:",word)
    else:
        print("\n Invalid input")
            
