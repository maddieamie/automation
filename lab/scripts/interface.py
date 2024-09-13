import automate
from rich.console import Console
from rich.prompt import Prompt

import time

import os
import re
import shutil

# interface options
# create/delete folder
# create/delete user
# choose folder ->
# sort / count -> what file type to count?/ rename - files based on a specific pattern (date, number by created date)
# choose log -> parse
# progress bars for all


# Instantiate a console object
console = Console()


def quit_program():
    console.print('See you later! :notes:')
    return False


def main():
    """Main function to run the CLI app."""
    while True:
        console.print("\n1. Folder Options \n2. User Options \n3. Log Options \n4. Quit")
        choice = Prompt.ask("Enter a number to choose a task.", choices=['1', '2', '3', '4'], default='4')

        if choice == '1':
            console.print("Folder: \n1. Make \n2. Delete \n3. Sort \n4. Count Files \n5. Exit")
            f_choice = Prompt.ask("Enter a number to choose a task.", choices=['1', '2', '3', '4', '5'])
            if f_choice == '1':
                directory = Prompt.ask("Which folder? Enter its name.")
                automate.make_folder(directory)
            elif f_choice == '2':
                directory = Prompt.ask("Which folder? Enter its name.")
                automate.del_folder(directory)
            elif f_choice == '3':
                directory = Prompt.ask("Which folder? Enter its name.")
                automate.sort_things(directory)
            elif f_choice == '4':
                directory = Prompt.ask("Which folder? Enter its name.")
                file_type = Prompt.ask("Which kind of file would you like to count in this folder?")
                automate.count_things(directory, file_type)
            else:
                break
        elif choice == '2':
            console.print("User: \n1. Create User \n2. Delete User \n3 Exit")
            u_choice = Prompt.ask("Enter a number to choose a task.", choices=['1', '2'])
            if u_choice == '1':
                user = Prompt.ask("Which user? Enter their name.")
                # progress bar
                automate.create_user(user)
            elif u_choice == '2':
                user = Prompt.ask("Which user? Enter their name.")
                automate.del_user(user)
            else:
                continue
        elif choice == '3':
            directory = Prompt.ask("Which folder contains your log? Enter its name.")
            # list files in folder to console
            log_folder = os.path.join(directory, 'logs')
            if os.path.exists(log_folder):
                os.listdir(log_folder)
            else:
                automate.sort_things(directory)
                os.listdir(log_folder)
            file = Prompt.ask("Which log file?")
            automate.parse_log(file)

        elif choice == '4':
            console.print("Are you sure you want to quit?")
            ans = Prompt.ask("Yes or no?", choices=['yes', 'no'], default='no')
            if ans == 'yes':
                quit_program()
            elif ans == 'no':
                continue
            else:
                console.print("Please type 'yes' or 'no'.")

        else:
            console.print("Boop!")
            break


if __name__ == "__main__":
    main()

