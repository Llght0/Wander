import os
import random

def login(): #initial login sequence
    with open('accounts.txt', 'r') as File:
        find_account = File.read().find(',')

    if find_account == -1:
        print("Welcome to the simulation... create an account to begin.")
        account_create()
    else:
        action = input("Log in Or Sign up.. [L/S] \n")
        if action == "L":
            account_login()
        elif action == "S":
            account_create()
        else:
            print("Invalid Option \n")
            login()

def account_login(file = 'accounts.txt'): #login IF they have an account
    username = input("Username: ")
    password = input("Password: ")

    with open(file, 'r') as File:
        find_account = File.read().find(username + ',' + password + '\n')

    if find_account != -1:
        print("Welcome back, " + username)
    else:
        print("Invalid User \n")
        login()
    return username

def account_create():
    username = input("Username: ")
    password = input("Password: ")

    with open('accounts.txt', 'a') as File:
        File.write(username + ',' + password + '\n')

    os.mkdir(username)

    character_create(username)

def character_create(username):
    char_name = input("Welcome to character creation! \nEnter a name for your character. \n")

    with open(username + '/characters.txt', 'a') as File:
        File.write(char_name + '\n')

def waiting():
    status = input("What do you wish to do? Wander, Quest or PVP \n")
    if status == "Wander":
        chance = random.randrange(1, 3) #determines event
        if chance == 1:
            print("*A wizard approaches* hello" + char_name)
        elif chance == 2:
            print("A wild coyote appears in front of you!")
        waiting()

    elif status == "Quest":
        print("No available quests")
        waiting()

    elif status == "PVP":
        print("Coming soon")
        waiting()

    else:
        print("Invalid Option \n")
        waiting()

weapons = {
    "common_wood_hammer": {'name': 'Wood Hammer', 'dmg': '1',},
    "common_copper_sword": {},
}

char_name = ""
char_class = ""
char_health = 0
char_speed = 0
char_weapon = "common_wood_hammer"
char_dmg = weapons[char_weapon]['dmg']

login()
waiting()