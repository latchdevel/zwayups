# -*- coding: utf-8 -*-
"""
    Python class to easy Z-Way JavaScript API Engine usage.
    https://z-wave.me/manual/z-way/JavaScript_Engine.html

    Methods:
        - get(device) -> Return device 'metrics:level' value
        - set(device,value) -> Set device 'metrics:level' value

    Copyright (c) Dec 2022 Jorge Rivera. All right reserved.
    License GNU Lesser General Public License v3.0.

"""

import requests

class ZwayServer():
    """
    Class to easy Z-Way JavaScript API Engine usage
    """

    def __init__(
        self,
        zway_prot = "http",
        zway_host = "localhost",
        zway_port = 8083,
        zway_user = "admin",
        zway_pass = None,
        zway_auth = None,
    ):
        """ Initialize a Z-Way Server instance """

        self.zway_prot = zway_prot
        self.zway_host = zway_host
        self.zway_port = zway_port
        self.zway_user = zway_user
        self.zway_pass = zway_pass
        self.zway_auth = zway_auth

    def get(self, device):
        """
        Get device 'metrics:level' value
        """

        if not isinstance(device,str):
            raise TypeError("The 'device' must be a string")
        elif len(device) < 1:
            raise ValueError("The 'device' is empty")

        url = ("{protocol}://{host}:{port}/JS/Run/controller.devices.get('{device}').get('metrics:level')").format(
            protocol = self.zway_prot,
            host = self.zway_host,
            port = self.zway_port,
            device = device
        )

        try:
            if self.zway_auth:
                resp = requests.get(url, headers={"Authorization": "Bearer ZWAYSession/{token}".format(token=self.zway_auth)})
            else:
                resp = requests.get(url, auth=(self.zway_user, self.zway_pass))
        except Exception as error:
            print("Error: {}".format(error))
            return None

        if resp.status_code == 200:
            return resp.text

        print("Error: {code} {error}".format(code=resp.status_code, error=resp.text))
        return None


    def set(self, device, value = None):
        """
        Set device 'metrics:level' value
        """

        if not isinstance(device,str):
            raise TypeError("The 'device' must be a string")
        elif len(device) < 1:
            raise ValueError("The 'device' is empty")

        if not value: value = ""

        url = ("{protocol}://{host}:{port}/JS/Run/controller.devices.get('{device}').set('metrics:level','{value}')").format(
            protocol = self.zway_prot,
            host = self.zway_host,
            port = self.zway_port,
            device = device,
            value = value
        )

        try:
            if self.zway_auth:
                resp = requests.get(url, headers={"Authorization": "Bearer ZWAYSession/{token}".format(token=self.zway_auth)})
            else:
                resp = requests.get(url, auth=(self.zway_user, self.zway_pass))
        except Exception as error:
            print("Error: {}".format(error))
            return False

        if resp.status_code == 200:
            return True

        print("Error: {code} {error}".format(code=resp.status_code, error=resp.text))
        return False
