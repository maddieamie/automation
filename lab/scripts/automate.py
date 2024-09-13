# create new folder with specified name
# handle deleted user -> create temp folder to hold user info of deleted user
# sort documents
# when given a folder, sort into logs and mail folders
# parse log file for errors and warnings
# errors.log: Contains all error messages.
# warnings.log: Contains all warning mess
# Counting the number of specific file types in a directory.

import os
import re
import shutil

from rich.progress import Progress
from rich.console import Console

# Instantiate a console object
console = Console()


def make_folder(folder_name):
    parent = "../assets/user-docs"

    # Join the parent directory with the directory name
    path = os.path.join(parent, folder_name)

    # Remove the directory
    with Progress() as progress:
        task = progress.add_task("[dark_sea_green2]Creating directory...", total=100)
        try:
            os.mkdir(path)
            progress.update(task, advance=50)
            console.print("Directory '%s' has been created successfully:" % directory)
            progress.update(task, advance=50)
        except OSError as error:
            progress.update(task, advance=100)
            console.print(error)
            console.print("Directory '%s' cannot be created:" % directory)


def change_directory_to_target(relative_path, folder_name):
    """
    Changes the current working directory to the target folder inside the given relative path.
    --> Will try to automate this process more in the future.

    Args:
        relative_path (str): The relative path from the current working directory.
        folder_name (str): The name of the folder to target within the relative path.
    """
    # Get the current working directory
    current_directory = os.getcwd()

    # Create the full path
    full_path = os.path.abspath(os.path.join(current_directory, relative_path))

    # Create the target path
    target = os.path.join(full_path, folder_name)

    # Change to the target directory
    os.chdir(target)
    return target


def del_folder(folder_name):
    parent = "../assets/user-docs"

    # Join the parent directory with the directory name
    path = os.path.join(parent, folder_name)

    # Remove the directory
    with Progress() as progress:
        task = progress.add_task("[hot_pink3]Deleting directory...", total=100)
        try:
            os.rmdir(path)
            progress.update(task, advance=50)
            console.print("Directory '%s' has been deleted successfully:" % directory)
            progress.update(task, advance=50)
        except OSError as error:
            progress.update(task, advance=100)
            console.print(error)
            console.print("Directory '%s' cannot be removed:" % directory)


def create_user(name):
    # Define the relative path from the current directory to the target directory
    relative_path = "../assets/user-docs"

    # Create the full path
    full_path = os.path.abspath(os.path.join(os.getcwd(), relative_path))

    # Check if the path exists, if not, create it
    with Progress() as progress:
        task1 = progress.add_task("[dark_sea_green1]Checking for user directory...", total=100)
        task2 = progress.add_task("[light_sky_blue1]Creating path...", total=100)
        task3 = progress.add_task("[thistle1]Creating user...", total=100)
        progress.update(task1, advance=50)
        if not os.path.exists(full_path):
            progress.update(task1, advance=50)
            os.makedirs(full_path)
            progress.update(task2, advance=50)
            # create user path
            user_path = os.path.join(full_path, name)
            os.mkdir(user_path)
            progress.update(task3, advance=100)


def del_user(name):
    # I need to find the user folder.......
    # Define the relative path from the current directory to the target directory
    relative_path = "../assets/user-docs"

    full_path = os.path.abspath(os.path.join(os.getcwd(), relative_path))
    user_path = os.path.join(full_path, name)

    # Check if the path exists, if not, create it
    with Progress() as progress:
        task1 = progress.add_task("[dark_sea_green1]Checking for user directory...", total=100)
        task2 = progress.add_task("[light_sky_blue1]Creating temp folder...", total=100)
        task4 = progress.add_task("[light_goldenrod2]Moving files...", total=100)
        task3 = progress.add_task("[thistle1]Deleting user...", total=100)
        progress.update(task1, advance=50)
        if not os.path.exists(user_path):
            progress.update(task1, advance=50)
            console.print(f'User {name} does not exist.')
        else:
            progress.update(task1, advance=50)
            progress.update(task2, advance=50)

            # create this in user-docs path
            temp_path = os.path.join(full_path, f'temp_user_{name}')
            os.mkdir(temp_path)

            progress.update(task2, advance=50)
            for file_name in os.listdir(user_path):
                shutil.move(os.path.join(user_path, file_name), temp_path)

            os.rmdir(user_path)

            progress.update(task3, advance=100)
            console.print(f"User {name} has been deleted. Their data is saved in '{temp_path}'.")


def sort_things(folder_name):
    current_dir = change_directory_to_target("../assets/user-docs", folder_name)

    if 'logs' not in os.listdir(current_dir):
        make_folder('logs')

    if 'mail' not in current_dir:
        make_folder('mail')

    for file in os.listdir(current_dir):
        filename, file_extension = os.path.splitext(file)
        if file_extension == '.log.txt':
            shutil.move(os.path.join(current_dir, file), os.path.join(current_dir, 'logs'))
        if file_extension == '.mail':
            shutil.move(os.path.join(current_dir, file), os.path.join(current_dir, 'mail'))

    console.print(f"{folder_name} sorted.")


def count_things(folder_name, file_type):
    current_dir = change_directory_to_target("../assets/user-docs", {folder_name})

    count = 0

    for file in os.listdir(current_dir):
        filename, file_extension = os.path.splitext(file)
        if file_extension == file_type:
            count += 1

    console.print(f"Folder {folder_name} has {count} items of {file_type}.")


def parse_log(log_file):

    w_pattern = 'WARNING'
    e_pattern = 'ERROR'

    with open(log_file) as log:
        warnings = [line for line in log if re.search(w_pattern, line)]
        errors = [line for line in log if re.search(e_pattern, line)]

    make_folder('extra_logs')

    with open("extra_logs/errors.log.txt", "w+") as new:
        new.writelines(errors)

    with open("extra_logs/warnings.log.txt", "w+") as new:
        new.writelines(warnings)

    console.log(f"Errors and warnings extracted.")







