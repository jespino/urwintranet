# -*- coding: utf-8 -*-

"""
urwintranet.controllers.base
~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


class Controller(object):
    view = None

    def handle(self, key):
        return key
