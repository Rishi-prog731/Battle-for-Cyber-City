
from cyber_city.api import System, ModbusSystem, TrafficLight, Power, District, SpecialDistrict

# Lights
G_NS = ModbusSystem(0)
Y_NS = ModbusSystem(1)
R_NS = ModbusSystem(2)
G_EW = ModbusSystem(3)
Y_EW = ModbusSystem(4)
R_EW = ModbusSystem(5)

# Traffic Lights
NS = TrafficLight(R_NS, Y_NS, G_NS)
EW = TrafficLight(R_EW, Y_EW, G_EW)

TRAFFICLIGHTS = [NS, EW]

# Power Grid
POWER_GRID = System()

# Power Systems
BD = Power(6, POWER_GRID)
HP = Power(7, POWER_GRID)
PF = Power(8, POWER_GRID)
IN = Power(9, POWER_GRID)
UN = Power(10, POWER_GRID)
RE = Power(11, POWER_GRID)

GRID = [BD, HP, PF, IN, UN, RE]

# Special Districts
H_P = ModbusSystem(12)
H_G = ModbusSystem(13)
HOSPITAL = SpecialDistrict("Hospital", HP, H_P, H_G)

PF_P = ModbusSystem(14)
PF_G = ModbusSystem(15)
POLICE_FIRE = SpecialDistrict("Police/Fire", PF, PF_P, PF_G)

# Districts
BUSINESS = District("Business", BD)
INDUSTRIAL = District("Industrial", IN)
UNIVERSITY = District("University", UN)
RESIDENTIAL = District("Residential", RE)

DISTRICTS = [
    BUSINESS, HOSPITAL, POLICE_FIRE, INDUSTRIAL, UNIVERSITY, RESIDENTIAL]
