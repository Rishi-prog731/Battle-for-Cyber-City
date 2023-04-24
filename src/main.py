from cyber_city.api import TrafficLight, System

# Lights
G_NS = System(0)
Y_NS = System(1)
R_NS = System(2)
G_EW = System(3)
Y_EW = System(4)
R_EW = System(5)

print(G_NS, Y_NS, R_NS, G_EW, Y_EW, R_EW)

# Actual Traffic Light Objects with Mappings
NS = TrafficLight(R_NS, Y_NS, G_NS)
EW = TrafficLight(R_EW, Y_EW, R_EW)

print(NS, EW)

#NS.state = TrafficLight.States.ALL_ON
NS.update()

TRAFFICLIGHTS = [NS, EW]


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
