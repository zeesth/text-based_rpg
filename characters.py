from random import randint
from time import sleep
from utils import roll, typing, wait_dot

class Creature:
    def __init__(self, level=1, dmg_dice=[1,1], armor_base=10, strength=0, dexterity=0, constitution=0, name="undefined" , player=False):
        self.armor = armor_base + dexterity
        self.damage = dmg_dice
        self.inventory = []
        self.is_player = player
        self.hit = level + strength
        self.hit_points = level * (constitution + 8)
        self.name = name
    
    def show_inv(self):
        for item in self.inventory:
            print("Your inventory has: " + (', '.join(item)) + ".")
    
    def addto_inv(item):
        self.inventory.append(item)

    def attack(target):
        hit_roll = roll(1, 20) + self.hit
        dmg_roll = 0
        if hit_roll >= target.armor:
            for dice in range(self.damage[0]):
                dmg_roll += roll(1, self.damage[1])
            
            target.hit_points -= dmg_roll

            if target.hit_points <= 0:
                target.death()

            else:
                pass

        else:
            pass
    
    def death(self):
        if self.is_player:
            self.game_over()
        else:
            self.loot()
    
    def loot(self):
        print("You can then loot: " + (', '.join(self.inventory)))

    def game_over(self):
        run = 0

    def start(self):
        print("""
ooooo       .o8            oooo                 o8o                   ooooooooo.                o8o                       
`888'      "888            `888                 `"'                   `888   `Y88.              `"'                       
 888   .oooo888   .ooooo.   888   .oooo.o      oooo  ooo. .oo.         888   .d88' oooo  oooo  oooo  ooo. .oo.    .oooo.o 
 888  d88' `888  d88' `88b  888  d88(  "8      `888  `888P"Y88b        888ooo88P'  `888  `888  `888  `888P"Y88b  d88(  "8 
 888  888   888  888   888  888  `"Y88b.        888   888   888        888`88b.     888   888   888   888   888  `"Y88b.  
 888  888   888  888   888  888  o.  )88b       888   888   888        888  `88b.   888   888   888   888   888  o.  )88b 
o888o `Y8bod88P" `Y8bod8P' o888o 8""888P'      o888o o888o o888o      o888o  o888o  `V88V"V8P' o888o o888o o888o 8""888P' 
""")
        wait_dot(cycle=5)
        typing("    You are in the outskirts of a place whose name you've long forgotten. ")
        self.name = input(typing("What is your name?\n"))
        sleep(1)
        background = input(typing("""What do you remember doing before?\n
        1. 'I remember tending to a farm.'\n
        2. 'I remember the streets and the cold of the winter.'\n
        3. 'I don't remember anything.'"""))
        while True:
            if background > 0 and background < 4:
                try:
                    int(background)
                    break
                except ValueError:
                    background = input(typing("Please type only the number corresponding to your choice: "))
            else:
                background = input(typing("Input a number from 1 to 3: "))
        


        