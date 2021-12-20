import os, random

os.chdir(os.path.dirname(os.path.abspath(__file__))) #sets cwd to this directory

#login
def character_create(username):
    global char_name
    char_name = input("\nWelcome to character creation!\n\u001b[4mEnter a name for your character.\u001b[0m\n")

    while True:
        char_race = input("\n\u001b[4mPick a race:\u001b[0m\nHuman\nOrc\nTroll\nElf\n\n").lower()
        if char_race in ["human", "orc", "troll", "elf"]:
            with open(f'{username}/{char_name}.wander', 'w') as f:
                f.write("100\n100\n5")
            break
        else:
            print("Invalid option!\n")

def account_create():
    global username
    username = input("Username: ")
    password = input("Password: ")

    with open('accounts.txt', 'a') as File: File.write(f'{username},{password}\n')

    os.mkdir(username)

    character_create(username)

if os.path.exists('accounts.txt') == 0 or os.stat('accounts.txt').st_size == 0:
    print("\n\u001b[4mWelcome to Wander... create an account to begin.\u001b[0m")
    account_create()
else:
    action = input("\n\u001b[4mLog in or Sign up? [L/S]\u001b[0m\n").lower()

    if action == "log in" or action == "l":
        username = input("\nEnter your username and password.\nUsername: ")
        password = input("Password: ")

        with open('accounts.txt', 'r+') as File: find_account = File.read().find(username + ',' + password + '\n')

        if find_account != -1: print("Welcome back, " + username)
        else: print("Invalid User\n")

    elif action == "sign up" or action == "s": account_create()

    else: print("Invalid Option\n")

#character picker
#for i in os.listdir(username):
#    print(i.split('.')[0])

#classes
weapons = {
    1: {'name': "Wood Hammer", 'dmg': 1, 'rarity': "common"},
    2: {'name': "Copper Sword", 'dmg': random.randint(2,4), 'rarity': "common"},
    3: {'name': "God's Fury", 'dmg': 100, 'rarity': "unique"},
}

class character:
    def __init__(self, name, maxhp=100, hp=100, attack=1):
        #stats
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.attack = attack
        #gear/items
        self.inventory = []
        self.weapon = None
    def takeDamage(self, dmg):
        old_hp = self.hp
        self.hp -= dmg
        print(f"{self.name} HP: {old_hp} => {self.hp}")
    def equipItem(self, item):
        old_atk = self.attack
        self.weapon = self.inventory[self.inventory.index(item)]
        self.inventory.remove(item)
        print(f"\nSuccessfully equipped: {item}\nAttack: {old_atk} => {self.attack}")

player = character(char_name)

#load player data
with open(f'{username}/{char_name}.wander', 'r') as f:
    data = f.readlines()

    player.maxhp = int(data[0])
    player.hp = int(data[1])
    player.attack = int(data[2])

#main game loop
while True:
    status = input("\n\u001b[4mWhat do you wish to do?  [W/I/CC]\u001b[0m\nWander\nInventory\nChange Character\n\n").lower()
    if status == "wander" or status == "w":
        chance = random.randint(1,2)

        if chance == 1: # Beast PvE Encounter
            beast = character("Beast", 50, 50, 2)
            print("\nYou stumble upon a wild Beast!")
            while beast.hp > 0:
                action = input("\n\u001b[4mWhat do you wish to do? [A/F]\u001b[0m\nAttack\nFlea\n\n").lower()
                if action == "attack" or action == "a":
                    beast.takeDamage(player.attack)
                    print("\nBeast uses Attack!")
                    player.takeDamage(beast.attack)

                elif action == "flea" or action == "f":
                    chance = random.randint(1,4)
                    if chance <= 3:
                        print("\nFlea failed!")
                    elif chance > 3:
                        print("\nFlea successfull.")
                        break

        elif chance == 2: # Tavern Instance Encounter
            Tavernkeeper = character("Tavernkeeper")
            print("\nBefore you appears a small tavern")
            print("\n\n\u001b[4mTavernkeeper's Inventory\u001b[0m\n")

    elif status == "inventory" or status == "i":
        if len(player.inventory) <= 0: print("This character's inventory is empty, collect items by playing!")
        else:
            for i in player.inventory: print(i)

    elif status == "change character" or status == "cc": character_create(username) #Remember to change to character picker

    elif status == "!quit" or status == "!disconnect":

        #save player data
        with open(f'{username}/{char_name}.wander', 'w') as f:
            f.write(f"{player.maxhp}\n{player.hp}\n{player.attack}")

        #exit
        print("\nThank you for playing Wander!") 
        break

    else: print("\nInvalid Option!")