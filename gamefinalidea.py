import random
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name}. {target.name} now has {target.health} health.")

    def heal(self,target):
        target.health += self.attack_power/4
        print(f"{self.name} attacks {target.name}. {target.name} now has {target.health} health.")
        if target.health >= 50:
            return

player = Character("Player", 50, 5)
enemy = Character("Enemy", 30, 7)

while player.health > 0 and enemy.health > 0:
    action = input("Do you want to attack (yes/no) or heal? ").lower()

    if action in ('yes','attack'):
        player.attack(enemy)
        if enemy.health > 0:
            enemy.attack(player)

    elif action == 'heal':
   
        if player.health == 50:
            print('full hp')
        else:
            player.heal(player)
            print('player healed')

    else:
        print("You decided not to attack.")
    

if player.health <= 0:
    print("You have been defeated!")
else:
    print("You defeated the enemy!")
