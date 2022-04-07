from src.arena import client, host

#from core import character

#player = character.new()

def play():
    while True:
        action = input("Join or Create an arena match. [J/C]\n").lower()
        if action == "create" or action == "c":
            host.initiate()
        elif action == "join" or action == "j":
            client.initiate()
            break
        elif action == "cancel":
            print("Returning to menu...")
            break
        else:
            print("Invalid Option!")

if __name__ == "__main__":
    play()
