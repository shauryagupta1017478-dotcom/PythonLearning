'''
input from user(rock ,paper , scissoe)
computer choice(computer wil choice remdomly)
result print

rock--rock > tie
rock--paper > paper win 
rock--scissor > rock win

paper--paper > tie
paper--rock >paper
paper--scissor >scissor win

scissor--scissor >tie 
scissor--rock >rock win 
scissor--paper > scissor win
'''



import random

iteam_list = ['rock' , 'paper' ,'scissor']
user_choice = input("enter your move( rock ,paper , scissoe)")
comp_choice = random.choice(iteam_list)
print(f'user choice = {user_choice} OR computerchoice = {comp_choice}')

if user_choice == comp_choice :
    print("both chooices same , match tie")

elif user_choice == 'rock' :
    if comp_choice == 'paper':
        print ("computer win")
    elif comp_choice == 'scissor':
        print ("rock win")

elif user_choice == 'paper':
    if comp_choice == 'rock':
        print("user win")
    elif comp_choice == 'scissor':
        print("computer win :")

elif user_choice == 'scissor' :
    if comp_choice == 'paper' :
        print("user win")
    elif comp_choice == 'rock' :
        print("computer win ")

else :
    print("our of choice")

