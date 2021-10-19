import os
import random

def login(): #initial login sequence
    with open('accounts.txt', 'w+') as File:
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

def account_login(): #login IF they have an account
    username = input("Username: ")
    password = input("Password: ")

    with open('accounts.txt', 'w+') as File:
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

def charcter_picker():
    character_create()
    #Add stuff <---------------------------------------------------------

def character_create(username):
    char_name = input("Welcome to character creation!\nEnter a name for your character.\n")
    char_class = input("Pick a class: Warrior, Hunter\n")

    if char_class != "Warrior" or "Hunter":
        print("Invalid option!\n")
        character_create()

    os.mkdir(username + "/" + char_name)

def waiting():
    status = input("What do you wish to do? Wander, Signout or Change character [W/S/CC]\n")
    if status == "W":
        chance = random.randrange(1, 3) #determines event
        if chance == 1:
            print("*A wizard approaches* hello" + char_name)
        elif chance == 2:
            print("A wild coyote appears in front of you!")
        waiting()

    elif status == "S":
        print("Signing out..")
        login()

    elif status == "CC":
        print(char_name + " lays down and falls asleep.")
        character_create() #Remember to change to character picker

    else:
        print("Invalid Option")
        waiting()

weapons = {
    "common_wood_hammer": {'name': 'Wood Hammer', 'dmg': 1,},
    "common_copper_sword": {'name': 'Copper Sword', 'dmg': random.randrange(2,4)},
}

usables = {
    "health_potion": {'name': 'Health Potion', 'hp': 10},
}

inventory = {}

char_name = ""
char_class = ""
char_hp = 100
char_speed = 1
char_weapon = "common_wood_hammer"
char_dmg = weapons[char_weapon]['dmg']

login()
waiting()