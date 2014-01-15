# -*- coding: utf-8 -*-

"""
urwintranet.ui.widgets.home
~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import urwid

from . import mixins


class Parts(urwid.ListBox):
    def __init__(self, widgets):
        super().__init__(urwid.SimpleListWalker(widgets))

class PartLine(urwid.Text):
    pass
