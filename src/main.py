from cyber_city.api import System, TrafficLight, Power, ModbusSystem

# Lights
G_NS = ModbusSystem(0)
Y_NS = ModbusSystem(1)
R_NS = ModbusSystem(2)
G_EW = ModbusSystem(3)
Y_EW = ModbusSystem(4)
R_EW = ModbusSystem(5)

print(
    G_NS,
    Y_NS,
    R_NS,
    G_EW,
    Y_EW,
    R_EW
)

# Traffic Lights
NS = TrafficLight(R_NS, Y_NS, G_NS)
EW = TrafficLight(R_EW, Y_EW, G_EW)

print(
    NS,
    EW
)

TRAFFICLIGHTS = [NS, EW]

# PowerGrid
POWER_GRID = System()

# Power
BD = Power(0, POWER_GRID)
HP = Power(1, POWER_GRID)
PF = Power(2, POWER_GRID)
IN = Power(3, POWER_GRID)
UN = Power(4, POWER_GRID)
RE = Power(5, POWER_GRID)

grid = [BD, HP, PF, IN, UN, RE]

print(
    BD,
    HP,
    PF,
    IN,
    UN,
    RE
)

print(
    POWER_GRID
)

# Actual City Distrcit Objects with Mappings
# BUSINESS = District("Business", 0)
# HOSPITAL = SpecialDistrict("Hospital", 1)
# POLICE_FIRE = SpecialDistrict("Police/Fire", 2)
# INDUSTRIAL = District("Industrial", 3)
# UNIVERSITY = District("University", 4)
# RESIDENTIAL = District("Residential", 5)
# 
# DISTRICTS = [
#     BUSINESS, HOSPITAL, POLICE_FIRE, INDUSTRIAL, UNIVERSITY, RESIDENTIAL]
