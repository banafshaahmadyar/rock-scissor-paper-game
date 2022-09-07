import random

user_score = 0
player_score = 0
return_to_code = True

# Here palyer should select his or her choies
print("rock...paper...scissor")

while return_to_code:
    # Here user can inter the loop of playiny this game
    lap = int(input("Enter the number of rounds you want to play? "))
    
    # by using of random in here lap of user will increase one by one
    for num in range(1, lap + 1):

        # Here player will enter the choice and will compare with computer
        user = input("Enter your choies ?")
        number = random.randint(1, 3)

        player = ""
        if number == 1:
            player = "rock"
            print("player choies rock")
        elif number == 2:
            player = "paper"
            print("player choies paper")
        elif number == 3:
            player = "scissor"
            print("player choies scissor")

        # in all game we have three choies and eight comparison.
        if player == "rock" and user == "paper":
            print("user win")
            user_score += 1

        elif player == "rock" and user == "scissor":
            print("player win")
            player_score += 1

        elif player == "paper" and user == "rock":
            print("player win")
            player_score += 1

        elif player == "paper" and user == "scissor":
            print("user win")
            user_score += 1

        elif player == "scissor" and user == "paper":
            print("player win")
            player_score += 1

        elif player == "scissor" and user == "rock":
            print("user win")
            user_score += 1
            
        elif player == "scissor" and user == "siccor":
            print("equals !!!")

        elif player == "rock" and user == "rock":
            print("equals !!!")
            
        elif player == "paper" and user == "paper":
            print("equals !!!")
        else:
            print("Ooops try again !!!")

    print(f"user {user_score} win ")
    print(f"player {player_score} win")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() == "y":
        return_to_code = True
    else:
        return_to_code = False
