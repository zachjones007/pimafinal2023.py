import random

class Character:
    def __init__(self, name, health, attack_power, mana):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.mana = mana 

    def statsup(self, target, proc):
        target.attack_power += 1
        if target.attack_power >= 20 or proc == 1:
            target.mana += 1
            target.health += 2

    def attack(self, target):
        target.health -= self.attack_power
        target.mana += 1
        print(f"{self.name} attacks {target.name}. {target.name} now has {target.health} health and now has {target.mana} mana")

    def heal(self, target):
        if target.mana >= 2:
            target.mana -= 2
            target.health += self.attack_power / 4
            if target.health >= 50:
                return
            print(f"{self.name} heals. {target.name} now has {target.health} health and {target.mana} mana left.")
        else:
            print('Not enough mana to heal')

player = Character("Player", 50, 5, 0)
enemy = Character("Enemy", 300, 7, 0)

while player.health > 0 and enemy.health > 0:
    action = input("Do you want to attack, buff or heal? ").lower()

    if action == 'attack':
        player.attack(enemy)
        if enemy.health > 0:
            enemy.attack(player)

    elif action == 'heal':
        if player.health == 50:
            print('You are already at full health!')
        else:
            player.heal(player)

    elif action == 'buff':
        proc = random.randint(1, 3) 
        player.statsup(player, proc)
        print('Extra stats')
        if proc == 1:
            print("bonus stats")

    else:
        print("You decided not to attack.")

if player.health <= 0:
    print("You have been defeated!")
else:
    print("You defeated the enemy!")
