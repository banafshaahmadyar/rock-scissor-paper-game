## ROCK...PAPER...SCISSOR

       **What Is Rock Paper Scissors?**
       
You may have played rock paper scissors before. 

Maybe you’ve used it to decide who pays for dinner or who gets first choice of players for a team.

If you’re unfamiliar, rock paper scissors is a hand game for two or more players.

Participants say “rock, paper, scissors” and then simultaneously form their hands into the shape of a rock (a fist

a piece of paper (palm facing downward), or a pair of scissors (two fingers extended).

The rules are straightforward:

   - Rock smashes scissors.
   - Paper covers rock.
   - Scissors cut paper.
   <img width="854" alt="image" src="https://user-images.githubusercontent.com/100950189/207933142-5f49a45e-bd9f-4b02-ad7d-32ddde2d3735.png">
   
   ## How it works
   ---
   The game is played with three possible hand signals that represent a rock, paper, and scissors.
   The rock is a closed fist; paper is a flat hand with fingers and thumb extended and the palm facing downward;
   and scissors is a fist with the index and middle fingers fully extended toward the opposing player.
   Rock wins against scissors; paper wins against rock; and scissors wins against paper.
   If both players throw the same hand signal, it is considered a tie, and play resumes until there is a clear winner. 
   ---
   
   ## Existing feather
   * This will stared with some limited values form player and player select form that choice
   * THen it will comare player choice with computer choice and show result
   * After that will Increase and decrease scores of winner and losser
   * At the end ask from player that wanna play again or no

<img width="545" alt="image" src="https://user-images.githubusercontent.com/100950189/206897696-c9eaab3c-a0a2-4827-a317-27360ec8d0eb.png">

## Data Model

---
This game is singal player game that one side is player and other side is computer.
Then will compare both side and show result.
Here i used multi functions like : def select_option(): , def validate_user_value(value): , def get_user_output(value): ,def Computer_option():
and def check_computer_result(user, computer): .

## Testing
---
I have manually tested this project by doing the following steps:
* Passed the code through the PEP8 linter and did't found any problem there
* I have entered invalid inputs like string, empty value, but every thing was working normally and each error was handled very well.
* I tested it in my local terminal and Heroku terminal it was working as expected
---

## Validator Testing
* PEP8
* No error on PEP9

## Deployment

---
This project was deployed in github and then Heroku

* Steps for deployment:
    * Fork or clone this repository
    * Create a new Heroku app
    * Set the buildbacks to ```Python``` and ```NodeJS``` in that order
    * Link the Heroku app to the repository
    * Click on **Deploy**
 ---


## Credits
---
* Code Institute for deployment terminal
* Google and other free websites for game idea
---
   
