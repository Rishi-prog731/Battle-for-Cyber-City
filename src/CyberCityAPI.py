class CyberCity():
    def __init__(self):
        self.districts = []

    def __str__(self):
        out = 'CyberCity\n'

        for i in self.districts:
            out += f'\t{str(i)}\n'
        
        return out

class District():
    def __init__(self, name, generator=False, trafficLight=False, trafficLightCount=0):
        self.name = name
        self.power = Power(generator)
        if trafficLight:
            self.trafficLight = []
            for i in range(trafficLightCount):
                self.trafficLight.append(TrafficLight(i))

    def __str__(self):
        out = f'{self.name}\n\t\t{str(self.power)}'
        if hasattr(self, 'trafficLight'):
            for i in self.trafficLight:
                out += f'\n\t\t{str(i)} '
        return out

class Power():
    def __init__(self, hasGenerator=False):
        self.on = True
        if hasGenerator:
            self.generator = False
    
    def __str__(self):
        out = f'Power: {"⚡" if self.on else "⚠ "}'
        if hasattr(self, 'generator'):
            out += f'  Generator: {"⚡" if self.generator else "⚠ "}'
        return out
    
    def PowerOn(self):
        self.on = True
    
    def PowerOff(self):
        self.on = False

    def GeneratorOn(self):
        if hasattr(self, 'generator'):
            self.generator = True
    
    def GeneratorOff(self):
        if hasattr(self, 'generator'):
            self.generator = False

class TrafficLight():
    def __init__(self, name=0):
        self.name = name
        self.red = 0
        self.yellow = 0
        self.green = 0

        self.RedLight()

    def __str__(self):
        out = f'{self.name}: {"🔴" if self.red else "⚫"}{"🟡" if self.yellow else "⚫"}{"🟢" if self.green else "⚫"}'
        return out

    def RedLight(self):
        self.red = 1
        self.yellow = 0
        self.green = 0

    def YellowLight(self):
        self.red = 0
        self.yellow = 1
        self.green = 0

    def GreenLight(self):
        self.red = 0
        self.yellow = 0
        self.green = 1