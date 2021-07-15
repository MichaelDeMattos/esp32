# -*- coding: utf-8 -*-

import webrepl

class WebRepl(object):
    def __init__(self, *args):
        pass
        
    """ Start webrepl (WebSocket) """
    def start_socket_webrepl(self, password):
        webrepl.start(password)
