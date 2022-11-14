import random

user_score = 0
player_score = 0


def select_option():
    user_option=input("Chooes rock, scissors or paper:  \n")
    if user_option in ["ROck" , "rock" , 'R' , 'r' ]:
        user_option="r"
    elif user_option in ["Paper" , "paper" , 'P' , 'p']:
        user_option ="p"
    elif user_option in ["Scissor" , "scissor" , 'S' , 's']:
        user_option = "s"
    else:
        print("Enter a valid value ")
        select_option()
        return user_option



def computer_option():
    computer_select=random.randint(1, 3)
    if computer_select == 1 :
        computer_select="r"
    elif computer_select == 2:
        computer_select = "p"
    else:
        computer_select = "s"
        return  computer_select


        

