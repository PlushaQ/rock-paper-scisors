import random, sys, time

START_PROMPT = """
-------------------------------------------

            Welcome in my game!                              
    It's standard version of famous
           ROCK, PAPER, SCISSORS
"""

MENU_PROMPT = """
-------------------------------------------

      Choose what do you want to do:
          'p' to play the game
          'c' to see credits
          'q' to quit the game

-------------------------------------------

Your choice: """

INSTRUCTION = """
-------------------------------------------

    Choose one of the following options:
            '0' to pick scissors
            '1' to pick paper
            '2' to pick rock

-------------------------------------------
"""

credits = """
-------------------------------------------

    This game was made by Maciej Fularz.
     github: https://github.com/PlushaQ

-------------------------------------------"""

player_wins = """
-------------------------------------------

          Computer choosed {}.
  You win. You are great! Congratulations! 

-------------------------------------------
"""
computer_wins = """
-------------------------------------------

          Computer choosed {}.
         You lose. Better luck next time. 
         
-------------------------------------------
"""

tie = """
-------------------------------------------

                It's tie. 
      You dont' lose, but you don't win.
         
-------------------------------------------
"""

play_options = {
    '0': 'scissors',
    '1': 'paper',
    '2': 'rock',
}


def game_core():
    user_choice = input("Your choice: ")
    while user_choice not in play_options.keys():
        print(INSTRUCTION)
        user_choice = input("Your choice: ")
    computer_choice = str(random.randint(0, 2))
    computer_str_choice = play_options[computer_choice]

    if user_choice == computer_choice:
        print(tie)
    else:
        if user_choice == '0':
            if computer_choice == '1':
                print(player_wins.format(computer_str_choice))
            else:
                print(computer_wins.format(computer_str_choice))

        if user_choice == '1':
            if computer_choice == '2':
                print(player_wins.format(computer_str_choice))
            else:
                print(computer_wins.format(computer_str_choice))

        if user_choice == '2':
            if computer_choice == '0':
                print(player_wins.format(computer_str_choice))
            else:
                print(computer_wins.format(computer_str_choice))
    
    continue_game = input("Do you want to play again (y/n)? ").lower()
    while continue_game not in ['y', 'n']:
        print("Pick correct value!")
        continue_game = input("Do you want to play again (y/n)? ").lower()
        
    if continue_game == 'y':
        game_core()
        



def start_game():
    print(INSTRUCTION)
    game_core()


def credit():
    print(credits)
    time.sleep(2)
    menu()

def quit_game():
    print("""
-------------------------------------------

        Thanks for playing my game!
                Goodbye!

-------------------------------------------
    """)
    sys.exit()

menu_options = {
    'p': start_game,
    'c': credit,
    'q': quit_game
}


def menu():
    print(START_PROMPT)
    user_input = None
    while user_input not in menu_options.keys():
        user_input = input(MENU_PROMPT)
    selected_function = menu_options[user_input]
    selected_function()
    menu()

if __name__ == '__main__':
    menu()