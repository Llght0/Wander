import random

from src.core import style

def pve(player, npc):
    style.typewriter(f"\nYou've stumbled upon a {npc.name}!")
    while npc.hp > 0:
        action = input("\n\u001b[4mWhat do you wish to do? [A/F]\u001b[0m\nAttack\nFlee\n\n").lower()
        if action == "attack" or action == "a":
            npc.takeDamage(player.attackDmg)
            print(f"\n{npc.name} uses Attack!")
            player.takeDamage(npc.attackDmg)

        elif action == "flee" or action == "f":
            chance = random.randint(1,4)
            if chance <= 3:
                print("\nFlee failed!")
            elif chance > 3:
                print("\nFlee successful.")
                break
