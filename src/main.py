from cyber_city.game import Role, Ability, GameDistrict
from cyber_city.api import System, ModbusSystem, Power, TrafficLight

# Lights
G_NS = ModbusSystem(0)
Y_NS = ModbusSystem(1)
R_NS = ModbusSystem(2)
G_EW = ModbusSystem(3)
Y_EW = ModbusSystem(4)
R_EW = ModbusSystem(5)

LIGHTS = [G_NS, Y_NS, R_NS, G_EW, Y_EW, R_EW]

# Special District Components
H_P = ModbusSystem(6)
H_G = ModbusSystem(7)
P_P = ModbusSystem(8)
P_G = ModbusSystem(9)
# Power Grid
POWER_GRID = System()
# Power Systems
BD = Power(10, POWER_GRID)
HP = Power(11, POWER_GRID)
PF = Power(12, POWER_GRID)
IN = Power(13, POWER_GRID)
UN = Power(14, POWER_GRID)
RE = Power(15, POWER_GRID)

GRID = [BD, HP, PF, IN, UN, RE]

# Traffic Lights
NS = TrafficLight(R_NS, Y_NS, G_NS)
EW = TrafficLight(R_EW, Y_EW, G_EW)

TRAFFICLIGHTS = [NS, EW]

# Defining the Roles
HACKER = Role("Hacker", 5000)
DEFENDER = Role("Defender", 5000)

# Defining the Defenders Abilities
ENC = Ability("Data Encryption", 300, 10)
AMAL = Ability("Anti-Malware", 600, 30)
FWAL = Ability("Firewall", 600, 30)
TRU = Ability("Trust Zones", 400, 15)
HON = Ability("Honey Pot", 500, 20)
MULAUTH = Ability("Multifactor Authentication", 300, 10)
AUDIT = Ability("Audit Devices & Assets", 500, 20)

# Defining the Attackers Abilities
MITM = Ability("Man in the Middle (Steal Data)", 300, 20)
MAL = Ability("Malware (Steal Data)", 600, 60)
DDOS = Ability("DDoS (Control)", 600, 60)
PHI = Ability("Phishing (Steal Data)", 400, 30)
TRO = Ability("Trojan (Control)", 500, 40)
PSWD = Ability("Password Attack (Steal Data)", 300, 20)
RAN = Ability("Ransomware (Control)", 500, 40)

# Pairing the matchups `defense for attacker`
MITM.matchup = ENC
MAL.matchup = AMAL
DDOS.matchup = FWAL
PHI.matchup = TRU
TRO.matchup = HON
PSWD.matchup = MULAUTH
RAN.matchup = AUDIT

# Setting the defender abilities
DEFENDER.abilities = [ENC, AMAL, FWAL, TRU, HON, MULAUTH, AUDIT]

# Setting the hacker abilities
HACKER.abilities = [MITM, MAL, DDOS, PHI, TRO, PSWD, RAN]

# Districts
HOSPITAL = GameDistrict("Hospital", HP, [MULAUTH, AUDIT], H_P, H_G)
POLICE_FIRE = GameDistrict("Police/Fire", PF, [FWAL, AUDIT], P_P, P_G)
BUSINESS = GameDistrict("Business", BD, [FWAL, MULAUTH])
INDUSTRIAL = GameDistrict("Industrial", IN, [AMAL])
UNIVERSITY = GameDistrict("University", UN, [TRU, MULAUTH])
RESIDENTIAL = GameDistrict("Residential", RE, [AMAL, FWAL])

DISTRICTS = [BUSINESS, HOSPITAL, POLICE_FIRE, INDUSTRIAL, UNIVERSITY, RESIDENTIAL]

for i in DISTRICTS:
    print(i.name + ": " + str(i.calc_compromise_level()) + "%")
