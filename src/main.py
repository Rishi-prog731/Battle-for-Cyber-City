import CyberCity as city
import time

# Actual Traffic Light Objects with Mappings
NS = city.TrafficLight("North-South", 0)
EW = city.TrafficLight("East-West", 3)

print(NS)
print(EW)

# Actual City Distrcit Objects with Mappings
BUSINESS = city.District("Business", 0)
HOSPITAL = city.SpecialDistrict("Hospital", 1, '127.0.0.1', 502)
POLICE_FIRE = city.SpecialDistrict("Police/Fire", 2, '127.0.0.1', 502)
INDUSTRIAL = city.District("Industrial", 3)
UNIVERSITY = city.District("University", 4)
RESIDENTIAL = city.District("Residential", 5)

print(BUSINESS)
print(HOSPITAL)
print(POLICE_FIRE)
print(INDUSTRIAL)
print(UNIVERSITY)
print(RESIDENTIAL)