import CyberCityAPI
import time

NS = CyberCityAPI.TrafficLight("North-South", 0)
EW = CyberCityAPI.TrafficLight("East-West", 3)

NS.toGreen()
EW.toRed()

NS.write()
EW.write()
