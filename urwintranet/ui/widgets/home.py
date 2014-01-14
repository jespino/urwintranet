# -*- coding: utf-8 -*-

"""
urwintranet.ui.widgets.home
~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import urwid

from . import mixins


class Home(mixins.FormMixin, urwid.ListBox):
    def __init__(self, widgets):
        super().__init__(urwid.SimpleListWalker(widgets))
