# -*- coding: utf-8 -*-

"""
urwintranet.controllers.home
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from urwintranet.ui import signals

from . import base


class HomeController(base.Controller):
    def __init__(self, view, executor, state_machine):
        self.view = view
        self.executor = executor
        self.state_machine = state_machine
