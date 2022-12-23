#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Waveshare UPS HAT (B) for Raspberry Pi.
    https://www.waveshare.com/wiki/UPS_HAT_(B)

    Shows Waveshare UPS HAT instant measures of battery current and charge percentage.

    Negative current value when battery discharging to power the Raspberry Pi.
    Positive current value when battery charging from external power.

    Copyright (c) Dec 2022 Jorge Rivera. All right reserved.
    License GNU Lesser General Public License v3.0.

"""

# Import class to easy Waveshare UPS HAT usage
# Requires 'smbus' module
from Waveshare_UPS_HAT import UpsHat

if __name__=='__main__':

    # Create Waveshare UPS HAT instance
    ups = UpsHat()

    # Show instant UPS battery current and charge percentage
    print('{{"current":{:.0f},"charge":{:.1f}}}'.format(ups.getCurrent(), ups.getCharge()))
