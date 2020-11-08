from random import choice
from time import sleep, ctime
from colorama import init, Fore, Style
import os

init(autoreset=True)

letters_and_numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUNWXYZ0123456789"


def cls():
    os.system("cls||clear")


counter, basis_for_the_password = 1, ""
saving_passwords = []

print(Style.BRIGHT + "Hello, you have launched the password generator!")
sleep(1)
print(Style.BRIGHT + "\nNow I will ask you a couple of questions about functionality. Answer them and you will get "
                     "your happiness! :)")
sleep(1)


symbols = input(Style.BRIGHT + 'Are you want add to list of letters and numbers addition symbols in type "!", "?", "$" etc. (Y, N): ')
if symbols.upper() == "Y":
    addition = r"!@~`@#№;$%^:&?*|\/<>"
    letters_and_numbers += addition
    print("Done operation!")

while True:
    try:
        how_many_passwords = int(input(Style.BRIGHT + "\nEnter how many passwords I must generate: "))
        how_len_passwords = int(input(Style.BRIGHT + "\nEnter len of the password/s: "))
        break
    except ValueError:
        print(Style.BRIGHT + "Try again write command!")

try:
    while how_many_passwords != 0:
        basis_for_the_password += choice(letters_and_numbers)
        if len(basis_for_the_password) == how_len_passwords:
            print(f"\n{counter}) " + Fore.CYAN + basis_for_the_password)
            counter += 1
            saving_passwords.append(basis_for_the_password)
            basis_for_the_password = ""
            how_many_passwords -= 1
        else:
            continue
except NameError:
    pass

file_write = input(Style.BRIGHT + "Can I write your passwords to .txt file? (Y, N): ")

if file_write.upper().startswith("Y"):
    name_of_file = input(Style.BRIGHT + "Write name of file: ")
    valid_files = ["pdf", "txt", "doc", "docx", "rtf"]
    while True:
        format_of_file = input(Style.BRIGHT + "Write format of file, if you want leave format by standard(.txt) press 'Enter': ")
        if format_of_file == "":
            format_of_file = "txt"

        if not format_of_file.lower() in valid_files:
            print(Style.BRIGHT + "You was write format whose may not suit. Maybe problem to open, reading etc.\n")
            continue_or_again = input(Style.BRIGHT + "Do you want to change your format?(Y, N): ")
            if continue_or_again.upper() == "Y":
                pass
            else:
                break
            sleep(2)
        else:
            break

    print(Style.BRIGHT + "Where are you want to save the file?:\n1) - Save in current directory;\n2) - By writing path for save of file.")
    while True:
        try:
            operation = int(input(Style.BRIGHT + "Write the number: "))
            if operation == 1 or 2:
                break
        except TypeError:
            pass

    if operation == 1:
        pass

    elif operation == 2:
        path = input(Style.BRIGHT + "Write the path by whose I must save your passwords: ")
        if os.path.isdir(path):
            os.chdir(path)

    write_or_append = "w+"

    full_file_name = f"{name_of_file}.{format_of_file}"

    if full_file_name in os.listdir():
        print(Style.BRIGHT + f"File under name {full_file_name} is create in current directory. Select next operation:"
              f"\n1) Delete the existing file and create a new one with different content;"
              f"\n2) Append passwords to the end of an existing file.")
        while True:
            try:
                number = int(input(Style.BRIGHT + "Choose a number: "))
                if number == 1 or 2:
                    break
            except TypeError:
                pass

        if number == 1:
            os.remove(full_file_name)
            print(Style.BRIGHT + "Previous file has been deleted.")
            sleep(1)

        elif number == 2:
            write_or_append = "a+"


    file = open(f"{full_file_name}", f"{write_or_append}")
    file.write(f"\nA file with a password {len(saving_passwords)} of length "
               f"{len (saving_passwords[0])} characters was created after the program generated the passwords."
               f"\nMain repository - https://github.com/Lineroy. Thanks for using program!\n")
    for i in range(1, len(saving_passwords) + 1):
        file.write(f"\n{i}) {saving_passwords[i - 1]}")

    print(Style.BRIGHT + "The password file was created successfully.")
    file.close()
    open_file = input(Style.BRIGHT + "Can I open created file for you?(Y, N): ")
    if open_file.upper() == "Y":
        os.startfile(fr"{os.getcwd()}\{full_file_name}")
    sleep(2)

cls()

print(Fore.YELLOW + """
██╗░░██╗░█████╗░██╗░░░██╗███████╗  ░█████╗░  ░██████╗░░█████╗░░█████╗░██████╗░
██║░░██║██╔══██╗██║░░░██║██╔════╝  ██╔══██╗  ██╔════╝░██╔══██╗██╔══██╗██╔══██╗
███████║███████║╚██╗░██╔╝█████╗░░  ███████║  ██║░░██╗░██║░░██║██║░░██║██║░░██║
██╔══██║██╔══██║░╚████╔╝░██╔══╝░░  ██╔══██║  ██║░░╚██╗██║░░██║██║░░██║██║░░██║
██║░░██║██║░░██║░░╚██╔╝░░███████╗  ██║░░██║  ╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝░░╚═╝  ░╚═════╝░░╚════╝░░╚════╝░╚═════╝░

                    ████████╗██╗███╗░░░███╗███████╗██╗
                    ╚══██╔══╝██║████╗░████║██╔════╝██║
                    ░░░██║░░░██║██╔████╔██║█████╗░░██║
                    ░░░██║░░░██║██║╚██╔╝██║██╔══╝░░╚═╝
                    ░░░██║░░░██║██║░╚═╝░██║███████╗██╗
                    ░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝""")

sleep(2)
