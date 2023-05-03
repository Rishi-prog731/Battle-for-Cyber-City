from cyber_city.game import Role, Ability, GameDistrict
from cyber_city.api import Power, ModbusSystem

HACK = Role("Hacker", 5000)
DEF = Role("Defender", 5000)

ENC = Ability("Data Encryption", 300, 10)
AMAL = Ability("Anti-Malware", 600, 30)
FWAL = Ability("Firewall", 600, 30)
TRU = Ability("Trust Zones", 400, 15)
HON = Ability("Honey Pot", 500, 20)
MUlAUTH = Ability("Multifactor Authentication", 300, 10)
AUDIT = Ability("Audit Devices & Assets", 500, 20)

MITM = Ability("Man in the Middle (Steal Data)", 300, 20, ENC)
MAL = Ability("Malware (Steal Data)", 600, 60, AMAL)
DDOS = Ability("DDoS (Control)", 600, 60, FWAL)
PHI = Ability("Phishing (Steal Data)", 400, 30, TRU)
TRO = Ability("Trojan (Control)", 500, 40, HON)
PSWD = Ability("Password Attack (Steal Data)", 300, 20, MUlAUTH)
RAN = Ability("Ransomware (Control)", 500, 40, AUDIT)

DEF.abilities = [
    ENC, AMAL, FWAL, TRU, HON, MUlAUTH, AUDIT
]

HACK.abilities = [
    MITM, MAL, DDOS, PHI, TRO, PSWD, RAN
]

print(HACK)
print()
print(DEF)

for ability in HACK.abilities:
    print(ability)
    print()

for ability in DEF.abilities:
    print(ability)
    print()

POWERGRID = [ ModbusSystem(1) ]
POWER = Power(1, POWERGRID)
DIS = GameDistrict("District 1", POWER)