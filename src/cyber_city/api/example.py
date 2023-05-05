"""
This is an example implementation for using the `cyber_city.api` module.
"""
from cyber_city.api import (
    System,
    ModbusSystem,
    TrafficLight,
    Power,
    District,
    SpecialDistrict,
)

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
LIGHTS = [G_NS, Y_NS, R_NS, G_EW, Y_EW, R_EW]
GRID = [BD, HP, PF, IN, UN, RE]
TRAFFICLIGHTS = [NS, EW]
DISTRICTS = [BUSINESS, HOSPITAL, POLICE_FIRE, INDUSTRIAL, UNIVERSITY, RESIDENTIAL]

# Writing and Doing things to the systems
TRAFFICLIGHTS[0].set_state(TrafficLight.States.RED_LIGHT)
TRAFFICLIGHTS[1].set_state(TrafficLight.States.GREEN_LIGHT)

# Write everything
for system in TRAFFICLIGHTS:
    system.write()
for system in DISTRICTS:
    system.write()
