from cyber_city.game import Role, Ability
from cyber_city.api import System, ModbusSystem, Power, SpecialDistrict, District, TrafficLight

# Lights
G_NS = ModbusSystem(0)
Y_NS = ModbusSystem(1)
R_NS = ModbusSystem(2)
G_EW = ModbusSystem(3)
Y_EW = ModbusSystem(4)
R_EW = ModbusSystem(5)
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

# Special Districts
HOSPITAL = SpecialDistrict("Hospital", HP, H_P, H_G)
POLICE_FIRE = SpecialDistrict("Police/Fire", PF, P_P, P_G)
# Districts
BUSINESS = District("Business", BD)
INDUSTRIAL = District("Industrial", IN)
UNIVERSITY = District("University", UN)
RESIDENTIAL = District("Residential", RE)

# Traffic Lights
NS = TrafficLight(R_NS, Y_NS, G_NS)
EW = TrafficLight(R_EW, Y_EW, G_EW)

# Arrays of Objects
LIGHTS = [
    G_NS, Y_NS, R_NS, G_EW, Y_EW, R_EW]
GRID = [
    BD, HP, PF, IN, UN, RE]
TRAFFICLIGHTS = [
    NS, EW]
DISTRICTS = [
    BUSINESS, HOSPITAL, POLICE_FIRE, INDUSTRIAL, UNIVERSITY, RESIDENTIAL]

# Defining the Roles
R_HACK = Role("Hacker", 5000)
R_DEF = Role("Defender", 5000)

# Defining the Defenders Abilities
A_ENC = Ability("Data Encryption", 300, 10)
A_AMAL = Ability("Anti-Malware", 600, 30)
A_FWAL = Ability("Firewall", 600, 30)
A_TRU = Ability("Trust Zones", 400, 15)
A_HON = Ability("Honey Pot", 500, 20)
A_MULAUTH = Ability("Multifactor Authentication", 300, 10)
A_AUDIT = Ability("Audit Devices & Assets", 500, 20)

# Defining the Attackers Abilities
A_MITM = Ability("Man in the Middle (Steal Data)", 300, 20)
A_MAL = Ability("Malware (Steal Data)", 600, 60)
A_DDOS = Ability("DDoS (Control)", 600, 60)
A_PHI = Ability("Phishing (Steal Data)", 400, 30)
A_TRO = Ability("Trojan (Control)", 500, 40)
A_PSWD = Ability("Password Attack (Steal Data)", 300, 20)
A_RAN = Ability("Ransomware (Control)", 500, 40)

# Pairing the matchups `defense for attacker`
A_MITM.matchup = A_ENC
A_MAL.matchup = A_AMAL
A_DDOS.matchup = A_FWAL
A_PHI.matchup = A_TRU
A_TRO.matchup = A_HON
A_PSWD.matchup = A_MULAUTH
A_RAN.matchup = A_AUDIT

# Setting the defender abilities
R_DEF.abilities = [
    A_ENC, A_AMAL, A_FWAL, A_TRU, A_HON, A_MULAUTH, A_AUDIT
]

# Setting the hacker abilities
R_HACK.abilities = [
    A_MITM, A_MAL, A_DDOS, A_PHI, A_TRO, A_PSWD, A_RAN
]
