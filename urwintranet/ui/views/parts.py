# -*- coding: utf-8 -*-

"""
urwintranet.ui.views.parts
~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

from urwintranet.ui.widgets import generic, parts

from . import base


class PartsView(base.View):
    def __init__(self):
        widgets = []
        tabs = generic.Tabs(["home", "parts", "holidays", "preferences", "talks", "logout"], 1)
        widgets.append(tabs)
        pony = generic.pony()
        widgets.append(pony)
        for part in ['prueba', 'hola']:
            part_line = parts.PartLine(part)
            widgets.append(part_line)
        self.widget = parts.Parts([tabs, pony])
