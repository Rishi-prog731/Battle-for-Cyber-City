import CyberCityAPI as c

city = c.CyberCity()

city.districts.append(c.District('Business'))
city.districts.append(c.District('Hospital', True))
city.districts.append(c.District('Police/Fire', True, True, 2))
city.districts.append(c.District('Industrial'))
city.districts.append(c.District('Univesity'))
city.districts.append(c.District('Residential'))

print(city)