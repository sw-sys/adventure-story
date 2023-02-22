import random

# user introduction to adventure
print(
  "You stumbled on a market stall while on an exotic trip. The vendor says to you..."
)


# store user character details
class is_person:

  def __init__(self, name, age):
    self.name = name
    self.age = age


# store weapon details
class get_weapon:

  def __init__(self, wtype, weaponSize):
    self.wtype = wtype
    self.weapsonSize = wsize


# store details of monster
class get_monster:

  def __init__(self, monster, monsterSize):
    self.monster = monster
    self.monsterSize = monsterSize


#data to put in to classes

# generate a location
randLocation = ["field", "dungeon", "cave"]
location = (random.choice(randLocation))

# generate weapon size
weaponSize = ["tiny", "small", "large", "giant"]
wsize = (random.choice(weaponSize))

#generate monster size
monsterSize = ["tiny", "small", "large", "giant"]
msize = (random.choice(monsterSize))

# story dialogue

name = input("Hello my friend. What is your name?")

print(f"It's great to meet you", name,", what a name.")

weapon = input(
  "Well this area is great for adventures. Which kind of fine weapon would you like to purchase today?"
)

monster = input(
  "What kind of monster do you hope to find out in these wildernesses?")

#end of user interaction
print("Good luck, I wish you success in all your endeavors...")

# user's adventure story
print("Later that day...Time to go on an adventure!")

print(f"{name} took a {wsize} {weapon} to a {location} and destroyed the {msize} {monster}.")