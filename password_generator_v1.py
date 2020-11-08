from random import choice
from time import sleep
from colorama import init, Fore, Style
from os import system

init(autoreset=True)

letters_and_numbers = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUNWXYZ0123456789"


def cls():
    system("cls||clear")


counter, basis_for_the_password = 1, ""

print(Style.BRIGHT + "Hello, you have launched the password generator!")
sleep(1)
print(Style.BRIGHT + "\nNow I will ask you a couple of questions about functionality. Answer them and you will get "
                     "your happiness! :)")
sleep(1)

try:
    how_many_passwords = int(input("\nEnter how many passwords I must generate: "))
    how_len_passwords = int(input("\nEnter len of the password/s: "))
except ValueError:
    print("Try again write command!")

try:
    while how_many_passwords != 0:
        basis_for_the_password += choice(letters_and_numbers)
        if len(basis_for_the_password) == how_len_passwords:
            print("\n" + str(counter) + ") " + Fore.CYAN + basis_for_the_password)
            counter += 1
            basis_for_the_password = ""
            how_many_passwords -= 1
        else:
            continue
except NameError:
    pass

None_command = input("\n")

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
