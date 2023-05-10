from cyber_city.game import Ability, GameDistrict, Game
from cyber_city.api import System, ModbusSystem, Power, TrafficLight

IP_POWER = "10.10.0.1"  # Power
IP_HOSPITAL = "10.10.0.2"  # Hospital
IP_POLICE_FIRE = "10.10.0.3"  # Police/Fire
IP_TRAFFIC = "10.10.0.4"  # Traffic

# Lights
G_NS = ModbusSystem(0, IP_TRAFFIC)
Y_NS = ModbusSystem(1, IP_TRAFFIC)
R_NS = ModbusSystem(2, IP_TRAFFIC)
G_EW = ModbusSystem(3, IP_TRAFFIC)
Y_EW = ModbusSystem(4, IP_TRAFFIC)
R_EW = ModbusSystem(5, IP_TRAFFIC)

LIGHTS = [G_NS, Y_NS, R_NS, G_EW, Y_EW, R_EW]

# Special District Components
H_P = ModbusSystem(6, IP_HOSPITAL)
H_G = ModbusSystem(7, IP_HOSPITAL)
P_P = ModbusSystem(8, IP_POLICE_FIRE)
P_G = ModbusSystem(9, IP_POLICE_FIRE)
# Power Grid
POWER_GRID = System()
# Power Systems
BD = Power(10, POWER_GRID, IP_POWER)
HP = Power(11, POWER_GRID, IP_POWER)
PF = Power(12, POWER_GRID, IP_POWER)
IN = Power(13, POWER_GRID, IP_POWER)
UN = Power(14, POWER_GRID, IP_POWER)
RE = Power(15, POWER_GRID, IP_POWER)

GRID = [BD, HP, PF, IN, UN, RE]

# Traffic Lights
NS = TrafficLight(R_NS, Y_NS, G_NS)
EW = TrafficLight(R_EW, Y_EW, G_EW)

TRAFFICLIGHTS = [NS, EW]

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

# Districts
HOSPITAL = GameDistrict("Hospital", HP, [MULAUTH, AUDIT], H_P, H_G)
POLICE_FIRE = GameDistrict("Police/Fire", PF, [FWAL, AUDIT], P_P, P_G)
BUSINESS = GameDistrict("Business", BD, [FWAL, MULAUTH])
INDUSTRIAL = GameDistrict("Industrial", IN, [AMAL])
UNIVERSITY = GameDistrict("University", UN, [TRU, MULAUTH])
RESIDENTIAL = GameDistrict("Residential", RE, [AMAL, FWAL])

DISTRICTS = [BUSINESS, HOSPITAL, POLICE_FIRE, INDUSTRIAL, UNIVERSITY, RESIDENTIAL]

GAME = Game(
    5000,
    5000,
    10,
    [ENC, AMAL, FWAL, TRU, HON, MULAUTH, AUDIT],
    [MITM, MAL, DDOS, PHI, TRO, PSWD, RAN],
    DISTRICTS,
    POWER_GRID,
    TRAFFICLIGHTS,
)
GAME.write_all()
