from CyberCity.CyberCity import *

# Actual Traffic Light Objects with Mappings
NS = TrafficLight("North-South", 0)
EW = TrafficLight("East-West", 3)

TRAFFICLIGHTS = [NS, EW]

for a in TRAFFICLIGHTS:
    print(a)

# Actual City Distrcit Objects with Mappings
BUSINESS = District("Business", 0)
HOSPITAL = SpecialDistrict("Hospital", 1, '127.0.0.1', 502)
POLICE_FIRE = SpecialDistrict("Police/Fire", 2, '127.0.0.1', 502)
INDUSTRIAL = District("Industrial", 3)
UNIVERSITY = District("University", 4)
RESIDENTIAL = District("Residential", 5)

DISTRICTS = [BUSINESS, HOSPITAL, POLICE_FIRE, INDUSTRIAL, UNIVERSITY, RESIDENTIAL]

for a in DISTRICTS:
    print(a)