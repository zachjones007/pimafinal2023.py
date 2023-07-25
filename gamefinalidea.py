import random

class Character:
    def __init__(self, name, health, attack_power, mana, bagspace=0, item_mapping=None):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.mana = mana 
        self.inventory = []
        self.bagspace = bagspace
        
        if item_mapping:
            self.item_mapping = item_mapping
        else:
            self.item_mapping = {
                1: {"name": 'HP potion lv1', "type": "item"},
                2: {"name": 'Mana potion lv1', "type": "item"},
                3: {"name": '10 gold coins', "type": "item"},
                4: {"name": 'HP potion lv2', "type": "item"},
                5: {"name": 'Mana potion lv2', "type": "item"},
                6: {"name": '20 gold coins', "type": "item"},
                7: {"name": 'Magic beans', "type": "item"}
            }

    def statsup(self, proc):
        self.attack_power += 1
        if self.attack_power >= 20 or proc == 1:
            self.mana += 1
            self.health += 2
            print(f'You have {self.mana} mana, {self.attack_power} attack power, and {self.health} HP.')

    def attack(self, target):
        target.health -= self.attack_power
        target.mana += 1
        print(f"{self.name} attacks {target.name}. {target.name} now has {target.health} health and {target.mana} mana.")

    def heal(self, proc):
        if self.health == 50:
            print('You are already at full health!')
            if proc == 1: 
                self.health -= 4
                print('You took unnecessary risks and got hit!')
        elif self.mana >= 5:
            self.health += 10
            self.mana -= 5
            print(f"{self.name} healed and now has {self.health} health and {self.mana} mana.")
        else:
            print('Not enough mana to heal.')

    def Bag(self):
        if self.bagspace >= 7:
            print('Your bag is full!')
            return

        item_number = random.randint(1, 7)
        item_name = self.item_mapping[item_number]["name"]
        self.inventory.append(item_name)
        self.bagspace += 1
        print(f"You found {item_name} and added it to your bag!")

    def separate_elements(self):
        items = []
        enemies = []

        for item in self.item_mapping.values():
            if item["type"] == "item":
                items.append(item["name"])
            elif item["type"] == "enemy":
                enemies.append(item["name"])

        return items, enemies

player = Character("Player", 50, 5, 0)
enemy = Character("Enemy", 300, 7, 0)

while player.health > 0 and enemy.health > 0:
    action = input("Do you want to attack, buff, heal or check bag? ").lower()

    if action == 'attack':
        player.attack(enemy)
        if enemy.health > 0:
            enemy.attack(player)

    elif action == 'heal':
        proc = random.randint(1, 2)
        player.heal(proc)

    elif action == 'buff':
        proc = random.randint(1, 3) 
        player.statsup(proc)
        print('Extra stats')

    elif action == 'check bag':
        player.Bag()

    else:
        print("You decided not to do anything.")

if player.health <= 0:
    print("You have been defeated!")
else:
    print("You defeated the enemy!")
