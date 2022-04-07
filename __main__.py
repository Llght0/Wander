import os, random

from src.arena import arena
from src.core import character, combat, style

os.chdir(os.path.dirname(os.path.abspath(__file__))) #sets cwd to this directory

#character picker
def character_pick(username):
    for i in os.listdir(username):
        print(i.split('.')[0])

#login
def character_create(username):
    global char_name
    char_name = input("\nWelcome to character creation!\n\u001b[4mEnter a name for your character.\u001b[0m\n\n")

    while True:
        char_race = input("\n\u001b[4mPick a race:\u001b[0m\nHuman\nOrc\nTroll\nElf\n\n").lower()
        if char_race in ["human", "orc", "troll", "elf"]:
            with open(f'{username}/{char_name}.wander', 'w') as f:
                #Write starter character data
                f.write((
                    f'{char_race} \n'
                    '100          \n'
                    '100          \n'
                    '5            \n'
                ))
            character_pick(username)
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

#starting sequence
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

#classes
class item:
    def __init__(self, name, rarity="Unique", isUsable=False, useReply="Item used."):
        self.name = name
        self.rarity = rarity
        self.isUsable = isUsable
        self.useReply = useReply
    def use(self):
        print(self.useReply)

class weapon(item):
    def __init__(self, name, rarity="Common", isUsable=True, useReply="Weapon Equipped."):
        super().__init__(name, rarity=rarity, isUsable=isUsable, useReply=useReply)

#initialize loot items
weapons = {
    1: weapon(""),
    2: weapon(""),
    3: weapon(""),
}

#load data & initialize player
with open(f'{username}/{char_name}.wander', 'r') as f:
    data = f.readlines()
    player = character.new(char_name, int(data[1]), int(data[2]), int(data[3]))

#main game loop
while True:
    status = input("\n\u001b[4mChoose an option. [S/A]\u001b[0m\nSolo\nArena\n\n").lower()
    if status == "solo" or status == "s":
        status = input("\n\u001b[4mWhat do you wish to do?  [W/I/CC]\u001b[0m\nWander\nInventory\nChange Character\n\n").lower()
        if status == "wander" or status == "w":
            chance = random.randint(1,2)

            if chance == 1:
                combat.pve(player, character.new("Wild Beast", 1, 50))

            elif chance == 2: # Tavern Instance Encounter
                tavernkeeper = character.new("Tavernkeeper")
                tavernkeeper.inventory.append(weapon("Wooden Hammer", "Common", True))
                style.typewriter("\nBefore you appears a small tavern.")
                print("\n\n\u001b[4mTavernkeeper's Inventory\u001b[0m\n")
                for i in tavernkeeper.inventory: 
                    print(i.name)
                while True:
                    action = input("\n\u001b[4mWhat would you like to do? [B/S/L]\u001b[0m\nBuy\nSell\nLeave\n\n").lower()
                    if action == "buy" or action == "b":
                        action = input("\nWhat do you wish to buy?\n\n")
                        if action in tavernkeeper.inventory:
                            player.inventory.append(tavernkeeper.inventory[action])
                        else:
                            print("\nInvalid Option!")
                    elif action == "sell" or action == "s":
                        pass
                    elif action == "leave" or action == "l":
                        break
                    else:
                        print("\nInvalid Option!")

        elif status == "inventory" or status == "i":
            if len(player.inventory) == 0: 
                print("This character's inventory is empty, collect items by playing!")
            else:
                for i in player.inventory: print(i.name)

        elif status == "change character" or status == "cc": 
            character_pick(username)

        elif status == "help" or status == "h":
            print((
            'How to exit the game:                                                                         \n'
            '   When in the action selection screen type !quit OR !disconnect, this will end the game loop.\n'
            ''
            ))

        elif status == "!quit" or status == "!disconnect":

            #save player data
            with open(f'{username}/{char_name}.wander', 'w') as f:
                f.write((
                    '             \n'
                    '5            \n'
                    '100          \n'
                    '100          \n'
                ))

            #exit
            print("\nThank you for playing Wander!") 
            break

        else: print("\nInvalid Option!")
    elif status == "arena" or status == "a":
        arena.play()
