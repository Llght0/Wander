class character:
    def __init__(self, name, maxhp=100, hp=100, attackDmg=1):
        #stats
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.attackDmg = attackDmg
        #gear/items
        self.inventory = []
        self.weapon = None
    def takeDamage(self, dmg):
        old_hp = self.hp
        self.hp -= dmg
        print(f"{self.name} HP: {old_hp} => {self.hp}")
    def equipItem(self, item):
        old_atk = self.attackDmg
        self.weapon = self.inventory[self.inventory.index(item)]
        self.inventory.remove(item)
        print(f"\nSuccessfully equipped: {item}\nAttack: {old_atk} => {self.attackDmg}")
