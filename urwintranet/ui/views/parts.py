# -*- coding: utf-8 -*-

"""
urwintranet.ui.views.parts
~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import urwid
import functools

from urwintranet.ui.widgets import generic, parts

from . import base


class PartsView(base.View):
    def __init__(self):
        tabs = generic.Tabs(["home", "parts", "holidays", "preferences", "talks", "logout"], 1)
        self.parts = []
        self.parts_buttons = []
        grid = generic.Grid([], 4, 2, 2, 'center')
        fill = urwid.Filler(grid, min_height=40)
        self.notifier = generic.FooterNotifier("")
        self.widget = urwid.Frame(fill,
                                  header=generic.Header(tabs),
                                  footer=generic.Footer(self.notifier))

    def populate(self, parts):
        self.parts = parts
        self.parts_buttons = [urwid.Button("{} - {}-{} ({})".format(p['id'], p['year'], p['month'], p['state_name'])) for p in parts['results'] ]
        min_width = functools.reduce(max, (len("{} - {}-{} ({})".format(p['id'], p['year'], p['month'], p['state_name'])) for p in parts['results']), 0)
        grid = generic.Grid(self.parts_buttons, min_width * 4, 2, 2, 'center')
        self.widget.set_body(urwid.Filler(grid, min_height=40))

