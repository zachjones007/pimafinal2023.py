#i think i need a class for enemy 
import random 
class Character:
    def __init__(self,enemy_attackpower,enemy_health, name, health, attack_power, mana, bagspace=0, item_mapping=None,cash = 0,enemy_moves_mapping=None,wins=0):
        self.name = name
        self.enemy_buffs = []  
        self.health = health
        self.attack_power = attack_power
        self.mana = mana 
        self.inventory = []
        self.bagspace = bagspace
        self.cash = cash
        self.enemy_moves_mapping=enemy_moves_mapping
        self.wins=wins
        self.enemy_health=enemy_health
        self.enemy_attackpower = enemy_attackpower
        if item_mapping:
            self.item_mapping = item_mapping
        else:
            self.item_mapping = {
                1: {"name": '10 gold coin', "type": "item"},
                2: {"name": '20 gold coins', "type": "item"},
                3: {"name": '30 gold coins', "type": "item"},
                4: {"name": '40 gold coins', "type": "item"},
                5: {"name": '50 gold coins', "type": "item"},
                6: {"name": '60 gold coins', "type": "item"},
                7: {"name": '70 gold coins', "type": "item"},
                8: {"name": '80 gold coins', "type": "item"},
                9: {"name": '90 gold coins', "type": "item"},
                10: {"name": '100 gold coins', "type": "item"},
                11: {"name": 'Magic beans', "type": "enemy"}
                    }

        if enemy_moves_mapping:
            self.enemy_moves_mapping = enemy_moves_mapping
        else:
            self.enemy_moves_mapping = {
                1: {"buff": '+1 damage ', "type": "item"},
                2: {"buff": '+2 damage', "type": "item"},
                3: {"buff": '+3 damage', "type": "item"},
                4: {"buff": '+40 hp', "type": "item"},
                5: {"buff": '+50 hp', "type": "item"},
                6: {"buff": '+60 hp', "type": "item"},
                7: {"buff": '+7 healing per turn', "type": "item"},
                8: {"buff": '+8 healing per turn', "type": "item"},
                9: {"buff": '+ 9 healing per turn', "type": "item"},
                10: {"buff": '- 80 hp ', "type": "item"},
                11: {"buff": '- 4 damage', "type": "enemy"}
                    }
    def evil_buffer(self, wins):
        for _ in range(wins):
            buff_number = random.randint(1, 11)
            buff_name = self.enemy_moves_mapping[buff_number]["buff"]
            self.enemy_buffs.append(buff_name)

            if buff_number in [4, 5, 6]:
                self.enemy_health += buff_number * 10
            elif buff_number == 10:
                self.enemy_health -= 80

            if buff_number <= 3:
                self.enemy_attackpower += buff_number
        return self.enemy_buffs

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
        if self.bagspace >= 10:
            print('Your bag is full!')
            return

        item_number = random.randint(1, 11)

        item_name = self.item_mapping[item_number]["name"]
        self.inventory.append(item_name)
        if item_number == 11:
            self.bagspace += 1
        cashamount = (item_number*10)
        if item_number <= 10:
            self.cash += cashamount
        print(f"You found {item_name} and added it to your bag!")
        itemstore = input('would you like to enter the shop?').lower()
        if any(letter in itemstore for letter in ["y", "e", "s"]):
            whichitem = int(input('would you like: hp potions(1), mana potions(2) or the magic beans(3)'))
            
            if whichitem == 1 and self.cash >= 35:
                self.health += 10
                self.cash -= 35
                print(f"Thanks for buying the hp potion. You now have {self.health} health and {self.cash} cash.")
            
            elif whichitem == 2 and self.cash >= 25:
                self.mana += 10
                self.cash -= 25
                print(f"Thanks for buying the mana potion. You now have {self.mana} mana and {self.cash} cash.")
            
            elif whichitem == 3 and self.cash >= 50:
                self.inventory.append('Magic beans')
                self.cash -= 50
                print(f" magic beans coming right up. they are now your inventory! cash: {self.cash}")
            
            else:
                print("You don't have enough cash for this item.")


    def separate_elements(self):
        items = []
        enemies = []
        potion = []

        for item in self.item_mapping.values():
            if item["type"] == "item":
                items.append(item["name"])
            elif item["type"] == "enemy":
                enemies.append(item["name"])
            elif item["type"] == "potion":
                potion.append(item["name"])

        print(items,enemies,potion)

wins = 0
lives = 1
player = Character(3, 50, "Player", 50, 5, 0) 
enemy = Character(7, 300, "Enemy", 300, 7, 0) 

while lives == 1 and player.health > 0:
    enemy_buffs = enemy.evil_buffer(wins)

    action = input("Do you want to attack, buff, heal, or check bag? ").lower()

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

    if enemy.health <= 0:
        print("You defeated the enemy")
        wins += 1
        enemy = Character(7, 300, "Enemy", 300, 7, 0)  # Create a new enemy for the next round

        print(f"you go deeper... you are on level {wins}")

    elif player.health <= 0:
        print("You have been defeated!")
        lives -= 1
        quit()nemy")
