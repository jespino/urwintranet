# -*- coding: utf-8 -*-

"""
urwintranet.controllers.home
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from urwintranet.ui import signals

from . import base

import functools


class PartsController(base.Controller):
    def __init__(self, view, executor, state_machine):
        self.view = view
        self.executor = executor
        self.state_machine = state_machine

        parts_f = self.executor.parts()
        parts_f.add_done_callback(self.handle_parts_response)

    def handle_parts_response(self, future):
        parts = future.result()
        if parts is None:
            return # FIXME

        self.view.populate(parts)
        for b, p in zip(self.view.parts_buttons, self.view.parts):
            signals.connect(b, "click", functools.partial(self.select_part, p))

        self.state_machine.transition(self.state_machine.PARTS)

    def select_part(self, part):
        pass

    def handle(self, key):
        if key == 'p':
            self.state_machine.parts()
        elif key == 'h':
            self.state_machine.home()
