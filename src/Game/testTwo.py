from flask import Flask, render_template, request
import random

app = Flask(__name__)

settings = [
'compromisedLevel=0',
'attackerDamage=10',
'defenderDefense=5',
'defenderBudget=1000',
'toolCost=200',
'locations="sectorOne","sectorTwo","sectorThree"',
]
settings = dict(line.strip().split("=") for line in settings)

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

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    global compromisedLevel, attackerPoints, defenderPoints, defenderBudget, defendedLocations
    
    # Get input from form
    locationToDefend = request.form.get("locationToDefend")
    locationToHack = request.form.get("locationToHack")
    
    # Defender's turn
    if locationToDefend:
        if locationToDefend not in locations:
            return "Invalid location.", 400
        defenderBudget -= toolCost
        defendedLocations.append(locationToDefend)
        toggleLights(locationToDefend, "on")
    
    # Attacker's turn
    if locationToHack:
        if locationToHack not in locations:
            return "Invalid location.", 400
        hackSuccess = random.choice([True, False])
        if hackSuccess:
            if locationToHack in defendedLocations:
                damage = max(0, attackerDamage - defenderDefense)
            else:
                damage = attackerDamage
            compromisedLevel += 10
            attackerPoints += 10
            message = "Hack successful!"
        else:
            defenderPoints += 10
            message = "Hack failed."
        toggleLights(locationToHack, "off")
    
    response = {
        "compromisedLevel": compromisedLevel,
        "attackerPoints": attackerPoints,
        "defenderPoints": defenderPoints,
        "defenderBudget": defenderBudget,
        "message": message if message else ""
    }
    return response

if __name__ == "__main__":
    app.run()