import random
import time
from colorama import Fore, Style, init
init(autoreset=True)
choices = ["Rock", "Paper", "Scissors"]
color_list = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
cpu_score = 0
player_score = 0
print(Fore.CYAN + "Type 'help' for game info and binds." + Style.RESET_ALL)  # Show help prompt at the start
while True:
    computer = random.choice(choices)  # Randomize computer's choice each round
    # Assign a random color to each choice
    colored_choices = [random.choice(color_list) + choice + Style.RESET_ALL for choice in choices]
    print(" - ".join(colored_choices))  # Print choices with dashes between them
    print("----------------------------------------")  # Add dashes before input
    player = input("Rock, Paper or  Scissors?").capitalize()
    print("----------------------------------------")  # Add dashes after input
    if player.lower() == 'help':
        print(Fore.GREEN + "Valid inputs:" + Style.RESET_ALL)
        print("  Rock, Paper, Scissors - play a round")
        print("  End - finish the game and show scores")
        print("  Help - show this help message")
        print("  Score - show the current scores")
        print("  Clear - clear the screen and show the current score")
        print("  Made by Noahw1567")
        print(Fore.MAGENTA + "{:^40}".format("Have fun! ^_^") + Style.RESET_ALL)
        print("========================================")
        continue
    if player.lower() == 'score':
        print(Fore.CYAN + f"Current Score -> Player: {player_score} | CPU: {cpu_score}" + Style.RESET_ALL)
        print("========================================")
        continue
    if player == '#09':
        player_score += 10
        # Rainbow effect for cheat code message
        cheat_msg = "Cheat code activated! +10 points! ^_^"
        rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
        rainbow_text = "".join(rainbow_colors[i % len(rainbow_colors)] + c for i, c in enumerate(cheat_msg)) + Style.RESET_ALL
        print(rainbow_text)
        print(f"Your score: {player_score}")
        print("=========================================")
        time.sleep(5)
        # Clear the last three lines (cheat message, score, dashes) by printing blank lines
        print("\033[F\033[K" * 3, end="")
        continue
    if player == '#10':
        cpu_score -= 1
        print(Fore.MAGENTA + "Cheat code activated! -1 CPU point!" + Style.RESET_ALL)
        print(f"CPU score: {cpu_score}")
        print("=========================================")
        time.sleep(5)
        # Clear the last three lines (cheat message, score, dashes) by printing blank lines
        print("\033[F\033[K" * 3, end="")
        continue
    if player.lower() == 'help++':
        cheat_msg = "Cheat Codes:\n  #09 - Adds 10 points to your score! ^_^\n  #10 - Removes 1 point from the CPU!"
        rainbow_colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
        rainbow_lines = cheat_msg.split('\n')
        for line in rainbow_lines:
            rainbow_text = "".join(rainbow_colors[i % len(rainbow_colors)] + c for i, c in enumerate(line)) + Style.RESET_ALL
            print(rainbow_text)
        print("========================================")
        time.sleep(10)
        # Move cursor up 4 lines and clear them (3 lines for cheat, 1 for dashes)
        print("\033[F\033[K" * 4, end="")
        continue
    if player.lower() == 'clear':
        # Clear the terminal screen (works in most terminals)
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.CYAN + f"Screen cleared! Current Score -> Player: {player_score} | CPU: {cpu_score}" + Style.RESET_ALL)
        print("========================================")
        continue
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print(Fore.YELLOW + "Tie!" + Style.RESET_ALL)
        print("----------------------------------------")
    elif player == "Rock":
        if computer == "Paper":
            print(Fore.RED + "You lose!" + Style.RESET_ALL, computer, "covers", player)
            cpu_score+=1
            print("========================================")
        else:
            print(Fore.GREEN + "You win!" + Style.RESET_ALL, player, "smashes", computer)
            player_score+=1
            print("========================================")
    elif player == "Paper":
        if computer == "Scissors":
            print(Fore.RED + "You lose!" + Style.RESET_ALL, computer, "cut", player)
            cpu_score+=1
            print("========================================")
        else:
            print(Fore.GREEN + "You win!" + Style.RESET_ALL, player, "covers", computer)
            player_score+=1
            print("========================================")
    elif player == "Scissors":
        if computer == "Rock":
            print(Fore.RED + "You lose..." + Style.RESET_ALL, computer, "smashes", player)
            cpu_score+=1
            print("========================================")
        else:
            print(Fore.GREEN + "You win!" + Style.RESET_ALL, player, "cut", computer)
            player_score+=1
            print("========================================")
    elif player=='End':
        print("Final Scores:")
        if cpu_score > player_score:
            print(Fore.RED + f"Player:{player_score}" + Style.RESET_ALL)
            print(Fore.GREEN + f"CPU:{cpu_score}" + Style.RESET_ALL)
        elif player_score > cpu_score:
            print(Fore.GREEN + f"Player:{player_score}" + Style.RESET_ALL)
            print(Fore.RED + f"CPU:{cpu_score}" + Style.RESET_ALL)
        else:
            print(Fore.BLUE + f"tie! CPU:{cpu_score} Player:{player_score}" + Style.RESET_ALL)
            print("----------------------------------------")
        break