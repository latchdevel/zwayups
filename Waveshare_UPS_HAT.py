# -*- coding: utf-8 -*-
"""
    Python class to easy Waveshare UPS HAT (B) usage.
    https://www.waveshare.com/wiki/UPS_HAT_(B)

    Methods:
        getCurrent() -> Return battery current mA
        getCharge() -> Return battery charge percentage

    Negative current value when battery discharging to power the Raspberry Pi.
    Positive current value when battery charging from external power.

    Copyright (c) Dec 2022 Jorge Rivera. All right reserved.
    License GNU Lesser General Public License v3.0.

"""

# Dummy INA219 class to get simulated measures if 
# 'smbus' module import or I2C/SMBus init fails.
from random import randint as _randint 
class DUMMY_INA219:
    """ Dummy INA219 measures """
    def __init__(self, i2c_bus, addr):
        print("Using dummy INA219 measures")
    def getCurrent_mA(self):
        return _randint(-100,100)
    def getBusVoltage_V(self):
        return _randint(740,840)/100.0

# Python class to easy INA219 usage
# Requires 'smbus' module
try:
    from INA219 import INA219
except Exception as error:
    print("Module 'smbus' import error: {}".format(error))
    class INA219(DUMMY_INA219): pass

# Waveshare UPS HAT (B) INA219 address
_INA219_ADDR        = 0x42

# Raspberry Pi I2C/SMBus 
_RPI_I2C_BUS        = 0x01

class UpsHat:
    """
        Class to easy Waveshare UPS HAT (B) usage
    """
    def __init__(self, i2c_bus=_RPI_I2C_BUS, addr=_INA219_ADDR):
        # Create an INA219 instance
        try:
            self.ina219 = INA219(i2c_bus=i2c_bus, addr=addr)
        except Exception as error:
            print("I2C/SMBus init error: {}".format(error))
            self.ina219 = DUMMY_INA219(i2c_bus=i2c_bus, addr=addr)

    def getCurrent(self):
        """ Get instant battery current mA """
        # Current in mA
        return self.ina219.getCurrent_mA()

    def getCharge(self):
        """ Get instant battery charge percentage """
         # Voltage on V- (load side)
        bus_voltage = self.ina219.getBusVoltage_V()

        charge = (bus_voltage - 6)/2.4*100
        if(charge > 100): charge = 100.0
        if(charge <   0): charge =   0.0

        return charge
