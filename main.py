import os, random

from character import character

os.chdir(os.path.dirname(os.path.abspath(__file__))) #sets cwd to this directory

#login
def character_create(username):
    global char_name
    char_name = input("\nWelcome to character creation!\n\u001b[4mEnter a name for your character.\u001b[0m\n\n")

    while True:
        char_race = input("\n\u001b[4mPick a race:\u001b[0m\nHuman\nOrc\nTroll\nElf\n\n").lower()
        if char_race in ["human", "orc", "troll", "elf"]:
            with open(f'{username}/{char_name}.wander', 'w') as File:
                #Write starter character data
                File.write( # char_race => maxHP => currentHP => attackDmg
                    f'''
                    {char_race}
                    100
                    100
                    5
                    '''
                    )
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

#initialize player
player = character(char_name)

#load player data
with open(f'{username}/{char_name}.wander', 'r') as f:
    data = f.readlines()

    player.maxhp = int(data[1])
    player.hp = int(data[2])
    player.attackDmg = int(data[3])

#main game loop
while True:
    status = input("\n\u001b[4mWhat do you wish to do?  [W/I/CC]\u001b[0m\nWander\nInventory\nChange Character\n\n").lower()
    if status == "wander" or status == "w":
        chance = random.randint(1,2)

        if chance == 1: # Beast PvE Encounter
            beast = character("Beast", 50, 50, 2)
            print("\nYou stumble upon a wild Beast!")
            while beast.hp > 0:
                action = input("\n\u001b[4mWhat do you wish to do? [A/F]\u001b[0m\nAttack\nFlee\n\n").lower()
                if action == "attack" or action == "a":
                    beast.takeDamage(player.attackDmg)
                    print("\nBeast uses Attack!")
                    player.takeDamage(beast.attackDmg)

                elif action == "flee" or action == "f":
                    chance = random.randint(1,4)
                    if chance <= 3:
                        print("\nFlee failed!")
                    elif chance > 3:
                        print("\nFlee successful.")
                        break

        elif chance == 2: # Tavern Instance Encounter
            tavernkeeper = character("Tavernkeeper")
            tavernkeeper.inventory.append(weapon("Wooden Hammer", "Common", True))
            print("\nBefore you appears a small tavern.\n\n\u001b[4mTavernkeeper's Inventory\u001b[0m\n")
            for i in tavernkeeper.inventory: print(i.name)
            action = input("\n\u001b[4mWhat would you like to do? [L]\u001b[0m\nBuy\nSell\nLeave\n\n")

    elif status == "inventory" or status == "i":
        if len(player.inventory) <= 0: 
            print("This character's inventory is empty, collect items by playing!")
        else:
            for i in player.inventory: print(i.name)

    elif status == "change character" or status == "cc": character_create(username) #Remember to change to character picker

    elif status == "help" or status == "h":
        print(
        '''
        How to exit the game:
            When in the action selection screen type !quit OR !disconnect, this will end the game loop.
        '''
            )

    elif status == "!quit" or status == "!disconnect":

        #save player data
        with open(f'{username}/{char_name}.wander', 'w') as f:
            f.write(f'''
                    
                    {player.maxhp}
                    {player.hp}
                    {player.attackDmg}
                    ''')

        #exit
        print("\nThank you for playing Wander!") 
        break

    else: print("\nInvalid Option!")