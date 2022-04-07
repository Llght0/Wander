class new:
    def __init__(self, name, attackDmg=1, maxhp=100, hp="maxhp"):
        #stats
        self.name = name
        self.attackDmg = attackDmg
        self.maxhp = maxhp
        if hp == "maxhp":
            self.hp = self.maxhp
        else:
             self.hp = hp
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
