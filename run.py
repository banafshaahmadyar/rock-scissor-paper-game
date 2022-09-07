import random

# user_score = 0
# player_score = 0

# Here palyer should select his or her choies
print("rock...paper...scissor")


# Here user can inter the loop of playiny this game
lap = int(input("please return your lap ?"))


# by using of random in here lap of user will increase one by one
for num in range(1, lap+1):

    # Here player will enter the choice and will compare with computer choice
    user = input("Enter your choies ?")
    number = random.randint(1, 3)

    player = ""
    if number == 1:
        player = "rock"
        print("player choies rock")
        # player_score +=1
    elif number == 2:
        player = "paper"
        print("player choies paper")
        # player_score +=1
    elif number == 3:
        player = "scissor"
        print("player choies scissor")
        # player_score +=1

# in all game we have three choies and eight compear and one out of compear.
    if player == "rock" and user == "paper":
        print("user win")
    elif player == "rock" and user == "scissor":
        print("player win")
    elif player == "paper" and user == "rock":
        print("player win")
    elif player == "paper" and user == "scissor":
        print("user win")
    elif player == "scissor" and user == "paper":
        print("player win")
    elif player == "scissor" and user == "rock":
        print("user win")
    elif player == "scissor" and user == "siccor":
        print("equals !!!")
    elif player == "rock" and user == "rock":
        print("equals !!!")
    elif player == "paper" and user == "paper":
        print("equals !!!")
    else:
        print("Ooops try again !!!")
