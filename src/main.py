from cyber_city.api import System, TrafficLight, PowerGrid

# Lights
G_NS = System(0)
Y_NS = System(1)
R_NS = System(2)
G_EW = System(3)
Y_EW = System(4)
R_EW = System(5)

# Traffic Lights
NS = TrafficLight(R_NS, Y_NS, G_NS)
EW = TrafficLight(R_EW, Y_EW, G_EW)

TRAFFICLIGHTS = [NS, EW]

# Power
BD = System(0)
HP = System(1)
PF = System(2)
IN = System(3)
UN = System(4)
RE = System(5)

grid = [BD, HP, PF, IN, UN, RE]

POWERGRID = PowerGrid(grid)

POWERGRID.systems[0].set(True)

print(
    BD,
    HP,
    PF,
    IN,
    UN,
    RE
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
