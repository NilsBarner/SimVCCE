
"""
General Object-oriented Abstraction of VC Cycle 

Evaporator:
    heat addition

Author: Cheng Maohua cmh@seu.edu.cn    
"""
from .port import *


class Evaporator:

    energy = "QIN"
    devtype = "EVAPORATOR"

    def __init__(self, dictDev):
        """ Initializes the Evaporator """
        self.name = dictDev['name']
        self.iPort = [Port(dictDev['iPort'])]
        self.oPort = [Port(dictDev['oPort'])]

        # map the port's name(str) to the obj
        self.portdict = {
            "iPort": self.iPort,
            "oPort": self.oPort
        }

    def state(self):
        """ ideal Isobaric """
        if self.oPort[0].p is not None and self.iPort[0].p is None:
            self.iPort[0].p = self.oPort[0].p
        elif self.iPort[0].p is not None and self.oPort[0].p is None:
            self.oPort[0].p = self.iPort[0].p

    def balance(self):
        """ mass and energy balance  """

        # mass balance
        if self.iPort[0].mdot is None and self.oPort[0].mdot is None:
            raise ValueError("mdot not none")

        if self.iPort[0].mdot is not None:
            self.oPort[0].mdot = self.iPort[0].mdot
        elif self.oPort[0].mdot is not None:
            self.iPort[0].mdot = self.oPort[0].mdot

        # energy balance
        self.Qin = self.iPort[0].mdot * (self.oPort[0].h - self.iPort[0].h)

    def __str__(self):
        result = '\n' + self.name
        result += '\n' + " PORTS "+Port.title
        result += '\n' + " iPort " + self.iPort[0].__str__()
        result += '\n' + " oPort " + self.oPort[0].__str__()
        result += '\nQin(kW): \t{:>.2f}'.format(self.Qin)
        return result
