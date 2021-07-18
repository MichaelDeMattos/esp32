# -*- coding: utf-8 -*-

import _thread
from time import sleep, localtime
from machine import Pin

class Project(object):
    def __init__(self, *args):

        """ Global vars """
        self.loop = True

        """ Blink led Board: (Esp32 Lolin Lite) in Pin 22 """
        _thread.start_new_thread(self.led_blink(), ())

    """ Blink led """
    def led_blink(self):
        try:

            led = Pin(22, Pin.OUT)

            while self.loop is True:
                led.value(not led.value())
                print("Blink Led!")
                sleep(1)
        
        except Exception as error:
            print("Error: ", error)

if __name__ == "__main__":
    Project()
