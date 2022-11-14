import random

player_score = 0
computer_score = 0


def Select_option():
    player_option = input("Chooes rock, scissors or paper: ")
    if player_option in ["ROck", "rock", 'R', 'r']:
        player_option = "r"
    elif player_option in ["Paper", "paper", 'P', 'p']:
        player_option = "p"
    elif player_option in ["Scissor", "scissor", 'S', 's']:
        player_option = "s"
    else:
        print("     Enter a valid value ")
        Select_option()
    return player_option


def Computer_option():
    computer_select = random.randint(1, 3)
    if computer_select == 1:
        computer_select = "r"
    elif computer_select == 2:
        computer_select = "p"
    else:
        computer_select = "s"
        Computer_option()
    return computer_select


while True:
    print("___________________________________________________________")

    player_option = Select_option()
    computer_select = Computer_option()

    print("__________________________________________________________")
    if player_option == "p":
        if computer_select == "r":
            print("     You select paper, Computer select rock. You win (: ")
            player_score += 1

        elif computer_select == "p":
            print("     You select paper, The computer select paper. You are alike ")

        elif computer_select == "s":
            print("     You select paper, The computer select scissor. You loss ): ")
            computer_score += 1

    elif player_option == "r":
        if computer_select == "r":
            print("     You select rock, Computer select rock. you are alike : ")

        elif computer_select == "s":
            print("     You select rock , The computer select scissor . You loss  );")
            computer_score += 1

        elif computer_select == "p":
            print("     You select rock, The computer select paper. You win (: ")
            player_score += 1

    elif player_option == "s":
        if computer_select== "r":
            print("     You chose scissors. The computer chose rock. You lose ):")
            computer_score += 1

        elif computer_select == "p":
            print("     You chose scissors. The computer chose paper. You win (:")
            player_score += 1

        elif computer_select == "s":
            print("     You chose scissors. The computer chose scissors. You tied.")

    print("")
    print("         Player score = " + str(player_score))
    print("         user score = " + str(computer_score))
    print("")

    User_Choies = input("       Wanna play agian ?(Y/N)")
    if User_Choies in ["yes", "Yes", "y", "Y"]:
        pass
    elif User_Choies in ["NO", "no", "N", "n"]:
        break
    else:
        break
