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

def account_create():
    username = input("Username: ")
    password = input("Password: ")

    with open('accounts.txt', 'a') as File:
        File.write(username + ',' + password + '\n')

    os.mkdir(username)

    character_create(username)

def character_create(username):
    char_name = input("Welcome to character creation!\nEnter a name for your character.\n")
    char_class = input("Pick a class: Warrior, Hunter\n")

    if char_class in classes:
        os.mkdir(username + "/" + char_name)
    else:
        print("Invalid option!\n")
        character_create(username)

classes = ["Warrior", "Hunter"]

login() #DO NOT REMOVE

weapons = {
    "common_wood_hammer": {'name': "Wood Hammer", 'dmg': 1,},
    "common_copper_sword": {'name': "Copper Sword", 'dmg': random.randint(2,4)},
    "unique_god's-fury": {'name': "God's Fury", 'dmg': 100}
}

usables = {
    "health_potion": {'name': 'Health Potion', 'hp': 10},
}

def waiting():
    status = input("What do you wish to do? Wander, Signout or Change character [W/S/CC]\n")
    if status == "W":
        chance = random.randint(2) #determines event
        if chance == 1:
            print()
        elif chance == 2:
            print()
        waiting()

    elif status == "S":
        print("Signing out..")
        login()

    elif status == "CC":
        character_create() #Remember to change to character picker

    else:
        print("Invalid Option")
        waiting()

waiting()