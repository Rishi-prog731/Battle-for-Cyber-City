""" API for CyberCity """

from typing import List
from pymodbus.client import ModbusTcpClient as ModbusClient

class TrafficLight():
    """ Traffic Light Object """
    HOST = '127.0.0.1'
    """ IP Address of the Modbus Server """
    PORT = 502
    """ Port of the Modbus Server """
    CLIENT = ModbusClient(HOST, PORT)
    @staticmethod
    def set_host(host: str):
        """
        Set the IP Address of the Modbus Server
        Args:
            host (str): IP Address of the Modbus Server
        """
        TrafficLight.HOST = host
        TrafficLight.CLIENT = ModbusClient(TrafficLight.HOST, TrafficLight.PORT)
    @staticmethod
    def set_port(port: int):
        """
        Set the Port of the Modbus Server
        Args:
            port (int): Port of the Modbus Server
        """
        TrafficLight.PORT = port
        TrafficLight.CLIENT = ModbusClient(TrafficLight.HOST, TrafficLight.PORT)
    def __init__(self, name: str, start_coil: int) -> None:
        """
        Initialize a Traffic Light Object
        """
        self.name = name
        """ Name of the Traffic Light """
        self.start_coil = start_coil
        """ Modbus coil address for GREEN Light, YELLOW is +1, RED is +2 """

        self.red = False
        """ RED Light state """
        self.yellow = False
        """ YELLOW Light state """
        self.green = False
        """ GREEN Light state """
    def __str__(self) -> str:
        """
        Returns the current state of the Traffic Light as a string
        Returns:
            str: Current state of the Traffic Light
        ⚫⚫⚫ for OFF
        ⚫⚫🔴 for RED
        ⚫🟡⚫ for YELLOW
        🟢⚫⚫ for GREEN
        """
        out = ''
        out += '🟢' if self.green else '⚫'
        out += '🟡' if self.yellow else '⚫'
        out += '🔴' if self.red else '⚫'
        return out
    def red_light(self) -> None:
        """ Set the Traffic Light to RED """
        self.red = True
        self.yellow = False
        self.green = False
    def is_red_light(self) -> bool:
        """
        Returns the RED Light state
        Returns:
            bool: RED Light state
        """
        return self.red and not self.yellow and not self.green
    def yellow_light(self) -> None:
        """ Set the Traffic Light to YELLOW """
        self.red = False
        self.yellow = True
        self.green = False
    def is_yellow_light(self) -> bool:
        """
        Returns the YELLOW Light state
        Returns:
            bool: YELLOW Light state
        """
        return not self.red and self.yellow and not self.green
    def green_light(self) -> None:
        """ Set the Traffic Light to GREEN """
        self.red = False
        self.yellow = False
        self.green = True
    def is_green_light(self) -> bool:
        """
        Returns the GREEN Light state
        Returns:
            bool: GREEN Light state
        """
        return not self.red and not self.yellow and self.green
    def all_lights_on(self) -> None:
        """ Set all Lights to ON """
        self.red = True
        self.yellow = True
        self.green = True
    def all_lights_off(self) -> None:
        """ Set all Lights to OFF """
        self.red = False
        self.yellow = False
        self.green = False
    def is_all_lights_on(self) -> bool:
        """
        Returns the state of all Lights
        Returns:
            bool: State of all Lights
        """
        return self.red and self.yellow and self.green
    def write(self) -> None:
        """ Write the current state of the Traffic Light to the Modbus Server """
        if TrafficLight.CLIENT.connect():
            TrafficLight.CLIENT.write_coils(self.start_coil, [self.green, self.yellow, self.red])
            TrafficLight.CLIENT.close()
        else:
            return
    def read(self) -> List[bool]:
        """
        Read the current state of the Traffic Light from the Modbus Server and update the Traffic Light
        Returns:
            List[bool]: Current state of the Traffic Light
        """
        if TrafficLight.CLIENT.connect():
            result = TrafficLight.CLIENT.read_coils(self.start_coil, 3)
            TrafficLight.CLIENT.close()
            [self.green, self.yellow, self.red] = result.bits[:3]
            return result.bits[:3]
        else:
            return []

