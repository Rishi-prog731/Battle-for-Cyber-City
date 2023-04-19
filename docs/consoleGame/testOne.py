import random

with open("settings.txt") as f:
    settings = dict(line.strip().split("=") for line in f)

compromisedLevel = 0
attackerDamage = int(settings["attackerDamage"])
defenderDefense = int(settings["defenderDefense"])

def toggleLights(location, sector):
    pass

attackerPoints = 0
defenderPoints = 0
defenderBudget = int(settings["defenderBudget"])
toolCost = int(settings["toolCost"])
locations = settings["locations"].split(",")
defendedLocations = []

for roundNum in range(1, 11):
    print("Round", roundNum)

    print("Defender's turn")
    print("Current budget:", defenderBudget)
    locationToDefend = input("Enter location to defend: ")
    if locationToDefend not in locations:
        print("Invalid location.")
        continue
    defenderBudget -= toolCost
    defendedLocations.append(locationToDefend)
    toggleLights(locationToDefend, "on")

    # Attacker tries to hack a location
    print("Attacker's turn")
    locationToHack = input("Enter location to hack: ")
    if locationToHack not in locations:
        print("Invalid location.")
        continue
    hackSuccess = random.choice([True, False])
    if hackSuccess:
        if locationToHack in defendedLocations:
            damage = max(0, attackerDamage - defenderDefense)
        else:
            damage = attackerDamage
        compromisedLevel += 10
        print("Hack successful!")
        attackerPoints += 10
    else:
        print("Hack failed.")
        defenderPoints += 10

    toggleLights(locationToHack, "off")
    print("Compromised level:", compromisedLevel)
    print("Attacker points:", attackerPoints)
    print("Defender points:", defenderPoints)
    print("------------------")

# Display final points
print("Final points:")
print("Attacker:", attackerPoints)
print("Defender:", defenderPoints)
