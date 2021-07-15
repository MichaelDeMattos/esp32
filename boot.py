# -*- coding: utf-8 -*-

import network, json
from resource_webrepl.socket_webrepl import WebRepl

class BootApp(object):
    def __init__(self, *args):
        """ Init network interface """
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.path = ("config.json")
        self.config = json.loads(open(self.path, "rb").read())
        self.connect()
        
    """ Start connect network """
    def connect(self):
        if not self.wlan.isconnected():
            print('connecting to network...')
            self.wlan.connect(self.config["network"], self.config["password"])
            while not self.wlan.isconnected():
                pass
				
        """ Run webrepl """ 
        WebRepl().start_socket_webrepl(self.config["ws"])

if __name__ == '__main__':
	BootApp()
