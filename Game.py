
"""
Make a game of rock, paper scissors against the computer. 
Problem
    Tell the user about the Game Instruction
    Tell user to enter either rock,paper or scissors
    Get the response from the user 
    
    Generate a random choice from (rock, paper, scissors)
    Compare user selection and computer selection
    Display who wins.
Extension
    Make sure the user enters a valid entry.
    Add a loop structure to play several times and keep a running score
    
Hint
  Rock  vs paper   -> paper wins
  Rock  vs scissor -> Rock wins
  paper vs scissor -> scissor wins

"""
list1=["Rock","paper","scissor"]
point_c=0
point_u=0

#Defining game instructions
print("Game Instructions:")
print("""Rock  vs paper   -> paper wins
  Rock  vs scissor -> Rock wins
  paper vs scissor -> scissor wins""")

#imporing random module
import random

while True:
    
    
    num=input("Do you want to play:(Y/N):")
    if(num=='Y' or num=='y'):

        #taking input from user
        user_input=input("Enter either Rock, Paper, Scissor:")
        print("\n\tUser's input->",user_input)
        user=user_input.lower()
        
        #taking input from computer
        computer=random.choice(list1)
        print("\n\tComputer's input->",computer)
        computer=computer.lower()

        print("\n\t",user,"\tVS",computer)
        
        #setting conditions according to the rule:
        if(user=="rock" and computer=="paper" or user=="paper" and computer=="scissor" or user=="scissor" and computer=="rock"):
            print("\n\tComputer wins")
            point_c += 1
            
        elif(user=="scissor" and computer=="paper" or user=="rock" and computer=="scissor" or user=="paper" and computer=="rock"):
            print("\n\tUser wins")
            point_u += 1
            
        elif(user==computer):
            print("\n\tDraw")
            
        else:
            print("\n\tInvalid input")
            
    #breaking while loop 
    elif(num=='N' or num=='n'):
        print("\n\tUser points:",point_u," computer points:",point_c)
        if(point_u > point_c):
            print("\n***User wins the game***")
        elif(point_u < point_c):
            print("\n***Computer wins the game***")
        else:
            print("\n***ITS A DRAW***")
        break
    
    else:
        print("\n\tInvalid input")
    
