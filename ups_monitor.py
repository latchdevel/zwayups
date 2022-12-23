#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Waveshare UPS HAT (B) for Raspberry Pi.
    https://www.waveshare.com/wiki/UPS_HAT_(B)

    Updates Z-Way device values for UPS battery current and charge percentage.

    Negative current value when battery discharging to power the Raspberry Pi.
    Positive current value when battery charging from external power.

    Copyright (c) Dec 2022 Jorge Rivera. All right reserved.
    License GNU Lesser General Public License v3.0.

"""

# Import class to easy Z-Way JavaScript API Engine usage
# Requires 'requests' module
from zway import ZwayServer

# Import class to easy Waveshare UPS HAT (B) usage
# Requires 'smbus' module
from Waveshare_UPS_HAT import UpsHat

import time

# Z-Way Server 
_ZWAY_HOST          = "localhost"
_ZWAY_PORT          = 8083
_ZWAY_USER          = "admin"
_ZWAY_PASS          = "admin123"

# Z-Way device for UPS battery current
_ZWAY_CURRENT_DEV   = "Code_Device_sensorMultilevel_44"

# Z-Way device for UPS battery charge percentage
_ZWAY_PERCENT_DEV   = "Code_Device_sensorMultilevel_43"

# Update interval seconds
_INTERVAL           = 10

def millis():
    """ Get millis """
    return int(time.time() * 1000)

if __name__=='__main__':

    # Create Waveshare UPS HAT instance
    ups = UpsHat()

    # Create ZwayServer instance
    zway = ZwayServer(
        zway_host=_ZWAY_HOST,
        zway_port=_ZWAY_PORT,
        zway_user=_ZWAY_USER,
        zway_pass=_ZWAY_PASS
    )

    # Get instant UPS HAT battery current mA
    current = ups.getCurrent()

    # Get instant UPS HAT battery charge percentage
    charge = ups.getCharge()

    print("Waveshare UPS HAT (B) Monitor")
    print('Instant battery current={:.0f}mA charge={:.1f}%'.format(current, charge))
    print("Updating Z-Way devices every {} seconds".format(_INTERVAL))

    while True:

        # Update Z-Way device for UPS battery current
        zway.set(_ZWAY_CURRENT_DEV,"{:.0f}".format(current))

        # Update Z-Way device for UPS battery charge percentage
        zway.set(_ZWAY_PERCENT_DEV,"{:.1f}".format(charge))

        # Loop interval seconds
        delay = millis()+(1000*_INTERVAL)
        current = ups.getCurrent()
        charge = ups.getCharge()
        while millis() < delay:
            current = ( current + ups.getCurrent() ) / 2.0
            charge = ( charge + ups.getCharge() ) / 2.0
            time.sleep(0.1)

        """
        # Shutdown happens when battery is below 25% and the device is actively discharging
        if(charge < 25 and current < 0):
            from sys import exit
            from subprocess import call
            call("sudo shutdown --poweroff", shell=True) #safe poweroff at 25 percent
            exit()   
        """
