# -*- coding: utf-8 -*-

"""
urwintranet.controllers.home
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from urwintranet.ui import signals

from . import base


class PartsController(base.Controller):
    def __init__(self, view, executor, state_machine):
        self.view = view
        self.executor = executor
        self.state_machine = state_machine

    def handle(self, key):
        if key == 'p':
            self.state_machine.parts()
        elif key == 'h':
            self.state_machine.home()
