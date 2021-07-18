# -*- coding: utf-8 -*- 

import network

""" This function return IFconfig-Network """
def ifconfig():
    try:

        wlan = network.WLAN(network.STA_IF)
        config = wlan.ifconfig()
        print("IP: {0}\nMASK: {1}\nROUTER: {2}\nEXTERNAL_IP: {3}".format(config[0], config[1], config[2], config[3]))
    
    except Exception as error:
        print("Error: ", error)

if __name__ == "__main__":
    ifconfig()
