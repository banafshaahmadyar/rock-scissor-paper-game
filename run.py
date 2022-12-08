import random

player_score = 0
computer_score = 0


def select_option():

    while True:
        player_option = input("Chooes rock, scissors or paper: ")
        if validate_user_value(player_option):
            return get_user_output(player_option)


def validate_user_value(value):
    if value in ["ROck", "rock", 'R', 'r', "Paper", "paper", 'P', 'p', "Scissor", "scissor", 'S', 's']:
        return True
    else:
        print("Enter a valid value")
        return False


def get_user_output(value):
    if value in ["ROck", "rock", 'R', 'r']:
        result = "r"
    elif value in ["Paper", "paper", 'P', 'p']:
        result = "p"
    elif value in ["Scissor", "scissor", 'S', 's']:
        result = "s"
    return result


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


def check_computer_result(user, computer):

    message = ""
    user_output = ""
    computer_output = ""
    status = ""
    p_score = 0
    c_score = 0

    if user == "r":
        if computer == "r":
            status = "alike"
        elif computer == "p":
            status = "win"
            p_score += 1
        elif computer == "s":
            status = "lose"
            c_score += 1
        user_output = "Rock"
    elif user == "p":
        if computer == "r":
            status = "win"
            p_score += 1
        elif computer == "p":
            status = "alike"
        elif computer == "s":
            status = "lose"
            c_score += 1
        user_output = "Paper"
    elif user == "s":
        if computer == "r":
            status = "win"
            p_score += 1
        elif computer == "p":
            status = "lose"
            c_score += 1
        elif computer == "s":
            status = "alike"
        user_output = "scissor"
    else:
        return False

    if computer == "r":
        computer_output = "Rock"
    elif computer == "p":
        computer_output = "Paper"
    elif computer == "s":
        computer_output = "scissor"

    message = f"      You select {user_output}, Computer Selected {computer_output}. You {status}"
    print(message)
    return [p_score, c_score]


while True:

    computer_select = Computer_option()
    print("===================================================================")
    player_option = select_option()

    result = check_computer_result(player_option, computer_select)
    if result == False:
        print("Invalid Data entered")
        pass
    else:
        player_score = player_score + int(result[0])
        computer_score = computer_score + int(result[1])
        print("")
        print("         Player score = " + str(player_score))
        print("         user score = " + str(computer_score))
        print("")
    print("===================================================================")

    if result != False:
        User_Choies = input("       Wanna play agian ?(Y/N)")
        if User_Choies in ["yes", "Yes", "y", "Y"]:
            pass
        elif User_Choies in ["NO", "no", "N", "n"]:
            break
        else:
            break