class Power():
    """ Power Object """
    HOST = '127.0.0.1'
    """ IP Address of the Modbus Server """
    PORT = 502
    """ Port of the Modbus Server """
    CLIENT = ModbusClient(HOST, PORT)
    @staticmethod
    def set_host(host: str):
        """
        Set the IP Address of the Modbus Server
        Args:
            host (str): IP Address of the Modbus Server
        """
        Power.HOST = host
        Power.CLIENT = ModbusClient(Power.HOST, Power.PORT)
    @staticmethod
    def set_port(port: int):
        """
        Set the Port of the Modbus Server
        Args:
            port (int): Port of the Modbus Server
        """
        Power.PORT = port
        Power.CLIENT = ModbusClient(Power.HOST, Power.PORT)
    GLOBAL_POWER = True
    @staticmethod
    def global_power_on():
        """ Set the global power state to ON """
        Power.GLOBAL_POWER = True
    @staticmethod
    def global_power_off():
        """ Set the global power state to OFF """
        Power.GLOBAL_POWER = False
    @staticmethod
    def is_global_power_on():
        """
        Returns the global power state
        Returns:
            bool: Global power state
        """
        return Power.GLOBAL_POWER
    def __init__(self, name: str, start_coil: int) -> None:
        """
        Initialize a Power Object
        """
        self.name = name
        """ Name of the Power """
        self.start_coil = start_coil
        """ Modbus coil address for the Power """
        self.power = False
        """ Power state """
    def __str__(self) -> str:
        """
        Returns the current state of the Power as a string
        Returns:
            str: Current state of the Power
        ⚫ for OFF
        ⚡ for ON
        """
        return "⚡" if self.power else "⚫"
    def power_on(self) -> None:
        """ Set the Power to ON """
        self.power = True
    def power_off(self) -> None:
        """ Set the Power to OFF """
        self.power = False
    def is_power_on(self) -> bool:
        """ Returns the Power state """
        return self.power
    def write(self) -> None:
        """ Write the current state of the Power to the Modbus Server """
        if Power.CLIENT.connect():
            Power.CLIENT.write_coils(self.start_coil, [self.power])
            Power.CLIENT.close()
        else:
            return
    def read(self) -> List[bool]:
        """
        Read the current state of the Power from the Modbus Server and update the Power
        Returns:
            List[bool]: Current state of the Power
        """
        if Power.CLIENT.connect():
            result = Power.CLIENT.read_coils(self.start_coil, 1)
            Power.CLIENT.close()
            [self.power] = result.bits[:1]
            return result.bits[:1]
        else:
            return []

class District():
    """ The District Object """
    def __init__(self, name: str, power_coil: int):
        """
        Initialize a District Object
        Args:
            name (str): Name of the District
            power_coil (int): Modbus coil address for the District Power
        """
        self.name = name
        """ Name of the District """
        self.power = Power(name, power_coil)
        """ Power Object for the District """
    def __str__(self) -> str:
        """
        Returns the current state of the District as a string
        Returns:
            str: Current state of the District
        """
        out = ""
        out += self.name
        out += "\t=>\t"
        out += str(self.power)
        return out

class SpecialDistrict(District):
    """ The Special District Object """
    HOST = '127.0.0.1'
    """ IP Address of the Modbus Server """
    PORT = 502
    """ Port of the Modbus Server """
    CLIENT = ModbusClient(HOST, PORT)
    @staticmethod
    def set_host(host: str):
        """
        Set the IP Address of the Modbus Server
        Args:
            host (str): IP Address of the Modbus Server
        """
        SpecialDistrict.HOST = host
        SpecialDistrict.CLIENT = ModbusClient(SpecialDistrict.HOST, SpecialDistrict.PORT)
    @staticmethod
    def set_port(port: int):
        """
        Set the Port of the Modbus Server
        Args:
            port (int): Port of the Modbus Server
        """
        SpecialDistrict.PORT = port
        SpecialDistrict.CLIENT = ModbusClient(SpecialDistrict.HOST, SpecialDistrict.PORT)
    def __init__(self, name: str, power_coil: int):
        """
        Initialize a Special District Object
        Args:
            name (str): Name of the Special District
            power_coil (int): Modbus coil address for the Special District Power
        """
        super().__init__(name, power_coil)
        self.start_coil = 0
        """ Modbus coil address for the Special District """
        self.special_power = True
        """ Special Power state """
        self.special_generator = False
        """ Special Generator state """
    def __str__(self) -> str:
        """
        Returns the current state of the Special District as a string
        Returns:
            str: Current state of the Special District
        """
        return super().__str__() + "⚡" if self.special_power else "🔌" + "\t" + "🔋" if self.special_generator else "🔌"
    def special_power_on(self) -> None:
        """ Set the Special Power to ON """
        self.special_power = True
    def special_power_off(self) -> None:
        """ Set the Special Power to OFF """
        self.special_power = False
    def is_special_power_on(self) -> bool:
        """ Returns the Special Power state """
        return self.special_power
    def special_generator_on(self) -> None:
        """ Set the Special Generator to ON """
        self.special_generator = True
    def special_generator_off(self) -> None:
        """ Set the Special Generator to OFF """
        self.special_generator = False
    def is_special_generator_on(self) -> bool:
        """ Returns the Special Generator state """
        return self.special_generator
    def write(self):
        """ Write the current state of the Special District to the Modbus Server """
        if SpecialDistrict.CLIENT.connect():
            SpecialDistrict.CLIENT.write_coils(self.start_coil, [self.special_power, self.special_generator])
            SpecialDistrict.CLIENT.close()
        else:
            return
    def read(self) -> List[bool]:
        """
        Read the current state of the Special District from the Modbus Server and update the Special District
        Returns:
            List[bool]: Current state of the Special District
        """
        if SpecialDistrict.CLIENT.connect():
            result = SpecialDistrict.CLIENT.read_coils(self.start_coil, 2)
            SpecialDistrict.CLIENT.close()
            [self.special_power, self.special_generator] = result.bits[:2]
            return result.bits[:2]
        else:
            return []
