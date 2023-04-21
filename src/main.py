from cyber_city.api import TrafficLight, District, SpecialDistrict

# Actual Traffic Light Objects with Mappings
NS = TrafficLight("North-South", 0)
EW = TrafficLight("East-West", 3)

TRAFFICLIGHTS = [NS, EW]

# Actual City Distrcit Objects with Mappings
BUSINESS = District("Business", 0)
HOSPITAL = SpecialDistrict("Hospital", 1)
POLICE_FIRE = SpecialDistrict("Police/Fire", 2)
INDUSTRIAL = District("Industrial", 3)
UNIVERSITY = District("University", 4)
RESIDENTIAL = District("Residential", 5)

DISTRICTS = [BUSINESS, HOSPITAL, POLICE_FIRE, INDUSTRIAL, UNIVERSITY, RESIDENTIAL]
